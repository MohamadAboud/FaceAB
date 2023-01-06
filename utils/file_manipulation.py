import os
from os import makedirs
from utils.dev import Developer


def isExists(path):
    return os.path.exists(path) == True


def CrateFolder(path):
    if isExists(path) == False:
        os.mkdir(path)


def ChangeNameFolder(path, oldname, newname):
    oldpath = os.path.join(path, oldname)
    newpath = os.path.join(path, newname)

    if isExists(newpath): raise FileExistsError()

    if isExists(oldpath):
        Developer.log(f"The folder will be rename\n-> from: \'{oldpath}\'\n-> to\'{newpath}\'", mode='warning')
        os.rename(oldpath, newpath)


def DeleteFolder(path):
    if isExists(path) == True:
        Developer.log(f"The folder will be deleted\n-> path: \'{path}\'", mode='warning')
        for file in os.listdir(path):  # loop to delete each file in folder
            os.remove(f'{path}/{file}')  # delete file

        os.rmdir(path)
