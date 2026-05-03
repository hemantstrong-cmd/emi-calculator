import streamlit as st
import pandas as pd

st.set_page_config(page_title="EMI Calculator", layout="centered")

st.title("🏦 EMI Calculator")

# Inputs
loan = st.number_input("Loan Amount (₹)", min_value=1.0, value=100000.0)
rate = st.number_input("Interest Rate (%)", min_value=0.1, value=10.0)
tenure = st.number_input("Tenure (Months)", min_value=1, value=12)

if st.button("Calculate EMI"):
    r = rate / 12 / 100
    emi = (loan * r * (1 + r)**tenure) / ((1 + r)**tenure - 1)

    total_payment = emi * tenure
    total_interest = total_payment - loan

    st.success(f"Monthly EMI: ₹ {round(emi, 2)}")
    st.info(f"Total Payment: ₹ {round(total_payment, 2)}")
    st.warning(f"Total Interest: ₹ {round(total_interest, 2)}")

    # EMI Schedule
    balance = loan
    data = []

    for month in range(1, tenure + 1):
        interest = balance * r
        principal = emi - interest
        balance -= principal

        data.append([month, round(emi,2), round(principal,2), round(interest,2), round(balance,2)])

    df = pd.DataFrame(data, columns=["Month", "EMI", "Principal", "Interest", "Balance"])

    st.subheader("📊 EMI Schedule")
    st.dataframe(df)

    # Chart
    st.subheader("📈 Principal vs Interest")
    st.line_chart(df[["Principal", "Interest"]])
