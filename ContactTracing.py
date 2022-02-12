import cv2 
import numpy as np
import datetime
from pyzbar.pyzbar import decode 

CameraCapture = cv2.VideoCapture(0)
CameraCapture.set(3,1080) #Width
CameraCapture.set(4,720) #Height

CameraScanner = True
while CameraScanner == True:
    success, frame = CameraCapture.read()

    for captureinfomartions in decode(frame):
        #Convert Informations to text file
        Make_txt_file = open("Data of User.txt", "w")
        Make_txt_file.write(f"{captureinfomartions.data.decode('utf-8')}\n" )
        
        #Add the time and date when data is scanned
        Date = datetime.datetime.now()
        Make_txt_file.write(Date.strftime("Date: %m/%d/%y \n"))
        Make_txt_file.write(Date.strftime("Time: %H:%M:%S"))  
        Make_txt_file.close()

        #Additional Effects for the program
        Filename = "SCANNING COMPLETE!"
        Qr_code_detector = np.array([captureinfomartions.polygon],np.int32)
        Qr_code_detector = Qr_code_detector.reshape((-1,1,2))
        cv2.polylines(frame, [Qr_code_detector], True, (0,128,0), 5)
        Qr_code_detector_2 = captureinfomartions.rect
        cv2.putText(frame, Filename, (Qr_code_detector_2 [0], Qr_code_detector_2[1]), cv2.FONT_HERSHEY_DUPLEX, 0.9,(0,128,0), 2)
               
    cv2.imshow('Kaydee Scanner', frame)
    cv2.waitKey(1)
