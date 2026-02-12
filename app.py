import streamlit as st

st.set_page_config(
    page_title="MD Faruk Abdulla | AI Research Hub",
    page_icon="🎓",
    layout="wide"
)

# Load custom CSS
with open("styles/style.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Hero Section
st.markdown('<div class="main-title">MD Faruk Abdulla</div>', unsafe_allow_html=True)
st.markdown("### Assistant Professor | AI, Cloud Security & Sustainable Systems")

st.markdown("---")

# About section
st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)
st.markdown("""
I’m an Assistant Professor (IT & CS) at **Parul University, Vadodara**.  
My work merges **Machine Learning, Cloud Security, Sustainable Computing,** and **AI systems** bringing real-world impact through research and technology.
""")

st.markdown("---")

# Research Domains
st.markdown('<div class="section-title">Core Research Domains</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    🔹 Machine Learning in Decision Systems  
    🔹 AI for Agro-Climatic Models  
    🔹 Intelligent Infrastructure Analytics
    """)

with col2:
    st.markdown("""
    🔹 Cloud Security & DDoS Detection  
    🔹 Circular Economy Integration  
    🔹 Sustainable Computational Frameworks
    """)

st.markdown("---")
