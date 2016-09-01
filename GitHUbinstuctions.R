##How to use GitHub
#1. create a new Repository ( project) on www.github.com
#2. Donwload that folder to your local computer. To do this
# a/ use "Terminal" on Mac; open the application
# b/ Navigate to the folder where you want to store the repository by using
  # ls = to show the list of files in a folder
  # cd and cd.. to move to the next folder or the previous one.
# c/git clone https://github.com/<reporsitoryname>.git  
  #(you can copy the link), to copy the repository local


data(iris)
library(dplyr)
head(iris)
summarize(iris,mean(Sepal.Length))