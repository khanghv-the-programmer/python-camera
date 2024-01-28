#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 19:58:26 2024

@author: thaihd
"""
from flask import Flask,request,jsonify
app=Flask(__name__)
app.app_context().push()

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
    print("Create New Camera succeed")
    
@app.route("/update-camera",methods=["PUT"])
def UpdateCameraRequest():
    data= request.get_json()
    UpdateCamera(data["id"], data["username"],
                    data["password"], data["ip"],
                    data["port"], data["status"])
    return jsonify(data),201
def UpdateCamera(id,username,password,ip,port,status):
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


CreateNewCamera(1, "test", "password", "ip", "port", "status")  
CreateNewCamera(2, "test", "password", "ip", "port", "status")    
UpdateCamera(1, "changed", "newPass", "newIp", "newPort", "newStatus")    
DeleteCamera(2)


if(__name__=="__main__"):
    app.run(debug=True,port=8000)
    
