<h1 align="center">FaceAB</h1>

## Introduction

The `FaceAB` software is a graphical interface program that uses advanced machine learning algorithms to perform real-time face recognition, age prediction, and gender prediction. Developed by `Mohamad Aboud`, the software is written in Python and utilizes several libraries
including :

* face_recognition.
* mediapipe.
* opencv.
* flet.

The FaceAB program offers a **user-friendly interface** that allows users to easily set up and configure the face recognition system to their specific needs. The program uses a deep learning-based approach to face recognition, which allows it to accurately identify individuals even in challenging lighting conditions and when faces are partially occluded.

In addition to its real-time face recognition capabilities, the FaceAB program also offers offline batch processing capabilities. This allows users to process large amounts of video or image data and generate reports on the individuals that are present in the data.

Overall, the FaceAB program is a versatile and powerful tool for implementing real-time face recognition in a variety of applications. Its user-friendly interface and advanced machine learning algorithms make it a valuable asset for any organization looking to incorporate face recognition technology into their systems.


## Technical details

The FaceAB software uses several libraries and technologies to perform real-time face recognition, age prediction, and gender prediction. These include:

1. `face_recognition`: This library is used for the core face recognition functionality of the FaceAB software. It uses a deep learning-based approach to face recognition, allowing it to accurately identify individuals even in challenging lighting conditions and when faces are partially occluded.

2. `mediapipe`: This library is used to process video streams in real-time, allowing the FaceAB software to recognize faces in live video feeds.


3. `opencv`: This library is used to perform a variety of computer vision tasks, including face detection, image preprocessing, and feature extraction.

4. `flet`: This library is a framework that allows building interactive multi-user web, desktop and mobile applications in `flutter language`.

In addition to these libraries, the FaceAB software also utilizes advanced machine learning algorithms, such as convolutional neural networks (CNNs), to accurately recognize faces and predict age and gender. These algorithms are trained on large datasets to improve their accuracy and performance.



## Installation and usage
To install and use the FaceAB software, you will need to have the following libraries and technologies installed on your system:

### Prerequisites
* `Python`: This is the programming language in which the FaceAB software is written. You can download and install Python from [here](https://www.python.org/downloads/release/python-391/).


 ```
 > python --version
 Python 3.9.1
 ```

### Requisites


* `face_recognition`: This library is used for the core face recognition functionality of the FaceAB software. You can install it using the following command: 
``` 
> pip install face_recognition
```

* `mediapipe`: This library is used to recognize body and vertex points in real time. You can install it using the following command:
``` 
> pip install mediapipe==0.9.0.1
```

<!-- * `cvzone`: ...
``` 
> pip install cvzone==1.5.6
``` -->

* `opencv`: This library is used to perform a variety of computer vision tasks. You can install it using the following command:
``` 
> pip install opencv-python==4.6.0.66
```

* `flet`: This library is used to build the graphical interface. You can install it using the following command:
``` 
> pip install flet==0.2.4
```

<strong> Or you can download all libraries via the following command: </strong>

```
> pip install -r requirements.txt
```


Once you have installed these libraries, you can download the `FaceAB` software from https://github.com/MohamadAboud/FaceAB. To run the software, open a terminal or command prompt and navigate to the directory where you downloaded the software. Then, use the following command to run the program:
```
> python main.py
```

The `FaceAB` software will then launch and you can use the user-friendly interface to set up and configure the face recognition system to your specific needs. You can then use the software to recognize faces in **real-time video streams** or **process offline batches of video or image data**.

Overall, the `FaceAB` software is easy to install and use.

## Limitations and future work
The `FaceAB `software is a powerful and versatile tool for implementing real-time face recognition, but it does have some limitations. Some of the current limitations of the software include:

The software is currently only available for use with Python. This may limit its compatibility with other programming languages and systems.

The software relies on a deep learning-based approach to face recognition, which can be computationally intensive. This may limit its performance on systems with limited resources.

The software currently only offers real-time face recognition and offline batch processing capabilities.

To address these limitations and improve the capabilities of the FaceAB software, there are several areas of future work that could be pursued. Some potential directions for future work include:

Developing versions of the FaceAB software for use with other programming languages, such as **C++** or **Java**. This would expand the compatibility of the software and allow it to be used in a wider range of applications and systems.

Investigating ways to optimize the performance of the software, such as through the use of specialized hardware or more efficient algorithms. This would allow the software to run more efficiently and effectively on a wider range of systems.

## Conclusion
`FaceAB` is a graphical interface software for real-time face recognition, age prediction, and gender prediction. Developed by `Mohamad Aboud`, the software uses advanced machine learning algorithms and technologies, such as **face_recognition**, **mediapipe**, **opencv**, and **flet**, to accurately identify individuals in real-time video streams. The software offers a user-friendly interface and offline batch processing capabilities, making it a versatile and powerful tool. While the software has some limitations, there are opportunities for future work to expand its capabilities and improve its performance.


## References
To learn more about the FaceAB software and its capabilities, please see the following references:

- `Mohamad Aboud's` profile: https://github.com/MohamadAboud
* `face_recognition` library: https://pypi.org/project/face-recognition/
* `mediapipe library`: https://pypi.org/project/mediapipe/
* `opencv library`: https://pypi.org/project/opencv-python/
* `flet library`: https://pypi.org/project/flet/

These references provide more detailed information about the FaceAB software, its capabilities, and its underlying technologies.


# Test
https://medium.com/analytics-vidhya/how-to-install-dlib-library-for-python-in-windows-10-57348ba1117f