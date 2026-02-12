import streamlit as st
import requests

st.set_page_config(
    page_title="MD Faruk Abdulla | AI Research Lab",
    page_icon="🚀",
    layout="wide"
)

# Load CSS
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# DARK/LIGHT TOGGLE
mode = st.sidebar.toggle("🌗 Dark Mode", value=True)

if not mode:
    st.markdown("""
        <style>
        body {background:white;color:black;}
        </style>
    """, unsafe_allow_html=True)

# HERO
st.markdown('<div class="main-title">MD Faruk Abdulla</div>', unsafe_allow_html=True)
st.markdown("### AI • Cloud Security • Sustainable Intelligent Systems")

st.image("assets/profile.jpg", use_container_width=False, output_format="JPEG")

st.markdown("---")

# COUNTERS
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="counter-box"><h2>6+</h2><p>Publications</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="counter-box"><h2>3</h2><p>Peer Reviews</p></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="counter-box"><h2>4</h2><p>Research Domains</p></div>', unsafe_allow_html=True)

st.markdown("---")

# ABOUT
st.subheader("About Me")

st.write("""
Assistant Professor at Parul University (IT & CS).  
Research integrates Machine Learning, Agro-Climatic Systems,
Cloud Security, and Sustainable Built Infrastructure.

Scopus Author Profile:
https://www.scopus.com/authid/detail.uri?authorId=60171729600

ORCID:
https://orcid.org/0009-0007-1478-7376
""")
