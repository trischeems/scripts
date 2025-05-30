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

cl_back = 1
cl_grey = 3
cl_darkRed = 4
cl_darkBlue = 6
cl_darkGreen = 7
cl_purple = 9
cl_brown = 10 
cl_red = 13
cl_lightGreen = 14
cl_while = 16
cl_yellow = 17
cl_lightBlue = 18
cl_pink = 20
cl_lightOrange = 21
cl_midnightGreen = 23 
cl_darkOrange = 24


################################################################
def DemoRig(*arg):
     cmds.file(file_path, o=True, f=True)

def reName(*arg):
	newName = cmds.textField("newName", query=True, text=True)
	objects = cmds.ls(selection=True)
	for i in objects:
		cmds.rename(i, newName)
#newName = cmds.textField("newName", edit=True, text="")                           

               
def frontName(*arg):
     #selected_objects = cmds.ls(selection=True)
	frontTextField = cmds.textField("frontName", query=True, text=True)
	objects = cmds.ls(selection=True)
	for i in objects:
		newNameF= frontTextField + i
		cmds.rename(i, newNameF)
          
    #frontTextField = cmds.textField("frontName", edit=True, text="")                           
def backName(*arg):
     #selected_objects = cmds.ls(selection=True)
	backTextField = cmds.textField("backName", query=True, text=True)
	objects = cmds.ls(selection=True)
	for i in objects:
		newNameB= i + backTextField
		cmds.rename(i, newNameB)
#backTextField = cmds.textField("backName", edit=True, text="")                           

def pasterdelete(*arg):
     mel.eval("""
     searchReplaceNames "pasted__" "/" "hierarchy";
              """)
     
def deleteImportName(*arg): 
     mel.eval("""
     treeViewChangeSelectCallback;
     namespaceEditCmd add namespaceEditor|namespaceEditorForm|treeView1;
     statusLineUpdateInputField;
     treeViewChangeSelectCallback;
     namespaceEditCmd add namespaceEditor|namespaceEditorForm|treeView1;
     statusLineUpdateInputField;
              """)

################################################################ connect options

def Node(*arg):
    cmds.NodeEditorWindow()
def connectEditor(*arg):
    cmds.ConnectionEditor()
def setdrivenkey(*arg):
    cmds.SetDrivenKey()
def addinfluence(*arg):
    cmds.AddInfluenceOptions()
def addattribute(*arg):
    cmds.AddAttribute()
def channelcontrol(*arg):
    cmds.ChannelControlEditor()
def jointSizeOptions(*arg):
    cmds.JdsWin()
def TextureViewWindow(*arg):
     cmds.TextureViewWindow()
def graphEditor(*arg):
     cmds.GraphEditor()
def jointTools(*arg):    
     cmds.JointTool()
def jointMirror(*arg):    
     cmds.MirrorJointOptions()
def CreateLattice(*arg):    
     cmds.CreateLattice()
def CopySkinWeights(*arg):    
     cmds.CopySkinWeights()
def SelectHierarchy(*arg): 
     cmds.SelectHierarchy()
def CreateBlendShapeOptions(*arg): 
     cmds.CreateBlendShapeOptions()
def CreateBlendShape(*arg): 
     cmds.CreateBlendShape()
def freezeOptions(*arg): 
     cmds.FreezeTransformationsOptions()
def ParentConstraintOptions(*arg): 
     cmds.ParentConstraintOptions()
def ScaleConstraintOptions(*arg): 
     cmds.ScaleConstraintOptions()
def OrientConstraint(*arg): 
     cmds.OrientConstraintOptions()
def AimConstraint(*arg): 
     cmds.AimConstraintOptions()
def PointConstraint(*arg): 
     cmds.PointConstraintOptions()
def PoleVectorConstraint(*arg): 
     cmds.PoleVectorConstraintOptions()
def orientJoint(*arg): 
     cmds.OrientJointOptions()
def PencilCurveTool(*arg): 
     cmds.PencilCurveTool()
def EPCurveTool(*arg): 
     cmds.EPCurveTool()
