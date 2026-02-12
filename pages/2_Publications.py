import streamlit as st

st.title("📖 Publications & Scholarly Contributions")

# Publication 1
st.markdown('<div class="pub-card">', unsafe_allow_html=True)
st.markdown("""
### Machine Learning Models for Agro-Climatic Decision Support Systems in Indian Agriculture  
**Journal of Information Systems Engineering & Management (2025)**  
DOI: https://doi.org/10.52783/jisem.v10i42s.8183  
Article Link: https://www.jisem-journal.com/index.php/journal/article/view/8183  

This study investigates ML-based agro-climatic decision support systems integrating soil, crop, and climate datasets. The research highlights Random Forest, CNN, and LSTM applications for improving predictive agriculture in India.
""")
st.markdown("</div>", unsafe_allow_html=True)

# Publication 2
st.markdown('<div class="pub-card">', unsafe_allow_html=True)
st.markdown("""
### Transforming Farming With Machine Intelligence  
**Journal of Neonatal Surgery (2025)**  
DOI: https://doi.org/10.63682/jns.v14i26s.6667  
Article Link: https://www.jneonatalsurg.com/index.php/jns/article/view/6667  

Explores plant affliction detection using Machine Learning approaches. Discusses practical deployment limitations and data challenges in precision agriculture.
""")
st.markdown("</div>", unsafe_allow_html=True)

# Publication 3
st.markdown('<div class="pub-card">', unsafe_allow_html=True)
st.markdown("""
### Machine Learning Techniques for Identifying DDoS Attacks in Cloud Computing  
**IET Conference Proceedings (2025)**  
DOI: https://doi.org/10.1049/icp.2025.1668  

Focuses on AI-based intrusion detection mechanisms within cloud infrastructures to improve resilience against DDoS attacks.
""")
st.markdown("</div>", unsafe_allow_html=True)

# Publication 4
st.markdown('<div class="pub-card">', unsafe_allow_html=True)
st.markdown("""
### Advancing Smart and Sustainable Construction  
**IGI Global Book Chapter (2025)**  
DOI: https://doi.org/10.4018/979-8-3373-2555-2.ch009  
Publisher Page: https://www.igi-global.com/gateway/chapter/390073  

Examines integration of circular economy principles, energy efficiency strategies, and economic viability into modern built environments.
""")
st.markdown("</div>", unsafe_allow_html=True)

st.success("All publications indexed via Scopus / Crossref. Full profiles available through Scopus Author ID.")
