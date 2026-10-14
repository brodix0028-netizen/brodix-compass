import streamlit as st
import pandas as pd

st.set_page_config(page_title="Brodix Compass", page_icon="🧭", layout="wide")
st.title("🧭 Brodix Compass - Employee Journey Companion")
st.caption("Emirates Challenge | Brodix Studio, Cebu PH")

st.sidebar.header("Employee Context")
emp_id = st.sidebar.selectbox("Select Employee", ["EMP-1000 - Ahmad (Onboarding Day 5)", "EMP-1045 - Priya (Visa Delay)"])
consent = st.sidebar.checkbox("Pulse Opt-In", value=True)
st.sidebar.info("Privacy: Employee-only view | Human-in-Loop: HR BP Sara Al")

if "EMP-1000" in emp_id:
    stage = "Day 5 - Onboarding"
    friction = "Laptop not issued - Expected by Day 3 per IT_Equipment_Policy [IT_OPS_001]"
    next_team = "IT Support"
else:
    stage = "Day 12 - Internal Mobility"
    friction = "Visa stalled >10 days - PRO to update per Visa_Process [HR_VISA_002]"
    next_team = "PRO Team"

tab1, tab2, tab3 = st.tabs(["📍 Journey Tracker", "📚 Policy Q&A", "🔀 Auto-Router"])

with tab1:
    c1,c2 = st.columns(2)
    c1.metric("Current Stage", stage)
    c2.metric("Friction", "YES", delta_color="inverse")
    st.error(f"⚠️ {friction}")
    st.warning(f"Action: Auto-route to {next_team} via HR BP with full context")

with tab2:
    q = st.text_input("Ask policy", "When should I get my laptop?")
    if q:
        st.success("Answer: Within Day 3, escalate Day 5")
        st.caption("Source: IT_Equipment_Policy.md [IT_OPS_001] | PRIV_004")

with tab3:
    if st.button("🚀 Route to Owner", type="primary"):
        st.json({"employee": emp_id.split()[0], "stage": stage, "routed_to": next_team, "owner": "HR BP Sara Al", "consent": consent, "source": "IT_OPS_001"})
        st.success(f"Handed off to {next_team}!")

st.divider()
st.markdown("**Guardrails:** Employee-side only, opt-in pulse, human owner, policy citations, no performance use.")
