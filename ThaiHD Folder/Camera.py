#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 19:58:26 2024

@author: thaihd
"""

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
        
CameraList = []
def CreateNewCamera(id,username,password,ip,port,status):
    newCamera = Camera(id,username,password,ip,port,status)    
    CameraList.append(newCamera)
    print("Create New Camera succeed")
    
def UpdateCamera(id,username,password,ip,port,status):
    for itemCamera in CameraList:
        if itemCamera.id == id:
            itemCamera.username=username
            itemCamera.password=password
            itemCamera.ip=ip
            itemCamera.port=port
            itemCamera.status=status
def DeleteCamera(id):
    for itemCamera in CameraList:
        if itemCamera.id == id:
            CameraList.remove((itemCamera))
            break
def PrintCameraInfo(id):
    for itemCamera in CameraList:
        if itemCamera.id == id:
            itemCamera.GetCameraInfo()
            break
            
CreateNewCamera(1, "test", "password", "ip", "port", "status")  
CreateNewCamera(2, "test", "password", "ip", "port", "status")    
UpdateCamera(1, "changed", "newPass", "newIp", "newPort", "newStatus")    
DeleteCamera(2)
PrintCameraInfo(2)