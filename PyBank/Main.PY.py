#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import pandas as pd



# In[5]:


file_path = (r"C:\Users\jasmi\Downloads\Starter_Code\Starter_Code\PyBank\Resources\budget_data.csv")
df = pd.read_csv(r"C:\Users\jasmi\Downloads\Starter_Code\Starter_Code\PyBank\Resources\budget_data.csv")
print(df)


# In[6]:


total_months = df.shape[0]
net_total = df['Profit/Losses'].sum()
df['Profit/Losses Change'] = df['Profit/Losses'].diff()
average_changes = df['Profit/Losses Change'].mean()


# In[7]:


index_max_increase = df['Profit/Losses Change'].idxmax()

index_max_decrease = df['Profit/Losses Change'].idxmin()

# Get the date and amount of the greatest decrease in profits
date_max_decrease = df.loc[index_max_decrease, 'Date']
amount_max_decrease = df.loc[index_max_decrease, 'Profit/Losses Change']



date_max_increase = df.loc[index_max_increase, 'Date']
amount_max_increase = df.loc[index_max_increase, 'Profit/Losses Change']


# In[8]:


print("Greatest decrease in profits:")
print(f"Date: {date_max_decrease}, Amount: {amount_max_decrease}")

print(f"Date: {date_max_increase}, Amount: {amount_max_increase}")
print("Changes in Profit/Losses over the entire period:")
print("\nAverage of the changes in Profit/Losses:", average_changes)
print("Net total amount of Profit/Losses over the entire period:", net_total)
print("Total number of months in the dataset:", total_months)


# In[ ]:




