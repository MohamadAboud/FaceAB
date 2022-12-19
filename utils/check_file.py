

class Check:
    isFirstTime = True

    @classmethod
    def init(cls):
        from utils.utils import isExists, makedirs

        if isExists("data"):
            if isExists("data/model"):
                Check.isFirstTime = not isExists("data/model/facemodel.clf")
        else:
            makedirs("data/users")
            makedirs("data/model")

        print(f"Test : {Check.isFirstTime}")