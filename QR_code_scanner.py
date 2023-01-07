import cv2
import numpy as np

class QR_Code_Scanner:
    def __init__(self, scrapper):
        self.scrapper = scrapper
        self.decoder = cv2.QRCodeDetector()
        # Create a VideoCapture object and read from input file
        # If the input is the camera, pass 0 instead of the video file name
        self.cap = cv2.VideoCapture(0)
        self.used_codes = {}

    def run(self):
        # Check if camera opened successfully
        if (self.cap.isOpened()== False): 
            print("Error opening video stream or file")

        # Read until video is completed
        while (self.cap.isOpened()):
            # Capture frame-by-frame
            ret, img = self.cap.read()
            if ret != True:
                break

            # Display the resulting frame
            try:
                data, points, _ = self.decoder.detectAndDecode(img) 
            except Exception as e:
                continue# size 250 * 250 np.array
            if points is not None:
                for point in points:
                    for i in range(len(point)):
                        pt1 = [int(val) for val in point[i]]
                        pt2 = [int(val) for val in point[(i + 1) % 4]]
                        img = cv2.line(img, pt1, pt2, color=(255, 0, 0), thickness=3)
                    img = cv2.putText(img, data, pt1, cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 255) if self.is_already_detected(data) else (0, 255, 0), 2, cv2.LINE_AA)
                
                if data:
                    self.on_detect(data)

            img = cv2.putText(img, f"codes : {self.scrapper.current_codes}", (25,25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.imshow('Frame', img)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # When everything done, release the video capture object
        self.cap.release()

        # Closes all the frames
        cv2.destroyAllWindows()

    def on_detect(self, code):
        if not self.is_already_detected(code):
            self.used_codes[code] = True
            self.scrapper.add_item(code)

    def is_already_detected(self, code):
        return bool(self.used_codes.get(code))
