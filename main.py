from sys import platform
import cv2


def checkOS():
    if platform == "linux":
        return "linux"

    elif platform == "darwin":
        return accessMacbookCamera()

    elif platform == "win32":
        return "windows"

    else:
        return osNotSupported()


def osNotSupported():
    return print(
        f"This platform and/or OS, {platform} and {platform.system()}, is currently not supported. Try using this script in a device running on linux, macos or windows."
    )


def accessMacbookCamera():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        detectFace(frame=frame)

        cv2.imshow("Video", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    return


def detectFace(frame):
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return


if __name__ == "__main__":
    checkOS()
