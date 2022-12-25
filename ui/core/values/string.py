from ui.core.languages.languages import Language


class Path:
    saveImg = "./data/users" # [ users folder -> user-00000 ]

class WelcomeScreenString:
    img = "/images/welcom_image_light.gif"

    @property
    def welcomText(self):
        return Language.getText(key="welcome_text")

    @property
    def subText(self):
        return Language.getText("face_recognition_application_text")

    @property
    def introText(self):
        return Language.getText("intro_text")

    @property
    def button1(self):
        return Language.getText("get_started_text")

    @property
    def button2(self):
        return Language.getText("start_text")

    @property
    def button3(self):
        return Language.getText("add_face_text")


class ImageScreenString:

    class PopUp:
        @property
        def title(self):
            return Language.getText(key="user_name_text")
        @property
        def subText(self):
            return Language.getText(key="sub_text")
        @property
        def buttonText1(self):
            return Language.getText(key="button1_text")
        
        @property
        def buttonText2(self):
            return Language.getText(key="button2_text")        
        
        @property
        def textFieldTitle(self):
            return Language.getText(key="text_field_title")
        
        @property
        def textFieldHintText(self):
            return Language.getText(key="text_field_hint_text")
        
        @property
        def textFieldError(self):
            return Language.getText(key="text_field_error")

        @property
        def fileNotExistsError(self):
            return Language.getText(key="file_not_exists")
 
        
        @property
        def osError(self):
            return Language.getText(key="os_error")
        
        @property
        def error(self):
            return Language.getText(key="error")
        
        @property
        def closeTooltip(self):
            return Language.getText(key="close_tooltip") 

    img = "images/loading_light.gif"
    
    @property
    def text1(self):
        return Language.getText(key="image_text1")
    
    @property
    def text2(self):
        return Language.getText(key="image_text2")
    @property
    def progressText1(self):
        return Language.getText(key="image_progress1_text")
    
    @property
    def progressText2(self):
        return Language.getText(key="image_progress2_text")


    popup = PopUp()


class TrainingScreenString:
    img = "images/traning_image.gif"
    doneImg = "images/done.gif"

    @property
    def progressText1(self):
        return Language.getText(key="training_progress_text") 

    
    @property
    def subText(self):
        return Language.getText(key="training_sub_text")

    @property
    def text1(self):
        return Language.getText(key="training_text1")

    
    @property
    def text2(self):
        return Language.getText(key="training_text2")

class AppString:
    @classmethod
    def alignment(cls):
        print(Language.getAlignment())
        return Language.getAlignment()


    name = "FACAB"
    welcomescreen = WelcomeScreenString()
    imagescreen = ImageScreenString()
    trainingscreen = TrainingScreenString()

    path = Path()