def createCircle(*arg): 
     cmds.circle( nr=(0, 1, 0), r=3)[0]
def SmoothBindSkin(*arg):
     cmds.SmoothBindSkinOptions()
def DetachSkin(*arg):
     cmds.DetachSkin()

def cubeAdd(*arg): 
     mel.eval('CreatePolygonCube;')
def sphereAdd(*arg):
     mel.eval('CreatePolygonSphere;')
def cylinderAdd(*arg):
     mel.eval('CreatePolygonCylinder;')
def torusAdd(*arg):
     mel.eval('CreatePolygonTorus;')
def coneAdd(*arg):
     mel.eval('CreatePolygonCone;')
def prismAdd(*arg):
     mel.eval('CreatePolygonPrism;')
def discAdd(*arg):
     mel.eval('CreatePolygonDisc;')
def pyramidAdd(*arg):
     mel.eval('CreatePolygonPyramid;')

def CombinePolygons(*arg):
     cmds.CombinePolygons()
def SeparatePolygon(*arg):
     cmds.SeparatePolygon()

     
def Otz(*arg): 
     mel.eval("""
     OptimizeScene;
     cleanUpScene 1;
              """)



################################################################ rigs

################################################################### translations

def freezeTrans(*arg):
     #cmds.FreezeTransformations()
     selections = cmds.ls(selection=True)
     for obj in selections:
          cmds.makeIdentity(selections, apply=True)
def resetPivot(*arg):
     cmds.ResetTransformations()
def centerPivot(*arg):
     cmds.CenterPivot()
def deleteHistory(*arg):
     selections = cmds.ls(selection=True)
     for obj in selections:
          cmds.DeleteHistory(selections, apply=True)
def MatchTransform(*arg):
     cmds.MatchTransform()

def unFreezeTrans(*arg):
     selections = cmds.ls(selection=True)
     for obj in selections:
          worlds = cmds.listRelatives(obj, parent=True)
          if worlds:
               cmds.parent(obj, world=True)
               cmds.makeIdentity(obj, apply=True, t=True)
               inPosition = cmds.xform(obj, query=True, rp=True, ws=True)
               rsPosition = [inPosition[0]*-1, inPosition[1]*-1, inPosition[2]*-1]
               cmds.xform(obj, t=rsPosition, ws=True)
               cmds.makeIdentity(obj, apply=True, t=True)
               cmds.xform(obj, t=inPosition, ws=True)
               cmds.parent(obj, worlds=True)
          else:
               cmds.makeIdentity(obj, apply=True, t=True)
               inPosition = cmds.xform(obj, query=True, rp=True, ws=True)
               rsPosition = [inPosition[0]*-1, inPosition[1]*-1, inPosition[2]*-1]
               cmds.xform(obj, t=rsPosition, ws=True)
               cmds.makeIdentity(obj, apply=True, t=True)
               cmds.xform(obj, t=inPosition, ws=True)

################################################################### controllers
def lockandhide(*arg):
    selected_attributes = cmds.channelBox("mainChannelBox", query=True, selectedMainAttributes=True)
    selected_objects = cmds.ls(selection=True)
    for obj in selected_objects:
        for attr in selected_attributes:
            cmds.setAttr(obj + "." + attr, lock=True, keyable=False)

