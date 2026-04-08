import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from analysis import load_data, overall_conversion, channel_performance

# Page config
st.set_page_config(page_title="Funnel Dashboard", layout="wide")

# Custom CSS (🔥 futuristic UI)
st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: white;
}

.metric-card {
    background: linear-gradient(145deg, #1e293b, #0f172a);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 0 20px rgba(0,255,255,0.2);
}

h1, h2, h3 {
    color: #38bdf8;
}

</style>
""", unsafe_allow_html=True)

# Load data
df = load_data()
metrics = overall_conversion(df)
channel_df = channel_performance(df)

# Title
st.title("🚀 Futuristic Marketing Funnel Dashboard")

# KPI Cards
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h3>Visitors</h3>
        <h2>{metrics["Visitors"]}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <h3>Leads</h3>
        <h2>{metrics["Leads"]}</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <h3>Customers</h3>
        <h2>{metrics["Customers"]}</h2>
    </div>
    """, unsafe_allow_html=True)

# Conversion Rates
st.subheader("📈 Conversion Rates")

col4, col5 = st.columns(2)

with col4:
    st.metric("Visitor → Lead %", f"{metrics['Visitor → Lead %']:.2f}%")

with col5:
    st.metric("Lead → Customer %", f"{metrics['Lead → Customer %']:.2f}%")

# Funnel Chart
st.subheader("🔻 Funnel Overview")

funnel_values = [
    metrics["Visitors"],
    metrics["Leads"],
    metrics["Customers"]
]

labels = ["Visitors", "Leads", "Customers"]

fig, ax = plt.subplots()
ax.bar(labels, funnel_values)
ax.set_title("Funnel Drop-Off")

st.pyplot(fig)

# Channel Performance
st.subheader("📊 Channel Performance")

st.dataframe(channel_df.style.background_gradient(cmap='Blues'))

# Insights Section
st.subheader("🧠 Insights")

best_channel = channel_df["Lead→Customer %"].idxmax()

st.success(f"🔥 Best converting channel: {best_channel}")

st.warning("⚠️ Focus on improving Visitor → Lead conversion")

st.info("💡 Try better landing pages & CTAs to improve leads")