# main2.py
import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login

# --- Ambil token dari secrets ---
hf_token = st.secrets["HF_TOKEN"]
login(token=hf_token)

# --- Cara 1: Pakai pipeline langsung ---
def run_with_pipeline():
    st.markdown("### 💡 Pipeline Mode")
    pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.2", token=hf_token)
    messages = [{"role": "user", "content": "Who are you?"}]
    result = pipe(messages)
    st.write(result)


# --- Cara 2: Load model + tokenizer manual ---
def run_manual_mode():
    st.markdown("### 🧪 Manual Mode")
    tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2", token=hf_token)
    model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2", token=hf_token)

    messages = [{"role": "user", "content": "Who are you?"}]
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
    ).to(model.device)

    outputs = model.generate(**inputs, max_new_tokens=40)
    output_text = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:])
    st.write(output_text)

# --- Streamlit UI ---
st.set_page_config(page_title="🦙 Mistral Playground")
st.title("🦙 Mistral 7B Instruct v0.2 – Local Test via Hugging Face")

mode = st.radio("Pilih mode:", ["Pipeline", "Manual"])

if mode == "Pipeline":
    run_with_pipeline()
else:
    run_manual_mode()
