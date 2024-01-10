import os

my_dir = ""
def copy_file(directory, delimiter):
    for file in os.listdir(directory):
        splitted = file.split("_")

        if len(splitted) >=2:
        

            prefix = splitted[0]
            suffix = delimiter.join(splitted[1:])

            new_prefix = "new1_" 
            new_name = new_prefix + suffix

            old_path = os.path.join(directory, file)
            new_path = os.path.join(directory, new_name)
            # print(new_name)
            os.rename(old_path, new_path)

            print(f"Renamed {old_path} to {new_path}")

        else:
            print(f"{file} ignored...")


copy_file(my_dir, "_")