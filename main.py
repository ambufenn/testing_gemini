import streamlit as st
import google.generativeai as genai
import os

# Konfigurasi API key dari secrets Streamlit
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Pilih model (boleh diganti: "gemini-1.5-pro" atau "gemini-1.5-flash")
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit App
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("🤖 Gemini Chatbot by Streamlit")

# Session state untuk menyimpan chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.chat = model.start_chat(history=[])

# Form input
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Ketik pesan:")
    submitted = st.form_submit_button("Kirim")

# Proses input
if submitted and user_input:
    # Tambahkan pesan pengguna
    st.session_state.chat_history.append(("🧑 Kamu", user_input))

    # Kirim ke Gemini
    response = st.session_state.chat.send_message(user_input)

    # Tambahkan respons ke history
    st.session_state.chat_history.append(("🤖 Gemini", response.text))

# Tampilkan chat history
for role, msg in st.session_state.chat_history:
    with st.chat_message(role.split()[0]):
        st.markdown(msg)
