#!/usr/bin/env python
# coding: utf-8

# In[11]:


import streamlit as st
import pandas as pd
import pyarrow as pa
from pyarrow import types


# In[ ]:


#file = "C:/Users/AJacobson1/Desktop/Transfer/Output/PricingOutput.csv"


# In[2]:


file = 'https://raw.githubusercontent.com/jazzfin21/pricetransparency-app/refs/heads/main/PricingOutput.csv'


# In[3]:


df = pd.read_csv(file, encoding='windows-1252')


# In[4]:


df = df.fillna('none')


# In[5]:


df = df.drop(columns=['A','0'])


# In[6]:


for col in df.columns:
    df[col] = df[col].astype(object)
    #print(col, ': ', df[col].dtype, df[col].dtype == pd.ArrowDtype(pa.string()))


# In[7]:


#arrow_table = pa.Table.from_pandas(df)


# In[12]:


#large_utf8_fields = []
#for field in arrow_table.schema:
    #if types.is_large_string(field.type): 
        #large_utf8_fields.append(field.name)


# In[ ]:


# Convert the DataFrame to a pyarrow Table
#df = pa.Table.from_pandas(df)

# Print the schema (which lists the pyarrow datatypes)
#print(table.schema)


# In[ ]:


unique_payors = df['payer_name'].unique()
selected_payor = st.selectbox('Select a payor to filter: ', unique_payors)

filtered_df = df[df['payer_name'] == selected_payor]


# In[ ]:


#df = df.to_dict(orient='dict')
#filtered_df = filtered_df.to_dict(orient='dict')


# In[ ]:


st.title('Northwell Health Competitor Price Transparency Data')
st.write('The table below contains hospital price transparency data from the latest machine-readable files published by Northwell Health competitor hospitals.')

st.dataframe(df)


# In[ ]:


st.write('Here is the data for the payor you selected.')
st.dataframe(filtered_df)

