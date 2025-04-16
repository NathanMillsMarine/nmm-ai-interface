import streamlit as st
from docx import Document

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
        st.success("✅ Report generation triggered (placeholder for now)")
        st.info("Full AI integration coming next. This confirms upload is working.")
else:
    st.info("Upload a .docx, .xlsx, or .json case file to begin.")
