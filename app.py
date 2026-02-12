import streamlit as st

st.set_page_config(
    page_title="MD Faruk Abdulla | AI Research Hub",
    page_icon="🎓",
    layout="wide"
)

# Load CSS
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# HERO SECTION
st.markdown('<div class="main-title">MD Faruk Abdulla</div>', unsafe_allow_html=True)
st.markdown("### Assistant Professor | AI, Cloud Security & Sustainable Intelligent Systems")

st.markdown("---")

# SLIDING BOX – PROFILE
st.markdown('<div class="slide-box">', unsafe_allow_html=True)
st.markdown("""
🎓 **Current Position:** Assistant Professor (IT & CS), Parul University, Vadodara  
📚 **Research Focus:** Machine Learning, Sustainable Construction, Cloud Security, Agro-Climatic AI Systems  
🔎 **Scopus Author ID:** https://www.scopus.com/authid/detail.uri?authorId=60171729600  
🌍 **ORCID:** https://orcid.org/0009-0007-1478-7376  

With multiple 2025 Scopus-indexed publications, my work bridges Artificial Intelligence with real-world sustainable and secure infrastructure challenges.
""")
st.markdown("</div>", unsafe_allow_html=True)

# RESEARCH IMPACT SECTION
st.markdown('<div class="section-title">Research Impact & Domains</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    🔹 AI-Driven Agro-Climatic Decision Systems  
    🔹 Machine Learning for DDoS Detection  
    🔹 Predictive Modeling for Sustainable Infrastructure  
    """)

with col2:
    st.markdown("""
    🔹 Circular Economy in Construction  
    🔹 Energy Efficient Built Environments  
    🔹 Secure Cloud Computing Frameworks  
    """)

st.markdown("---")

st.markdown('<div class="footer">© 2026 MD Faruk Abdulla | AI & Sustainable Computing Research Portal</div>', unsafe_allow_html=True)
