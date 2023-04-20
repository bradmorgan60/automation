
import os
import shutil
from turtle import down

# print(os.listdir())
# Rename files in demo folder
def rename():
    os.chdir("/Users/bradmorgan60/OneDrive/Documents/demo")

    for file in os.listdir():
        file_name, extension = os.path.splitext(file)
        f_title, f_type, f_num = file_name.split(' ')

        f_title = f_title.strip()
        f_type = f_type.strip()
        f_num = f_num.strip()[1:].zfill(2)

        
        new_name = "{}-{}{}".format(f_num, f_title, extension)
        os.rename(file, new_name)

# rename()

# downloads = os.listdir("/Users/bradmorgan60/downloads")
my_dir = "/Users/bradmorgan60/OneDrive/Documents/automation"

# Move files from downloads to current directory
def move():
    os.chdir("/Users/bradmorgan60/Downloads")

    for file in os.listdir():
        f_name, f_ext = os.path.splitext(file)

        if f_ext == '.txt':
            shutil.move(file, my_dir)
            
        elif f_ext == ".pdf":
            shutil.move(file, my_dir)

# move()

# Move files in current directory back to downloads
def move_back():
    os.listdir()
    downloads = "/Users/bradmorgan60/downloads"

    for file in os.listdir():
        f_name, f_ext = os.path.splitext(file)

        if f_ext == ".txt":
            shutil.move(file, downloads)

        elif f_ext == ".pdf":
            shutil.move(file, downloads)

move_back()






        
    

