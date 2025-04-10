import os
basepath = 'C:/Users/Bhumika/PycharmProjects/PythonProject/collections'

def getallfiles(basepath):
    for entry in os.listdir(basepath):
        full_path = os.path.join(basepath, entry)
        if os.path.isdir(os.path.join(full_path)):
            getallfiles(full_path)
        else:
            print(entry)

getallfiles(basepath)


