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
        print(CONN_STR)
        self.postgresql_engine = create_engine(CONN_STR,connect_args={'options': '-csearch_path={}'.format(SCHEMA)})

        self.active_camera = Cameras()

        # url = 'rtsp://admin:admin@192.168.1.7:8080/h264_ulaw.sdp'

    def run(self):
        try:
            with DBConnection(self.postgresql_engine) as session:
                active_camera = session.query(Cameras).filter(Cameras.is_active == 'True', Cameras.is_used == 'False').first()
                print(active_camera)
                url = f'rtsp://{active_camera.username}:{active_camera.password}@{active_camera.ip}:{active_camera.port}/h264_ulaw.sdp'
                print(url)
                c = cv2.VideoCapture(url)
            # Create the MOG2 background subtractor object
                mog = cv2.createBackgroundSubtractorMOG2()
                self.counter = 0
                self.captures = []
                while True:
                # frame : image read from capture
                    self.ret, frame = c.read()
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
                        self.counter = 0
                        # start capture
                        # capture add từ từ mỗi 1s
                        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
                        self.reval, buffer = cv2.imencode('.jpg', frame, encode_param)
                        self.base64_image = base64.b64encode(buffer).decode('utf-8')   
                        
                        # image_data = base64.b64decode(base64_image)            
                        # image_buffer = BytesIO(image_data)
                        # img = Image.open(image_buffer)
                        # img.show()
                        
                    cv2.imshow('Motion Detection', cv2.resize(frame, (1280, 720)))
                # 1s add vào captures
                    if cv2.waitKey(1) == ord('q'):
                        break

        except Exception as e:
            raise e
            







            