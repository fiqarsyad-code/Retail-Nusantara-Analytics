import streamlit as st
import pandas as pd


st.title(
    "PT Retail Nusantara Analytics"
)


FILE = "Business_Analytics_PT_Retail_Nusantara."


data = pd.read_excel(FILE)


st.success(
    "File Excel berhasil dibaca"
)


st.dataframe(
    data.head()
)
