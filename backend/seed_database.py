import os
import re
import chromadb
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    """Reads the raw text from the compiled PDF file safely."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(
            f"Missing source file: '{pdf_path}'. Please run 'python generate_pdf.py' first!"
        )
    
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n"
    return full_text

def parse_pdf_to_bookshelf_schema(raw_text):
    """
    Parses flat PDF text streams cleanly into Bookshelf's structured schema.
    Features a dynamic fallback to protect against empty chunk extraction.
    """
    lines = raw_text.split("\n")
    cleaned_lines = []
    for line in lines:
        if "GOVERNMENT OF INDIA" in line or "CONFIDENTIAL" in line or "Page " in line:
            continue
        cleaned_lines.append(line)
    
    processed_text = "\n".join(cleaned_lines)
    book_title = "National Procurement, Governance, and Compliance Omnibus Act (2026)"
    bookshelf_data = []
    
    # Try parsing via strict Section Boundaries first
    sections = re.split(r'(SECTION I:|SECTION II:|SECTION III:)', processed_text)
    
    if len(sections) > 1:
        # Section-based structural extraction layout
        for i in range(1, len(sections), 2):
            section_marker = sections[i]
            section_body = sections[i+1]
            section_lines = section_body.split("\n")
            full_section_name = section_marker + section_lines[0]
            clause_blob = "\n".join(section_lines[1:])
            
            clause_matches = re.findall(r'((?:Clause|Paragraph|Rule|Section|Criterion)\s+\d+[^:]+):', clause_blob)
            clause_texts = re.split(r'(?:Clause|Paragraph|Rule|Section|Criterion)\s+\d+[^:]+:', clause_blob)
            
            topics_list = []
            text_payloads = [t.strip() for t in clause_texts[1:]]
            
            for idx, topic_title in enumerate(clause_matches):
                if idx < len(text_payloads):
                    topics_list.append({
                        "topic_title": topic_title.strip(),
                        "text_body": text_payloads[idx]
                    })
            
            if topics_list:
                bookshelf_data.append({
                    "chapter_name": full_section_name.strip(),
                    "topics": topics_list
                })

    # 🚨 DYNAMIC FALLBACK: If regex layout grouping returns 0 records, chunk by paragraphs
    if not bookshelf_data:
        print("⚠️ Section structures not found via regex. Initiating paragraph-level fallback chunking...")
        paragraphs = [p.strip() for p in processed_text.split("\n\n") if len(p.strip()) > 30]
        
        fallback_topics = []
        for idx, para in enumerate(paragraphs):
            # Formulate mock titles based on the text layout
            first_words = " ".join(para.split()[:4]) + "..."
            fallback_topics.append({
                "topic_title": f"Clause Clause {idx + 1} ({first_words})",
                "text_body": para
            })
            
        bookshelf_data.append({
            "chapter_name": "SECTION I: GENERAL POLICY OMNIBUS CORE",
            "topics": fallback_topics
        })
        
    return book_title, bookshelf_data

def seed_vector_database():
    pdf_filename = "National_Procurement_and_Governance_Omnibus_Act_2026.pdf"
    db_directory = "./bookshelf_knowledge_base"
    
    print("📖 [PHASE 1: EXTRACTION] Parsing target PDF document buffers...")
    raw_pdf_text = extract_text_from_pdf(pdf_filename)
    
    print("🗺️ [PHASE 2: MAPPING] Translating data lines into Bookshelf relational schemas...")
    book_title, structured_chapters = parse_pdf_to_bookshelf_schema(raw_pdf_text)
    
    print("⚡ [PHASE 3: CONNECTING] Mounting local persistent ChromaDB collection cluster...")
    chroma_client = chromadb.PersistentClient(path=db_directory)
    
    # Reset the internal collection arrays on re-runs to avoid duplicate record packing anomalies
    try:
        chroma_client.delete_collection(name="gov_policies")
        print("🗑️ Cleared existing 'gov_policies' collection for a clean seed install.")
    except Exception:
        pass
    
    # Initialize a fresh collection space cleanly
    collection = chroma_client.create_collection(name="gov_policies")
    
    print("🚀 [PHASE 4: EMBEDDING] Encoding and indexing clause matrix packages into vector engine...")
    
    vector_id_counter = 1
    for chapter in structured_chapters:
        chapter_name = chapter["chapter_name"]
        
        for topic in chapter["topics"]:
            title = topic["topic_title"]
            body = topic["text_body"]
            
            # Combine clause headers with descriptions to optimize model semantic clarity searches
            complete_document_chunk = f"{title}: {body}"
            
            # Build trace validation metadata payloads to feed downstream RAG citation engines
            metadata_payload = {
                "book_source": book_title,
                "chapter_origin": chapter_name,
                "topic_label": title,
                "file_reference": pdf_filename
            }
            
            # Insert item block directly into local ChromaDB storage
            collection.add(
                documents=[complete_document_chunk],
                metadatas=[metadata_payload],
                ids=[f"id_clause_{vector_id_counter:03d}"]
            )
            vector_id_counter += 1

    print(f"\n🎉 [COMPLETE] Database Ingestion Sequence Finalized successfully!")
    print(f"📦 Total Indexed Records: {vector_id_counter - 1} chunks safely written to storage block '{db_directory}'.\n")

if __name__ == "__main__":
    seed_vector_database()