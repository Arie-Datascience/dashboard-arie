import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Arie", layout="wide")

st.title("📊 Dashboard Profesional Arie")

st.sidebar.header("Filter Data")

bulan = st.sidebar.selectbox(
    "Pilih Bulan",
    ["Semua", "Jan", "Feb", "Mar", "Apr", "Mei"]
)

data = pd.DataFrame({
    "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei"],
    "Penjualan": [20, 35, 30, 50, 45],
    "Customer": [100, 150, 130, 200, 180]
})

if bulan != "Semua":
    data = data[data["Bulan"] == bulan]

total_sales = data["Penjualan"].sum()
total_customer = data["Customer"].sum()

col1, col2 = st.columns(2)

col1.metric("Total Sales", f"{total_sales} Juta")
col2.metric("Total Customer", total_customer)

st.bar_chart(data.set_index("Bulan"))
st.dataframe(data)
