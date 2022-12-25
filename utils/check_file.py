

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

        from utils.dev import Developer
        Developer.log(f"Is first time : {Check.isFirstTime}",mode='info')