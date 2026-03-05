#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np


# In[2]:


file = r"C:\Users\AJacobson1\Desktop\Transfer\Output\PricingOutput.csv"


# In[3]:


df = pd.read_csv(file)


# In[4]:


unique_payors = df['payer_name'].unique()
selected_payor = st.selectbox('Select a payor to filer: ', unique_payors)

filtered_df = df[df['payer_name'] == selected_payor]


# In[5]:


st.title('Northwell Health Competitor Price Transparency Data')
st.write('The table below contains hospital price transparency data from the latest machine-readable files published by Northwell Health competitor hospitals.')

st.dataframe(df, use_container_width=True)


# In[6]:


st.write('Here is the data for the payor you selected.')
st.dataframe(filtered_df)

