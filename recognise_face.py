import cv2 
import numpy
from mtcnn import MTCNN
from datetime import datetime, date


def recognise(file: str, directory: str):
    """The function takes a file as a paramenter. No return type, creates new files for recognised faces in gien directory
    
    Args: 
        file (string): File to recognise
        direcoty (string) : Folder to store faces
    """
    # Read file using openCV
    img = cv2.imread(file)

    # Alias MTCNN for readibility
    detector = MTCNN()

    # Detect faces using CNN 
    results = detector.detect_faces(img)
    i = 1

    # Output the detected faces into their individual picture in given directory.
    for result in results:
        x, y, w, h = result['box']  # returns many diff vals, selecting only box.
        faces = img[y : y + h, x : x + w]
        itr_file_name = directory + '/' + 'face' + str(i) + '.jpg'    # to not rewrite faces
        print(f"Recognised face: {i}, writen to: {itr_file_name}")
        cv2.imwrite(itr_file_name,faces)
        i += 1  


def capture_image(directory):

    cap = cv2.VideoCapture(0)
    name = ''
    while True:
        _, img = cap.read()

        cv2.imshow('original', img)

        if cv2.waitKey(1) == ord('q'):
            break
        elif cv2.waitKey(1) == ord('r'):
            name = "test/image.jpg"
            print(name)
            cv2.imwrite(name, img)
            print('Saving an image!')
            continue
        else:
            continue

    cap.release()
    cv2.destroyAllWindows()
    return (name, (date.today()).strftime("%B %d, %Y"))
        