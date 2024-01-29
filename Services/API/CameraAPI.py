#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 19:58:26 2024

@author: thaihd
"""
import urllib

from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy import select
from Services.model import Users, Captures, Cameras, Events
from Services.Utilize import DBConnection
from Services.Utilize.ReadConfigurationFile import read_config_from_file as config

CONN_URI = config.connection["postgres"]
PASSWORD = config.connection["postgres_password"]
DATABASE = config.connection["postgres_database"]
SCHEMA = config.schema["postgres_schema"]
CONN_STR = CONN_URI.format(password=urllib.parse.quote(PASSWORD),database=DATABASE)
postgresql_engine = create_engine(CONN_STR,connect_args={'options': '-csearch_path={}'.format(SCHEMA)})
app=Flask(__name__)
app.app_context().push()


class Camera:

    def __init__(self, id, username, password, ip, port, status):
        self.id = id
        self.username = username
        self.password = password
        self.ip = ip
        self.port = port
        self.status = status
        print("New camera init")

    def GetCameraInfo(self):
        print(f'Camera id {self.id}')
        print(f"Camera username {self.username}")
        print(f"Camera password {self.password}")
        print(f"Camera IP {self.ip}")
        print(f"Camera Port {self.port}")
        print(f"Camera Status {self.status}")
        return self

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'ip': self.ip,
            'port': self.port,
            'status': self.status,
        }


from sqlalchemy import MetaData

metadata = MetaData()
    
#conn = sqlite3.connect("jdbc:postgresql://cameraip.cilyqldqbjqk.ap-southeast-1.rds.amazonaws.com:5432/postgres", check_same_thread=False)
#conn = sqlite3.connect("/Users/thaihd/Database/NewDatabase.db", check_same_thread=False)
c=postgresql_engine

tableName="Camera"
#Create Database
try:
    with DBConnection(postgresql_engine) as session:
        DBSession = session
        conn =session.connection().connection
        cursor = conn.cursor()

except Exception as e:
    raise e
#Create Camera
def CreateCameraTable():
    DBSession.execute(text(f""" CREATE TABLE IF NOT EXISTS {tableName}
                id serial not null primary key,
                    username VACHAR,
                    password VACHAR, 
                    ip VACHAR,
                    port VACHAR,
                    status VACHAR """))
CameraList = []

@app.route("/create-camera",methods=["POST"])
def CreateCameraRequest():
    data= request.get_json()
    CreateNewCamera(data["id"], data["name"], data["username"],
                    data["password"], data["ip"],
                    data["port"])
    return jsonify(data),201
def CreateNewCamera(id,name,username,password,ip,port):
    newCamera = Cameras()
    newCamera.id = id
    newCamera.name = name
    newCamera.username = username
    newCamera.password = password
    newCamera.ip = ip
    newCamera.port = port

    CameraList.append(newCamera)
    with DBConnection(postgresql_engine) as session:
        camera = session.query(Cameras).filter(Cameras.id == id).first()
        cmd=text(f"INSERT INTO {newCamera.__tablename__} (name, username, password, ip, port,is_active, is_used)\
        VALUES('{name}','{username}','{password}','{ip}','{port}','{False}','{False}')")
        session.execute(cmd)
        session.commit()
        return "Create New Camera succeed", 200
    
@app.route("/update-camera",methods=["PUT"])
def UpdateCameraRequest():
    data= request.get_json()
    UpdateCamera(data["id"], data["name"], data["username"],
                    data["password"], data["ip"],
                    data["port"])
    return jsonify(data),201
def UpdateCamera(id,name,username,password,ip,port):
    # for itemCamera in CameraList:
    #     if itemCamera.id == id:
    #         itemCamera.name=name
    #         itemCamera.username = username
    #         itemCamera.password=password
    #         itemCamera.ip=ip
    #         itemCamera.port=port
    #         break

    with DBConnection(postgresql_engine) as session:
        cmd=text(f"UPDATE Camera \
                  SET username = '{username}', password = '{password}', \
                      name = '{name}',\
                      ip = '{ip}', port = '{port}'\
                  WHERE id='{id}'")
        session.execute(cmd)
        session.commit()
        return "Update Camera succeed", 200
@app.route("/delete-camera/<camera_id>",methods=["DELETE"])
def DeleteCameraRequest(camera_id):
    id = int(camera_id)
    if DeleteCamera(id)==True:
        return "Deleted Camera"
    else :
        return "Cannot find any Camera"
    
def DeleteCamera(id):
    with DBConnection(postgresql_engine) as session:
        cmd=text(f"DELETE FROM camera \
                                  WHERE id='{id}'")
        session.execute(cmd)
        session.commit()
        return True
    return False    
@app.route("/get-camera-info/<camera_id>")
def GetCamera(camera_id): 
    id = int(camera_id)
    with DBConnection(postgresql_engine) as session:
        camera = session.query(Cameras).filter(Cameras.id == id).first()
        #session.execute(cmd)
        #session.commit()
        return jsonify(camera.serialize()), 200
    for itemCamera in CameraList:
        if itemCamera.id == id:
            camera = itemCamera.serialize()
            return jsonify(camera),200

if(__name__=="__main__"):
    app.run(debug=True)


