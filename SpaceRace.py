#!/usr/bin/env python
# coding: utf-8

# In[2]:

import streamlit as st
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()
get_ipython().run_line_magic('matplotlib', 'inline')

import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px
from plotly.subplots import make_subplots

import warnings
warnings.filterwarnings("ignore")


# In[3]:


df = pd.read_csv('Space_Corrected.csv')


# In[4]:


df = df.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1)
df.head()


# In[5]:


ds = df["Company Name"].value_counts().head(28)
ds


# In[6]:


ds = df['Company Name'].value_counts().reset_index()

ds.columns = [
    'Name of Company', 
    'Number of Launches'
]

ds = ds.sort_values(['Number of Launches'])

fig = px.bar(
    ds, 
    x='Number of Launches', 
    y="Name of Company", 
    orientation='h', 
    title='Number of Launches per Company', 
    color_discrete_sequence =['blue'],
    width=800,
    height=1000 
)

fig.show()


# In[7]:


ds = df['Status Rocket'].value_counts().reset_index()

ds.columns = [
    'status', 
    'count'
]

fig = px.pie(
    ds, 
    values='count', 
    names="status", 
    title='Status of the Rocket',
    width=500, 
    height=500,
    color_discrete_sequence=px.colors.sequential.Agsunset
)

fig.show()


# In[8]:


ds = df['Status Mission'].value_counts().reset_index()

ds.columns = [
    'Mission Status', 
    'Count'
]

fig = px.bar(
    ds, 
    x='Mission Status', 
    y="Count", 
    orientation='v', 
    title='Mission Status Distribution', 
    width=500,
    height=500,
    color_discrete_sequence =['purple']
)

fig.show()


# In[9]:


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


sun = df.groupby(['country', 'Company Name', 'Status Mission'])['Datum'].count().reset_index()

sun.columns = [
    'country', 
    'company', 
    'status', 
    'count'
]

