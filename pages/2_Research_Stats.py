import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Research Statistics")

labels = ["AI Agriculture","Cloud Security","Sustainable Construction"]
values = [2,1,2]

fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct='%1.1f%%')
st.pyplot(fig)
