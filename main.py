import cv2
from sys import platform

from scripts.haar_cascades import HaarCascades_FaceDetection
from scripts.mtcnn import Mtcnn_FaceDetection


def checkOS():
    if platform == "linux":
        return "linux"

    elif platform == "darwin":
        return accessMacbookCamera(mode="haar")

    elif platform == "win32":
        return "windows"

    else:
        return osNotSupported()


def osNotSupported():
    return print(
        f"This platform and/or OS, {platform} and {platform.system()}, is currently not supported. Try using this script in a device running on linux, macos or windows."
    )


def accessMacbookCamera(mode):
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if mode == "haar":
            HaarCascades_FaceDetection(frame=frame, haar_mode=4)

        if mode == "mtcnn":
            frame = Mtcnn_FaceDetection(frame=frame)

        cv2.imshow("Video", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    return


if __name__ == "__main__":
    checkOS()
