import streamlit as st

st.title("EMI Calculator")

loan = st.number_input("Loan Amount")
rate = st.number_input("Interest Rate (%)")
tenure = st.number_input("Months")

if st.button("Calculate"):
    r = rate / 12 / 100
    emi = (loan * r * (1 + r)**tenure) / ((1 + r)**tenure - 1)
    st.write("EMI =", round(emi, 2))
