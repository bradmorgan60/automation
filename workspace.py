import os

# print(os.getcwd())
my_dir_RE0 = 'c:/Users/KF511GX/OneDrive - Corteva/Wave 3/Testing/Cutover/RE0'
my_dir_PE0 = 'c:/Users/KF511GX/OneDrive - Corteva/Wave 3/Testing/Cutover/PE0'
my_dir_RE6 = 'c:/Users/KF511GX/OneDrive - Corteva/Wave 3/Testing/Cutover/RE6'

def RE6_Batch_Jobs_Rename(directory, delimiter):
    for file in os.listdir(directory):

        splitted = file.split(delimiter)

        # print(splitted)

        if len(splitted) >= 2:

        #     print(splitted)

            # old_prefix = splitted[0]
            suffix = delimiter.join(splitted[1:])

            new_prefix = "ZRE6300-"

            new_file = new_prefix + suffix

            # print(new_file)

            old_path = os.path.join(directory, file)
            new_path = os.path.join(directory, new_file)

            os.rename(old_path, new_path)

            print(f"Renamed {old_path} to {new_path}")

        else:
            print(f"Ignored: {file}. Unable to determine prefix")
        

def RE0_Batch_Jobs_Rename(directory, delimiter):
    for file in os.listdir(directory):

        splitted = file.split(delimiter)

        # print(splitted)

        if len(splitted) >= 2:

        #     print(splitted)

            # old_prefix = splitted[0]
            suffix = delimiter.join(splitted[1:])

            new_prefix = "ZRE0300-"

            new_file = new_prefix + suffix

            # print(new_file)

            old_path = os.path.join(directory, file)
            new_path = os.path.join(directory, new_file)

            os.rename(old_path, new_path)

        

            print(f"Renamed {old_path} to {new_path}")

        else:
            print(f"Ignored: {file}. Unable to determine prefix")
        

def PE0_Batch_Jobs_Rename(directory, delimiter):
    for file in os.listdir(directory):

        splitted = file.split(delimiter)

        if len(splitted) >= 2:

            old_prefix = splitted[0]
            suffix = delimiter.join(splitted[1:])

            new_prefix = "ZPE0300-"

            new_file = new_prefix + suffix

            old_path = os.path.join(directory, file)
            new_path = os.path.join(directory, new_file)

            os.rename(old_path, new_path)

            print(f"Renamed {old_path} to {new_path}")

        else:
            print(f"Ignored: {file}. Unable to determine prefix")
        

# RE0_Batch_Jobs_Rename(my_dir_RE0, "-")
# PE0_Batch_Jobs_Rename(my_dir_PE0, "-")
RE6_Batch_Jobs_Rename(my_dir_RE6, "-")
    
    

    
    

