import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(page_title="Process Safety Risk Calculator", page_icon="🛡️")

st.title("🛡️ Industrial JHA Risk Calculator")
st.markdown("""
This tool replicates the **standardized risk assessment logic** I implemented for 24+ industrial units. 
It uses a $5 \\times 5$ matrix to determine the required level of safety intervention.
""")

# Sidebar inputs
st.sidebar.header("Input Parameters")
task_name = st.sidebar.text_input("Process Task Name", "e.g., Kiln Maintenance")

# Probability and Severity Scales
prob = st.sidebar.select_slider(
    "Probability of Occurrence",
    options=[1, 2, 3, 4, 5],
    help="1: Improbable, 5: Frequent"
)

sev = st.sidebar.select_slider(
    "Severity of Impact",
    options=[1, 2, 3, 4, 5],
    help="1: Negligible, 5: Catastrophic"
)

# Logic
risk_score = prob * sev

# Visual Display
st.subheader(f"Analysis for: {task_name}")
col1, col2 = st.columns(2)
col1.metric("Risk Score", risk_score)

if risk_score >= 15:
    st.error("### Result: CRITICAL RISK")
    st.markdown("**Action Required:** STOP WORK. Engineering controls or process redesign mandatory.")
elif risk_score >= 8:
    st.warning("### Result: MEDIUM RISK")
    st.markdown("**Action Required:** Administrative controls and mandatory PPE required.")
else:
    st.success("### Result: LOW RISK")
    st.markdown("**Action Required:** Standard Operating Procedures (SOP) apply.")

# Educational Table
with st.expander("View Risk Matrix Logic"):
    st.table(pd.DataFrame({
        "Score Range": ["1-4", "5-14", "15-25"],
        "Classification": ["Low", "Medium", "High/Critical"],
        "Intervention": ["SOP", "Admin/PPE", "Engineering Control/Shutdown"]
    }))
