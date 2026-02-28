import streamlit as st
import pandas as pd

# ===============================
# KONFIGURASI HALAMAN
# ===============================
st.set_page_config(page_title="Dashboard Arie", layout="wide")

# ===============================
# DATA SAMPLE
# ===============================
data = pd.DataFrame({
    "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei"],
    "Penjualan": [20, 35, 30, 50, 45],
    "Customer": [100, 150, 120, 200, 180]
})

st.sidebar.header("Filter Data")

bulan = st.sidebar.selectbox(
    "Pilih Bulan",
    ["Semua"] + list(data["Bulan"].unique())
)

if bulan != "Semua":
    data = data[data["Bulan"] == bulan]
    
# ===============================
# JUDUL
# ===============================
st.title("📊 Dashboard Penjualan Arie")
st.subheader("Upload Data CSV")

uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    data = pd.DataFrame({
        "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei"],
        "Penjualan": [20, 35, 30, 50, 45],
        "Customer": [100, 150, 130, 200, 180]
    })
    
st.markdown("Analisis Data Sederhana dengan Streamlit 🚀")

# ===============================
# SIDEBAR
# ===============================
st.sidebar.title("Menu Filter")
selected_month = st.sidebar.selectbox("Pilih Bulan", data["Bulan"])

# ===============================
# FILTER DATA
# ===============================
filtered_data = data[data["Bulan"] == selected_month]

# ===============================
# HITUNG TOTAL
# ===============================
total_sales = filtered_data["Penjualan"].sum()
total_customer = filtered_data["Customer"].sum()

# ===============================
# HITUNG GROWTH
# ===============================
last_sales = data["Penjualan"].iloc[-1]
prev_sales = data["Penjualan"].iloc[-2]
sales_growth = ((last_sales - prev_sales) / prev_sales) * 100

last_customer = data["Customer"].iloc[-1]
prev_customer = data["Customer"].iloc[-2]
customer_growth = ((last_customer - prev_customer) / prev_customer) * 100

# ===============================
# METRICS
# ===============================
col1, col2 = st.columns(2)

col1.metric(
    "Total Sales",
    f"{total_sales} Juta",
    f"{sales_growth:.2f}%"
)

col2.metric(
    "Total Customer",
    total_customer,
    f"{customer_growth:.2f}%"
)

# ===============================
# CHART
# ===============================
st.subheader("📈 Trend Penjualan & Customer")
st.line_chart(data.set_index("Bulan"))

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.markdown("Created by Arie | Mode Brutal Data Science 🔥")
