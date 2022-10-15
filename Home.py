import streamlit as st
from PIL import Image
import plotly.express as px
import numpy as np 
import pandas as pd 
import plotly as py
import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt

#Homepage configuration

im = Image.open("Space.jpeg")

st.set_page_config(
    page_title="Space Race",
    page_icon= im,
    layout="wide",
    initial_sidebar_state="expanded")

hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
header{visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# ---Side-Bar----

with st.sidebar:
    st.write('''
    Hey there! 👋🏻 

    I am Yasmine Darwich, an MSBA student at AUB 👱‍♀️🏫! 

    I enjoy working with datasets and analyzing information 🎯. 
    
    Let's connect:

    [LinkedIn](https://www.linkedin.com/in/yasmine-darwich/)

    [Twitter](https://twitter.com/DonaLeb_)

    [Instagram](https://www.instagram.com/dona.leb/)

    ''')
    st.write("---")

st.title("The Space Race 🚀")

st.markdown(
        """
        #### The dataset was obtained from Kaggle and includes all the space missions since the beginning of Space Race (1957 till 2020).
        """
    )

st.info(
        """
        👈 Click on the left sidebar menu to navigate to the different visualizations! 
        """
    )

from PIL import Image
image = Image.open('Space.jpeg')
col1, col2, col3 = st.columns([0.2, 5, 0.2])
col2.image('Space.jpeg', use_column_width=True)

