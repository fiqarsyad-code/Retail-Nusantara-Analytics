import streamlit as st
import pandas as pd
import plotly.express as px

st.title(
    "PT Retail Nusantara Analytics"
)


FILE = "Business_Analytics_PT_Retail_Nusantara..xlsx"


data = pd.read_excel(FILE)
# ===============================
# KPI DASHBOARD
# ===============================

total_revenue = data["Total_Price"].sum()

total_transaction = data["Transaction_ID"].nunique()

total_qty = data["Qty"].sum()

average_basket = total_revenue / total_transaction


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
        f"{total_transaction}"
    )


with col3:
    st.metric(
        "Total Quantity",
        f"{total_qty}"
    )


with col4:
    st.metric(
        "Average Basket",
        f"Rp {average_basket:,.0f}"
    )

# ===============================
# SALES TREND ANALYSIS
# ===============================

st.divider()

st.subheader("📈 Sales Trend")


data["Date_Time"] = (
    data["Date_Time"]
    .astype(str)
    .str.replace(".", ":", regex=False)
)


data["Date_Time"] = pd.to_datetime(
    data["Date_Time"],
    dayfirst=True
)

sales_trend = (
    data
    .groupby("Date_Time")["Total_Price"]
    .sum()
    .reset_index()
)


fig = px.line(
    sales_trend,
    x="Date_Time",
    y="Total_Price",
    markers=True,
    title="Revenue Trend Over Time"
)


fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Revenue (Rp)"
)


st.plotly_chart(
    fig,
    use_container_width=True
)

st.success(
    "File Excel berhasil dibaca"
)


st.dataframe(
    data.head()
)
