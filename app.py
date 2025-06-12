import streamlit as st
from PIL import Image

st.set_page_config(page_title="Vida Team", layout="wide")
st.title("👥 Meet the Vida Team")
st.markdown("We're building the future of emotional intelligence in mental health.")

def show_member(img_path, name, title, bio):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(f"static/{img_path}", width=150)
    with col2:
        st.subheader(f"{name} – {title}")
        st.markdown(bio)

show_member(
    "indrani.jpeg", "Indrani Mazumdar", "AI Architect & Founder",
    """
- AI Architect in Generative AI and Multimodal ML
- AI system builder for healthcare
- Adjunct Data Scientist, Mount Sinai
- Creator of Vida's agent-based triage framework
"""
)

show_member(
    "kaustav.jpg", "Kaustav Mukherjee", "Technical & Research Advisor",
    """
- Assistant Research Professor, Mount Sinai
- Hematologist and bioinformatician
- Advises on biomedical data strategy and longitudinal design
"""
)

show_member(
    "chi.jpg", "Chi Chan, Ph.D.", "Consulting Psychologist",
    """
- Assistant Professor, Psychology Division, Mount Sinai
- Licensed clinical psychologist
- Exploring collaboration for emotional validation and clinical design
"""
)

