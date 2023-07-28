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
        ret, img = cap.read()
        cv2.imshow("Frame", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    return



if __name__ == "__main__":
    checkOS()