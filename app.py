import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="Data Analytics Dashboard", layout="wide")

# --- SIDEBAR: YOUR PROFESSIONAL BIO ---
with st.sidebar:
    st.title("👨‍💻 Developer Profile")
    st.info("Built by [Your Name] | Python Developer")
    st.markdown("[🔗 Visit my LinkedIn](https://www.linkedin.com/in/YOUR_USERNAME)")
    st.divider()
    st.subheader("🚀 Tech Stack")
    st.write("- Python / Streamlit\n- Pandas (Data Science)\n- Plotly (Visualizations)")

# --- MAIN UI ---
st.title("📊 Business Intelligence Dashboard")
st.markdown("### Interactive Spending & Budget Analysis")

# 1. MOCK DATA (Simulating a business ledger)
data = {
    "Category": ["Marketing", "Software", "Payroll", "Travel", "Office Supplies"],
    "Budget": [5000, 2000, 15000, 3000, 1000],
    "Actual": [4200, 2100, 15000, 3500, 800]
}
df = pd.DataFrame(data)

# 2. KEY METRICS (The "Numbers" LinkedIn loves)
c1, c2, c3 = st.columns(3)
total_budget = df["Budget"].sum()
total_actual = df["Actual"].sum()
c1.metric("Total Budget", f"${total_budget:,}")
c2.metric("Total Spent", f"${total_actual:,}")
c3.metric("Variance", f"${total_budget - total_actual:,}", delta_color="normal")

st.divider()

# 3. VISUALIZATIONS
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Budget vs. Actual")
    fig = px.bar(df, x="Category", y=["Budget", "Actual"], barmode="group")
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("Expense Distribution")
    fig_pie = px.pie(df, values="Actual", names="Category", hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)