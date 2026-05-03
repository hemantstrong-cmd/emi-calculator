import streamlit as st

st.set_page_config(page_title="CMA Tool", layout="centered")

st.title("🏦 CMA Data Tool (Up to ₹10 Lakh Limits)")

# -------- Customer Profile --------
st.header("👤 Customer Details")
name = st.text_input("Customer Name")
business = st.text_input("Business Type")

# -------- P&L --------
st.header("📊 Profit & Loss")

sales = st.number_input("Sales / Turnover (₹)", min_value=0.0)
purchases = st.number_input("Purchases (₹)", min_value=0.0)
expenses = st.number_input("Other Expenses (₹)", min_value=0.0)

gross_profit = sales - purchases
net_profit = gross_profit - expenses

st.write(f"Gross Profit: ₹ {gross_profit}")
st.write(f"Net Profit: ₹ {net_profit}")

# -------- Balance Sheet --------
st.header("📑 Balance Sheet")

stock = st.number_input("Stock (₹)", min_value=0.0)
debtors = st.number_input("Debtors (₹)", min_value=0.0)
cash = st.number_input("Cash (₹)", min_value=0.0)

creditors = st.number_input("Creditors (₹)", min_value=0.0)
existing_loan = st.number_input("Existing Loan (₹)", min_value=0.0)

total_assets = stock + debtors + cash
total_liabilities = creditors + existing_loan
net_worth = total_assets - total_liabilities

st.write(f"Total Assets: ₹ {total_assets}")
st.write(f"Total Liabilities: ₹ {total_liabilities}")
st.write(f"Net Worth: ₹ {net_worth}")

# -------- CMA Analysis --------
st.header("📈 CMA Analysis")

working_capital = stock + debtors
margin = 0.25 * working_capital   # 25% margin
mpbf = working_capital - margin   # MPBF

current_ratio = total_assets / creditors if creditors != 0 else 0
drawing_power = working_capital - creditors

st.write(f"Working Capital: ₹ {working_capital}")
st.write(f"Margin (25%): ₹ {margin}")
st.write(f"MPBF (Eligible Limit): ₹ {mpbf}")
st.write(f"Drawing Power: ₹ {drawing_power}")
st.write(f"Current Ratio: {round(current_ratio,2)}")

# -------- Decision --------
st.header("📌 Decision Summary")

if current_ratio >= 1.33 and mpbf > 0:
    st.success("Eligible for Working Capital Limit ✅")
else:
    st.warning("Needs Review / Not Eligible ⚠️")
