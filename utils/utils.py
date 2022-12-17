import os

def isExists(path):
    return os.path.exists(path) == True


def CrateFolder(path):
    if isExists(path) == False:
        os.mkdir(path)

def ChangeNameFolder(path,oldname, newname):
    oldpath = os.path.join(path,oldname)
    newpath = os.path.join(path,newname)
    if isExists(oldpath) == True:
        os.rename(oldpath, newpath)

def DeleteFolder(path):
    if isExists(path) == True:
        for file in os.listdir(path):  # loop to delete each file in folder
            os.remove(f'{path}/{file}')  # delete file

        os.rmdir(path)

