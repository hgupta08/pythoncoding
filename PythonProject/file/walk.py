import os
basepath = 'C:/Users/Bhumika/PycharmProjects/PythonProject/collections/'

for dirpath, dirnames, files in os.walk(basepath):
    # print(f'Found directory: {dirpath}')
    # print(dirnames)
    for file_name in files:
        print(file_name)