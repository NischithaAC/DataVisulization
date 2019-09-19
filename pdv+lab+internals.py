
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.read_csv('Accident_Cities.csv')
df1=pd.read_csv('Accident_States.csv')
df.head()


# In[3]:


#1
df["TotalInjured"] = df["Persons Injured - 2011"] + df["Persons Injured - 2012"]+df["Injured - 2013"]+df["Injured - 2014"]+df["Injured - 2015"]
three_cities=df.sort_values("TotalInjured",ascending=False).head(3)
three_cities["Name of City"]


# In[4]:


#2
df[df["Persons Injured - 2012"].le(df['Persons Injured - 2011'])]["Name of City"].head(3)


# In[5]:


import pandas as pd
df1=pd.read_csv('Accident_States.csv',skiprows=1)
df1.head(2)


# In[42]:


df1["overSpeed"] = df1["2010"]+df1["2011"]+df1["2012"]+df1["2013"]+df1["2014"]+df1["2015"]
states = df1.sort_values("overSpeed",ascending=False)
states["States/UTs"].head(5)


# In[6]:


import matplotlib.pyplot as plt
df1["overSpeed"] = df1["2010"]+df1["2011"]+df1["2012"]+df1["2013"]+df1["2014"]+df1["2015"]
y = states["States/UTs"]
x = df["overSpeed"]
plt.plot(x)
plt.show()

