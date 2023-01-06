import cv2
import face_recognition


def drawBox(frame, start_point: tuple, end_point: tuple, color=(255, 255, 255)):
    def drwaLine(frame, x, y, top=False, bottom=False, left=False, right=False):
        lenght = 30

        if top and left:
            cv2.line(frame, (x, y), (x + lenght, y), color, 4)
            cv2.line(frame, (x, y), (x, y + lenght), color, 4)
        elif top and right:
            cv2.line(frame, (x, y), (x - lenght, y), color, 4)
            cv2.line(frame, (x, y), (x, y + lenght), color, 4)

        elif bottom and left:
            cv2.line(frame, (x, y), (x + lenght, y), color, 4)
            cv2.line(frame, (x, y), (x, y - lenght), color, 4)
        elif bottom and right:
            cv2.line(frame, (x, y), (x - lenght, y), color, 4)
            cv2.line(frame, (x, y), (x, y - lenght), color, 4)

        return frame

    # -----------------------------------------------------------------------------

    left, top = start_point
    bottom, right = end_point

    frame = drwaLine(frame, left, top, left=True, top=True)
    frame = drwaLine(frame, right, top, right=True, top=True)
    frame = drwaLine(frame, left, bottom, left=True, bottom=True)
    frame = drwaLine(frame, right, bottom, right=True, bottom=True)

    return frame


def cropFace(frame):
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_small_frame)

    # Display the results
    for (top, right, bottom, left) in face_locations:
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        frameCopy = frame.copy()
        frame = drawBox(frame, (left, top), (bottom, right))

        top -= 45
        right += 20
        bottom += 20
        h = bottom - top
        w = right - left

        cropped_face = frameCopy[top: (top + h), left: (left + w)].copy()
        cropped_face = cv2.cvtColor(cropped_face, cv2.COLOR_BGR2RGB)

        return frame, cropped_face
