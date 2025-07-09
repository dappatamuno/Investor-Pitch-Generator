import streamlit as st
from app.generator import generate_pitch
from app.pdf_exporter import export_pdf

st.set_page_config(page_title="🚀 AI Business Pitch Generator", layout="centered")
st.title("🚀 AI Business Pitch Generator")

with st.form("pitch_form"):
    name = st.text_input("Startup Name")
    industry = st.text_input("Industry")
    problem = st.text_area("What problem are you solving?")
    solution = st.text_area("What is your solution?")
    business_model = st.text_input("Business Model")
    target_market = st.text_input("Target Market")
    advantage = st.text_input("Competitive Advantage")
    submitted = st.form_submit_button("Generate Pitch Deck")

if submitted:
    with st.spinner("Generating deck..."):
        slides = generate_pitch({
            "name": name,
            "industry": industry,
            "problem": problem,
            "solution": solution,
            "business_model": business_model,
            "target_market": target_market,
            "advantage": advantage,
        })

        for slide in slides:
            st.subheader(slide['title'])
            for bullet in slide['content']:
                st.markdown(f"- {bullet}")

        if st.button("Download as PDF"):
            export_pdf(slides)
            with open("generated_pitch.pdf", "rb") as f:
                st.download_button("📥 Download", f, file_name="pitch_deck.pdf")