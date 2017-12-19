
# coding: utf-8

# In[470]:


import pandas as pd
import numpy as np


# In[471]:


import os


# In[482]:


files = ['012016.xlsx',
 '022016.xlsx',
 '032016.xlsx',
 '042016.xlsx',
 '052016.xlsx',
 '062016.xlsx',
 '072016.xlsx',
 '082016.xlsx',
 '092016.xlsx',
 '102016.xlsx',
 '112016.xlsx',
 '122016.xlsx',
 '201501.xlsx',
 '201502.xlsx',
 '201503.xlsx',
 '201504.xlsx',
 '201505.xlsx',
 '201506.xlsx',
 '201507.xlsx',
 '201508.xlsx',
 '20150901through0915.xlsx',
 '20150916through0930.xlsx',
 '201510through201511.xlsx',
 '201512.xlsx']

all_data = pd.DataFrame()

for f in files:
    ice_logs = pd.read_excel(f)
    pretty_log = ice_logs.rename(columns={c: c.replace(' ','_') for c in ice_logs.columns})
    all_data = all_data.append(pretty_log)

df = all_data[['Organization','Received_Date','Request_Description','Request_ID']]
# df = all_data.dropna(axis=0,how='all')
df.head()
                               
# beautiful_log = pretty_log.set_index('Request_ID',inplace=True)
#     print(beautiful_log)
# #     pretty_log.head()
# # #     all_data = all_data.append(df)


# In[484]:


df.set_index('Request_ID', inplace=True)


# In[475]:


pd.to_datetime('Recieved_Date', format='%Y%m%d', errors='ignore')


# In[489]:


df.head()


# In[476]:


ftw = pd.read_json('foia_data.json', orient='rows')
closer = pd.DataFrame.transpose(ftw)
trac_page = closer.rename(columns={c: c.replace('FOIA Case\xa0#','Request_ID') for c in closer.columns})


# In[490]:


trac_page.set_index('Request_ID', inplace=True)
trac_page.head()


# In[478]:


last_log = trac_page.rename(columns={c: c.replace(' ','_') for c in trac_page.columns})
last1_log = last_log.rename(columns={c: c.replace('Organization','Home') for c in last_log.columns})
last2_log = last1_log.rename(columns={c: c.replace('Company','Organization') for c in last1_log.columns}) 
last3_log = last2_log.rename(columns={c: c.replace('Date_Received','Received_Date') for c in last2_log.columns})
last4_log = last3_log.rename(columns={c: c.replace('Description','Request_Description') for c in last3_log.columns})
                                                     
last4_log.head()


# In[491]:


left = last4_log[['Organization','Received_Date','Request_Description','Requestor_Type','Date_Closed','Outcome_Type','Denial_Reason','Process_Time']]
result = df.append(left)


# In[497]:


result.sort_index()


# In[505]:


result.to_excel('fioa_finished.xlsx')

