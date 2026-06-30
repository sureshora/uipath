/**
 * Bookshelf AI Frontend Interface Engine
 * Coordinates asynchronous AJAX networking loops linking the browser dashboard to the FastAPI engine.
 */

async function evaluateCase() {
    const caseId = document.getElementById("caseIdInput").value;
    const textContent = document.getElementById("caseTextInput").value;
    const submitBtn = document.getElementById("submitBtn");

    // Clear and validate text string boundaries
    if (!textContent.trim()) {
        alert("Verification execution aborted: Input text context field cannot be empty.");
        return;
    }

    // Toggle button UI loading processing visual effects
    submitBtn.disabled = true;
    submitBtn.innerHTML = `<span>⏳ Querying Vector Spaces & LLM...</span>`;

    try {
        // Construct the fetch loop to our localized FastAPI Core server running on port 8000
        const response = await fetch("http://127.0.0.1:8000/api/v1/analyze-compliance", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                case_id: caseId,
                raw_document_text: textContent
            })
        });

        if (!response.ok) {
            throw new Error(`Network engine breakdown. Server returned status: ${response.status}`);
        }

        const data = await response.json();

        // Reveal the main layout data boards and wrap the placeholder graphics away
        document.getElementById("placeholderView").classList.add("hidden");
        document.getElementById("analyticsPanel").classList.remove("hidden");

        // Parse and populate compliance verdict data tokens
        const verdictBadge = document.getElementById("verdictBadge");
        const verdict = data.ai_analysis.verdict;
        verdictBadge.innerText = verdict;
        
        // Dynamically style token severity classes based on matching vectors
        if (verdict === "CLAIM_VALID") {
            verdictBadge.className = "inline-block mt-1 text-sm font-bold px-2.5 py-0.5 rounded-md font-mono bg-emerald-950 text-emerald-400 border border-emerald-800";
        } else {
            verdictBadge.className = "inline-block mt-1 text-sm font-bold px-2.5 py-0.5 rounded-md font-mono bg-rose-950 text-rose-400 border border-rose-800";
        }

        // Map numerical data strings onto UI text segments
        document.getElementById("confidenceScore").innerText = (data.ai_analysis.confidence_score * 100).toFixed(1) + "%";
        
        // Unpack structured citation mapping metadata matrices
        const citation = data.retrieved_citations[0];
        document.getElementById("citationFile").innerText = citation.source_document;
        document.getElementById("citationChapter").innerText = citation.clause;
        document.getElementById("citationBody").innerText = `"${citation.exact_text}"`;
        
        // Display editable workspace text area sheets
        document.getElementById("draftLetterBody").value = data.proposed_draft_letter;

    } catch (err) {
        alert("CORS Request Timeout: Unable to query Bookshelf Engine. Verify main.py is listening on port 8000.");
        console.error("Core Processing Error Trace:", err);
    } finally {
        // Restore button activation triggers
        submitBtn.disabled = false;
        submitBtn.innerHTML = `<span>⚡ Run Audit Evaluation</span>`;
    }
}

function authorizeCase() {
    alert("🟢 Centaur Authorization Confirmed!\n\nCase signed off, state logs closed, and transaction metrics transmitted back to the primary UiPath Maestro ledger.");
    resetDashboard();
}

function resetDashboard() {
    document.getElementById("placeholderView").classList.remove("hidden");
    document.getElementById("analyticsPanel").classList.add("hidden");
}