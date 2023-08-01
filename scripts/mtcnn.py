import cv2

from mtcnn import MTCNN


def Mtcnn_FaceDetection(frame):
    mtcnn = MTCNN()
    faces = mtcnn.detect_faces(img=frame)

    for face in faces:
        x, y, w, h = face["box"]
        cv2.rectangle(
            img=frame, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=5
        )

    return frame