def create2Ctrl(*arg):
    # select point object 
    selected_objects = cmds.ls(selection=True)
    scale_value = float(cmds.textField("scaleTextField", query =True, text=True))
    
    for obj in selected_objects:
        pivot_position = cmds.xform(selected_objects, query=True, worldSpace=True, rotatePivot=True)
        
        # create grp 1
        group = cmds.group( empty=True, name= obj + '_Main_Grp')
        cmds.xform(group, worldSpace=True, translation=pivot_position)
        
        # create ctrl 1
        controller = cmds.circle( nr=(0, 1, 0), r=3, name= obj + '_Main_Ctrl')[0]
        cmds.xform(controller, worldSpace=True, translation=pivot_position)
        cmds.parent(controller, group)
        
        # creat grp 2
        child_group = cmds.group(empty=True, name=obj + '_Grp')
        cmds.xform(child_group, worldSpace=True, translation=pivot_position)
        cmds.setAttr(controller + ".scale", scale_value, scale_value, scale_value)
        cmds.parent(child_group, controller)
        
        # creat ctrl 2 in grp 2
        inner_controller = cmds.circle(nr=(0, 1, 0), r=2, name=obj + '_Ctrl')[0]
        cmds.xform(inner_controller, worldSpace=True, translation=pivot_position)
        cmds.setAttr(inner_controller + ".scale", scale_value, scale_value, scale_value)
        cmds.parent(inner_controller, child_group)
        
        # creat joint in ctrl 2
        joint = cmds.joint(name=obj + '_jnt')
        cmds.xform(joint, worldSpace=True, translation=pivot_position)

           
def CreateRevFK(*arg):

    obj = pm.ls(sl=1)[0]
    sn = obj.split('_')
    locators = pm.ls(sn[0] + '_' + sn[1] + '*' + 'Loc')
    #enloc = sn[0] + '_' + sn[0] + '*' + 'EndLOC'   
    nameGuide = obj.split('_FK_GUIDES')[0]
         
    prevCtl = None
    ctlGrp = None
    name = sn[1]
    ctlGrpList = []
  
    for i in range(len(locators)):
        if ctlGrp:
            prevCtl = ctl
            pm.parent(prevCtl, ctlGrp )
                   
        ctl = pm.circle(radius=1,nr=(0, 1, 0))[0]
        pm.setAttr(ctl + ".overrideEnabled", 1)
        pm.setAttr(ctl + ".overrideRGBColors",1)
        pm.setAttr(ctl + ".overrideColorRGB", 1 ,1 ,0)          
        pm.rename(ctl,'{}_{}_Ctrl'.format(name, i+1))
        
        pos = pm.xform(locators[i], q=True, ws=True, t=True)
        rot = pm.xform(locators[i], q=True, ws=True, ro=True)
    
        pm.setAttr(ctl + '.translate' , pos)
        pm.setAttr(ctl + '.rotate' , rot)
          
        grp = ctl.replace('Ctrl','Grp')
        ctlGrp = pm.group ( em = 1 , name = grp)
        pm.setAttr(ctlGrp + '.translate' , pos)
        pm.setAttr(ctlGrp + '.rotate' , rot)
        if prevCtl:
            pm.parent(ctlGrp, prevCtl)   
        ctlGrpList.append(ctlGrp)
    pm.parent (('{}_fwdFk{}_Ctrl'.format(name, len(locators) )) , ctlGrp )


##################################### controller #################################
def create1Ctrl(*arg):
    selected_objects = cmds.ls(selection=True)
    scale_value = float(cmds.textField("scaleTextField", query =True, text=True))
    for obj in selected_objects:
        pivot_position = cmds.xform(selected_objects, ws=True, query=True, rotatePivot=True)
        
        # create grp 
        group= cmds.group(empty=True, name= obj +'_Main_Grp')
        cmds.xform(group, ws=True, translation=pivot_position)


        #creat Ctr
        controller = cmds.circle(nr=(0, 1, 0), r=3, name= obj +'_Main_Ctrl')[0]
        cmds.xform(controller, ws=True, translation=pivot_position)
        cmds.setAttr(controller + ".scale", scale_value, scale_value, scale_value)
        cmds.parent(controller, group)

        # create joint
        joint = cmds.joint(name=obj + '_jnt')
        cmds.xform(joint, ws=True, translation=pivot_position)
        cmds.parent(joint, controller)

def create1Ctrlparentobj(*arg):
    selected_objects = cmds.ls(selection=True)
#     scale_value = float(cmds.textField("scaleTextField", query =True, text=True))
    for obj in selected_objects:
        pivot_position = cmds.xform(selected_objects, ws=True, query=True, rotatePivot=True)
        
        # create grp 
        joint = cmds.joint(name=obj + '_jnt')
        cmds.xform(joint, ws=True, translation=pivot_position)
        cmds.parent(joint, world=True)

