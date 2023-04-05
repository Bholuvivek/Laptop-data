import streamlit as st
from PIL import Image
import os

from pathlib import Path


# cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# prof_pic = cur_dir / "assets" / "mera photo hoga"

cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
prof_pic = cur_dir / "assets" / "photo.jpg"


# Description
PAGE_TITLE = "LAPTOP PRICE RECOMMENDATION PAGE"
PAGE_ICON = "✨"
NAME = "VIVEK KUMAR"
DESCRIPTION = """
I am a CSE student, currently in 3rd year and enthusiastic in data science, data analysis & Machine Learning, aspire to learn new thing at every second. 
Fan of 07
"""
EMAIL = "viveksinghpihuli@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/vivekbholu/",
    "GitHub": "https://github.com/Bholuvivek",
}
PROJECTS_REQUIRMENTS_DONE= {
    "🍿🍿 The Things are done so far for this project......",
    "🏆 All the information are scraped from flipkart.com and are produced the raw data in a .csv file",
    "🏆 Cleaning and do all the preprocessing task through pandas library of python to get a clean dataframe",
    "🏆 Done the data preprocessing task by regex in python",
    "🏆 Done all the visualization task through plotly library of python"
    "🏆 Making the model through Random Forest Regressior, to get the desired prediction of laptop prize 😊"
    "🏆 Last but not the list make the website through streamlit framework through python and deploy in "
    "streamlit app."
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Hi!! :red[Everyone]")
st.subheader("welcome all, let's enjoy together😎😎😎😎")

# Load css, pdf and profile pic

# with open(css_file) as f:
#     st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

prof = Image.open(prof_pic)


# Header section

col1, col2 = st.columns(2, gap = "small")
with col1:
    st.image(prof, width=220)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📩", EMAIL)

st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write('\n')
st.subheader("Knowledge & Self-declaration ")
st.write(
    """
- ✔️ Currently a student, studied in 3rd year
- ✔️ Intermediate knowledge in python, still exploring and trying to grasp a good hand in python
- ✔️ Has understanding in data science and trying to find the hardness behind the easy word ML 
- ✔️ Has team management and problem solving capability
- ✔️ Always try to learn new things through challenges and tasks 
- ✔️ Some time get confused to himself and has somewhat little patience
"""
)
st.subheader("Project Name - Laptop Price Prediction")
st.subheader("Project Requirements ...............")
st.write(
    """
- 🍿🍿 The Things are done so far for this project......
- 🏆 All the information are scraped from flipkart.com and are produced the raw data in a .csv file
- 🏆 Cleaning and do all the preprocessing task through pandas library of python to get a clean dataframe
- 🏆 Done the data preprocessing task by regex in python
- 🏆 Done all the visualization task through plotly library of python
- 🏆 Making the model through Random Forest Regressior, to get the desired prediction of laptop price 😊
- 🏆 Last but not the list make the website through streamlit framework through python and deploy in 
streamlit app."
"""
)


#st.subheader("👉 THE GITHUB LINK OF THIS PROJECT:-")
#st.subheader("https://github.com/Bholuvivek/Laptop-Price-Prediction")
st.subheader("The Documentation of this Project")
st.write("https://docs.google.com/document/d/1DZ0k8nyx6DJ-zMH0fssyoSYx4sCJsDo4uiFXgYP39zQ/edit")




