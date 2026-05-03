import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="CMA Pro Tool", layout="wide")

st.title("🏦 CMA PRO TOOL (Bank Style - Up to ₹10 Lakh Limits)")

# -------- Customer --------
st.header("👤 Customer Details")
name = st.text_input("Customer Name")
business = st.text_input("Business Type")

# -------- P&L --------
st.header("📊 Profit & Loss")

sales = st.number_input("Sales", min_value=0.0)
purchases = st.number_input("Purchases", min_value=0.0)
expenses = st.number_input("Expenses", min_value=0.0)

gross_profit = sales - purchases
net_profit = gross_profit - expenses

# -------- Balance Sheet --------
st.header("📑 Balance Sheet")

stock = st.number_input("Stock", min_value=0.0)
debtors = st.number_input("Debtors", min_value=0.0)
cash = st.number_input("Cash", min_value=0.0)

creditors = st.number_input("Creditors", min_value=0.0)
loan = st.number_input("Loan", min_value=0.0)

total_assets = stock + debtors + cash
total_liabilities = creditors + loan
net_worth = total_assets - total_liabilities

# -------- CMA --------
working_capital = stock + debtors
margin = 0.25 * working_capital
mpbf = working_capital - margin
drawing_power = working_capital - creditors

current_ratio = total_assets / creditors if creditors != 0 else 0

# -------- Ratios --------
quick_assets = debtors + cash
quick_ratio = quick_assets / creditors if creditors != 0 else 0

gp_ratio = (gross_profit / sales * 100) if sales != 0 else 0
np_ratio = (net_profit / sales * 100) if sales != 0 else 0

stock_turnover = sales / stock if stock != 0 else 0
debtor_days = (debtors / sales * 365) if sales != 0 else 0

de_ratio = loan / net_worth if net_worth != 0 else 0

# -------- Projection --------
st.header("📈 3-Year Projection")

y1 = st.number_input("Year 1 Sales", min_value=0.0)
y2 = st.number_input("Year 2 Sales", min_value=0.0)
y3 = st.number_input("Year 3 Sales", min_value=0.0)

proj_df = pd.DataFrame({
    "Year": ["Year1", "Year2", "Year3"],
    "Sales": [y1, y2, y3]
})

# -------- Display --------
st.header("📊 CMA Summary")

st.write(f"Net Profit: ₹ {net_profit}")
st.write(f"Net Worth: ₹ {net_worth}")
st.write(f"MPBF: ₹ {mpbf}")
st.write(f"Drawing Power: ₹ {drawing_power}")
st.write(f"Current Ratio: {round(current_ratio,2)}")

st.header("📊 Ratios")

st.write(f"Quick Ratio: {round(quick_ratio,2)}")
st.write(f"Gross Profit %: {round(gp_ratio,2)}")
st.write(f"Net Profit %: {round(np_ratio,2)}")
st.write(f"Stock Turnover: {round(stock_turnover,2)}")
st.write(f"Debtor Days: {round(debtor_days,0)}")
st.write(f"Debt Equity Ratio: {round(de_ratio,2)}")

st.dataframe(proj_df)

# -------- Excel Export --------
buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:

    proj_df.to_excel(writer, sheet_name="Projection", index=False)

    summary = pd.DataFrame({
        "Particulars": ["Sales","Net Profit","Net Worth","MPBF","DP","Current Ratio"],
        "Values": [sales, net_profit, net_worth, mpbf, drawing_power, current_ratio]
    })
    summary.to_excel(writer, sheet_name="Summary", index=False)

    ratios = pd.DataFrame({
        "Ratio": ["Quick","GP%","NP%","Stock Turnover","Debtor Days","DE Ratio"],
        "Value": [quick_ratio,gp_ratio,np_ratio,stock_turnover,debtor_days,de_ratio]
    })
    ratios.to_excel(writer, sheet_name="Ratios", index=False)

st.download_button(
    "📥 Download CMA Report",
    buffer,
    file_name=f"CMA_{name}.xlsx"
)