def createjntbind(*arg):
    selected_objects = cmds.ls(selection=True)
    for obj in selected_objects:
        pivot_position = cmds.xform(selected_objects, ws=True, query=True, rotatePivot=True)
        joint = cmds.joint(name=obj + '_jnt')
        cmds.xform(joint, ws=True, translation=pivot_position)
        cmds.parent(joint, world=True)
        cmds.skinCluster(joint, obj, toSelectedBones=True, bindMethod=0, skinMethod=0, normalizeWeights=1, maximumInfluences=3, obeyMaxInfluences=True)

def createJoint(*arg):
    selected_obj = cmds.ls(sl=True)
    if selected_obj:
     for curve in selected_obj:
          pivot_position = cmds.xform(selected_obj, ws=True, query=True, rotatePivot=True)
          Joint = cmds.joint(name= curve + "_jnt")
          cmds.xform(Joint, ws=True, translation=pivot_position)
          # cmds.setParent(Joint, curve)

def ctrlIn(*arg):
    selected_objects = cmds.ls(selection=True)
    scale_value = float(cmds.textField("scaleTextField", query =True, text=True))

    #parent_objects = cmds.checkBox("Parent", query=True, value=True)
    for obj in selected_objects:
        pivot_position = cmds.xform(selected_objects, ws=True, query=True, rotatePivot=True)
        
        # create grp 
        group= cmds.group(empty=True, name= obj +'_Main_Grp')
        cmds.xform(group, ws=True, translation=pivot_position)

        #creat Ctr
        controller = cmds.circle(nr=(0, 1, 0), r=3, name= obj +'_Main_Ctrl')[0]
        cmds.xform(controller, ws=True, translation=pivot_position)
        cmds.parent(controller, group)
        cmds.setAttr(group + ".scale", scale_value, scale_value, scale_value)
        cmds.parent(obj, controller)

        #if parent_objects:
            #cmds.button(label="parentCtrl", command=lambda obj=obj, controller=controller: cmds.parent(obj, controller)) 
def ctrlInB(*arg):
    selected_objects = cmds.ls(selection=True)
    scale_value = float(cmds.textField("scaleTextField", query =True, text=True))

    #parent_objects = cmds.checkBox("Parent", query=True, value=True)
    for obj in selected_objects:
        pivot_position = cmds.xform(selected_objects, ws=True, query=True, rotatePivot=True)
        
        # create grp 
        group= cmds.group(empty=True, name= obj +'_Main_Grp')
        cmds.xform(group, ws=True, translation=pivot_position)

        #creat Ctr
        controller = cmds.spaceLocator(name= obj +'_Main_Ctrl')[0]
        cmds.xform(controller, ws=True, translation=pivot_position)
        cmds.parent(controller, group)
        cmds.setAttr(group + ".scale", scale_value, scale_value, scale_value)
        cmds.parent(obj, controller)            



def add_blend_attribute(*arg):    
    selected_objects = cmds.ls(selection=True)
    for obj in selected_objects:   
        cmds.addAttr(selected_objects, longName='Blendshape', attributeType='float', min=1, max=10, keyable=True)   





################################################################  set driven key #################################################################
def add_color_attribute(*arg):    
    selected_objects = cmds.ls(selection=True)
    for obj in selected_objects:       
        cmds.addAttr(selected_objects, longName='Color', attributeType='long', min=1, max=10, keyable=True)


