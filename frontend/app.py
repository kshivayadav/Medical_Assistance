import streamlit as st
import requests
import uuid

BACKEND_URL = "https://medical-assistance-h1go.onrender.com/ask"

st.set_page_config(
    page_title="AI Medical Assistant",
    page_icon="🩺",
    layout="centered"
)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:
    st.title("🩺 Medical AI")

    st.markdown("### 📌 Project Overview")
    st.markdown("""
    **AI Medical Assistant** is an intelligent chatbot that provides:
    
    - 💊 Medication information  
    - ⚠️ Side effects & interactions  
    - 🧬 General health guidance  
    - 📖 Evidence-based responses  
    
    ⚠️ This tool does not replace professional medical advice.
    """)

    st.divider()

    st.markdown("### ⚙️ Controls")

    if st.button("🔄 Start New Session"):
        st.session_state.messages = []
        st.session_state.session_id = str(uuid.uuid4())
        st.rerun()

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.markdown("### 🧠 Model Info")
    st.markdown("""
    - Backend: FastAPI  
    - LLM: Groq API  
    - UI: Streamlit  
    """)

    st.divider()

    st.caption("Version 1.0 | Built with ❤️")

st.title("🩺 AI Medical Assistant")



if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_input = st.chat_input("Ask your medical question...")

if user_input:


    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Send to backend
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    BACKEND_URL,
                    json={
                        "question": user_input,
                        "session_id": st.session_state.session_id
                    },
                    timeout=60
                )
                if response.status_code == 200:
                        data = response.json()
                        answer = data.get("answer", "No answer returned.")
                else:
                    answer = f"⚠️ Backend error ({response.status_code})"

            except Exception as e:
                answer = f"⚠️ Backend not reachable: {e}"

            st.markdown(answer)
            
    

    
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )