import cv2
import numpy as np
import time

QR_codes = []

def QRCODE_DETECTOR():
    decoder = cv2.QRCodeDetector()
    # Create a VideoCapture object and read from input file
    # If the input is the camera, pass 0 instead of the video file name
    cap = cv2.VideoCapture(0)

    # Check if camera opened successfully
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")

    # Read until video is completed
    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, img = cap.read()
        if ret != True:
            break

        # Display the resulting frame
        data, points, _ = decoder.detectAndDecode(img) # size 250 * 250 np.array
        if points is None:
            continue

        if data and data not in QR_codes:
            QR_codes.append(data)

        print(QR_codes)

        points = points[0]
        img = cv2.putText(img, str(data), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 2, cv2.LINE_AA)
        for i in range(len(points)):
            pt1 = [int(val) for val in points[i]]
            pt2 = [int(val) for val in points[(i + 1) % 4]]
            img = cv2.line(img, pt1, pt2, color=(255, 0, 0), thickness=3)

        cv2.imshow('Frame', img)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # When everything done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()