def Color_Set_Attr(*args):
    global driven_obj
    global driver_obj

    selected = cmds.ls(selection=True)
    name_attribute = str(cmds.textField("Name_Attr_field", query=True, text=True))
    Type_attribute = str(cmds.textField("Type_Attr_field", query=True, text=True))
    min_value = float(cmds.textField("min_value_attribute", query=True, text=True))
    max_value = float(cmds.textField("max_value_attribute", query=True, text=True))

    for obj in selected:
          type_attr = "{}".format(Type_attribute)
          cmds.addAttr(obj, longName=name_attribute, attributeType=type_attr , min=min_value, max=max_value, keyable=True)  
          # cmds.setAttr("{}.min".format(obj + "." + name_attribute), min_attr)
          # cmds.setAttr("{}.max".format(obj + "." + name_attribute), max_attr)  
    driver_obj = str(cmds.textField("driver_field", query =True, text=True))
    driven_obj = str(cmds.textField("driven_field", query =True, text=True))
    exp = str(cmds.textField("exp_color_attr", query =True, text=True))  
    cmds.delete(exp)

    driven_attr = "{}.frameExtension".format(driven_obj)
    driver_attr = "{}.{}".format(driver_obj, name_attribute)

    cmds.setDrivenKeyframe(driven_attr, currentDriver=driver_attr, driverValue=min_value, value=min_value)
#     cmds.setDrivenKeyframe(driven_attr, currentDriver=driver_attr, driverValue=2, value=2)
    cmds.setDrivenKeyframe(driven_attr, currentDriver=driver_attr, driverValue=max_value, value=max_value)

    cmds.selectKey(clear=True)
    cmds.selectKey("{}.frameExtension".format(driven_obj), add=True)
    cmds.keyTangent(inTangentType="linear", outTangentType="linear")
#     mel.eval('if( `checkBoxGrp -q -v1 attrBoundaryBox` ) addAttr -e -minValue `min 1 10` ' +  ".{}".format(name_attribute) + '; if( `checkBoxGrp -q -v2 attrBoundaryBox` ) addAttr -e -maxValue `max 1 10`  ' +  ".{}".format(name_attribute) + '; dynRenameUpdateMinMax ' +  ".{}".format(name_attribute) + ';')
def add_attribute_ctrl(*arg):
    selected = cmds.ls(selection=True)
    name_attribute = str(cmds.textField("Name_Attr_field", query=True, text=True))
    Type_attribute = str(cmds.textField("Type_Attr_field", query=True, text=True))
    min_value = float(cmds.textField("min_value_attribute", query=True, text=True))
    max_value = float(cmds.textField("max_value_attribute", query=True, text=True))
    for obj in selected:
          type_attr = "{}".format(Type_attribute)
          cmds.addAttr(obj, longName=name_attribute, attributeType=type_attr , min=min_value, max=max_value, keyable=True)  

def set_key_attr(*arg):
     select_obj = cmds.ls(sl=True)
     driver_obj = str(cmds.textField("driver_field", query=True, text=True))
     driven_obj = str(cmds.textField("driven_field", query=True, text=True))
     driver_name = str(cmds.textField("driver_name_attr", query=True, text=True))
     driven_name = str(cmds.textField("driven_name_attr", query=True, text=True))
     min_value = float(cmds.textField("min_value_attribute", query=True, text=True))
     max_value = float(cmds.textField("max_value_attribute", query=True, text=True))
     driver_attr = driver_obj + "." + driver_name
     driven_attr = driven_obj + "." + driven_name

     cmds.setDrivenKeyframe(driven_attr, currentDriver=driver_attr, driverValue=min_value, value=min_value)
     cmds.setDrivenKeyframe(driven_attr, currentDriver=driver_attr, driverValue=max_value, value=max_value)
     if set_key_attr:
          cmds.textField("key_warning", edit=True, text="Set Driven Key Complete !!!")
          cmds.warning("Set Driven Key Complete")
     cmds.selectKey(clear=True)
     cmds.selectKey(driven_attr, add=True)
     cmds.keyTangent(inTangentType="spline", outTangentType="spline")
     cmds.setInfinity(pri='cycleRelative')
     cmds.setInfinity(poi='cycleRelative')


