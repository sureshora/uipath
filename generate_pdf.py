import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    """Custom canvas to compute total page count dynamically and add headers/footers."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#4A5568"))
        
        # Header (Top of every page)
        self.drawString(54, 750, "GOVERNMENT OF INDIA • COMPLIANCE & AUDIT DIRECTION")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 742, 558, 742)
        
        # Footer (Bottom of every page)
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#718096"))
        self.drawString(54, 40, "CONFIDENTIAL — FOR ADMINISTRATIVE INTEL SYSTEMS ONLY")
        
        # Dynamic Page Count: "Page X of Y"
        page_string = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 40, page_string)
        self.restoreState()


def build_master_pdf(filename="National_Procurement_and_Governance_Omnibus_Act_2026.pdf"):
    # Target 0.75-inch margins
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=72,
        bottomMargin=72
    )

    styles = getSampleStyleSheet()
    
    # Define Custom Corporate Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#1A365D"),
        spaceAfter=12,
        alignment=1 # Center aligned
    )
    
    section_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#2C5282"),
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )
    
    clause_title_style = ParagraphStyle(
        'ClauseTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#2D3748"),
        spaceBefore=8,
        spaceAfter=2,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'ClauseBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#4A5568"),
        spaceAfter=8
    )

    story = []

    # Title Banner Block
    story.append(Spacer(1, 10))
    story.append(Paragraph("NATIONAL PROCUREMENT, GOVERNANCE, AND COMPLIANCE OMNIBUS ACT (2026)", title_style))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#1A365D"), spaceAfter=15))

    raw_data = [
        # SECTION 1
        {"section": "SECTION I: PUBLIC PROCUREMENT & TENDER COMPLIANCE", "clauses": [
            ("Clause 14-B (Subsidiary Financial Pooling)", "Registered legal entities under a parent holding corporation may leverage consolidated global audited statements to satisfy regional net-worth thresholds, irrespective of the physical location of the subsidiary's primary operating office."),
            ("Paragraph 4(2) (MSE Protections)", "Micro and Small Enterprises (MSEs) registered with the designated bodies shall be provided tender documents free of cost and are exempt from payment of Earnest Money Deposit (EMD)."),
            ("Rule 170(i) (Startup Turnover Relaxations)", "Ministries and Departments may relax conditions of prior turnover and prior experience for Startups recognized by DPIIT, subject to meeting quality standards."),
            ("Section 9.3 (Portal Glitches & Outages)", "In the event of verified hosting server unavailabilities or system lockouts within the final hour of a bid window, the competent authority shall issue a corrigendum extending the timeline by a minimum of 24 hours."),
            ("Paragraph 2 (Make in India Value Calculation)", "Class-I Local Supplier means a supplier whose goods, services, or works offered for procurement have local content equal to or more than 50% of the total value calculation."),
            ("Clause 6.1 (Consortium Aggregation)", "The combined financial turnovers of all joint venture partners shall be aggregated to determine compliance with the minimum financial eligibility parameters."),
            ("Section 4.7.2 (Minor Form Deviations)", "Non-material deviations, minor formatting variances, or alternative standardized banking language that doesn't restrict liability limits should not result in immediate technical disqualification."),
            ("Rule 166 (Proprietary Article Certificates)", "Proprietary Article Certificates shall only be granted when to the knowledge of the user department, no other alternative machine or equipment is available that fulfills the identical functional requirement."),
            ("Section 6 (MSE Price Preference Protocols)", "MSEs quoting price within price band of L1+15 percent shall also be allowed to supply a portion up to 25 percent of total tendered value by bringing down their price to L1 price."),
            ("Section 7.6 (Performance Security Release)", "Performance Security shall be refunded to the contractor without interest within a maximum period of 60 days after the date of completion of all contractual obligations, including defect liability timelines.")
        ]},
        # SECTION 2
        {"section": "SECTION II: PUBLIC GRIEVANCES & CITIZEN CHARTERS", "clauses": [
            ("Paragraph 12.2 (DBT Timeline Mandates)", "Once a direct subsidy application achieves 'Approved' status and passed technical verification, electronic fund transfers shall be finalized within a maximum of 45 days."),
            ("Rule 64 (Provisional Pension Allocations)", "Where a pension case cannot be finalized due to administrative lapses or missing historical verifications, the Head of Office shall immediately authorize a provisional pension to prevent hardship to the retiree."),
            ("Section 7(1) (RTI Statutory Limit)", "The Public Information Officer shall provide the requested information or reject the request with reasons within thirty days of the receipt of the application."),
            ("Section 224 (Encroachment Removal Protocols)", "The Commissioner or authorized officer shall cause any illegal structural projection, barrier, or encroachment upon a public street or public footpath to be removed without prior notice."),
            ("Section 4.1 (Utility Spike Disputations)", "Where a consumer disputes an exceptional billing spike, the utility shall suspend disconnection protocols and issue a provisional bill based on a 3-month rolling average while an inspector verifies the meter."),
            ("Section 8(a) (Welfare Medicine Diversion)", "Public hospital pharmacies are strictly prohibited from prioritizing paid inventory over mandated free-distribution welfare allocations for recognized BPL cardholders."),
            ("Section 12(1)(c) (RTE Disadvantaged Quotas)", "Private unaided schools shall admit in class I, to the extent of at least 25% of the strength of that class, children belonging to weaker sections and disadvantaged groups in the neighborhood."),
            ("Schedule B-3 (Senior Citizen Pass Turnaround)", "Concession concessions and specialty smart-cards for senior citizens shall be issued within fifteen working days from the date of submission of age-proof documents."),
            ("Section 9.4 (Low-Income Asset Floors)", "Exclusions based on existing property ownership shall not apply if the applicant's undivided ancestral landholding size is less than 300 square feet."),
            ("Clause 11.2 (Public Lighting Emergency Repairs)", "Public grid lighting faults along major avenues must be physically inspected and rectified within 48 hours of initial reporting due to public safety concerns.")
        ]},
        # SECTION 3
        {"section": "SECTION III: REGULATORY COMPLIANCE & LICENSING", "clauses": [
            ("Section 11(3) (Deemed Approval Windows)", "If the regulatory authority fails to communicate a final decision or feedback within a maximum of 90 days from receiving a complete EIA application, clearance shall be deemed granted."),
            ("Schedule 4 (Kitchen Chimney Code Parameters)", "Ventilation and exhaust systems must ensure sufficient airflow to prevent grease accumulation; directional routing constraints are restricted to avoiding intake contamination zones only."),
            ("Section 40 (Financial Sovereign Localization)", "All banking and payment processing entities shall ensure that the entire end-to-end data transaction trail is processed and stored exclusively within data servers located inside the borders of India."),
            ("Annexure 4 (Pharmaceutical Zonal Grading)", "Moisture and humidity tolerances for secondary packaging storage areas are subject to ambient standard controls and shall not be evaluated against sterile core environmental contamination metrics."),
            ("Section 4.2 (Fire NOC Evaluation Window)", "Upon receiving a certified third-party fire equipment safety audit, the municipal fire authority shall verify documents and issue or deny the NOC within thirty working days."),
            ("Rule 6.3 (Digital Prescription Authentications)", "Registered medical practitioners are authorized to issue digital prescriptions via electronic portals using valid electronic or biometric signatures protected under the Information Technology Act."),
            ("Rule 22 (Aviation Airspace Categorization)", "Operations within a designated Yellow Zone require explicit localized Air Traffic Control authorization, upon submission of which flight permissions shall be systematically cleared."),
            ("Section 9(2) (Mineral Pithead Calculations)", "The holder of a mining lease shall pay royalty in respect of any mineral removed from the leased area calculated based on the Average Pithead Price published by the Indian Bureau of Mines."),
            ("Criterion 4.1 (Digital Repository Assets)", "Library resource metrics shall value digital repository access, cloud database subscriptions, and virtual terminal nodes on par with physical textbook inventories."),
            ("Section 65 (Emergency Work Hour Exemptions)", "The state government or competent labor authority may issue written orders exempting any factory from weekly working hour restrictions during exceptional seasonal demand peaks, up to a maximum cap of 60 hours.")
        ]}
    ]

    # Dynamically structure layout blocks
    for block in raw_data:
        story.append(Spacer(1, 10))
        story.append(Paragraph(block["section"], section_style))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E1"), spaceAfter=10, spaceBefore=4))
        
        for title, text in block["clauses"]:
            story.append(Paragraph(title, clause_title_style))
            story.append(Paragraph(text, body_style))
            story.append(Spacer(1, 4))
            
    # Compile Flowables into PDF layout using dynamic page canvas
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"✅ Success! Generated structured master file: '{filename}'")

if __name__ == "__main__":
    build_master_pdf()