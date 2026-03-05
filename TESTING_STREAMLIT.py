#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd


# In[ ]:


#file = "C:/Users/AJacobson1/Desktop/Transfer/Output/PricingOutput.csv"


# In[ ]:


file = 'https://raw.githubusercontent.com/jazzfin21/pricetransparency-app/refs/heads/main/PricingOutput.csv'


# In[ ]:


df = pd.read_csv(file, encoding='windows-1252')


# In[ ]:


df = df.fillna('none')


# In[ ]:


df = df.drop(columns=['A','0'])


# In[ ]:


#df = df.to_html(index=False)


# In[ ]:


for col in df.columns:
    df[col] = df[col].astype(str)
    #print(col, ': ', df[col].dtype, df[col].dtype == pd.ArrowDtype(pa.string()))


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

st.write(df)


# In[ ]:


st.write('Here is the data for the payor you selected.')
st.write(filtered_df)

