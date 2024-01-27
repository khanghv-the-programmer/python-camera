#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 19:58:26 2024

@author: thaihd
"""
import sqlite3
from flask import Flask,request,jsonify

app=Flask(__name__)
app.app_context().push()

conn = sqlite3.connect("jdbc:postgresql://cameraip.cilyqldqbjqk.ap-southeast-1.rds.amazonaws.com:5432/postgres", check_same_thread=False)
#conn = sqlite3.connect("/Users/thaihd/Database/NewDatabase.db", check_same_thread=False)
c=conn.cursor()
tableName="Camera"
def DropCameraTable():
    c.execute(f""" DROP TABLE IF EXISTS {tableName}
                """)
#Create Database
c.execute(f""" CREATE TABLE IF NOT EXISTS {tableName}(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                username VACHAR,
                password VACHAR,
                ip VACHAR,
                port VACHAR,
                status VACHAR
            )""")

#Create Camera
class Camera:

    def __init__(self,id,username,password,ip,port,status):
        self.id=id
        self.username=username
        self.password=password
        self.ip=ip
        self.port=port
        self.status=status
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
CameraList = []

@app.route("/create-camera",methods=["POST"])
def CreateCameraRequest():
    data= request.get_json()
    CreateNewCamera(data["id"], data["username"],
                    data["password"], data["ip"],
                    data["port"], data["status"])
    return jsonify(data),201
def CreateNewCamera(id,username,password,ip,port,status):
    newCamera = Camera(id,username,password,ip,port,status)    
    CameraList.append(newCamera)
    c.execute(f"INSERT INTO {tableName} (username, password, ip, port,status)\
        VALUES('{username}','{password}','{ip}','{port}','{status}')")
    conn.commit()
    print("Create New Camera succeed")
    
@app.route("/update-camera",methods=["PUT"])
def UpdateCameraRequest():
    data= request.get_json()
    UpdateCamera(data["id"], data["username"],
                    data["password"], data["ip"],
                    data["port"], data["status"])
    return jsonify(data),201
def UpdateCamera(id,username,password,ip,port,status):
    c.execute("UPDATE {tableName} \
              SET username = '{username}', password = '{password}', \
                  ip = '{ip}', port = '{port}', \
                  status = '{status}'\
              WHERE id='{id}'")
    for itemCamera in CameraList:
        if itemCamera.id == id:
            itemCamera.username=username
            itemCamera.password=password
            itemCamera.ip=ip
            itemCamera.port=port
            itemCamera.status=status
@app.route("/delete-camera/<camera_id>",methods=["DELETE"])
def DeleteCameraRequest(camera_id):
    id = int(camera_id)
    if DeleteCamera(id)==True:
        return "Deleted Camera"
    else :
        return "Cannot find any Camera"
    
def DeleteCamera(id):
    for itemCamera in CameraList:
        if itemCamera.id == id:
            CameraList.remove((itemCamera))
            return True
    return False    
@app.route("/get-camera-info/<camera_id>")
def GetCamera(camera_id): 
    id = int(camera_id)
    for itemCamera in CameraList:
        if itemCamera.id == id:
            camera = itemCamera.serialize()
            return jsonify(camera),200


if(__name__=="__main__"):
    app.run(debug=True)
    
