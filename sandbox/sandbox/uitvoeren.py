import scipy as sp
data = sp.genfromtxt("train_users.csv", delimiter=",")

print (data[:5]) # prints first 5 rows, all columns
#print (data.shape) #show the dimentions of the data
#result => tuple with (numbers of records , number of columns)


# try to plot the first data
from pylab import *

#initialize variables, N is the number of countries
N= 12

#plot the barchart
bar(arrange(N), X, align= 'center')