################################################################ loop expressions #########################################################################
def loopVibrating(*arg):
     selected_objects = cmds.ls(selection=True)
     pivot_position = cmds.xform(selected_objects, ws=True, query=True, rotatePivot=True)
     for obj in selected_objects:
          group = cmds.group(empty=True, name = 'VibratingLoop_Grp')
          cmds.xform(group, worldSpace=True, translation=pivot_position)
          Controller = cmds.circle(nr=(0, 1, 0), r=2, name = 'ctrlloop')[0]
          cmds.xform(Controller, worldSpace=True, translation=pivot_position)
          cmds.addAttr(Controller, longName = 'Level', attributeType = 'float', min = 0, max = 10, keyable=True) 
          cmds.parent(Controller, group)

          Joint = cmds.joint(name = 'loop')[0]
          cmds.xform(Joint, worldSpace=True, radius=1, translation=pivot_position)
          cmds.parent(Joint, Controller)

def addExpressionToObject(*args):
    selected_objects = cmds.ls(selection=True)
    expression_code = '''
    $min = 0.005 - ctrlloop.Level/10;
    $max = 0.005 + ctrlloop.Level/10;
    
    loop.translateX = rand($min, $max);
    loop.translateY = rand($min, $max);
    loop.translateZ = rand($min, $max);
    loop.rotateX = rand($min, $max);
    loop.rotateY = rand($min, $max);
    loop.rotateZ = rand($min, $max);

    '''

    for obj in selected_objects:
        expression_node = cmds.expression(n='Tri_3D', s=expression_code, o=obj)
        cmds.expression(expression_node, enable=True)
 

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

################################################################ color line objects

def redColorCtrl(*arg):
     selected_curves = cmds.ls(selection=True, dag=True, shapes=True)
     if selected_curves:
          for curve in selected_curves:
               cmds.setAttr(curve + ".overrideEnabled", True)
               cmds.setAttr(curve + ".overrideColor", cl_red)
               cmds.setAttr(curve + ".overrideRGBColors", False)
                 
def pinkColorCtrl(*arg):
     selected_curves = cmds.ls(selection=True, dag=True, shapes=True)
     if selected_curves:
          for curve in selected_curves:
               cmds.setAttr(curve + ".overrideEnabled", True)
               cmds.setAttr(curve + ".overrideColor", cl_pink)
               cmds.setAttr(curve + ".overrideRGBColors", False)


def yellowColorCtrl(*arg):
     selected_curves = cmds.ls(selection=True, dag=True, shapes=True)
     if selected_curves:
          for curve in selected_curves:
               cmds.setAttr(curve + ".overrideEnabled", True)
               cmds.setAttr(curve + ".overrideColor", cl_yellow)
               cmds.setAttr(curve + ".overrideRGBColors", False)

def blueLColorCtrl(*arg):
     selected_curves = cmds.ls(selection=True, dag=True, shapes=True)
     if selected_curves:
          for curve in selected_curves:
               cmds.setAttr(curve + ".overrideEnabled", True)
               cmds.setAttr(curve + ".overrideColor", cl_lightBlue)

def greenColorCtrl(*arg):
     selected_curves = cmds.ls(selection=True, dag=True, shapes=True)
     if selected_curves:
          for curve in selected_curves:
               cmds.setAttr(curve + ".overrideEnabled", True)
               cmds.setAttr(curve + ".overrideColor", cl_lightGreen)
               cmds.setAttr(curve + ".overrideRGBColors", False)

def whileColorCtrl(*arg):
     selected_curves = cmds.ls(selection=True, dag=True, shapes=True)
     if selected_curves:
          for curve in selected_curves:
               cmds.setAttr(curve + ".overrideEnabled", True)
               cmds.setAttr(curve + ".overrideColor", cl_while)
               cmds.setAttr(curve + ".overrideRGBColors", False)


def blueColorCtrl(*arg):
     selected_curves = cmds.ls(selection=True, dag=True, shapes=True)
     if selected_curves:
          for curve in selected_curves:
               cmds.setAttr(curve + ".overrideEnabled", True)
               cmds.setAttr(curve + ".overrideColor", cl_darkBlue)
               cmds.setAttr(curve + ".overrideRGBColors", False)

def purpleColorCtrl(*arg):
     selected_curves = cmds.ls(selection=True, dag=True, shapes=True)
     if selected_curves:
          for curve in selected_curves:
               cmds.setAttr(curve + ".overrideEnabled", True)
               cmds.setAttr(curve + ".overrideColor", cl_purple)
               cmds.setAttr(curve + ".overrideRGBColors", False)

