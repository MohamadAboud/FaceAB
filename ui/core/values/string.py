from ui.core.languages.languages import Language

ar = {}
en = {}

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
        title = "User Name"
        subText = "Can you tell me your name\nso we can set up your profile"
        buttonText1 = "Submit & Add another face"
        buttonText2 = "Submit & Train"

        textFieldTitle = "Name"
        textFieldHintText = "Enter your name"
        textFieldError = "Name is required"

        fileNotExistsError = "This name already exists"
        osError = "This name is not valid"
        error = "You have an error"

        closeTooltip = "Your facial data will be deleted,\n are you sure?"

    img = "images/loading_light.gif"
    text1 = "Verification Process"
    text2 = "Smile & blink your eyes,then move your\nhead slowly to complete the process"

    progressText1 = "Loading..."
    progressText2 = "recognised"


    popup = PopUp()


class TrainingScreenString:
    img = "images/traning_image.gif"
    doneImg = "images/done.gif"

    progressText1 = "training"
    subText = "We are now in the process of creating\n the model for you"

    text1 = "Successful!"
    text2 = "Smile & blink your eyes,then move your\nhead slowly to complete"

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

