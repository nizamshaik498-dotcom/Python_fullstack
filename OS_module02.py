#For creating directories using (makedirs()).

import os
directory="Pydir"
parent_dir="D:\\Users\\nizam\\OneDrive\\Documents\\GitHub\\Python_fullstack"
path=os.path.join(parent_dir,directory)
os.makedirs(path)
print("Directory '%s' created" % directory)
directory="pyd"
parent_dir="D:\\Users\\nizam\\OneDrive\\Documents\\GitHub\\Python_fullstack"
mode=0o666
path=os.path.join(parent_dir,directory)
os.makedirs(path,mode)
print("Directory '%s' created" % directory)