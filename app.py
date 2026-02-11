import streamlit as st

st.set_page_config(
    page_title="MD Faruk Abdulla | AI Research Portal",
    page_icon="🎓",
    layout="wide"
)

# Load CSS
def load_css():
    with open("styles/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Hero Section
st.markdown('<div class="main-title">MD Faruk Abdulla</div>', unsafe_allow_html=True)
st.markdown("### Assistant Professor | AI & Intelligent Systems Researcher")

st.markdown("---")

# About Section
st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)

st.markdown("""
I am an Assistant Professor (IT & CS) at Parul University, Vadodara.  
My research focuses on building intelligent, secure, and sustainable computing systems that integrate Machine Learning, Cloud Security, and Sustainable Infrastructure.

With multiple 2025 Scopus-indexed publications, I actively contribute to interdisciplinary research combining Artificial Intelligence and real-world industrial challenges.
""")

st.markdown("---")

# Research Domains
st.markdown('<div class="section-title">Research Domains</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **🤖 Machine Learning & AI**
    - Predictive Models
    - Agro-Climatic Decision Systems
    - Intelligent Infrastructure
    """)

with col2:
    st.markdown("""
    **☁ Cloud Security & Sustainable Computing**
    - DDoS Detection
    - Secure Cloud Architectures
    - Circular Economy Integration
    """)

st.markdown("---")

# Academic Highlights
st.markdown('<div class="section-title">Academic Highlights</div>', unsafe_allow_html=True)

st.markdown("""
- Assistant Professor – Parul University (Dec 2023 – Present)
- Industry Embedded Program Coordinator
- Project Coordinator
- Peer Reviewer (Franklin Open, IGI Global)
""")

st.markdown("---")

# Metrics Section
st.markdown('<div class="section-title">Research Identifiers</div>', unsafe_allow_html=True)

st.markdown("""
- **ORCID:** https://orcid.org/0009-0007-1478-7376  
- **Scopus Author ID:** 60020142800  
- **Scopus Author ID:** 60171729600  
""")

st.markdown('<div class="footer">© 2026 MD Faruk Abdulla | AI & Sustainable Computing Research</div>', unsafe_allow_html=True)
