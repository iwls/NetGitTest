##How to use GitHub
#1. create a new Repository ( project) on www.github.com
#2. Donwload that folder to your local computer. To do this
# a/ use "Terminal" on Mac; open the application
# b/ Navigate to the folder where you want to store the repository by using
  # ls = to show the list of files in a folder
  # cd and cd.. to move to the next folder or the previous one.
# c/git clone https://github.com/<reporsitoryname>.git  
    #(you can copy the link), to copy the repository local
    # this will pull all information in
#d/ git status ( you have an untracket file => Github doesnt know the file exists)
#e/ git add <Filename>.<extension>
#f/ git commmit -m "<message body>" -- this commits the new file to github and adds a message
    #it is still not on the github website , you still need to push it
#g/ git push   #This will push the files from the computer to Github

##To download it again on another computer you need to pull it 
#h/ git pull
data(iris)
library(dplyr)
head(iris)
summarize(iris,mean(Sepal.Length))
