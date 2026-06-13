import streamlit as st
import requests

# ----------------------------
# Page Config
# ----------------------------

st.set_page_config(
    page_title="Enterprise RAG Assistant",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------
# Session State
# ----------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ----------------------------
# Header
# ----------------------------

st.title("🤖 Enterprise RAG Assistant")
st.markdown(
    "Upload PDFs and chat with your documents using RAG + Llama 3"
)

# ----------------------------
# Sidebar
# ----------------------------

with st.sidebar:

    st.header("📄 Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        if st.button("Upload PDF"):

            with st.spinner("Uploading and processing PDF..."):

                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        "application/pdf"
                    )
                }

                response = requests.post(
                    "http://127.0.0.1:8000/upload",
                    files=files
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success("PDF Uploaded Successfully")

                    st.write(
                        f"Chunks Created: {result['chunks']}"
                    )

                else:
                    st.error("Upload Failed")

# ----------------------------
# Chat Section
# ----------------------------

st.subheader("💬 Chat With Documents")

# Display Previous Messages

for message in st.session_state.chat_history:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if "sources" in message:

            st.caption(
                "📚 Sources: "
                + ", ".join(message["sources"])
            )

# Chat Input

user_question = st.chat_input(
    "Ask a question about your PDFs..."
)

# ----------------------------
# Send Question
# ----------------------------

if user_question:

    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    with st.chat_message("user"):
        st.markdown(user_question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={
                    "query": user_question
                }
            )

            if response.status_code == 200:

                result = response.json()

                answer = result["answer"]

                sources = result.get(
                    "sources",
                    []
                )

                st.markdown(answer)

                if sources:

                    st.caption(
                        "📚 Sources: "
                        + ", ".join(sources)
                    )

                st.session_state.chat_history.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": sources
                    }
                )

            else:

                st.error(
                    "Error communicating with backend."
                )