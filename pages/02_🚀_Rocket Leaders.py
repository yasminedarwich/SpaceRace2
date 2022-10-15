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


st.title('Overview of 🚀 launches ever since the beginning of the Space Race in 1957')


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



#Status of rocket


ds = df['Status Rocket'].value_counts().reset_index()

ds.columns = [
    'status', 
    'count'
]

#Status Distribution


ds = df['Status Mission'].value_counts().reset_index()

ds.columns = [
    'Mission Status', 
    'Count'
]


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


#Top 5 Companies Dynamic Line 

data = df.groupby(['Company Name', 'year'])['Status Mission'].count().reset_index()

data.columns = [
    'company', 
    'year', 
    'starts'
]

top5 = data.groupby(['company'])['starts'].sum().reset_index().sort_values('starts', ascending=False).head(5)['company'].tolist()


# In[14]:
col4, col5 = st.columns(2)

data = data[data['company'].isin(top5)]

with col4:
    fig5 = px.line(
    data, 
    x="year", 
    y="starts", 
    title='Dynamic of Top 5 Companies by # of Launches', 
    width=600,
    color='company'
)
    st.plotly_chart(fig5)

#Failures in 2020 


data = df.groupby(['Company Name', 'year'])['Status Mission'].count().reset_index()

data.columns = [
    'company', 
    'year', 
    'starts'
]

data = data[data['year']==2020]


# In[16]:


data = df[df['Status Mission']=='Failure']
data = data.groupby(['Company Name', 'year'])['Status Mission'].count().reset_index()

data.columns = [
    'company', 
    'year', 
    'starts'
]

data = data[data['year']==2020]

with col5:
    fig6 = px.bar(
    data, 
    x="company", 
    y="starts", 
    title='Failures in 2020', 
    width=600
)
    st.plotly_chart(fig6)

#Leaders by launches 

ds = df.groupby(['year', 'country'])['Status Mission'].count().reset_index().sort_values(['year', 'Status Mission'], ascending=False)
ds = pd.concat([group[1].head(1) for group in ds.groupby(['year'])])
ds.columns = ['year', 'country', 'launches']

with col4:
    fig7 = px.bar(
    ds, 
    x="year", 
    y="launches", 
    color='country', 
    width=600,
    title='Leaders by Launches per year (countries)'
)
    st.plotly_chart(fig7)

#Leaders by success launch 

ds = df[df['Status Mission']=='Success']
ds = ds.groupby(['year', 'country'])['Status Mission'].count().reset_index().sort_values(['year', 'Status Mission'], ascending=False)
ds = pd.concat([group[1].head(1) for group in ds.groupby(['year'])])
ds.columns = ['year', 'country', 'launches']

with col5:
    fig8 = px.bar(
    ds, 
    x="year", 
    y="launches", 
    color='country', 
    title='Leaders by Success Launches per year (Countries)',
    width=600
)
    st.plotly_chart(fig8)

#Company launch leaders 

ds = df.groupby(['year', 'Company Name'])['Status Mission'].count().reset_index().sort_values(['year', 'Status Mission'], ascending=False)
ds = pd.concat([group[1].head(1) for group in ds.groupby(['year'])])
ds.columns = ['year', 'company', 'launches']

with col4:
    fig9 = px.bar(
    ds, 
    x="year", 
    y="launches", 
    color='company', 
    title='Leaders by Launches per year (Companies)',
    width=600
)
    st.plotly_chart(fig9)

#Success Company Launches 

ds = df[df['Status Mission']=='Success']
ds = ds.groupby(['year', 'Company Name'])['Status Mission'].count().reset_index().sort_values(['year', 'Status Mission'], ascending=False)
ds = pd.concat([group[1].head(1) for group in ds.groupby(['year'])])
ds.columns = ['year', 'company', 'launches']

with col5:
    fig10 = px.bar(
    ds, 
    x="year", 
    y="launches", 
    color='company', 
    title='Leaders by Success Launches per year (Companies)',
    width=600
)
    st.plotly_chart(fig10)



