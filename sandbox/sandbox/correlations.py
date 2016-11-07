##Calculation of pearson correlation coefficient

#Data
a = [1,4,6]
b = [1,2,3]

#method one
import numpy
print(numpy.corrcoef(a,b))

#method 2
from scipy.stats.stats import pearsonr
print(pearsonr(a,b))