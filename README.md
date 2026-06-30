# 📚 Bookshelf AI — Enterprise Governance Core

> **Hackathon Submission:** Track 1 — UiPath Maestro Case
> **Core Philosophy:** 🛡️ Human Validation at Input • 🔐 Human Authorization at Output
> **Built With:** Coding Agents (Cursor / Claude Code)

Bookshelf AI is an AI-native Knowledge Operating System (**KnowledgeOS**) engineered to bridge the gap between unstructured compliance documents and enterprise automation.

By decoupling the core AI vector brain from execution workflows, Bookshelf AI acts as a high-integrity **RAG (Retrieval-Augmented Generation)** engine that provides traceably audited compliance matching for **UiPath Maestro Case** pipelines.

---

# 🎯 1. The Core Business Problem

In regulated industries and the public sector, pure AI automation faces a critical blocker:

## The Liability & Hallucination Bottleneck

### 1. The Accountability Vacuum

AI models cannot legally assume liability for compliance auditing errors or mistaken legal determinations.

### 2. The Context Blindness

General LLMs lack specialized, localized enterprise or statutory domain knowledge, resulting in operational hallucinations.

### 3. The Auditability Mandate

Regulatory compliance requires a strict, visible, and transparent audit trail showing **exactly why** an action or decision was made.

---

# ✅ The Solution

Bookshelf AI solves the liability gap through an unshakeable **Centaur Workflow (Human-in-the-Loop).**

Instead of executing operations blindly, our FastAPI core:

* Matches incoming case vectors against official immutable text schemas.
* Stores and retrieves knowledge from a local vector database.
* Generates traceably cited responses.
* Hands over execution to **UiPath Action Center**.
* Enables qualified humans to authorize or reject workflows before live deployment.

---

# 🏗️ 2. System Architecture & Folder Layout

The project enforces a strict separation of concerns.

```text
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
```

---

# 🚀 3. Installation & Local Setup

Follow these steps to launch the platform locally.

## Step 1: Clone & Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

## Step 2: Configure OpenAI API Key

### macOS / Linux

```bash
export OPENAI_API_KEY="your-api-key"
```

### Windows Command Prompt

```cmd
set OPENAI_API_KEY="your-api-key"
```

---

## Step 3: Generate the Master Policy PDF

```bash
python backend/generate_pdf.py
```

This generates the publication-grade compliance handbook.

---

## Step 4: Seed the Vector Database

```bash
python backend/seed_database.py
```

This process:

* Parses the PDF
* Chunks text intelligently
* Creates embeddings
* Stores vectors into ChromaDB

---

## Step 5: Start the FastAPI Server

```bash
python backend/main.py
```

Server will start at:

```text
http://127.0.0.1:8000
```

---

# 🎨 4. Running the Complete System Demo

For a live end-to-end demo:

### 1. Keep FastAPI Running

```bash
python backend/main.py
```

---

### 2. Open Dashboard

Navigate to:

```text
frontend/index.html
```

Open directly in your browser.

---

### 3. Select an Evaluation Case

Example:

```text
Tender Ref #MND-992.

Apex Infra was disqualified because audited financials
were from our Maharashtra subsidiary instead of our
local Chennai office.

Our parent company meets all global net-worth criteria.
```

---

### 4. Run Audit Evaluation

Click:

```text
Run Audit Evaluation
```

Bookshelf AI will:

* Query ChromaDB
* Retrieve matching clauses
* Request GPT-4o analysis
* Produce cited findings
* Generate a draft response
* Present human approval options

---

# 🛰️ 5. API Reference for UiPath Maestro Case

## Endpoint

```http
POST /api/v1/analyze-compliance
```

Primary endpoint monitored by UiPath Maestro Case state machines.

---

## Request Payload

```json
{
  "case_id": "CASE-2026-TENDER-992",
  "raw_document_text": "Tender Ref #MND-992. Apex Infra was disqualified because audited financials were from our Maharashtra subsidiary instead of our local Chennai office. Our parent company meets all global net-worth criteria."
}
```

---

## Response Payload

```json
{
  "case_id": "CASE-2026-TENDER-992",
  "status": "PROCESSED_SUCCESS",

  "ai_analysis": {

    "verdict": "CLAIM_VALID",

    "confidence_score": 0.96,

    "summary_of_findings":
    "The applicant legal entity leverages Clause 14-B
    (Subsidiary Financial Pooling) under the Omnibus Act,
    which permits regional net-worth validation via
    consolidated global corporate holding records."

  },

  "retrieved_citations": [

    {

      "source_document":
      "National_Procurement_and_Governance_Omnibus_Act_2026.pdf",

      "chapter_origin":
      "SECTION I: PUBLIC PROCUREMENT & TENDER COMPLIANCE",

      "clause":
      "Clause 14-B (Subsidiary Financial Pooling)",

      "exact_text":

      "Registered legal entities under a parent holding
      corporation may leverage consolidated global audited
      statements to satisfy regional net-worth thresholds."

    }

  ],

  "proposed_draft_letter":

  "Dear Applicant,

  Reference case CASE-2026-TENDER-992,

  Your claim under Clause 14-B has been processed
  and validated.

  The technical disqualification is revoked."

}
```

---

# 📈 6. Commercial SaaS Scalability Roadmap

Bookshelf AI is structured to evolve into a full multi-tenant enterprise SaaS platform.

## 1. Distributed Vector Compute

Replace local ChromaDB with:

* Pinecone
* Milvus
* Weaviate

Benefits:

* Horizontal scaling
* High availability
* Faster retrieval

---

## 2. Multi-Tenant Isolation

Introduce:

* JWT Authentication
* Clerk
* Auth0

Capabilities:

* Tenant isolation
* Workspace separation
* Secure namespace routing

---

## 3. Asynchronous Object Pipelines

Move document storage to:

* Amazon S3
* MinIO

Process ingestion using:

* Celery
* Redis workers

Benefits:

* Background parsing
* Faster uploads
* Parallel processing

---

## 4. Monetization Triggers

Integrate:

* Stripe Billing
* Usage Metering
* Rate Limiting

Features:

* API subscription plans
* Usage quotas
* Enterprise licensing
* Pay-as-you-scale pricing

---

# 🛡️ Bookshelf AI Philosophy

> **Human Validation at Input**
> Every document entering the system is reviewed, structured, and indexed with traceable metadata.

> **Human Authorization at Output**
> Every AI recommendation is explainable, cited, auditable, and approved by humans before execution.

Bookshelf AI does not replace enterprise governance.

**It augments it with trustworthy AI.**
