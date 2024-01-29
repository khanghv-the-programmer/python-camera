from Services.model import Cameras
from sqlalchemy import and_
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
            camera = Cameras(name=name,username=user_name, password=password)
            instance_camera.append(camera)
            self.bulkInsertUser(instance_camera)
        except Exception as E:
            raise E


