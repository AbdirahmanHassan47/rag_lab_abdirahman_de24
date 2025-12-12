import streamlit as st
import requests

st.set_page_config(page_title="Youtuber RAG Bot")

API_URL = "http://127.0.0.1:8000/rag/query"


def layout():
    st.title("The Youtuber – A cool Chatbot")

    
    question = st.text_input("Ask a question about the videos:")

    if st.button("Send") and question.strip():
        try:
            
            response = requests.post(API_URL, json={"prompt": question})

            if response.status_code != 200:
                st.error(f"API error: {response.status_code}")
                st.code(response.text)
                return

            data = response.json()
            answer = data.get("answer", "No answer returned")

            st.markdown("### Youtuber:")
            st.markdown(answer)

            
            filename = data.get("filename")
            filepath = data.get("filepath")
            if filename or filepath:
                st.caption(f"Source: {filename} ({filepath})")

        except Exception as e:
            st.error(f"Request failed: {e}")


if __name__ == "__main__":
    layout()