def blackColorCtrl(*arg):
     selected_curves = cmds.ls(selection=True, dag=True, shapes=True)
     if selected_curves:
          for curve in selected_curves:
               cmds.setAttr(curve + ".overrideEnabled", True)
               cmds.setAttr(curve + ".overrideColor", cl_back)
               cmds.setAttr(curve + ".overrideRGBColors", False)


def greyColorCtrl(*arg):
     selected_curves = cmds.ls(selection=True, dag=True, shapes=True)
     if selected_curves:
          for curve in selected_curves:
               cmds.setAttr(curve + ".overrideEnabled", True)
               cmds.setAttr(curve + ".overrideColor", cl_grey)
               cmds.setAttr(curve + ".overrideRGBColors", False)

def cl_brownColorCtrl(*arg):
     selected_curves = cmds.ls(selection=True, dag=True, shapes=True)
     if selected_curves:
          for curve in selected_curves:
               cmds.setAttr(curve + ".overrideEnabled", True)
               cmds.setAttr(curve + ".overrideColor", cl_brown)
               cmds.setAttr(curve + ".overrideRGBColors", False)

def cl_darkRedColorCtrl(*arg):
     selected_curves = cmds.ls(selection=True, dag=True, shapes=True)
     if selected_curves:
          for curve in selected_curves:
               cmds.setAttr(curve + ".overrideEnabled", True)
               cmds.setAttr(curve + ".overrideColor", cl_darkRed)
               cmds.setAttr(curve + ".overrideRGBColors", False)

def cl_lightOrangeColorCtrl(*arg):
     selected_curves = cmds.ls(selection=True, dag=True, shapes=True)
     if selected_curves:
          for curve in selected_curves:
               cmds.setAttr(curve + ".overrideEnabled", True)
               cmds.setAttr(curve + ".overrideColor", cl_lightOrange)
               cmds.setAttr(curve + ".overrideRGBColors", False)

def cl_midnightGreenColorCtrl(*arg):
     selected_curves = cmds.ls(selection=True, dag=True, shapes=True)
     if selected_curves:
          for curve in selected_curves:
               cmds.setAttr(curve + ".overrideEnabled", True)
               cmds.setAttr(curve + ".overrideColor", cl_midnightGreen)
               cmds.setAttr(curve + ".overrideRGBColors", False)

def cl_darkBlueColorCtrl(*arg):
     selected_curves = cmds.ls(selection=True, dag=True, shapes=True)
     if selected_curves:
          for curve in selected_curves:
               cmds.listRelatives(curve, shapes=True)
               cmds.setAttr(curve + ".overrideEnabled", True)
               cmds.setAttr(curve + ".overrideColor", cl_darkBlue)
               cmds.setAttr(curve + ".overrideRGBColors", False)

def refillcolorctrl(*arg):
     allObjs = cmds.ls(sl=True)
     for obj in allObjs:
            shapes = cmds.listRelatives(obj, shapes=True)
            for shape in shapes:
                 cmds.setAttr("{0}.overrideEnabled".format(shape), False)
                
def holdOut(*arg):
     selected_objects = cmds.ls(sl=True)
     for obj in selected_objects:
        holdout_state = cmds.getAttr(obj + ".holdOut")
        cmds.setAttr(obj + ".holdOut", not holdout_state)

################################################################ joints
"""def jointsize(*args):
    slider_value = cmds.intSliderGrp("sliderGrp", query=True, value=True)
    joint_scale = slider_value / 50.100
    
    selected_joints = cmds.ls(selection=True, type="joint")
    if selected_joints:
        for joint in selected_joints:
            cmds.setAttr(joint + ".radius", joint_scale)

def scaleJoint(*arg):
     scaleJoint_value = cmds.textField("scaleJointTextField", query=True, text=True)

     try:
          scaleJoint_value = float(scaleJoint_value)
     except ValueError:
          cmds.warning("Dien vao gia tri")
          return
     
     selected_joints = cmds.ls(selection=True, type="joint")
     if selected_joints :
          for joint in selected_joints:
               cmds.setAttr(joint + ".radius", scaleJoint_value)"""




