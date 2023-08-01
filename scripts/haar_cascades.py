import cv2


def HaarCascades_FaceDetection(frame, haar_mode):
    """haar_mode is the XML document that references the Haar algorithm used.

    Some options:

    "1" : haarcascade_frontalface_default.xml

    "2" : haarcascade_frontalface_alt.xml

    "3" : haarcascade_frontalface_alt2.xml

    "4" : haarcascade_frontalface_alt_tree.xml

    """

    if haar_mode == 1:
        haar_mode = "haarcascade_frontalface_default.xml"
    if haar_mode == 2:
        haar_mode = "haarcascade_frontalface_alt.xml"
    if haar_mode == 3:
        haar_mode = "haarcascade_frontalface_alt2.xml"
    if haar_mode == 4:
        haar_mode = "haarcascade_frontalface_alt_tree.xml"
    else:
        haar_mode = "haarcascade_frontalface_default.xml"

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + haar_mode)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=7, minSize=(50, 50)
    )

    for x, y, w, h in faces:
        cv2.rectangle(
            img=frame, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=3
        )

    return
