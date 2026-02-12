import streamlit as st

st.title("📚 Publications")

category = st.selectbox("Filter by Type", 
                        ["All","Journal","Conference","Book Chapter"])

publications = [
    {"title":"Agro-Climatic Decision Systems",
     "type":"Journal",
     "link":"https://doi.org/10.52783/jisem.v10i42s.8183"},
     
    {"title":"Transforming Farming with Machine Intelligence",
     "type":"Journal",
     "link":"https://doi.org/10.63682/jns.v14i26s.6667"},
     
    {"title":"DDoS Detection in Cloud",
     "type":"Conference",
     "link":"https://doi.org/10.1049/icp.2025.1668"},
     
    {"title":"Smart & Sustainable Construction",
     "type":"Book Chapter",
     "link":"https://doi.org/10.4018/979-8-3373-2555-2.ch009"}
]

for pub in publications:
    if category == "All" or pub["type"] == category:
        st.markdown('<div class="pub-card">', unsafe_allow_html=True)
        st.markdown(f"### {pub['title']}")
        st.markdown(f"Type: {pub['type']}")
        st.markdown(f"🔗 {pub['link']}")
        st.markdown("</div>", unsafe_allow_html=True)
