import streamlit as st
from rag import ask_pdf


st.set_page_config(
    page_title="AI PDF Research Assistant",
    page_icon="🤖"
)


st.title("🤖 AI PDF Research Assistant")

st.write(
    "Ask questions about your research document."
)


question = st.text_input(
    "Ask a question about the PDF:"
)


if st.button("Ask AI"):

    if question:

        with st.spinner("Thinking..."):

            answer, sources = ask_pdf(question)

        st.subheader("🤖 Answer")

        st.write(answer)

        st.subheader("📚 Sources")

        for source in sources:

            st.write(f"• {source}")

    else:

        st.warning("Please enter a question.")