def inbetweenjoints(*args):
    ladcurve=cmds.textField("loadcurve",q=True,text=True)
    numberofjoints=cmds.textField("numberofjointfeild",q=True,text=True)
    curveinfo=cmds.arclen(ladcurve,ch=1)
    curvelength=cmds.getAttr(curveinfo + ".arcLength")
    getUvalue=float(1.0/(int(numberofjoints)-1))
    newvalue=0
    cmds.select(cl=1)
    newjntstart=cmds.joint(n= "joint10")
    pathanimationstart=cmds.pathAnimation(newjntstart,c=ladcurve)
    startctrl=cmds.circle(n=newjntstart + "_Ctrl",r=0.5,nr=(0,1,0))
    startctrlgrp=cmds.group(n=newjntstart + "Ctrl_Grp")
    cmds.delete(cmds.pointConstraint(newjntstart,startctrlgrp))
    cmds.parentConstraint(startctrl,newjntstart,mo=1)
    cmds.select(cl=1)
    newjntstartlist=[]
    newgrpstartlist=[]
    newctrlstartlist=[]
    for eachnumberofjoints in range(1,int(numberofjoints)):
        newjnt=cmds.joint(n= "joint1" + str(eachnumberofjoints))
        newjntstartlist.append(newjnt)
        circlectrl=cmds.circle(n=newjnt + "_Ctrl",r=0.5,nr=(0,1,0))
        ctrlgrp=cmds.group(n=newjnt + "Ctrl_Grp")
        newctrlstartlist.append(circlectrl)
        newgrpstartlist.append(ctrlgrp)
        pathanimation=cmds.pathAnimation(newjnt,c=ladcurve)
        newvalue +=getUvalue
        cmds.setAttr(pathanimation + ".uValue",newvalue)
        cmds.delete(cmds.ls("addDoubleLinear*"))
        cmds.delete(pathanimation)
        cmds.setAttr(newjnt + ".jointOrientX",0)
        cmds.setAttr(newjnt + ".jointOrientY",0)
        cmds.setAttr(newjnt + ".jointOrientZ",0)
        cmds.delete(cmds.pointConstraint(newjnt,ctrlgrp))
        cmds.parentConstraint(circlectrl,newjnt,mo=1)
        cmds.select(clear=1)
    cmds.parent(newjntstartlist[0],newjntstart)
    cmds.parent(newgrpstartlist[0],startctrl)
    for each in range(0,len(newjntstartlist)-1):
        cmds.parent(newjntstartlist[each+1],newjntstartlist[each])
        cmds.parent(newgrpstartlist[each+1],newctrlstartlist[each])
    cmds.select(newjntstart,hi=1)
    cmds.joint(e=1,oj="xyz",secondaryAxisOrient="xup",zso=1)
    cmds.setAttr(newjntstartlist[-1] + ".jointOrientX",0)
    cmds.setAttr(newjntstartlist[-1] + ".jointOrientY",0)
    cmds.setAttr(newjntstartlist[-1] + ".jointOrientZ",0)

def addcurve(*args):
    lodcurve=cmds.ls(selection=1)
    addcurve =cmds.textField("loadcurve", edit=True, text=lodcurve[0])
    
################################################################ skin weight



#def freezeTransform(*arg):

################################################################ tools
#def autoWheel(*args):
#    script_folder = Tools
 #   script_file = 'AutoWheel.py'
#
  #  script_path = os.path.join(script_folder, script_file)
 #   if os.path.exists(script_path):
   #       execfile(script_path)
    #else:
     #   cmds.warning('file script: {}'.format(script_path))
#
 #   cmds.showWindow("triWin")

# cmds.addAttr(obj, ln=attr, proxy="%s.%s"%(baseCtrl, attr), at="float", min=0, max=1, keyable=1)













