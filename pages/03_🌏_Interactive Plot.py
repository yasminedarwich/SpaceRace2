import streamlit as st
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()

import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px
from plotly.subplots import make_subplots

import warnings
warnings.filterwarnings("ignore")


st.title('Interactive Plot! Choose your own X and Y Axis!')


df = pd.read_csv('Space_Corrected.csv')


df = df.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1)
df.head()


col1, col2 = st.columns(2)
    
x_axis_val = col1.selectbox('Select the X-axis', options=df.columns)
y_axis_val = col2.selectbox('Select the Y-axis', options=df.columns)
col = st.color_picker('Select a plot color!')

fig = px.scatter(
    df, 
    x=x_axis_val, 
    y=y_axis_val, 
    orientation='h', 
    color_discrete_sequence =['blue'],
    width=600,
    height=900 
)
fig.update_traces(marker=dict(color=col))
st.plotly_chart(fig, use_container_width=True)


if st.button('Click me for a Surprise! '):
            st.markdown('😆 🎈 😆 🎈')
            st.balloons()

