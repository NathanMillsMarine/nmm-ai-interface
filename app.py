
import streamlit as st
from docx import Document
import time

st.set_page_config(page_title="Nathan Mills Marine – AI Report Generator", layout="wide")
st.title("Nathan Mills Marine – AI Report Generator")

uploaded_file = st.file_uploader("📤 Upload Case File (.docx, .xlsx, or .json)", type=["docx", "xlsx", "json"])

if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")
    
    if uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(uploaded_file)
        st.subheader("Preview of Uploaded Report:")
        for para in doc.paragraphs[:5]:
            st.write(para.text)

    if st.button("Generate Report"):
        progress = st.progress(0)
        status = st.empty()
        
        progress.progress(10)
        status.text("🔍 Parsing input...")
        time.sleep(1)

        progress.progress(35)
        status.text("🧠 Generating AI report content...")
        time.sleep(2)

        progress.progress(70)
        status.text("📝 Formatting into .docx file...")
        time.sleep(1)

        progress.progress(100)
        status.text("✅ Report generation complete.")

        st.success("Report generated and saved to project folder (placeholder).")
        st.download_button("⬇️ Download Report (Example)", data="This is a placeholder report.", file_name="NMM_AI_Report.docx")

else:
    st.info("Upload a .docx, .xlsx, or .json case file to begin.")
