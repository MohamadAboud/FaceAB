class CameraSource:
    camNumber = 0

    @classmethod
    def changeCamera(cls, src):
        if src >= 0:
            cls.camNumber = src

    @classmethod
    def setAsDefault(cls):
        cls.camNumber = 0
