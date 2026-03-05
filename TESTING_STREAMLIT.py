#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd


# In[2]:


#file = "C:/Users/AJacobson1/Desktop/Transfer/Output/PricingOutput.csv"


# In[3]:


file = 'https://raw.githubusercontent.com/jazzfin21/pricetransparency-app/refs/heads/main/PricingOutput.csv'


# In[4]:


df = pd.read_csv(file, encoding='utf8')


# In[5]:


df['payer_name'] = df['payer_name'].fillna('none')


# In[6]:


for col in df.columns:
    df[col] = df[col].astype(str)


# In[7]:


df = df.drop(columns=['A','0'])


# In[8]:


#df['standard_charge_dollar'].dtype


# In[9]:


unique_payors = df['payer_name'].unique()
selected_payor = st.selectbox('Select a payor to filer: ', unique_payors)

filtered_df = df[df['payer_name'] == selected_payor]


# In[11]:


st.title('Northwell Health Competitor Price Transparency Data')
st.write('The table below contains hospital price transparency data from the latest machine-readable files published by Northwell Health competitor hospitals.')

st.dataframe(df)


# In[12]:


st.write('Here is the data for the payor you selected.')
st.dataframe(filtered_df)

