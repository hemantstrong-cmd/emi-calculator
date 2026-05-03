import streamlit as st
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import io

st.title("🏦 CMA Full Tool (3-Year + Formats + PDF)")

# -------- CUSTOMER --------
name = st.text_input("Customer Name")

# -------- P&L (3 Years) --------
st.header("📊 Profit & Loss (3 Years)")

sales1 = st.number_input("Sales Year 1")
sales2 = st.number_input("Sales Year 2")
sales3 = st.number_input("Sales Year 3")

profit1 = st.number_input("Profit Year 1")
profit2 = st.number_input("Profit Year 2")
profit3 = st.number_input("Profit Year 3")

pl_df = pd.DataFrame({
    "Year": ["Y1","Y2","Y3"],
    "Sales": [sales1,sales2,sales3],
    "Profit": [profit1,profit2,profit3]
})

# -------- BALANCE SHEET --------
st.header("📑 Balance Sheet (3 Years)")

assets1 = st.number_input("Assets Y1")
assets2 = st.number_input("Assets Y2")
assets3 = st.number_input("Assets Y3")

liab1 = st.number_input("Liabilities Y1")
liab2 = st.number_input("Liabilities Y2")
liab3 = st.number_input("Liabilities Y3")

bs_df = pd.DataFrame({
    "Year":["Y1","Y2","Y3"],
    "Assets":[assets1,assets2,assets3],
    "Liabilities":[liab1,liab2,liab3]
})

# -------- CMA FORMAT V (MPBF) --------
st.header("📈 MPBF Calculation")

stock = st.number_input("Stock")
debtors = st.number_input("Debtors")
creditors = st.number_input("Creditors")

wc = stock + debtors
margin = wc * 0.25
mpbf = wc - margin

st.write(f"MPBF: ₹ {mpbf}")

# -------- RATIOS --------
current_ratio = assets3 / creditors if creditors != 0 else 0
st.write(f"Current Ratio: {round(current_ratio,2)}")

# -------- DISPLAY TABLES --------
st.subheader("P&L Statement")
st.dataframe(pl_df)

st.subheader("Balance Sheet")
st.dataframe(bs_df)

# -------- PDF GENERATION --------
def create_pdf():
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    elements = []
    elements.append(Paragraph(f"CMA Report - {name}", styles['Title']))
    elements.append(Paragraph(f"MPBF: {mpbf}", styles['Normal']))
    elements.append(Paragraph(f"Current Ratio: {current_ratio}", styles['Normal']))

    doc.build(elements)
    buffer.seek(0)
    return buffer

pdf = create_pdf()

st.download_button(
    label="📥 Download CMA PDF",
    data=pdf,
    file_name="CMA_Report.pdf",
    mime="application/pdf"
)
