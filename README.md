<div align="center">

# 🚀 RightNowAudit
### AI-Powered Compliance Automation Platform

### 🏆 UiPath Hackathon Submission – Track 1 (Maestro)

<img src="https://img.shields.io/badge/UiPath-Maestro-orange?style=for-the-badge" />
<img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge" />
<img src="https://img.shields.io/badge/KnowledgeOS-RAG-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/AI-Human--in--the--Loop-red?style=for-the-badge" />
<img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge" />

---

### 🌐 Live Demo

## https://rightnowaudit.com

---

**Enterprise AI Compliance • KnowledgeOS • Human-in-the-Loop • Explainable AI**

</div>

---

# 📖 Overview

RightNowAudit is an **AI-powered Enterprise Compliance Automation Platform** that transforms complex policy documents, regulations, and grievance cases into explainable, auditable, and human-approved decisions.

Unlike traditional Generative AI systems that can hallucinate or provide unverifiable responses, RightNowAudit combines **Retrieval-Augmented Generation (RAG)**, **KnowledgeOS**, **UiPath Maestro**, and **Human Authorization** to deliver transparent, traceable, and enterprise-ready compliance automation.

---

# 🎯 Business Problem

Organizations spend significant time reviewing:

- 📄 Compliance Cases
- 📄 Tender Documents
- 📄 Internal Policies
- 📄 Government Regulations
- 📄 Audit Reports
- 📄 Employee Grievances

Manual reviews are:

- ❌ Slow
- ❌ Expensive
- ❌ Inconsistent
- ❌ Difficult to Audit

---

# ✅ Solution

RightNowAudit automates compliance analysis while keeping humans in control.

The platform:

✅ Understands uploaded cases

✅ Searches enterprise knowledge

✅ Retrieves supporting regulations

✅ Generates explainable AI recommendations

✅ Produces editable response drafts

✅ Routes the case for Human Approval

✅ Maintains a complete audit trail

---

# ✨ Key Features

- 🤖 AI-powered Compliance Analysis
- 📚 Enterprise KnowledgeOS (RAG)
- 🔎 Policy & Regulation Matching
- 📊 Confidence Score
- 📑 Knowledge Source Citations
- ✍️ Editable Response Drafts
- 👨‍💼 Human Approval Workflow
- 📜 Complete Audit Trail
- 🌐 REST API Integration
- ⚡ Enterprise Ready

---

# 🏗️ Solution Architecture

```
                  User
                    │
                    ▼
        ┌────────────────────┐
        │   UiPath Maestro   │
        └────────────────────┘
                    │
                    ▼
        ┌────────────────────┐
        │  AI Compliance     │
        │     Workflow       │
        └────────────────────┘
                    │
     ┌──────────────┼──────────────┐
     ▼              ▼              ▼

 Coding Agent   Agent Builder   KnowledgeOS

     │              │              │
     └──────────────┼──────────────┘
                    ▼
          Compliance Decision
                    │
                    ▼
           Human Authorization
                    │
                    ▼
             Final Audit Report
```

---

# 🤖 AI Agents Used

## ✅ Coding Agents

- API Integration
- Compliance Logic
- Business Rules
- Data Processing
- Report Generation
- Knowledge Retrieval

---

## ✅ UiPath Agent Builder (Low-Code Agents)

- Natural Language Understanding
- Policy Interpretation
- Compliance Reasoning
- Decision Summarization
- Recommendation Generation

---

# 🧩 UiPath Components Used

- ✅ UiPath Studio
- ✅ UiPath Maestro
- ✅ REFramework
- ✅ Sequences
- ✅ Flowcharts
- ✅ State Machines
- ✅ Invoke Workflow
- ✅ HTTP Request Activities
- ✅ Excel Activities
- ✅ PDF Activities
- ✅ Word Activities
- ✅ JSON Activities
- ✅ Data Tables
- ✅ Logging
- ✅ Exception Handling
- ✅ Orchestrator Assets *(Optional)*
- ✅ Orchestrator Queues *(Optional)*

---

# 💻 Technology Stack

| Layer | Technology |
|--------|------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | FastAPI |
| AI | OpenAI |
| Knowledge | KnowledgeOS |
| Vector Database | ChromaDB |
| Database | SQLite / PostgreSQL |
| Automation | UiPath Maestro |
| API | REST API |

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/rightnowaudit.git
```

## Install Dependencies

```bash
pip install -r backend/requirements.txt
```

## Configure Environment

Set your API Keys and application configuration.

## Seed Knowledge Base

```bash
python backend/seed_database.py
```

## Run Backend

```bash
python backend/main.py
```

---

# 📂 Project Structure
## 🏗️ System Architecture & Folder Layout

The project enforces a strict separation of concerns between core logic, backend data vectors, and front-end management.


bookshelf-ai-governance/
│
├── backend/                          # 🧠 Backend API Core
│   ├── bookshelf_knowledge_base/     # ChromaDB vector collections
│   ├── generate_pdf.py               # Master Policy PDF Generator
│   ├── seed_database.py              # PDF Parser & Vector Embedding Engine
│   ├── main.py                       # FastAPI REST Server
│   └── requirements.txt              # Python module requirements
│
├── frontend/                         # 🎨 Front-End Interface
│   └── index.html                    # Tailwind Compliance Dashboard
│
├── uipath-automation/                 # 🤖 UiPath Orchestration Components
│   ├── BookShelfAI-Compliance/       # 📊 Primary Case Verification Workflow Pipeline
│   └── BookShelfAI/                  # 📡 Standard REST Reusability API Connector Sequence
│
└── README.md                         # Product Documentation
💡 UiPath Project Breakdown: The automation architecture is split into two distinct, decoupled packages:

BookShelfAI-Compliance: Handles high-level case lifecycle checks, error processing, and validation pipelines.

BookShelfAI: Provides clean, reusable API automation snippets that connect raw text blocks straight to our FastAPI gateway endpoints.

# 📤 Input

- 📄 PDF
- 📄 DOCX
- 📄 TXT
- 📄 Compliance Cases
- 📄 Tender Documents

---

# 📥 Output

- ✅ Compliance Verdict
- ✅ Confidence Score
- ✅ Supporting Evidence
- ✅ Policy Citations
- ✅ Draft Response Letter
- ✅ Audit Report

---

# 👨‍⚖️ Human-in-the-Loop

## Human Validation at Input

Every document is validated before AI processing.

## Human Authorization at Output

Every AI recommendation is reviewed and approved by a human before execution.

---

# 📈 Future Roadmap

- ☁️ Multi-Tenant SaaS
- 🌍 Enterprise Knowledge Marketplace
- 📱 Mobile Companion
- 🤖 Autonomous Compliance Agents
- 📊 Analytics Dashboard
- 🔗 ERP Integration
- 🛰️ Cloud Deployment

---

# 📜 License

Licensed under the **MIT License**.

---

# 👨‍💻 Author

**Suresh Kumar Thulasi Ram**

Founder — **AdmnWizard AI LLC**

### 🌐 Live Demo

https://rightnowaudit.com

---

<div align="center">

### ⭐ If you found this project useful, please give it a Star!

Made with ❤️ using **UiPath • FastAPI • KnowledgeOS • RAG • AI**

</div>
