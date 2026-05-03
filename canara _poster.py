import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

st.title("🏦 Canara Bank Official Poster (PDF Generator)")

# Inputs
branch = st.text_input("Branch Name", "Etah Branch")
subject = st.text_input("Subject", "CASA Drive Notice")
content = st.text_area("Content", "All staff are requested to participate in CASA/PLI drive.")
authority = st.text_input("Issued By", "Branch Manager")

def create_pdf():
    file_name = "canara_poster.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=A4)

    styles = getSampleStyleSheet()
    style = styles["Normal"]
    title_style = styles["Title"]

    elements = []

    # Header
    elements.append(Paragraph("CANARA BANK", title_style))
    elements.append(Paragraph("OFFICIAL NOTICE / CIRCULAR", style))
    elements.append(Spacer(1, 12))

    # Branch
    elements.append(Paragraph(f"<b>Branch:</b> {branch}", style))
    elements.append(Spacer(1, 12))

    # Subject
    elements.append(Paragraph(f"<b>Subject:</b> {subject}", style))
    elements.append(Spacer(1, 12))

    # Content
    elements.append(Paragraph(content, style))
    elements.append(Spacer(1, 20))

    # Authority
    elements.append(Paragraph(f"<b>Issued By:</b> {authority}", style))

    doc.build(elements)
    return file_name

if st.button("Generate PDF"):
    file = create_pdf()
    with open(file, "rb") as f:
        st.download_button("📥 Download PDF", f, file_name="Canara_Bank_Notice.pdf")
