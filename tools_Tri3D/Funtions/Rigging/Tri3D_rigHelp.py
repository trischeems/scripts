import maya.cmds as cmds
from PySide2 import QtWidgets, QtGui, QtCore
import os

IMAGE_PATH = os.path.join(os.path.dirname(__file__), "Help")

def RightEye(*arg):
    if cmds.window("helpRig", exists=True):
        cmds.deleteUI("helpRig")
    WD = cmds.window("helpRig", title="Setup Rig Help", sizeable=False, resizeToFitChildren=True)
    cmds.windowPref("helpRig", remove=True)

    cmds.columnLayout("Face", adj=True)
    cmds.image(image= IMAGE_PATH+"/RightEye.jpg")
    cmds.showWindow(WD)

def LeftEye(*arg):
    if cmds.window("helpRig", exists=True):
        cmds.deleteUI("helpRig")
    WD = cmds.window("helpRig", title="Setup Rig Help", sizeable=False, resizeToFitChildren=True)
    cmds.windowPref("helpRig", remove=True)

    cmds.columnLayout("Face", adj=True)
    cmds.image(image= IMAGE_PATH+"/LeftEye.jpg")
    cmds.showWindow(WD)

def MUL(*arg):
    if cmds.window("helpRig", exists=True):
        cmds.deleteUI("helpRig")
    WD = cmds.window("helpRig", title="Setup Rig Help", sizeable=False, resizeToFitChildren=True)
    cmds.windowPref("helpRig", remove=True)

    cmds.columnLayout("Face", adj=True)
    cmds.image(image= IMAGE_PATH+"/MUL.jpg")
    cmds.showWindow(WD)

def BW1(*arg):
    if cmds.window("helpRig", exists=True):
        cmds.deleteUI("helpRig")
    WD = cmds.window("helpRig", title="Setup Rig Help", sizeable=False, resizeToFitChildren=True)
    cmds.windowPref("helpRig", remove=True)

    cmds.columnLayout("Face", adj=True)
    cmds.image(image= IMAGE_PATH+"/BW1.jpg")
    cmds.showWindow(WD)

def BW2(*arg):
    if cmds.window("helpRig", exists=True):
        cmds.deleteUI("helpRig")
    WD = cmds.window("helpRig", title="Setup Rig Help", sizeable=False, resizeToFitChildren=True)
    cmds.windowPref("helpRig", remove=True)

    cmds.columnLayout("Face", adj=True)
    cmds.image(image= IMAGE_PATH+"/BW2.jpg")
    cmds.showWindow(WD)  

def Corner(*arg):
    if cmds.window("helpRig", exists=True):
        cmds.deleteUI("helpRig")
    WD = cmds.window("helpRig", title="Setup Rig Help", sizeable=False, resizeToFitChildren=True)
    cmds.windowPref("helpRig", remove=True)

    cmds.columnLayout("Face", adj=True)
    cmds.image(image= IMAGE_PATH+"/Corner.jpg")
    cmds.showWindow(WD)  

def BW3(*arg):
    if cmds.window("helpRig", exists=True):
        cmds.deleteUI("helpRig")
    WD = cmds.window("helpRig", title="Setup Rig Help", sizeable=False, resizeToFitChildren=True)
    cmds.windowPref("helpRig", remove=True)

    cmds.columnLayout("Face", adj=True)
    cmds.image(image= IMAGE_PATH+"/BW3.jpg")
    cmds.showWindow(WD) 

def BW4(*arg):
    if cmds.window("helpRig", exists=True):
        cmds.deleteUI("helpRig")
    WD = cmds.window("helpRig", title="Setup Rig Help", sizeable=False, resizeToFitChildren=True)
    cmds.windowPref("helpRig", remove=True)

    cmds.columnLayout("Face", adj=True)
    cmds.image(image= IMAGE_PATH+"/BW4.jpg")
    cmds.showWindow(WD) 

def MLL(*arg):
    if cmds.window("helpRig", exists=True):
        cmds.deleteUI("helpRig")
    WD = cmds.window("helpRig", title="Setup Rig Help", sizeable=False, resizeToFitChildren=True)
    cmds.windowPref("helpRig", remove=True)

    cmds.columnLayout("Face", adj=True)
    cmds.image(image= IMAGE_PATH+"/MLL.jpg")
    cmds.showWindow(WD)
    
def INB(*arg):
    if cmds.window("helpRig", exists=True):
        cmds.deleteUI("helpRig")
    WD = cmds.window("helpRig", title="Setup Rig Help", sizeable=False, resizeToFitChildren=True)
    cmds.windowPref("helpRig", remove=True)

    cmds.columnLayout("Face", adj=True)
    cmds.image(image= IMAGE_PATH+"/INB.jpg")
    cmds.showWindow(WD)
        
def OTB(*arg):
    if cmds.window("helpRig", exists=True):
        cmds.deleteUI("helpRig")
    WD = cmds.window("helpRig", title="Setup Rig Help", sizeable=False, resizeToFitChildren=True)
    cmds.windowPref("helpRig", remove=True)

    cmds.columnLayout("Face", adj=True)
    cmds.image(image= IMAGE_PATH+"/OTB.jpg")
    cmds.showWindow(WD)
            
def JAW(*arg):
    if cmds.window("helpRig", exists=True):
        cmds.deleteUI("helpRig")
    WD = cmds.window("helpRig", title="Setup Rig Help", sizeable=False, resizeToFitChildren=True)
    cmds.windowPref("helpRig", remove=True)

    cmds.columnLayout("Face", adj=True)
    cmds.image(image= IMAGE_PATH+"/JAW.jpg")
    cmds.showWindow(WD)
                
def TG(*arg):
    if cmds.window("helpRig", exists=True):
        cmds.deleteUI("helpRig")
    WD = cmds.window("helpRig", title="Setup Rig Help", sizeable=False, resizeToFitChildren=True)
    cmds.windowPref("helpRig", remove=True)

    cmds.columnLayout("Face", adj=True)
    cmds.image(image= IMAGE_PATH+"/TG.jpg")
    cmds.showWindow(WD)