import os

os.chdir("/Users/bradmorgan60/OneDrive/Documents/demo")

# print(os.listdir())

for file in os.listdir():
    file_name, extension = os.path.splitext(file)
    f_title, f_type, f_num = file_name.split(' ')

    f_title = f_title.strip()
    f_type = f_type.strip()
    f_num = f_num.strip()[1:].zfill(2)

    
    new_name = "{}-{}{}".format(f_num, f_title, extension)
    os.rename(file, new_name)




