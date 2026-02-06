import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Clinical Trial Workflow Tracker",
    layout="centered"
)

st.title("🧪 Clinical Trial Workflow Tracker")
st.caption("CTA-focused clinical trial site tracking dashboard")

# Load data
df = pd.read_csv("data/trial_sites.csv")

st.subheader("📋 Trial Site Overview")
st.dataframe(df, use_container_width=True)

st.subheader("✅ Compliance Status")

def check_compliance(site):
    if site["Status"] != "Active":
        return "❌ Site not active"
    if site["Documents_Complete"] != "Yes":
        return "⚠️ Missing essential documents"
    return "✅ Compliant"

for _, row in df.iterrows():
    st.write(f"**{row['Site_Name']}** → {check_compliance(row)}")
