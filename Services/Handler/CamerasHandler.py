from Services.model import Cameras
from sqlalchemy import and_
from sqlalchemy import text
from Services.Utilize import DBConnection
import pandas as pd
from sqlalchemy.dialects import postgresql
class CameraHandler:
    def __init__(self,engine=None,session=None):
        self.engine=engine
        self.session=session
    def getCamera(self,condition=None):
        try:
            if condition == None:
                condition = []
                condition.append(1==1)
            with DBConnection(self.engine) as session:
                query = session.query(Cameras.id,
                                    Cameras.name,
                                    Cameras.ip,
                                    Cameras.port,
                                    Cameras.username,
                                    Cameras.password,
                                    Cameras.is_active,
                                    Cameras.is_used)\
                    .filter(and_(*condition))
                query_stm = str(query.statement.compile(compile_kwargs={"literal_binds": True},
                                                            dialect=postgresql.dialect()))
                data = pd.read_sql_query(query.statement,session.bind)
        except Exception as E:
            raise E
        return data

    def bulkInsertCamera(self,cameras):
        try:
            with DBConnection(self.engine) as session:
                session.bulk_save_objects(cameras, return_defaults=True)
                session.commit()
        except Exception as E:
            raise E
    def insertCamera(self,data):
        try:
            instance_camera = []
            name = data["name"]
            user_name = data["username"]
            password = data['password']
            ip = data["ip"]
            port = data["port"]
            camera = Cameras(name=name,username=user_name, password=password,ip=ip, port=port)
            instance_camera.append(camera)
            self.bulkInsertCamera(instance_camera)
        except Exception as E:
            raise E
    def deleteCamera(self,id):
        try:
            with DBConnection(self.engine) as session:
                cmd = text(f"DELETE FROM camera \
                                                  WHERE id='{id}'")
                session.execute(cmd)
                session.commit()
        except Exception as E:
            raise E

    def updateCamera(self, id,con):
        try:
            with DBConnection(self.engine) as session:
                cmd = text(f"UPDATE camera \
                           SET is_active = {con} \
                         WHERE id='{id}'")
                session.execute(cmd)
                session.commit()
        except Exception as E:
            raise E

    def deleteEvent(self, id):
        try:
            with DBConnection(self.engine) as session:
                cmd = text(f"DELETE FROM event \
                                WHERE camera_id='{id}'")
                session.execute(cmd)
                session.commit()
        except Exception as E:
            raise E
    def deleteCapture(self,id):
        try:
            with DBConnection(self.engine) as session:
                cmd = text(f"delete from capture c \
                                using (select e.id \
                                        from event e \
                                        join camera  c2 on c2.id  = e.camera_id\
                                        where c2.id = {id}) ev\
                                where ev.id = c.event_id ")
                session.execute(cmd)
                session.commit()
        except Exception as E:
            raise E


    def getCapture(self,camera_id,from_date,to_date):
        try:
            with DBConnection(self.engine) as session:
                captures = []
                cmd = text(f"SELECT e.camera_id ,c.image, c.capture_time \
                            FROM streaming_camera.capture c  \
                            INNER JOIN streaming_camera.event e  ON e.id=c.event_id\
                            WHERE e.camera_id ='{camera_id}' and c.capture_time between '{from_date}' and '{to_date}'")
                captures=session.execute(cmd).all()

                return captures
        except Exception as E:
            raise E

    def getLastCapture(self,camera_id):
        try:
            with DBConnection(self.engine) as session:
                cmd = text(f"SELECT e.camera_id ,c.image, c.capture_time \
                            FROM streaming_camera.capture c  \
                            INNER JOIN streaming_camera.event e  ON e.id=c.event_id\
                            WHERE e.camera_id ='{camera_id}' \
                            ORDER BY c.capture_time DESC")
                captures=session.execute(cmd).first()

                return captures
        except Exception as E:
            raise E