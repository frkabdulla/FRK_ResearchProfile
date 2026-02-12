import streamlit as st

st.title("📖 Publications & Research Highlights")

# Publication 1
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("""
### 📌 Machine Learning Models for Agro-Climatic Decision Support Systems  
**Journal of Information Systems Engineering & Management (2025)**  
🔗 DOI: https://doi.org/10.52783/jisem.v10i42s.8183
""")
st.markdown("""
This work explores how Machine Learning models support climate-driven decision systems in Indian agriculture, using heterogeneous data like soil, weather, and crop statistics.  
ML methods examined range from Random Forest to CNN and LSTM, revealing opportunities and data challenges for real-world DSS applications.  
""")
st.markdown("</div>", unsafe_allow_html=True)

# Publication 2 (example)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("""
### 📌 (More publications will be added soon)  
Additional details for your other 2025 works will be included — linking URLs, abstracts, and impact metrics.  
""")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
