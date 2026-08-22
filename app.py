import streamlit as st
import pandas as pd


st.title(
    "PT Retail Nusantara Analytics"
)


FILE = "Business_Analytics_PT_Retail_Nusantara..xlsx"


data = pd.read_excel(FILE)
# ===============================
# KPI CALCULATION
# ===============================

total_revenue = data["Total_Sales"].sum()

total_transaction = data["Transaction_ID"].nunique()

total_qty = data["Qty"].sum()

avg_transaction = total_revenue / total_transaction


st.divider()

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Total Revenue",
        f"Rp {total_revenue:,.0f}"
    )


with col2:
    st.metric(
        "Total Transaction",
        total_transaction
    )


with col3:
    st.metric(
        "Total Quantity",
        total_qty
    )


with col4:
    st.metric(
        "Average Basket",
        f"Rp {avg_transaction:,.0f}"
    )

st.success(
    "File Excel berhasil dibaca"
)


st.dataframe(
    data.head()
)
