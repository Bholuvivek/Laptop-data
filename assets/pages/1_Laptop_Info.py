import streamlit as st
from matplotlib import image
import os
import time
import pickle
import pandas as pd


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "data.jpg")


st.set_page_config(page_title="KnowAboutTheLaptop",
                   page_icon="☠",
                   layout="wide"
)
st.title("Know About The Laptop 😕😕")

img = image.imread(IMAGE_PATH)
st.image(img, width=700, caption="Beaware of Information")

data_path = os.path.join(dir_of_interest, "data", "dataframe.pkl")

lap = pickle.load(open(data_path, 'rb'))

df = pd.DataFrame(lap)

laptop = df["Product"].values
index = df["Product"].index
st.subheader("Info About Some of Laptop Model")
selected_laptop_name = st.selectbox(" Please select the model:- ", laptop)
st.write("do you wanna see :red[_Wait_For_THE_RESULT_] 🤩")
butt = st.button("Click Here!!!")
if butt:
    info = df.loc[df['Product'] == selected_laptop_name]
    st.write(info.iloc[0])
    st.subheader("Go To the next page for Prediction the Laptop Price 🎁")












# st.image(noimg)


# img = Image.open(urlopen(p[0]))
# print(img)


# NLP section --------------------------------------------------------------------------------------------------



#
# # ------------------------------------------------------------------------------------------------------------------
#

# movie_index = movies_list[movies_list["Movies"] == selected_movie_name].index[0]
# if butt:
#     with st.spinner('Take patience, wait for it.....'):
#         time.sleep(5)
#     st.success('Done!')
#     st.write("Your entered movie details:-")
#     st.write("Your Movie Name - ", selected_movie_name)
#     try:
#         url = img_url(selected_movie_name)
#         st.image(url[0], width=200)
#
#     except:
#         pass
#     st.write("Lead Star - ", movies_list.iloc[movie_index].first_name)
#     st.write("Director - ", movies_list.iloc[movie_index].Director)
#     st.write("Rating - ", movies_list.iloc[movie_index].Rating)
#     st.write("TV-Show Type - ", movies_list.iloc[movie_index].tv_shows)
#     st.write("Tags - ", movies_list.iloc[movie_index].tags)
#
#     st.markdown("Your movie link - {}".format(movies_list.iloc[movie_index].imb_link))
#     st.subheader("The Top 5 listed Movies of High rating(Rating > 7.0)")
#     recom = recommand(selected_movie_name)
#
#     for i in range(len(recom)):
#         st.write("{}) {}".format(i+1, recom[i]))
#
#         try:
#             url = img_url(recom[i])
#             st.image(url[0], width=200)
#
#         except:
#             pass
#         idx = movies_list[movies_list["Movies"] == recom[i]].index[0]
#         st.write("Lead Star - ", movies_list.iloc[idx].first_name)
#         st.write("Director - ", movies_list.iloc[idx].Director)
#         st.write("Rating - ", movies_list.iloc[idx].Rating)
#         st.write("TV-Show Type - ", movies_list.iloc[idx].tv_shows)
#         st.write("Tags - ", movies_list.iloc[idx].tags)
#         link = movies_list.iloc[idx].imb_link
#         st.markdown("Movie link - {}".format(link), unsafe_allow_html=True)
#
#     st.subheader("Hope You Enjoyed 🙄🙄")
#
