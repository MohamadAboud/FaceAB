from enum import Enum
from ui.core.languages.en import EngMap
from ui.core.languages.ar import ArMap

class Language:
    class LCode(Enum):
        arabicCode = "AR"
        englishCode = "EN"

    allLanguage = LCode

    currentLanguageCode = allLanguage.englishCode.value

    @classmethod
    def changeLanguage(cls):
        if cls.currentLanguageCode == cls.allLanguage.englishCode.value:
            cls.currentLanguageCode = cls.allLanguage.arabicCode.value
        else:
            cls.currentLanguageCode = cls.allLanguage.englishCode.value

        # update ui state ...
        from ui.navigator import Navigator
        Navigator.restart()

    @classmethod
    def getText(cls,key):
        if cls.currentLanguageCode == cls.allLanguage.englishCode.value:
            return EngMap.get(key,"None")
        else:
            return ArMap.get(key,"لا شيء")

    @classmethod
    def getAlignment(cls):
        if cls.currentLanguageCode == cls.allLanguage.englishCode.value:
            return "start"
        else:
            return "end"