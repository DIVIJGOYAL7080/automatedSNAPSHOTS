import random
import cv2
import dropbox
import time


def take_snapshot():
    video_capture_object = cv2.VideoCapture(0)
    result = True

    while result:
        ret, frame = video_capture_object.read()
        image_name = "img" + str(random.randint(1, 100)) + ".png"

        cv2.imwrite(image_name, frame)
        start_time = time.time

        result = False

    print("Snapshot taken")
    video_capture_object.release()
    cv2.destroyAllWindows()

    return image_name


def upload_snapshot(image_name, access_token):
    file_to = "/snapshots/" + image_name

    dbx = dropbox.Dropbox(access_token)

    with open(image_name, 'rb') as file:
        dbx.files_upload(file.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded!")