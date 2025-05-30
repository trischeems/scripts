############################################################################################################

###############################
###############################
                ###
                ###
                ###
                ###             #######################       ###          ##########        ##########
                ###             #######################       ###           #########        ###########
                ###             ###                 ###       ###                  ##        ##        ##
                ###             ###                 ###       ###                 ##         ##          ##
                ###             ###                 ###       ###            ########        ##          ##
                ###             ###                 ###       ###                   ##       ##         ##
                ###             ###                 ###       ###                  ##        ##        ##
                ###             ###                 ###       ###          ########          ##########

########### " Contacts with me : info.tri3d@gmail.com "
########### " Gumroad : https://phamtri.gumroad.com/"
########### " Copyright by Tri 3D "
########### " Thanks for you !!! "


import maya.cmds as cmds
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import os
import random
import webbrowser
from PySide2 import QtGui
import subprocess

file_path = os.path.join(os.path.dirname(__file__), "Demo.ma")


################################################################
driven_obj =""
driver_obj =""



################################################################
def DemoRig(*arg):
     cmds.file(file_path, o=True, f=True)

def graphEditor(*arg):
     cmds.GraphEditor()

def freezeOptions(*arg): 
     cmds.FreezeTransformationsOptions()

def Otz(*arg): 
     mel.eval("""
     OptimizeScene;
     cleanUpScene 1;
              """)

def groupobj(*arg):
    selObj = mc.ls(sl=True)
    for all in selObj:
        grp = mc.group(em=True)
        rnm_grp = mc.rename(grp,all + "_grp")
        mc.parent(rnm_grp,all)
        mc.setAttr(rnm_grp + ".tx", 0)
        mc.setAttr(rnm_grp + ".ty", 0)
        mc.setAttr(rnm_grp + ".tz", 0)
        mc.setAttr(rnm_grp + ".rx", 0)
        mc.setAttr(rnm_grp + ".ry", 0)
        mc.setAttr(rnm_grp + ".rz", 0)
        mc.setAttr(rnm_grp + ".sx", 1)
        mc.setAttr(rnm_grp + ".sy", 1)
        mc.setAttr(rnm_grp + ".sz", 1)
        mc.delete(mc.parentConstraint(all,rnm_grp))
        mc.ungroup(all)
        mc.parent(all,rnm_grp)
        mc.makeIdentity(all, apply=True, t=True, r=True, s=True)
        
################################################################ copyRight
def openWebMessFB(*args):
    webpage_url = "https://www.facebook.com/messages/t/108516382068518/"

    webbrowser.open(webpage_url)
def openWebPageFB(*args):
    webpage_url = "https://www.facebook.com/profile.php?id=100087409486213"

    webbrowser.open(webpage_url)    
def openWebgumroad(*args):
    webpage_url = "https://phamtri.gumroad.com/"
    webbrowser.open(webpage_url)

def openWebRiggingCause(*args):
    webpage_url = "https://phamtri.gumroad.com/l/basic?layout=profile"
    webbrowser.open(webpage_url)

def openWebRiggingSlide(*args):
    webpage_url = "https://docs.google.com/presentation/d/1ELEz1J8mR2REnp3-We48rX2ARDdkeFXH2o6wSLT8pLs/edit?usp=sharing"
    webbrowser.open(webpage_url)
        
def openGmail(*args):
     webpage_url = "https://mail.google.com/mail/u/0/#inbox?compose=VpCqJRzBSwJKQztWDTJMgbKRMktKhpdTjnmjtwdFzGMWVZpjZxFLTGJbwcjZkgttCcFklgb"
     webbrowser.open(webpage_url)

def copyEmail(*args):
    text_to_copy = "info.tri3d@gmail.com"
    clipboard = QtGui.QGuiApplication.clipboard()
    clipboard.setText(text_to_copy)
    cmds.warning("Copy : info.tri3d@gmail.com to clipboard")
    cmds.confirmDialog(title='Copy_Email', message="Copy Email done !   \n\n         UwU")












