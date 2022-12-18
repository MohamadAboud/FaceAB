import math
import os
import face_recognition
from face_recognition.face_detection_cli import image_files_in_folder
from sklearn.neighbors import KNeighborsClassifier
import pickle
########################################################################
from ui.routes.routes import TrainingScreen
from utils.dev import Developer



class TrainingModel:

    mainDir = "./data"
    trainDir = f"{mainDir}/users"
    modelDir = f'{mainDir}/model'

    __modelName = "facemodel.clf"

    model = None

    @classmethod
    def train(cls):
        Developer.log("StartTrainingModel", mode='info')

        # ------------------------------------------------------
        n_neighbors = 2  # or 2 3 ...
        algorithm = 'ball_tree'
        # ------------------------------------------------------

        X_train = []
        Y_train = []
        folders = os.listdir(cls.trainDir)

        folderValue = 100/len(folders) # 25
        # ----------------------------------
        page = TrainingScreen.instance
        page.increaseProgressBar(value=0)

        for folderName in folders:
            fullPathName = os.path.join(cls.trainDir, folderName)
            if not os.path.isdir(fullPathName):
                continue

            # Loop through each training image for the current Folder..................
            Developer.log("'{}' Images processing start...............\n".format(folderName), mode='info')
            images = image_files_in_folder(fullPathName)

            if len(images) == 0 : continue

            increment_value = folderValue / len(images)
            for imagePath in images:
                image = face_recognition.load_image_file(imagePath)
                face_bounding_boxes = face_recognition.face_locations(image)

                TrainingScreen.instance.increaseProgressBar(value=increment_value)

                if len(face_bounding_boxes) != 1:
                    # If there are no people (or too many people) in a training image, skip the image.
                    Developer.log("Image '{}' not suitable for training: {}".format(imagePath,
                                                                                    "Didn't find a face" if len(
                                                                                        face_bounding_boxes) < 1 else "Found more than one face"),
                                  mode='warning')
                else:
                    # Add face encoding for current image to the training set
                    trainingArray = face_recognition.face_encodings(image, known_face_locations=face_bounding_boxes)[0]
                    personName = folderName

                    X_train.append(trainingArray)
                    Y_train.append(personName)


            Developer.log("\n'{}' images processing has been completed\n".format(folderName), mode='info')

        print(
            f"name : {X_train}",
            f"X : {len(X_train)}"
        )

        # Determine how many neighbors to use for weighting in the KNN classifier
        if n_neighbors is None:
            n_neighbors = int(round(math.sqrt(len(X_train))))
            Developer.log("Chose n_neighbors automatically:", n_neighbors, mode='info')

        # Create and train the KNN classifier
        model = KNeighborsClassifier(
            n_neighbors=n_neighbors,
            algorithm=algorithm,
            weights='distance'
        )
        model.fit(X_train, Y_train)

        # Save the KNN ...
        cls._save(model)

        cls.model = model

    @classmethod
    def load(cls):
        path = f"{cls.modelDir}/{cls.__modelName}"

        if path is None:
            raise FileExistsError("No training model found")

        with open(path, 'rb') as model:
            knn_clf = pickle.load(model)
            cls.model = knn_clf

    @classmethod
    def _save(cls, model):
        # Save the trained KNN classifier ...
        path = f"{cls.modelDir}/{cls.__modelName}"
        with open(path, 'wb') as file:
            pickle.dump(model, file)

        Developer.log(f"\nTraining completed successfully\n....'{path}'", mode='info')