import streamlit as st

# --- App Title ---
st.title("Change Management Assessment Dossier")

# --- Select Change Type ---
st.header("1. Change Type")
track_type = st.radio("Select the track:", ["Full Track", "Fast Track"])

# --- Change Metadata ---
st.header("2. Change Metadata")
change_title = st.text_input("Title of Change")
change_id = st.text_input("Change Reference ID")
change_owner = st.text_input("Change Owner / Engineer")

# --- Standards-Based Assessment ---
st.header("3. Standards-Based Compliance Review")
st.markdown("Based on CM2, EIA-649, and configuration management principles.")

cm2_check = st.checkbox("CM2: Is the change part of a closed-loop process?")
eia_check = st.checkbox("EIA-649: Are configuration items identified and controlled?")
traceability = st.checkbox("Is full traceability of affected items ensured?")
stakeholder_review = st.checkbox("Has all stakeholder feedback been reviewed?")

# --- Summary Output ---
st.header("4. Dossier Summary")

if st.button("Generate Summary"):
    st.markdown("### Assessment Dossier")
    st.markdown(f"- **Track Type**: {track_type}")
    st.markdown(f"- **Title**: {change_title}")
    st.markdown(f"- **Reference ID**: {change_id}")
    st.markdown(f"- **Owner**: {change_owner}")
    st.markdown("#### Compliance Checklist")
    st.markdown(f"- CM2 Closed Loop: {'✅' if cm2_check else '❌'}")
    st.markdown(f"- EIA-649 Compliance: {'✅' if eia_check else '❌'}")
    st.markdown(f"- Traceability: {'✅' if traceability else '❌'}")
    st.markdown(f"- Stakeholder Review: {'✅' if stakeholder_review else '❌'}")
