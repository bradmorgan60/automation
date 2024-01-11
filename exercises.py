import os


# my_dir = "C:/Users/KF511GX/OneDrive - EY/Documents/Engineering"

# my_dir = input("Enter the directory: ")

# C:\Users\KF511GX\OneDrive - EY\Documents\Engineering

# listdir just lists all files / folders in a directory
# for file in os.listdir(my_dir):
#     print(file)


# for file in os.scandir(my_dir):
#     print(file)

print(f"Operating system: {os.name}")
print(f"\nCurrent working directory: {os.getcwd()}")

try: 
    filename = 'demo1.txt'
    f = open(filename, 'r')
    f.read()
    f.close()
except IOError:
    print("Not accessed or problem reading: " + filename)

