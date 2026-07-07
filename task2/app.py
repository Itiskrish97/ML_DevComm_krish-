import streamlit as st
from pypdf import PdfReader
from ollama import chat
from PIL import Image
import tempfile
import os

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Local AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.header("🤖 Models")

    st.success("✅ Llama 3")
    st.success("✅ Moondream")

    st.markdown("---")

    st.write(
        "Local AI Assistant running entirely on Ollama."
    )

# ==========================================
# TITLE
# ==========================================

st.title("🤖 Local AI Assistant")

st.caption(
    "Powered by Ollama, Llama 3 and Moondream"
)

# ==========================================
# CHATBOT SECTION
# ==========================================

st.header("💬 Chat with Llama 3")

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("🗑️ Clear Chat History"):
    st.session_state.messages = []
    st.rerun()

user_message = st.chat_input(
    "Ask me anything..."
)

if user_message:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    with st.spinner("Llama 3 is thinking..."):

        response = chat(
            model="llama3",
            messages=st.session_state.messages
        )

    assistant_reply = response["message"]["content"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

st.divider()

# ==========================================
# PDF SECTION
# ==========================================

st.header("📄 PDF Question Answering")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:

    try:

        reader = PdfReader(uploaded_file)

        text = ""

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted

        st.success("PDF loaded successfully!")

        st.text_area(
            "PDF Content Preview",
            text[:5000],
            height=300
        )

        question = st.text_input(
            "Ask a question about the PDF"
        )

        if question:

            prompt = f"""
Document:

{text}

Question:
{question}
"""

            with st.spinner(
                "Llama 3 is analyzing the document..."
            ):

                response = chat(
                    model="llama3",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

            st.subheader("Answer")

            st.write(
                response["message"]["content"]
            )

    except Exception as e:

        st.error(
            f"Error processing PDF: {e}"
        )

st.divider()

# ==========================================
# IMAGE SECTION
# ==========================================

st.header("🖼️ Image Analysis")

image_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"],
    key="image"
)

if image_file:

    try:

        image = Image.open(image_file)

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        image_question = st.text_input(
            "Ask a question about the image"
        )

        if image_question:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".jpg"
            ) as tmp:

                image.save(tmp.name)

                temp_image_path = tmp.name

            with st.spinner(
                "Moondream is analyzing the image..."
            ):

                response = chat(
                    model="moondream",
                    messages=[
                        {
                            "role": "user",
                            "content": image_question,
                            "images": [temp_image_path]
                        }
                    ]
                )

            st.subheader(
                "Image Answer"
            )

            st.write(
                response["message"]["content"]
            )

            os.remove(
                temp_image_path
            )

    except Exception as e:

        st.error(
            f"Error processing image: {e}"
        )