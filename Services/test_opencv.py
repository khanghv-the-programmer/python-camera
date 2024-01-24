import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import base64
from PIL import Image
from io import BytesIO

url = 'rtsp://192.168.1.7:8080/h264_ulaw.sdp'
c = cv2.VideoCapture(url)
# Create the MOG2 background subtractor object
mog = cv2.createBackgroundSubtractorMOG2()
counter = 0
captures = []
while True:
    ret, frame = c.read()
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        fgmask = mog.apply(gray)
    
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        fgmask = cv2.erode(fgmask, kernel, iterations=1)
        fgmask = cv2.dilate(fgmask, kernel, iterations=1)
    
        contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
        for contour in contours:
        # Ignore small contours
            
            if cv2.contourArea(contour) < 1000:
                # 3s liên tục không có chuyển động -> lưu mảng captures và capture = []
                continue
        
        # Draw bounding box around contour
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            counter = 0
            # start capture
            # capture add từ từ mỗi 1s
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            reval, buffer = cv2.imencode('.jpg', frame, encode_param)
            base64_image = base64.b64encode(buffer).decode('utf-8')   
            # image_data = base64.b64decode(base64_image)            
            # image_buffer = BytesIO(image_data)
            # img = Image.open(image_buffer)
            # img.show()
            
        cv2.imshow('Motion Detection', frame)
        # 1s add vào captures
        if cv2.waitKey(1) == ord('q'):
            break
    except Exception as e:
        print('Ahihi')
    
c.release()
cv2.destroyAllWindows()    



    