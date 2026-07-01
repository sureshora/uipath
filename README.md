# 📚 Bookshelf AI — Enterprise Governance Core

> **Hackathon Submission:** Track 1 — UiPath Maestro Case  
> **Core Philosophy:** 🛡️ Human Validation at Input • 🔐 Human Authorization at Output  
> **Built With:** Coding Agents (Cursor / Claude Code)

Bookshelf AI is an AI-native Knowledge Operating System (**KnowledgeOS**) engineered to bridge the gap between unstructured compliance documents and enterprise automation.

By decoupling the core AI vector brain from execution workflows, Bookshelf AI acts as a high-integrity **RAG (Retrieval-Augmented Generation)** engine that provides traceably audited compliance matching for **UiPath Maestro Case** pipelines.

---

# 🎯 1. The Core Business Problem

In highly regulated industries and the public sector, pure generative AI automation faces a critical blocker:

## The Liability & Hallucination Bottleneck

### 1. The Accountability Vacuum
AI models cannot legally assume liability for compliance auditing errors or mistaken statutory determinations.

### 2. The Context Blindness
General LLMs lack specialized, localized enterprise or statutory domain knowledge, resulting in operational hallucinations.

### 3. The Auditability Mandate
Regulatory compliance requires a strict, visible, and transparent audit trail showing **exactly why** an action or decision was made.

---

# ✅ The Solution

Bookshelf AI solves the liability gap through an unshakeable **Centaur Workflow (Human-in-the-Loop).**

Instead of executing downstream operations blindly, our FastAPI core:
* Matches incoming case vectors against official immutable text schemas.
* Stores and retrieves knowledge securely from a local vector database.
* Generates traceably cited and referenced responses.
* Hands over structured execution parameters to **UiPath Maestro Case** state machines and **UiPath Action Center**.
* Enables qualified human operators to explicitly authorize or reject workflows before live system deployment.

---

# 🏗️ 2. System Architecture & Folder Layout

The project enforces a strict separation of concerns between core logic, backend data vectors, and front-end management.


bookshelf-ai-governance/
│
├── backend/
│   ├── bookshelf_knowledge_base/
│   │      └── ChromaDB vector collections
│   │
│   ├── generate_pdf.py
│   │      └── Creates master Policy Act PDF
│   │
│   ├── seed_database.py
│   │      └── Parses PDF & creates vector embeddings
│   │
│   ├── main.py
│   │      └── FastAPI server with REST APIs
│   │
│   └── requirements.txt
│          └── Backend dependencies
│
├── frontend/
│   └── index.html
│          └── Tailwind compliance dashboard
│
└── README.md
       └── Project documentation

🚀 3. Installation & Local Setup
Follow these steps to launch the platform locally.

Step 1: Clone & Install Dependencies
Bash
pip install -r backend/requirements.txt
Step 2: Configure OpenAI API Key
macOS / Linux
Bash
export OPENAI_API_KEY="your-api-key"
Windows Command Prompt
DOS
set OPENAI_API_KEY="your-api-key"
Step 3: Generate the Master Policy PDF
Bash
python backend/generate_pdf.py
This generates the publication-grade compliance reference handbook.

Step 4: Seed the Vector Database
Bash
python backend/seed_database.py
This data pipeline:

Parses the generated Policy PDF.

Chunks data segments intelligently.

Generates contextual mathematical text embeddings.

Stores index records locally within ChromaDB collections.

Step 5: Start the FastAPI Server
Bash
python backend/main.py
The server will start locally at:

Plaintext
[http://127.0.0.1:8000](http://127.0.0.1:8000)
🎨 4. Running the Complete System Demo
For a live end-to-end sandbox demonstration:

1. Keep FastAPI Running
Bash
python backend/main.py
2. Open Dashboard
Navigate to frontend/index.html and launch it directly in any modern browser.

3. Select an Evaluation Case
Input your test case details into the application payload target. For example:

Plaintext
Tender Ref #MND-992.

Apex Infra was disqualified because audited financials
were from our Maharashtra subsidiary instead of our
local Chennai office.

Our parent company meets all global net-worth criteria.
4. Run Audit Evaluation
Click "Run Audit Evaluation". Bookshelf AI will:

Query ChromaDB vector embeddings.

Retrieve matching policy clauses.

Process the content using GPT-4o analysis.

Produce traceably cited findings.

Generate a structured response sheet with human authorization action buttons.

🛰️ 5. API Reference for UiPath Maestro Case
Endpoint
HTTP
POST /api/v1/analyze-compliance
This is the primary endpoint monitored by your active UiPath Maestro Case orchestration sequence.

Request Payload
JSON
{
  "case_id": "CASE-2026-TENDER-992",
  "raw_document_text": "Tender Ref #MND-992. Apex Infra was disqualified because audited financials were from our Maharashtra subsidiary instead of our local Chennai office. Our parent company meets all global net-worth criteria."
}
Response Payload
JSON
{
  "case_id": "CASE-2026-TENDER-992",
  "status": "PROCESSED_SUCCESS",
  "ai_analysis": {
    "verdict": "CLAIM_VALID",
    "confidence_score": 0.96,
    "summary_of_findings": "The applicant legal entity leverages Clause 14-B (Subsidiary Financial Pooling) under the Omnibus Act, which permits regional net-worth validation via consolidated global corporate holding records."
  },
  "retrieved_citations": [
  🚀 3. Installation & Local Setup
Follow these steps to launch the platform locally.

Step 1: Clone & Install Dependencies
Bash
pip install -r backend/requirements.txt
Step 2: Configure OpenAI API Key
macOS / Linux
Bash
export OPENAI_API_KEY="your-api-key"
Windows Command Prompt
DOS
set OPENAI_API_KEY="your-api-key"
Step 3: Generate the Master Policy PDF
Bash
python backend/generate_pdf.py
This generates the publication-grade compliance reference handbook.

Step 4: Seed the Vector Database
Bash
python backend/seed_database.py
This data pipeline:

Parses the generated Policy PDF.

Chunks data segments intelligently.

Generates contextual mathematical text embeddings.

Stores index records locally within ChromaDB collections.

Step 5: Start the FastAPI Server
Bash
python backend/main.py
The server will start locally at:

Plaintext
[http://127.0.0.1:8000](http://127.0.0.1:8000)
🎨 4. Running the Complete System Demo
For a live end-to-end sandbox demonstration:

1. Keep FastAPI Running
Bash
python backend/main.py
2. Open Dashboard
Navigate to frontend/index.html and launch it directly in any modern browser.

3. Select an Evaluation Case
Input your test case details into the application payload target. For example:

Plaintext
Tender Ref #MND-992.

Apex Infra was disqualified because audited financials
were from our Maharashtra subsidiary instead of our
local Chennai office.

Our parent company meets all global net-worth criteria.
4. Run Audit Evaluation
Click "Run Audit Evaluation". Bookshelf AI will:

Query ChromaDB vector embeddings.

Retrieve matching policy clauses.

Process the content using GPT-4o analysis.

Produce traceably cited findings.

Generate a structured response sheet with human authorization action buttons.

🛰️ 5. API Reference for UiPath Maestro Case
Endpoint
HTTP
POST /api/v1/analyze-compliance
This is the primary endpoint monitored by your active UiPath Maestro Case orchestration sequence.

Request Payload
JSON
{
  "case_id": "CASE-2026-TENDER-992",
  "raw_document_text": "Tender Ref #MND-992. Apex Infra was disqualified because audited financials were from our Maharashtra subsidiary instead of our local Chennai office. Our parent company meets all global net-worth criteria."
}
Response Payload
JSON
{
  "case_id": "CASE-2026-TENDER-992",
  "status": "PROCESSED_SUCCESS",
  "ai_analysis": {
    "verdict": "CLAIM_VALID",
    "confidence_score": 0.96,
    "summary_of_findings": "The applicant legal entity leverages Clause 14-B (Subsidiary Financial Pooling) under the Omnibus Act, which permits regional net-worth validation via consolidated global corporate holding records."
  },
  "retrieved_citations": [
    {
      "source_document": "National_Procurement_and_Governance_Omnibus_Act_2026.pdf",
      "chapter_origin": "SECTION I: PUBLIC PROCUREMENT & TENDER COMPLIANCE",
      "clause": "Clause 14-B (Subsidiary Financial Pooling)",
      "exact_text": "Registered legal entities under a parent holding corporation may leverage consolidated global audited statements to satisfy regional net-worth thresholds."
    }
  ],
  "proposed_draft_letter": "Dear Applicant,\n\nReference case CASE-2026-TENDER-992,\n\nYour claim under Clause 14-B has been processed and validated.\n\nThe technical disqualification is revoked."
}
📈 6. Commercial SaaS Scalability Roadmap
Bookshelf AI is architected to easily transition from a local workspace prototype into a highly distributed multi-tenant enterprise SaaS tool.

1. Distributed Vector Compute
Replace the local memory ChromaDB instance with a production-grade cloud solution like Pinecone, Milvus, or Weaviate to ensure high availability, horizontal chunk replication, and faster millisecond search metrics over millions of active corporate forms.

2. Multi-Tenant Isolation
Introduce JWT Identity Architecture paired with authenticators like Clerk or Auth0 to enforce data perimeter security boundaries, tenant resource segmentation, and custom workspace namespace routing rules.

3. Asynchronous File Storage & Compute
Offload file ingestion patterns into dedicated Amazon S3 or MinIO storage clouds. Run background ingestion queues using asynchronous task distributors like Celery powered by a Redis cache backend for real-time parallel stream handling.

4. Monetization Triggers
Integrate a transactional billing service framework like Stripe Billing with accurate usage metering blocks and custom request rate limiters to run transparent subscription management rules, enterprise licensing parameters, and scalable API pricing options.

🛡️ Bookshelf AI Philosophy
Human Validation at Input

Every document entering the system is reviewed, structured, and indexed with traceable metadata.

Human Authorization at Output

Every AI recommendation is explainable, cited, auditable, and approved by humans before execution.

Bookshelf AI does not replace enterprise governance. It augments it with trustworthy, deterministic AI.

Author & Project Acknowledgements
Suresh Kumar Thulasi Ram

Founder, AdminWizard AI LLC

Built using the UiPath Platform, FastAPI backend services, and modern Retrieval-Augmented Generation frameworks.
  ],
  "proposed_draft_letter": "Dear Applicant,\n\nReference case CASE-2026-TENDER-992,\n\nYour claim under Clause 14-B has been processed and validated.\n\nThe technical disqualification is revoked."
}
📈 6. Commercial SaaS Scalability Roadmap
Bookshelf AI is architected to easily transition from a local workspace prototype into a highly distributed multi-tenant enterprise SaaS tool.

1. Distributed Vector Compute
Replace the local memory ChromaDB instance with a production-grade cloud solution like Pinecone, Milvus, or Weaviate to ensure high availability, horizontal chunk replication, and faster millisecond search metrics over millions of active corporate forms.

2. Multi-Tenant Isolation
Introduce JWT Identity Architecture paired with authenticators like Clerk or Auth0 to enforce data perimeter security boundaries, tenant resource segmentation, and custom workspace namespace routing rules.

3. Asynchronous File Storage & Compute
Offload file ingestion patterns into dedicated Amazon S3 or MinIO storage clouds. Run background ingestion queues using asynchronous task distributors like Celery powered by a Redis cache backend for real-time parallel stream handling.

4. Monetization Triggers
Integrate a transactional billing service framework like Stripe Billing with accurate usage metering blocks and custom request rate limiters to run transparent subscription management rules, enterprise licensing parameters, and scalable API pricing options.

🛡️ Bookshelf AI Philosophy
Human Validation at Input

Every document entering the system is reviewed, structured, and indexed with traceable metadata.

Human Authorization at Output

Every AI recommendation is explainable, cited, auditable, and approved by humans before execution.

Bookshelf AI does not replace enterprise governance. It augments it with trustworthy, deterministic AI.

Author & Project Acknowledgements
Suresh Kumar Thulasi Ram

Founder, AdminWizard AI LLC

Built using the UiPath Platform, FastAPI backend services, and modern Retrieval-Augmented Generation frameworks.


