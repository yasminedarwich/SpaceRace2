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


st.title('Which companies are launching the most 🚀?')


df = pd.read_csv('Space_Corrected.csv')


df = df.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1)
df.head()


ds = df["Company Name"].value_counts().head(28)



# Rockets Launched By company

ds = df['Company Name'].value_counts().reset_index()

ds.columns = [
    'Name of Company', 
    'Number of Launches'
]

ds = ds.sort_values(['Number of Launches'])

col1, col2 = st.columns(2)

with col1:
    col = st.color_picker('Select a plot color!')
    fig = px.bar(
    ds, 
    x='Number of Launches', 
    y="Name of Company", 
    orientation='h', 
    title='Number of Launches per Company', 
    color_discrete_sequence =['blue'],
    width=600,
    height=900 
)
    fig.update_traces(marker=dict(color=col))
    st.plotly_chart(fig)

#Status of rocket


ds = df['Status Rocket'].value_counts().reset_index()

ds.columns = [
    'status', 
    'count'
]
with col2:
    fig1 = px.pie(
    ds, 
    values='count', 
    names="status", 
    title='Status of the Rocket',
    width=400, 
    height=400,
    color_discrete_sequence=px.colors.sequential.Agsunset
)
    st.plotly_chart(fig1)

#Status Distribution


ds = df['Status Mission'].value_counts().reset_index()

ds.columns = [
    'Mission Status', 
    'Count'
]

with col2:
    fig2 = px.bar(
    ds, 
    x='Mission Status', 
    y="Count", 
    orientation='v', 
    title='Mission Status Distribution', 
    width=400,
    height=400,
    color_discrete_sequence =['purple']
)
    fig2.update_traces(marker=dict(color=col))
    st.plotly_chart(fig2)

#sunburst

countries_dict = {
    'Russia' : 'Russian Federation',
    'New Mexico' : 'USA',
    "Yellow Sea": 'China',
    "Shahrud Missile Test Site": "Iran",
    "Pacific Missile Range Facility": 'USA',
    "Barents Sea": 'Russian Federation',
    "Gran Canaria": 'USA'
}

df['country'] = df['Location'].str.split(', ').str[-1].replace(countries_dict)


# In[10]:

col3, col4 = st.columns(2)


sun = df.groupby(['country', 'Company Name', 'Status Mission'])['Datum'].count().reset_index()

sun.columns = [
    'country', 
    'company', 
    'status', 
    'count'
]

with col3:
    fig3 = px.sunburst(
    sun, 
    path=[
        'country', 
        'company', 
        'status'
    ], 
    values='count', 
    title='Sunburst Chart including Countries, Companies & their Success',
    width=600,
    height=600
)
    st.plotly_chart(fig3)

#Most Experienced Companies

df['date'] = pd.to_datetime(df['Datum'])
df['year'] = df['date'].apply(lambda datetime: datetime.year)
df['month'] = df['date'].apply(lambda datetime: datetime.month)
df['weekday'] = df['date'].apply(lambda datetime: datetime.weekday())


# In[12]:


ds = df.groupby(['Company Name'])['year'].nunique().reset_index()

ds.columns = [
    'company', 
    'count'
]

with col4:
    fig4 = px.bar(
    ds, 
    x="company", 
    y="count", 
    width=600,
    height=600,
    title='Most Experienced Companies (Years of Launches)', labels={'company':'Company', 'count':'# of Years'}
).update_xaxes(categoryorder="total descending")
    fig4.update_traces(marker=dict(color=col))
    st.plotly_chart(fig4)
