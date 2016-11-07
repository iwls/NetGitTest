#This package work really well, also with csv files that have a header row

import pandas as pd
df = pd.read_csv("train_users.csv")

print(df[:5]) #Shows first 5 rows of dataset
#print(df.head())  #Alternative to show first 5 rows



#other methods that I was able to read the data, but I had issues to haev columns in INT instead of string etc
# to deal with the column names

#import csv

#with open("train_users.csv") as csvfile:
#    reader = csv.reader(csvfile, delimiter = ",")
#    id=[]
#    gender=[]
#    country=[]
#    age=[]
#    for row in reader:
#        id.append(row[0])
#        gender.append(row[4])
#        age.append(row[5])
#        country.append(row[15])