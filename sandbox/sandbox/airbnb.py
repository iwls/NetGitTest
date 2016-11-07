import pandas as pd
df = pd.read_csv("train_users.csv")

#print(df.head()) #shows the top 5 rows of the data
#print(df[:5]) #shows the first 5 rows of the data

##Print all the ID's
#print(df['id'])
#print(df['id'][:5]) #Prints 5 first rows of ID

#print(df['date_account_created'])

##Selecting mutilpe columns
#print(df[['id', 'age']])

##most selected country
#print(df['country_destination'].value_counts())
##top 5 most selected countries
#a = df['country_destination'].value_counts()
#print(a[:5])

##show the diffferent signup_methods and the count of them in the population.
#a = df['signup_flow'].value_counts()
#print(a.sort_index())

import numpy as np
import matplotlib.pyplot as plt

N = 50
x = np.random.rand(N)
y = np.random.rand(N)  ## this generates N random numbers between 0.00000000 and 0.99999999
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses


plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()


#signup_method
#affiliate_channel
#signup_flow
#language


##plot in a bar chart
#a.plot(kind= 'bar')


#print(year_to_age(df['age'],0,200))

#print(type(df)) #this is pandas.core.frame.DataFrame'

