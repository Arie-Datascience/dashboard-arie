import streamlit as st
import pandas as pd

st.title("📊 Dashboard Penjualan Arie")
st.markdown("Analisis data penjualan sederhana menggunakan Streamlit")
Tambah judul dashboard

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
# Hitung growth bulan terakhir vs bulan sebelumnya
last_sales = data["Penjualan"].iloc[-1]
prev_sales = data["Penjualan"].iloc[-2]

sales_growth = ((last_sales - prev_sales) / prev_sales) * 100

last_customer = data["Customer"].iloc[-1]
prev_customer = data["Customer"].iloc[-2]

customer_growth = ((last_customer - prev_customer) / prev_customer) * 100
col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Sales",
        f"{total_sales} Juta",
        f"{sales_growth:.1f}%"
    )

with col2:
    st.metric(
        "Total Customer",
        total_customer,
        f"{customer_growth:.1f}%"
    )

st.bar_chart(data.set_index("Bulan"))
st.dataframe(data)