fig = px.sunburst(
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

fig.show()


# In[11]:


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

fig = px.bar(
    ds, 
    x="company", 
    y="count", 
    title='Most Experienced Companies (Years of Launches)', labels={'company':'Company', 'count':'# of Years'}
).update_xaxes(categoryorder="total descending")

fig.show()


# In[13]:


data = df.groupby(['Company Name', 'year'])['Status Mission'].count().reset_index()

data.columns = [
    'company', 
    'year', 
    'starts'
]

top5 = data.groupby(['company'])['starts'].sum().reset_index().sort_values('starts', ascending=False).head(5)['company'].tolist()


# In[14]:


data = data[data['company'].isin(top5)]

fig = px.line(
    data, 
    x="year", 
    y="starts", 
    title='Dynamic of Top 5 Companies by # of Launches', 
    color='company'
)

fig.show()


# In[15]:


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

fig = px.bar(
    data, 
    x="company", 
    y="starts", 
    title='Failures in 2020', 
    width=600
)

fig.show()


# In[17]:


ds = df.groupby(['year', 'country'])['Status Mission'].count().reset_index().sort_values(['year', 'Status Mission'], ascending=False)
ds = pd.concat([group[1].head(1) for group in ds.groupby(['year'])])
ds.columns = ['year', 'country', 'launches']

fig = px.bar(
    ds, 
    x="year", 
    y="launches", 
    color='country', 
    title='Leaders by Launches per year (countries)'
)

fig.show()


# In[18]:


ds = df[df['Status Mission']=='Success']
ds = ds.groupby(['year', 'country'])['Status Mission'].count().reset_index().sort_values(['year', 'Status Mission'], ascending=False)
ds = pd.concat([group[1].head(1) for group in ds.groupby(['year'])])
ds.columns = ['year', 'country', 'launches']

fig = px.bar(
    ds, 
    x="year", 
    y="launches", 
    color='country', 
    title='Leaders by Success Launches per year (Countries)',
    width=800
)

fig.show()


# In[19]:


ds = df.groupby(['year', 'Company Name'])['Status Mission'].count().reset_index().sort_values(['year', 'Status Mission'], ascending=False)
ds = pd.concat([group[1].head(1) for group in ds.groupby(['year'])])
ds.columns = ['year', 'company', 'launches']

fig = px.bar(
    ds, 
    x="year", 
    y="launches", 
    color='company', 
    title='Leaders by Launches per year (Companies)',
    width=800
)

fig.show()


# In[20]:


ds = df[df['Status Mission']=='Success']
ds = ds.groupby(['year', 'Company Name'])['Status Mission'].count().reset_index().sort_values(['year', 'Status Mission'], ascending=False)
ds = pd.concat([group[1].head(1) for group in ds.groupby(['year'])])
ds.columns = ['year', 'company', 'launches']

fig = px.bar(
    ds, 
    x="year", 
    y="launches", 
    color='company', 
    title='Leaders by Success Launches per year (Companies)',
    width=800
)

fig.show()


# In[21]:


labels=list(df["Status Mission"].value_counts().keys())
sizes=df["Status Mission"].value_counts()
explode=[]
for i in labels:
    explode.append(0.05)
plt.figure(figsize=(10,8))
sliceColors = ['mediumpurple', 'blue', 'cyan','yellow']
plt.pie(sizes,labels=labels,explode=explode, autopct='%1.2f%%', startangle=25, shadow=False, colors=sliceColors)
plt.title("Success rate of Mission", fontsize=18, loc="right")
plt.axis("equal")
plt.tight_layout()


# In[22]:


plt.figure(figsize=(30,5))
cmp = df.groupby(['Company Name','Status Mission']).count()['Detail'].reset_index()
cmp = cmp[cmp['Status Mission']=="Success"].sort_values('Detail',ascending=False)
sns.barplot(x='Company Name',y='Detail',data=cmp[1:20])
plt.ylabel('No of successful missions')
t=plt.title('Company vs Sucessful Missions')


# In[23]:


plt.figure(figsize=(30,5))
cmp = df[df['Status Mission']!="Success"].groupby('Company Name').count().sort_values('Detail',ascending=False).reset_index()
sns.barplot(x='Company Name',y='Detail',data=cmp[1:20])
plt.ylabel('No of unsuccessful missions')
t=plt.title('Company vs Unsucessful Missions')


# In[24]:


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
df['day'] = df['Datum'].apply(lambda x:x.split()[0])
df_days = df.groupby('day').count()['Detail'].reset_index()

df_days['day'] = pd.Categorical(df_days['day'], categories=days, ordered=True)
df_days = df_days.sort_values('day')
plt.figure(figsize=(11,4))
sns.barplot(x='day', y='Detail', data=df_days)
plt.ylabel('No of launches')
plt.xlabel('Day of the Week')
b=plt.title('Launches per Days of the Week')


# In[25]:


from calendar import month_abbr
plt.figure(figsize=(12,6))
df['month'] = df['Datum'].apply(lambda x: x.split()[1])
df_month = df.groupby('month').count()['Detail'].reset_index()
df_month['month'] = pd.Categorical(df_month['month'], categories=list(month_abbr)[1:], ordered=True)
df_month = df_month.sort_values('month')
bar=sns.barplot(x='month',y='Detail',data=df_month)
for p in bar.patches:
    bar.annotate(int(p.get_height()), 
               (p.get_x() + p.get_width()/2, p.get_height()), ha='center', va='center', 
               xytext=(0,7), textcoords = 'offset points')
plt.ylabel('No of launches')
plt.xlabel('Month')
_ = plt.title('# of rockets Launched per Month')


# In[26]:


df['year'] = df['Datum'].apply(lambda x:x.split()[3])
date= df.groupby('year').count()['Detail'].reset_index()
plt.figure(figsize=(20,6))
b=sns.barplot(x='year', y='Detail', data=date)
plt.ylabel('No of launches')
plt.xlabel('Year')
plt.title('# of Launches per Year')
_=b.set_xticklabels(b.get_xticklabels(), rotation=90, horizontalalignment='right')


# In[27]:


colors=['#ad51c9','#fffc45','#00a7d5']
status= df['Status Mission'].unique()
j=0
for s in status[1:]:
    df[df['Status Mission']==s].groupby('year').count()['Detail'].plot(kind='bar',figsize=(18,5),color=colors[j])
    j+=1
plt.ylabel('# of Unsuccessful Missions')
t = plt.title("# & Type of Unsuccessful Missions per Year")
t=plt.legend(status[1:])


# In[28]:


budget = df.copy().dropna()
budget.loc[:, ' Rocket'] = budget[' Rocket'].apply(lambda x:float(x.replace(',','')))
b = budget.groupby('Company Name').sum().sort_values(' Rocket', ascending=False).reset_index()


# In[29]:


plt.figure(figsize=(20,4))
bar = sns.barplot(x='Company Name',y=' Rocket',data=b)
bar.set_xticklabels(bar.get_xticklabels(), rotation=30)
plt.ylabel('Money spent on Missions in million $')
t=plt.title('Budget per Company')


# In[30]:


df['Hour']=df['Datum'].apply(lambda datum: int(datum.split()[-2][:2]) if datum.split()[-1]=='UTC' else np.nan)
hr = df.groupby('Hour').count()['Detail'].reset_index()
px.bar(hr, x='Hour',y='Detail',labels={'Detail':'No of Missions','Hour':"Time(24hrs)"},title="# of Launches in Time",width=700,height=400)


# In[ ]:





# In[ ]:




