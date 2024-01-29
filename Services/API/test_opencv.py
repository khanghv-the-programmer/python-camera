import sys
sys.path.append('D:\Python_assignment')
import cv2
import time
import base64
from PIL import Image
from io import BytesIO
import psycopg2
from Services.Utilize.ReadConfigurationFile import read_config_from_file as config
from Services.Utilize import DBConnection
import urllib
from sqlalchemy import create_engine
from Services.model import Users, Captures, Cameras, Events
from sqlalchemy.sql import text
import time
import json
from sqlalchemy.orm import Session
import datetime



# conn = psycopg2.connect(database="streaming_camera",
#                         host="cameraip.cilyqldqbjqk.ap-southeast-1.rds.amazonaws.com",
#                         user="postgres",
#                         password="cameraip2024",
#                         port="5432")


# cnxn = pyodbc.connect('DRIVER={SQL Server};\
#                       SERVER=KIRA;\
#                       DATABASE=streaming_camera;\
#                       UID=sa;\
#                       PWD=123')

# db_cursor = conn.cursor()

# db_cursor.execute("Select * from ")
class CameraThread():

    def __init__(self):
        CONN_URI = config.connection["postgres"]
        PASSWORD = config.connection["postgres_password"]
        DATABASE = config.connection["postgres_database"]
        SCHEMA = config.schema["postgres_schema"]
        CONN_STR = CONN_URI.format(password=urllib.parse.quote(PASSWORD),database=DATABASE)
        self.postgresql_engine = create_engine(CONN_STR,connect_args={'options': '-csearch_path={}'.format(SCHEMA)})

        self.active_camera = None
        self.event = None
        self.captures = []
        self.session = None
        self.video_capture = None
        # url = 'rtsp://admin:admin@192.168.1.7:8080/h264_ulaw.sdp'

    def run(self):
        
        try:
            with DBConnection(self.postgresql_engine) as session:
                session = Session(bind=self.postgresql_engine)
                self.active_camera = session.query(Cameras).filter(Cameras.is_active == 'True', Cameras.is_used == 'False').first()
                if(self.active_camera is None):
                    print("No camera found!")
                    return
                self.url = f'rtsp://{self.active_camera.username}:{self.active_camera.password}@{self.active_camera.ip}:{self.active_camera.port}/h264_ulaw.sdp'
                cmd = text(f'Update streaming_camera.camera set is_used=true where id={self.active_camera.id}')
                session.execute(cmd)
                session.commit()
        except Exception as e:
            raise e    
        
        try:
            last_execute_time = time.time()
            self.video_capture = c = cv2.VideoCapture(self.url)
            mog = cv2.createBackgroundSubtractorMOG2()
            self.counter = 0
            self.captures = []
            while True:
            # frame : image read from capture
                ret, frame = c.read()
                if frame is None:
                    continue
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
                fgmask = mog.apply(gray)
            
                kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                fgmask = cv2.erode(fgmask, kernel, iterations=1)
                fgmask = cv2.dilate(fgmask, kernel, iterations=1)
            
                contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                if any(cv2.contourArea(contour) > 1000 for contour in contours) == False:
                        current_time = time.time()
                        if(current_time - last_execute_time >= 3):
                            if self.event is not None:
                                new_event = Events(camera_id=self.active_camera.id)
                                session.add(new_event)
                                session.commit()
                                if len(self.captures) > 0:
                                    for capture in self.captures:
                                        capture.event_id =  new_event.id
                                        session.add(capture)
                                    session.commit()
                                self.event = None
                                self.captures = []
                            last_execute_time = current_time
                for contour in contours:
                # Ignore small contours
                    
                    if cv2.contourArea(contour) < 1000:
                        continue
                
                # Draw bounding box around contour
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    # start capture
                    # capture add từ từ mỗi 1s
                current_time = time.time()
                if(current_time - last_execute_time >= 3):
                    if self.event is None:
                        self.event = Events(camera_id=self.active_camera.id)
                    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 30]
                    self.reval, buffer = cv2.imencode('.jpg', frame, encode_param)
                    base64_image = base64.b64encode(buffer).decode('utf-8') 
                    self.captures.append(Captures(image=base64_image, capture_time=datetime.datetime.now()))
                    last_execute_time = current_time
                    # image_data = base64.b64decode(base64_image)            
                    # image_buffer = BytesIO(image_data)
                    # img = Image.open(image_buffer)
                    # img.show()
                    
                cv2.imshow('Motion Detection', cv2.resize(frame, (1280, 720)))
            # 1s add vào captures
                if cv2.waitKey(1) == ord('q'):
                    cmd = text(f'Update camera set is_used=False where id={self.active_camera.id}') 
                    session.execute(cmd)
                    session.commit()
                    break
                

        except Exception as e:
            cmd = text(f'Update camera set is_used=False where id={self.active_camera.id}') 
            session.execute(cmd)
            session.commit()
            raise e
    
    def generate_frame(self, ip):
        try:
            with DBConnection(self.postgresql_engine) as session:
                session = Session(bind=self.postgresql_engine)
                self.active_camera = session.query(Cameras).filter(Cameras.is_active == 'True', Cameras.is_used == 'True', Cameras.ip == ip).first()
                if(self.active_camera is None):
                    print("No camera found!")
                    return
                self.url = f'rtsp://{self.active_camera.username}:{self.active_camera.password}@{self.active_camera.ip}:{self.active_camera.port}/h264_ulaw.sdp'
                cmd = text(f'Update streaming_camera.camera set is_used=true where id={self.active_camera.id}')
                session.execute(cmd)
                session.commit()
        except Exception as e:
            raise e   
        try:
            print("Ahihi", self.url)
            video_capture = cv2.VideoCapture(self.url)
            mog = cv2.createBackgroundSubtractorMOG2()
            while True:
            # frame : image read from capture
                ret, frame = video_capture.read()
                if frame is None:
                    continue
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
                fgmask = mog.apply(gray)
            
                kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                fgmask = cv2.erode(fgmask, kernel, iterations=1)
                fgmask = cv2.dilate(fgmask, kernel, iterations=1)
            
                contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for contour in contours:
                # Ignore small contours
                    
                    if cv2.contourArea(contour) < 1000:
                        continue
                
                # Draw bounding box around contour
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    
                _, buffer = cv2.imencode('.jpg', frame)
                frame_data = buffer.tobytes()

                yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_data + b'\r\n')
                

        except Exception as e:
            yield ('Ahihi')








            