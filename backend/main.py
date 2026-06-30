import os
import json
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import chromadb
from openai import OpenAI
# 1. Import the dotenv loader
from dotenv import load_dotenv

# 2. Load environment variables from the .env file immediately
load_dotenv()

# Initialize the FastAPI App instance
app = FastAPI(
    title="Bookshelf AI - Enterprise Governance Core",
    description="Cross-platform API layer linking UiPath Maestro Case and Web Dashboards with high-integrity RAG pipelines.",
    version="1.0.0"
)

# 🌐 Enable CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🛠️ SECURITY INITIALIZATION
# Safely verify that your OpenAI API key was successfully loaded
if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError(
        "❌ CRITICAL ERROR: OPENAI_API_KEY is not set. "
        "Please check your local .env file in the project root."
    )

# Instantiate the centralized OpenAI client engine (it automatically looks for os.environ["OPENAI_API_KEY"])
openai_client = OpenAI()

# Connect to our persistent Bookshelf AI vector store directory
DB_DIRECTORY = "./bookshelf_knowledge_base"
chroma_client = chromadb.PersistentClient(path=DB_DIRECTORY)

try:
    # Fetch the pre-seeded collection created by seed_database.py
    collection = chroma_client.get_collection(name="gov_policies")
except Exception as e:
    print(f"\n❌ Error: Could not find 'gov_policies' collection inside {DB_DIRECTORY}.")
    print("👉 Please execute 'python seed_database.py' first to populate the vector store archive.\n")
    raise e


# 📝 Define the Pydantic input schema matching incoming UI or UiPath payloads
class GrievancePayload(BaseModel):
    case_id: str
    raw_document_text: str


@app.get("/", tags=["System Status"])
async def root():
    """Simple health-check endpoint to verify server status during the hackathon demo."""
    return {
        "status": "ONLINE",
        "system": "Bookshelf AI Governance Engine",
        "database_connected": True,
        "active_collection": "gov_policies"
    }


@app.post("/api/v1/analyze-compliance", status_code=status.HTTP_200_OK, tags=["Compliance Auditor"])
async def analyze_compliance_case(payload: GrievancePayload):
    """
    Main execution endpoint called by UiPath Maestro Case state machines or web dashboards.
    Performs semantic vector matching across corporate books and drafts an authorized response strategy.
    """
    try:
        # 1. Input Log validation trace for the demo console window
        print(f"\n📥 [INCOMING CASE RECEIVED] ID: {payload.case_id}")
        print(f"📄 [RAW TEXT SNIPPET]: {payload.raw_document_text[:120]}...")

        # 2. Query Bookshelf AI's vector database using standard semantic distance matching
        search_results = collection.query(
            query_texts=[payload.raw_document_text],
            n_results=1  # Fetch the singular most contextually accurate matching clause
        )

        # Validate if a vector match was safely extracted from storage
        if not search_results['documents'] or len(search_results['documents'][0]) == 0:
            raise HTTPException(
                status_code=444, 
                detail="No matching regulatory framework found in database storage."
            )

        # Extract matching document text and its relational organizational schemas
        retrieved_document_chunk = search_results['documents'][0][0]
        metadata_origin = search_results['metadatas'][0][0]

        print(f"🔍 [VECTOR SEARCH SUCCESS] Matched: {metadata_origin.get('topic_label')}")

        # 3. Construct a high-integrity instruction system prompt for the Cloud LLM
        system_instruction = (
            "You are an elite Public Sector Compliance Officer operating under strict administrative review rules.\n"
            "Analyze the citizen's or business's grievance query utilizing strictly the provided legal policy context.\n"
            "Determine if the claim is valid or if there is an operational compliance violation.\n"
            "Then, draft a highly formal, precise official response letter to the applicant citing specific sections.\n"
            "You must respond strictly with a valid JSON object containing exactly these keys:\n"
            "- 'verdict': (Either 'CLAIM_VALID', 'NON_COMPLIANCE_DETECTED', or 'COMPLIANCE_BREACH')\n"
            "- 'confidence_score': (A floating decimal between 0.0 and 1.0 based on matching precision)\n"
            "- 'summary_of_findings': (A concise paragraph detailing the objective rationale behind the decision)\n"
            "- 'proposed_draft_letter': (The final structured, polite response letter text ready for a human to sign off on)"
        )

        user_content_prompt = f"Policy Context Reference:\n{retrieved_document_chunk}\n\nGrievance:\n{payload.raw_document_text}"

        # 4. Trigger the Cloud LLM execution loop using JSON enforcement configuration
        llm_response = openai_client.chat.completions.create(
            model="gpt-4o",
            response_format={"type": "json_object"},  # Force the model to output strict JSON structures
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_content_prompt}
            ],
            temperature=0.1  # Keep randomness low to prevent compliance hallucinations
        )

        # Extract string content from the API response object
        raw_json_string_from_ai = llm_response.choices[0].message.content
        
        # 5. Compile the final structured output response package to return to the requester
        structured_ai_metrics = json.loads(raw_json_string_from_ai)

        output_package = {
            "case_id": payload.case_id,
            "status": "PROCESSED_SUCCESS",
            "ai_analysis": {
                "verdict": structured_ai_metrics.get("verdict"),
                "confidence_score": structured_ai_metrics.get("confidence_score"),
                "summary_of_findings": structured_ai_metrics.get("summary_of_findings")
            },
            "retrieved_citations": [
                {
                    "source_document": metadata_origin.get("file_reference"),
                    "chapter_origin": metadata_origin.get("chapter_origin"),
                    "clause": metadata_origin.get("topic_label"),
                    "exact_text": retrieved_document_chunk
                }
            ],
            "proposed_draft_letter": structured_ai_metrics.get("proposed_draft_letter")
        }

        print(f"📤 [RESPONSE EXPORT READY] Verification metrics packaged successfully for {payload.case_id}\n")
        return output_package

    except Exception as e:
        print(f"❌ [INTERNAL SERVER ERROR LOG]: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    print("⚡ Launching Bookshelf AI API Server for UI Dashboards and UiPath Orchestration Layers...")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)