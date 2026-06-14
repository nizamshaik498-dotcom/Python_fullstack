#For checking the current working directory
import os
cwd=os.getcwd() #CWD(current working directory)
print("Currenrt working directory: ",cwd)

#Changing current working directory
def current_path(label):
    print(f"current working directory{label}")
    print(os.getcwd())
    print()

current_path("before")
os.chdir('../')
current_path("after")

#Creating directory(mkdir)
import os
directory ="python full stack"
parent_dir="D:/ETHNUS/"
path=os.path.join(parent_dir,directory)
os.mkdir(path)

print("Directory '%s' created" % directory)
directory="python stack"
parent_dir="D:/ETHNUS"
mode=0o666      #Default code for mode (0o666)
path=os.path.join(parent_dir,directory)
os.mkdir(path,mode)
print("Directory '%s' created" % directory)