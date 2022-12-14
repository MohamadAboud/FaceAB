from  utils.utils import *

class Check:
    isFirstTime = True

    @classmethod
    def init(cls):
        check = isExists("data") == True
        Check.isFirstTime = check == False

        if  check == False : CrateFolder("data"); CrateFolder("data/users"); CrateFolder("data/model")