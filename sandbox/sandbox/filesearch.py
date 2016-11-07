# show all files in a directory with the full path
import os
#a = os.getcwd() #uses the current directory path

def print_dir(dir_path):
    for name in os.listdir(dir_path):
        print(os.path.join(dir_path, name))

z = '/Users/ianwls/Documents/Test_python/'

#print_dir(z)

#a = os.getcwd() #this looks up the current path of the directory

###Provides a list of files/folders in a certain folder
def all_files_path (pad):
    if os.path.exists(pad):
        files = os.listdir(pad)
        return files
    else:
        return ("path does not exist")


#b = all_files_path(z)
#b= ['.DS_Store', 'EAU_NL_complete.pdf', 'Test1' , 'GO_1-2016_FlipBook_NL.pdf']

def all_files(lijst):
    if os.path.exists(lijst):               # checks if the path exists
        bestand = []                        # creates empty list bestand
        map = []                            # creates empty list map
        for name in os.listdir(lijst):      # for every name in list check if it is a file or a list
            a = os.path.join(lijst, name)
            if os.path.isfile(a):
                bestand.append(name)
            if os.path.isdir(a):
                map.append(name)
        if map:
            for x in map:
                link = os.path.join(lijst, name)
                print(link)
                bestand.extend(all_files(link))
    return bestand
print(all_files(z))




