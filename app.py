import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="Data Analytics Dashboard", layout="wide")

# --- SIDEBAR: YOUR PROFESSIONAL BIO ---
with st.sidebar:
    st.title("👨‍💻 Developer Profile")
    # TIP: Replace [Your Name] with your actual name for LinkedIn!
    st.info("Built by [Your Name] | Python Developer")
    st.markdown("[🔗 Visit my LinkedIn](https://www.linkedin.com/in/jhapriya821)")
    st.divider()
    st.subheader("🚀 Tech Stack")
    st.write("- Python / Streamlit\n- Pandas (Data Science)\n- Plotly (Visualizations)")

# --- MAIN UI ---
st.title("📊 Business Intelligence Dashboard")
st.markdown("### Interactive Spending & Budget Analysis")

# 1. DATA SETUP
data = {
    "Category": ["Marketing", "Software", "Payroll", "Travel", "Office Supplies"],
    "Budget": [5000, 2000, 15000, 3000, 1000],
    "Actual": [4200, 2100, 15000, 3500, 800]
}
df = pd.DataFrame(data)

# 2. KEY METRICS
c1, c2, c3 = st.columns(3)
total_budget = df["Budget"].sum()
total_actual = df["Actual"].sum()
variance = total_budget - total_actual

c1.metric("Total Budget", f"${total_budget:,}")
c2.metric("Total Spent", f"${total_actual:,}")
# Normal delta color: Green if positive (under budget), Red if negative (over budget)
c3.metric("Variance", f"${variance:,}", delta=f"${variance:,}")

st.divider()

# 3. VISUALIZATIONS
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Budget vs. Actual")
    fig = px.bar(df, x="Category", y=["Budget", "Actual"], barmode="group")
    # Updated 'width' setting for 2026 Streamlit standards
    st.plotly_chart(fig, width='stretch')

with col_right:
    st.subheader("Expense Distribution")
    fig_pie = px.pie(df, values="Actual", names="Category", hole=0.4)
    # FIX: Changed 'fig' to 'fig_pie' here
    st.plotly_chart(fig_pie, width='stretch')