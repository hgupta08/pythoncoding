import os
# entries = os.listdir('C:/Users/Bhumika/PycharmProjects/PythonProject')
# for entry in entries:
#     print(entry)

# List all subdirectories using os.listdir
basepath = 'C:/Users/Bhumika/PycharmProjects/PythonProject'

for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath,entry)):
        print(entry)

print("--------------------------------")
# List all files in a directory using os.listdir


import os

def list_files_recursive(path):

    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            list_files_recursive(full_path)
        else:
            print(full_path)

# Specify the directory path you want to start from
directory_path = './'
list_files_recursive(basepath)

# import os
#
# def list_files_walk(start_path):
#     for root, dirs, files in os.walk(start_path):
#         for file in files:
#             print(os.path.join(root, file))
#
# # Specify the directory path you want to start from
# directory_path = './'
# list_files_walk(basepath)


#
# for entry in os.listdir(basepath):
#     if os.path.isdir(os.path.join(basepath, entry)):
#         print(entry)