
class Path:
    saveImg = "./data/users" # [ users folder -> user-00000 ]

class SplashScreenString:
    img = "/images/splashscreen_robot.gif"
    welcomText = "Welcome"
    subText = ['Face','Recognition','application']
    introText = ['is a facial recognition app which','detects person from your training model']
    button1 = "Get Started"
    button2 = "Start"
    button3 = "Add Face"

class ImageScreenString:

    class PopUp:
        title = "Sign in"
        subText = "Lorem ipsum dolor sit amet, \nconsectetur adipiscing elit. Maecenas est felis,"
        buttonText= "Done"

        textFieldTitle = "Name"
        textFieldHintText = "Enter your name"
        textFieldError = "Name is required"

        fileNotExistsError = "This name already exists"
        osError = "This name is not valid"
        error = "You have an error"

        closeTooltip = "Your facial data will be deleted,\n are you sure?"

    img = "images/loading.gif"
    text1 = "Verification Process"
    text2 = "Smile & blink your eyes,then move your\nhead slowly to complete the process"

    progressText1 = "Loading..."
    progressText2 = "recognised"


    popup = PopUp()


class TrainingScreenString:
    img = "https://picsum.photos/id/250/200/300"

    progressText1 = "training"
    subText = "We are now in the process of creating\n the model for you"

    text1 = "Successful!"
    text2 = "Smile & blink your eyes,then move your\nhead slowly to complete"

class AppString:

    name = "FACAB"
    splashscreen = SplashScreenString()
    imagescreen = ImageScreenString()
    trainingscreen = TrainingScreenString()

    path = Path()

