import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm


joint_ER = "EyeR"
joint_EL = "EyeL"

joint_Neck = "Neck"

Jnt_MUL ="Mid_Up_Lip"
Jnt_MDL ="Mid_Down_Lip"
Jnt_RCL = "R_Corner_Lip"
Jnt_BW1 = "R_Between_1"
Jnt_BW2 = "R_Between_2"
Jnt_BW3 = "R_Between_3"
Jnt_BW4 = "R_Between_4"

Jnt_LCL = "L_Corner_Lip"
Jnt_BW5 = "L_Between_1"
Jnt_BW6 = "L_Between_2"
Jnt_BW7 = "L_Between_3"
Jnt_BW8 = "L_Between_4"

####################################
####################################
Color1 = 18 # blue
Color2 = 13 # red
Color3 = 17 # yellow
Color4 = 14 # green
Color5 = 21 # orange
ColorCurve1 = 3 # xam
ColorCurve2 = 18 # xanh
ColorCurve3 = 17 # vang
################################## Eye 
def rightEye(*arg):
    selected_object = cmds.ls(sl=True)
    for obj in selected_object :
        Eye_Joint_R = cmds.joint(n="EyeR")
        cmds.matchTransform(Eye_Joint_R, obj , rot=True, pos=True)
        cmds.parent(Eye_Joint_R, joint_Neck)
    cmds.textField("RE_Car_Text", edit=True, text="Right Eye Done !")
    cmds.checkBox("RE_Car_CheckBox", enable=True, edit=True, value=True)
def dltRE(*arg):
    cmds.delete(joint_ER)
    cmds.textField("RE_Car_Text", edit=True, text=" Delete !")

def leftEye(*arg):
    selected_object = cmds.ls(sl=True)
    for obj in selected_object :
        Eye_Joint_L = cmds.joint(n="EyeL")
        cmds.matchTransform(Eye_Joint_L, obj , rot=True, pos=True)
        cmds.parent(Eye_Joint_L, joint_Neck)
    cmds.textField("LE_Car_Text", edit=True, text="Left Eye Done !")
    cmds.checkBox("LE_Car_CheckBox", enable=True, edit=True, value=True)
def dltLE(*arg):
    cmds.delete(joint_EL)
    cmds.textField("LE_Car_Text", edit=True, text=" Delete !")


################################### mouths
def MidUpLip(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="Mid_Up_Lip",position=vertex_pos)
    cmds.parent(joint, world=True)
    cmds.textField("MUL_Car_Text", edit=True, text="Mid Up Lip Done !")
    cmds.checkBox("MUL_Car_CheckBox", enable=True, edit=True, value=True)
def dltMUL(*arg):
    cmds.delete(Jnt_MUL)
    cmds.textField("MUL_Car_Text", edit=True, text=" Delete !")


def MidBW1(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="R_Between_1",position=vertex_pos)
    cmds.parent(joint, Jnt_MUL)
    cmds.textField("RB1_Car_Text", edit=True, text="R Between 1 Done !")
    cmds.checkBox("RB1_Car_CheckBox", enable=True, edit=True, value=True)
def dltBW1(*arg):
    cmds.delete(Jnt_BW1)
    cmds.textField("RB1_Car_Text", edit=True, text=" Delete !")


def MidBW2(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="R_Between_2",position=vertex_pos)
    cmds.parent(joint, Jnt_BW1)
    cmds.textField("RB2_Car_Text", edit=True, text="R Between 2 Done !")
    cmds.checkBox("RB2_Car_CheckBox", enable=True, edit=True, value=True)
def dltBW2(*arg):
    cmds.delete(Jnt_BW2)
    cmds.textField("RB2_Car_Text", edit=True, text=" Delete !")


def R_Corner_Lip(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="R_Corner_Lip",position=vertex_pos)
    cmds.parent(joint, Jnt_BW2)
    cmds.textField("RCL_Car_Text", edit=True, text="Right Corner Lip Done !")
    cmds.checkBox("RCL_Car_CheckBox", enable=True, edit=True, value=True)
def dltRCL(*arg):
    cmds.delete(Jnt_RCL)
    cmds.textField("RCL_Car_Text", edit=True, text=" Delete !")


def MidBW3(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="R_Between_3",position=vertex_pos)
    cmds.parent(joint, Jnt_RCL)
    cmds.textField("RB3_Car_Text", edit=True, text="R Between 3 Done !")
    cmds.checkBox("RB3_Car_CheckBox", enable=True, edit=True, value=True)
def dltBW3(*arg):
    cmds.delete(Jnt_BW3)
    cmds.textField("RB3_Car_Text", edit=True, text=" Delete !")


def MidBW4(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="R_Between_4",position=vertex_pos)
    cmds.parent(joint, Jnt_BW3)
    cmds.textField("RB4_Car_Text", edit=True, text="R Between 4 Done !")
    cmds.checkBox("RB4_Car_CheckBox", enable=True, edit=True, value=True)
def dltBW4(*arg):
    cmds.delete(Jnt_BW4)
    cmds.textField("RB4_Car_Text", edit=True, text=" Delete !")


def MidDownLip(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="Mid_Down_Lip",position=vertex_pos)
    cmds.parent(joint, Jnt_MUL)
    cmds.textField("MDL_Car_Text", edit=True, text="Mid Down Lip Done !")
    cmds.checkBox("MDL_Car_CheckBox", enable=True, edit=True, value=True)
def dltMDL(*arg):
    cmds.delete(Jnt_MDL)
    cmds.textField("MDL_Car_Text", edit=True, text=" Delete !")

def MirrorMouth(*arg):
    mel.eval("""                
    select -r R_Between_1 ;
    mirrorJoint -mirrorYZ -mirrorBehavior -searchReplace "R" "L";
             
    select -r Mid_Up_Lip ;
    select -tgl Neck ;
    parent;
             
             
             """)
    
    cmds.textField("MR_Text", edit=True, text="Mirror Done !")
    cmds.checkBox("MR_CheckBox", edit=True, value=True) 
def buildFace(*arg):
    groupMain = cmds.group(name="Main_Face_Grp_dont_FreezeTransformations", empty=True)
    Main_Functions = cmds.curve(name="Main_Face",d=1, p=[
        (-0.43, 0, -0.86),
        (0.43, 0, -0.86),
        (0.43, 0, 0.71),
        (-0.43, 0, 0.71),
        (-0.43, 0, -0.86)])
    
    # mel.eval("""
    # setAttr "Main_Face.overrideEnabled" 1;
    # changeObjColor Main_Face.overrideColor AttributeEditor|MainAttributeEditorLayout|formLayout92|AEmenuBarLayout|AErootLayout|AEStackLayout|AErootLayoutPane|AEbaseFormLayout|AEcontrolFormLayout|AttrEdtransformFormLayout|scrollLayout3|columnLayout33|frameLayout50|columnLayout37|frameLayout56|columnLayout48|columnLayout51|objIndexColorSlider;
    # updateLayerColor Main_Face.overrideColor AttributeEditor|MainAttributeEditorLayout|formLayout92|AEmenuBarLayout|AErootLayout|AEStackLayout|AErootLayoutPane|AEbaseFormLayout|AEcontrolFormLayout|AttrEdtransformFormLayout|scrollLayout3|columnLayout33|frameLayout50|columnLayout37|frameLayout56|columnLayout48|columnLayout51|objIndexColorSlider;
    # """)

    mel.eval('setAttr -lock true -keyable false -channelBox false "Main_Face.v";')
    Functions = cmds.curve(name="LineFunction",d=1, p=[        
        (-0.4, 0, 0.45),
        (0.4, 0, 0.45),
        (0.4, 0, 0.68),
        (-0.4, 0, 0.68),
        (-0.4, 0, 0.45)])

    mel.eval("""
    curve -d 2 -p -0.08 0 0.65 -p -0.08 0 0.56 -p -0.08 0 0.48 -p -0.06 0 0.48 -p -0.05 0 0.48 -p -0.03 0 0.54 -p -0.01 0 0.6 -p 0 0 0.62 -p 0 0 0.62 -p 0.01 0 0.61 -p 0.01 0 0.6 -p 0.03 0 0.54 -p 0.05 0 0.48 -p 0.07 0 0.48 -p 0.08 0 0.48 -p 0.08 0 0.56 -p 0.08 0 0.65 -p 0.07 0 0.65 -p 0.06 0 0.65 -p 0.06 0 0.58 -p 0.06 0 0.51 -p 0.04 0 0.58 -p 0.01 0 0.65 -p 0 0 0.65 -p -0.01 0 0.65 -p -0.03 0 0.58 -p -0.06 0 0.5 -p -0.06 0 0.58 -p -0.06 0 0.65 -p -0.07 0 0.65 -p -0.08 0 0.65;
                          """)
    cmds.CenterPivot()    
    mel.eval("""    
    select -r LineFunction ;
    //setAttr "curveShape2.template" 1;
             """)
    cmds.parent(Functions, Main_Functions)
    cmds.listRelatives(Main_Functions, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Main_Functions), True)
    cmds.setAttr("{0}.overrideColor".format(Main_Functions), ColorCurve2)  
    cmds.parent(Main_Functions, groupMain)

    Ctrl_grp = cmds.group(name="Ctrl_Grp", empty=True)
    cmds.parent(Ctrl_grp, Main_Functions)
    Line_grp = cmds.group(name="Line_grp", empty=True)
    cmds.parent(Line_grp, Main_Functions)
    Line2 = cmds.curve(name="Line2",d=1, p=[(-0.14, 0, -0.14),
        (0.14, 0, -0.14),
        (0.14, 0, 0.14),
        (-0.14, 0, 0.14),
        (-0.14, 0, -0.14)])
    gr4 = cmds.group(n="BR", empty=True)
    Func4 = cmds.curve(name="Bow_Ctrl_R", d=1, p=[        
        (0, 0, -0.36),(0.12, 0, -0.36),
        (0.24, 0, -0.24),(0.36, 0, -0.12),(0.36, 0, 0),(0.36, 0, 0.12),(0.24, 0, 0.24),
        (0.12, 0, 0.36),(0, 0, 0.36),(-0.12, 0, 0.36),(-0.24, 0, 0.24),(-0.36, 0, 0.12),
        (-0.36, 0, 0),(-0.36, 0, -0.12),(-0.24, 0, -0.24),(-0.12, 0, -0.36),(0, 0, -0.36)])
    cmds.parent(Func4, gr4)
    cmds.parent(gr4, Line2) 
    mel.eval("""
    setAttr "BR.scaleZ" 0.140;
    setAttr "BR.scaleX" 0.140;
    setAttr "BR.scaleY" 0.140;
             """)   
             
    cmds.parent(Line2, Line_grp)     
    mel.eval("""
    setAttr "Line2.translateX" -0.216;
    setAttr "Line2.translateZ" -0.646;

    select -r Line2 ;
    //setAttr "curveShape4.template" 1;

             """)
    cmds.listRelatives(Line2, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Line2), True)
    cmds.setAttr("{0}.overrideColor".format(Line2), ColorCurve1)  

    Line3 = cmds.curve(name="Line3",d=1, p=[(-0.14, 0, -0.14),
        (0.14, 0, -0.14),
        (0.14, 0, 0.14),
        (-0.14, 0, 0.14),
        (-0.14, 0, -0.14)])
    gr3 = cmds.group(n="BL", empty=True)
    Func3 = cmds.curve(name="Bow_Ctrl_L", d=1, p=[        
        (0, 0, -0.36),(0.12, 0, -0.36),
        (0.24, 0, -0.24),(0.36, 0, -0.12),(0.36, 0, 0),(0.36, 0, 0.12),(0.24, 0, 0.24),
        (0.12, 0, 0.36),(0, 0, 0.36),(-0.12, 0, 0.36),(-0.24, 0, 0.24),(-0.36, 0, 0.12),
        (-0.36, 0, 0),(-0.36, 0, -0.12),(-0.24, 0, -0.24),(-0.12, 0, -0.36),(0, 0, -0.36)])
    cmds.parent(Func3, gr3)
    cmds.parent(gr3, Line3) 
    mel.eval("""
    setAttr "BL.scaleZ" 0.140;
    setAttr "BL.scaleX" 0.140;
    setAttr "BL.scaleY" 0.140;
             """)  
    
    cmds.parent(Line3, Line_grp)        
    mel.eval("""
    setAttr "Line3.translateX" 0.216;
    setAttr "Line3.translateZ" -0.646;
    setAttr -lock true -keyable false -channelBox false "Line3.v";    
    select -r Line3 ;

             """)
    cmds.listRelatives(Line3, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Line3), True)
    cmds.setAttr("{0}.overrideColor".format(Line3), ColorCurve1)  

 
    
    Line4 = cmds.curve(name="Line4",d=1, p=[(-0.14, 0, -0.14),
        (0.14, 0, -0.14),
        (0.14, 0, 0.14),
        (-0.14, 0, 0.14),
        (-0.14, 0, -0.14)])
    gr1 = cmds.group(n="ER", empty=True)
    Func1 = cmds.curve(name="Eye_Ctrl_R", d=1, p=[        
        (0, 0, -0.36),(0.12, 0, -0.36),
        (0.24, 0, -0.24),(0.36, 0, -0.12),(0.36, 0, 0),(0.36, 0, 0.12),(0.24, 0, 0.24),
        (0.12, 0, 0.36),(0, 0, 0.36),(-0.12, 0, 0.36),(-0.24, 0, 0.24),(-0.36, 0, 0.12),
        (-0.36, 0, 0),(-0.36, 0, -0.12),(-0.24, 0, -0.24),(-0.12, 0, -0.36),(0, 0, -0.36)])
    cmds.parent(Func1, gr1)
    cmds.parent(gr1, Line4) 
    mel.eval("""
    setAttr "ER.scaleZ" 0.140;
    setAttr "ER.scaleX" 0.140;
    setAttr "ER.scaleY" 0.140;
             """)   
             
    cmds.parent(Line4, Line_grp)    
    mel.eval("""
    setAttr "Line4.translateX" -0.216;
    setAttr "Line4.translateZ" -0.264;
    setAttr -lock true -keyable false -channelBox false "Line4.v";
    select -r Line4 ;

             """)
    cmds.listRelatives(Line4, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Line4), True)
    cmds.setAttr("{0}.overrideColor".format(Line4), ColorCurve1)  

    Line5 = cmds.curve(name="Line5",d=1, p=[(-0.14, 0, -0.14),
        (0.14, 0, -0.14),
        (0.14, 0, 0.14),
        (-0.14, 0, 0.14),
        (-0.14, 0, -0.14)])
    gr2 = cmds.group(n="EL", empty=True)
    Func2 = cmds.curve(name="Eye_Ctrl_L", d=1, p=[        
        (0, 0, -0.36),(0.12, 0, -0.36),
        (0.24, 0, -0.24),(0.36, 0, -0.12),(0.36, 0, 0),(0.36, 0, 0.12),(0.24, 0, 0.24),
        (0.12, 0, 0.36),(0, 0, 0.36),(-0.12, 0, 0.36),(-0.24, 0, 0.24),(-0.36, 0, 0.12),
        (-0.36, 0, 0),(-0.36, 0, -0.12),(-0.24, 0, -0.24),(-0.12, 0, -0.36),(0, 0, -0.36)])
    cmds.parent(Func2, gr2)
    cmds.parent(gr2, Line5) 
    mel.eval("""
    setAttr "EL.scaleZ" 0.140;
    setAttr "EL.scaleX" 0.140;
    setAttr "EL.scaleY" 0.140;
             """)   
    cmds.parent(Line5, Line_grp)    
    mel.eval("""
    setAttr "Line5.translateX" 0.216;
    setAttr "Line5.translateZ" -0.264;
    setAttr -lock true -keyable false -channelBox false "Line5.v";
    select -r Line5 ;

             """)
    cmds.listRelatives(Line5, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Line5), True)
    cmds.setAttr("{0}.overrideColor".format(Line5), ColorCurve1)  


    Line6 = cmds.curve(name="Line6",d=1, p=[(-0.14, 0, -0.14),
        (0.14, 0, -0.14),
        (0.14, 0, 0.14),
        (-0.14, 0, 0.14),
        (-0.14, 0, -0.14)])
    gr5 = cmds.group(n="MM", empty=True)
    Func5 = cmds.curve(name="Mouth", d=1, p=[        
        (0, 0, -0.36),(0.12, 0, -0.36),
        (0.24, 0, -0.24),(0.36, 0, -0.12),(0.36, 0, 0),(0.36, 0, 0.12),(0.24, 0, 0.24),
        (0.12, 0, 0.36),(0, 0, 0.36),(-0.12, 0, 0.36),(-0.24, 0, 0.24),(-0.36, 0, 0.12),
        (-0.36, 0, 0),(-0.36, 0, -0.12),(-0.24, 0, -0.24),(-0.12, 0, -0.36),(0, 0, -0.36)])
    cmds.parent(Func5, gr5) 
    cmds.parent(Line6, Line_grp)     
    mel.eval("""
    setAttr "Line6.scaleZ" 1.5;
    setAttr "Line6.scaleX" 1.5;
    setAttr "Line6.scaleY" 1.5;
    setAttr "Line6.translateZ" 0.20;
    select -r Line6 ;

             """)
    cmds.listRelatives(Line6, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Line6), True)
    cmds.setAttr("{0}.overrideColor".format(Line6), ColorCurve1)  
    cmds.parent(gr5, Line6) 
    mel.eval("""
    setAttr "MM.scaleZ" 0.140;
    setAttr "MM.scaleX" 0.140;
    setAttr "MM.scaleY" 0.140;
    setAttr "MM.translateZ" -0.14;
    
             """)  


    mel.eval("""
    setAttr -keyable false -channelBox true "Main_Face.tx";
    setAttr -keyable false -channelBox true "Main_Face.ty";
    setAttr -keyable false -channelBox true "Main_Face.tz";
    setAttr -keyable false -channelBox true "Main_Face.rx";
    setAttr -keyable false -channelBox true "Main_Face.ry";
    setAttr -keyable false -channelBox true "Main_Face.rz";
    setAttr -keyable false -channelBox true "Main_Face.sx";
    setAttr -keyable false -channelBox true "Main_Face.sy";
    setAttr -keyable false -channelBox true "Main_Face.sz";
             """)
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_R.ty";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_R.sz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_R.sx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_R.sy";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_R.ry";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_R.rx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_R.rz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_R.v";')
    cmds.transformLimits(Func4, tx=(-1, 1), ty=(0, 0), tz=(-1, 1), rx=(0, 0), ry=(0, 0), rz=(0, 0), sx=(1, 1), sy=(1, 1), sz=(1, 1), etx=(True, True), ety=(True, True), etz=(True, True))
    cmds.listRelatives(Func4, shapes=True)
    cmds.addAttr(Func4, longName='______________________', attributeType='enum', en='____________', keyable=True)
    mel.eval('setAttr -lock true "Bow_Ctrl_R.______________________";')
    # cmds.addAttr(Func4, longName = 'Blink', attributeType = 'float', min = 0, max = 10, keyable=True) 
    # cmds.addAttr(Func4, longName = 'Iris', attributeType = 'float', min = 0, max = 10, keyable=True) 
    # cmds.addAttr(Func4, longName = 'Pupil', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.setAttr("{0}.overrideEnabled".format(Func4), True)
    cmds.setAttr("{0}.overrideColor".format(Func4), ColorCurve3) 

    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_L.ty";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_L.sz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_L.sx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_L.sy";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_L.ry";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_L.rx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_L.rz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_L.v";')
    cmds.transformLimits(Func3, tx=(-1, 1), ty=(0, 0), tz=(-1, 1), rx=(0, 0), ry=(0, 0), rz=(0, 0), sx=(1, 1), sy=(1, 1), sz=(1, 1), etx=(True, True), ety=(True, True), etz=(True, True))
    cmds.listRelatives(Func3, shapes=True)
    cmds.addAttr(Func3, longName='______________________', attributeType='enum', en='____________', keyable=True)
    mel.eval('setAttr -lock true "Bow_Ctrl_L.______________________";')
    # cmds.addAttr(Func3, longName = 'Blink', attributeType = 'float', min = 0, max = 10, keyable=True) 
    # cmds.addAttr(Func3, longName = 'Iris', attributeType = 'float', min = 0, max = 10, keyable=True) 
    # cmds.addAttr(Func3, longName = 'Pupil', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.setAttr("{0}.overrideEnabled".format(Func3), True)
    cmds.setAttr("{0}.overrideColor".format(Func3), ColorCurve3) 

    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_R.ty";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_R.sz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_R.sx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_R.sy";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_R.ry";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_R.rx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_R.rz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_R.v";')
    cmds.transformLimits(Func1, tx=(-1, 1), ty=(0, 0), tz=(-1, 1), rx=(0, 0), ry=(0, 0), rz=(0, 0), sx=(1, 1), sy=(1, 1), sz=(1, 1), etx=(True, True), ety=(True, True), etz=(True, True))
    cmds.listRelatives(Func1, shapes=True)
    cmds.addAttr(Func1, longName='______________________', attributeType='enum', en='____________', keyable=True)
    mel.eval('setAttr -lock true "Eye_Ctrl_R.______________________";')
    cmds.addAttr(Func1, longName = 'Blink', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.addAttr(Func1, longName = 'Iris', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.addAttr(Func1, longName = 'Pupil', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.setAttr("{0}.overrideEnabled".format(Func1), True)
    cmds.setAttr("{0}.overrideColor".format(Func1), ColorCurve3) 

    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_L.ty";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_L.sz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_L.sx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_L.sy";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_L.ry";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_L.rx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_L.rz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_L.v";')
    cmds.transformLimits(Func2, tx=(-1, 1), ty=(0, 0), tz=(-1, 1), rx=(0, 0), ry=(0, 0), rz=(0, 0), sx=(1, 1), sy=(1, 1), sz=(1, 1), etx=(True, True), ety=(True, True), etz=(True, True))
    cmds.listRelatives(Func2, shapes=True)
    cmds.addAttr(Func2, longName='______________________', attributeType='enum', en='____________', keyable=True)
    mel.eval('setAttr -lock true "Eye_Ctrl_L.______________________";')
    cmds.addAttr(Func2, longName = 'Blink', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.addAttr(Func2, longName = 'Iris', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.addAttr(Func2, longName = 'Pupil', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.setAttr("{0}.overrideEnabled".format(Func2), True)
    cmds.setAttr("{0}.overrideColor".format(Func2), ColorCurve3) 

    mel.eval('setAttr -lock true -keyable false -channelBox false "Mouth.ty";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Mouth.sz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Mouth.sx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Mouth.sy";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Mouth.ry";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Mouth.rx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Mouth.rz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Mouth.v";')
    cmds.transformLimits(Func5, tx=(-1, 1), ty=(0, 0), tz=(0, 2), rx=(0, 0), ry=(0, 0), rz=(0, 0), sx=(1, 1), sy=(1, 1), sz=(1, 1), etx=(True, True), ety=(True, True), etz=(True, True))
    cmds.listRelatives(Func5, shapes=True)
    cmds.addAttr(Func5, longName='______________________', attributeType='enum', en='____________', keyable=True)
    mel.eval('setAttr -lock true "Mouth.______________________";')
    cmds.addAttr(Func5, longName = 'Happy', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.addAttr(Func5, longName = 'Sad', attributeType = 'float', min = 0, max = 10, keyable=True) 
    # cmds.addAttr(Func5, longName = 'Wow', attributeType = 'float', min = 0, max = 10, keyable=True) 
    # cmds.addAttr(Func5, longName = 'Angry', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.setAttr("{0}.overrideEnabled".format(Func5), True)
    cmds.setAttr("{0}.overrideColor".format(Func5), ColorCurve3)     

    mel.eval("""
    rename "curve1" "Mouth_Function";
    """)
    cmds.parent("Mouth_Function", "LineFunction")
    groupMain_xf = cmds.xform(joint_Neck, query=True, translation=True, worldSpace=True)
    groupMain_xf_tuple = tuple(groupMain_xf)
    cmds.xform(groupMain, worldSpace=True, translation=groupMain_xf_tuple)

    mel.eval("""
    setAttr -lock true -keyable false -channelBox false "Line6.tx";
    setAttr -lock true -keyable false -channelBox false "Line2.tx";
    setAttr -lock true -keyable false -channelBox false "Line5.tx";
    setAttr -lock true -keyable false -channelBox false "Line4.tx";
    setAttr -lock true -keyable false -channelBox false "Line3.tx";
    setAttr -lock true -keyable false -channelBox false "LineFunction.tx";
    setAttr -lock true -keyable false -channelBox false "Line6.ty";
    setAttr -lock true -keyable false -channelBox false "Line2.ty";
    setAttr -lock true -keyable false -channelBox false "Line5.ty";
    setAttr -lock true -keyable false -channelBox false "Line4.ty";
    setAttr -lock true -keyable false -channelBox false "Line3.ty";
    setAttr -lock true -keyable false -channelBox false "LineFunction.ty";
    setAttr -lock true -keyable false -channelBox false "Line6.tz";
    setAttr -lock true -keyable false -channelBox false "Line2.tz";
    setAttr -lock true -keyable false -channelBox false "Line5.tz";
    setAttr -lock true -keyable false -channelBox false "Line4.tz";
    setAttr -lock true -keyable false -channelBox false "Line3.tz";
    setAttr -lock true -keyable false -channelBox false "LineFunction.tz";
    setAttr -lock true -keyable false -channelBox false "Line6.rx";
    setAttr -lock true -keyable false -channelBox false "Line2.rx";
    setAttr -lock true -keyable false -channelBox false "Line5.rx";
    setAttr -lock true -keyable false -channelBox false "Line4.rx";
    setAttr -lock true -keyable false -channelBox false "Line3.rx";
    setAttr -lock true -keyable false -channelBox false "LineFunction.rx";
    setAttr -lock true -keyable false -channelBox false "Line6.ry";
    setAttr -lock true -keyable false -channelBox false "Line2.ry";
    setAttr -lock true -keyable false -channelBox false "Line5.ry";
    setAttr -lock true -keyable false -channelBox false "Line4.ry";
    setAttr -lock true -keyable false -channelBox false "Line3.ry";
    setAttr -lock true -keyable false -channelBox false "LineFunction.ry";
    setAttr -lock true -keyable false -channelBox false "Line6.rz";
    setAttr -lock true -keyable false -channelBox false "Line2.rz";
    setAttr -lock true -keyable false -channelBox false "Line5.rz";
    setAttr -lock true -keyable false -channelBox false "Line4.rz";
    setAttr -lock true -keyable false -channelBox false "Line3.rz";
    setAttr -lock true -keyable false -channelBox false "LineFunction.rz";
    setAttr -lock true -keyable false -channelBox false "Line6.sx";
    setAttr -lock true -keyable false -channelBox false "Line2.sx";
    setAttr -lock true -keyable false -channelBox false "Line5.sx";
    setAttr -lock true -keyable false -channelBox false "Line4.sx";
    setAttr -lock true -keyable false -channelBox false "Line3.sx";
    setAttr -lock true -keyable false -channelBox false "LineFunction.sx";
    setAttr -lock true -keyable false -channelBox false "Line6.sy";
    setAttr -lock true -keyable false -channelBox false "Line2.sy";
    setAttr -lock true -keyable false -channelBox false "Line5.sy";
    setAttr -lock true -keyable false -channelBox false "Line4.sy";
    setAttr -lock true -keyable false -channelBox false "Line3.sy";
    setAttr -lock true -keyable false -channelBox false "LineFunction.sy";
    setAttr -lock true -keyable false -channelBox false "Line6.sz";
    setAttr -lock true -keyable false -channelBox false "Line2.sz";
    setAttr -lock true -keyable false -channelBox false "Line5.sz";
    setAttr -lock true -keyable false -channelBox false "Line4.sz";
    setAttr -lock true -keyable false -channelBox false "Line3.sz";
    setAttr -lock true -keyable false -channelBox false "LineFunction.sz";
    setAttr -lock true -keyable false -channelBox false "Line6.v";
    setAttr -lock true -keyable false -channelBox false "Line2.v";
    setAttr -lock true -keyable false -channelBox false "Line5.v";
    setAttr -lock true -keyable false -channelBox false "Line4.v";
    setAttr -lock true -keyable false -channelBox false "Line3.v";
    setAttr -lock true -keyable false -channelBox false "LineFunction.v";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.tx";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.ty";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.tz";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.rx";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.ry";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.rz";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.sx";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.sy";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.sz";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.v";
    """)
    cmds.listRelatives("Mouth_Function", shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format("Mouth_Function"), True)
    cmds.setAttr("{0}.overrideColor".format("Mouth_Function"), Color5)  
    mel.eval("""
    setAttr "Main_Face_Grp_dont_FreezeTransformations.rotateX" 90;
    select -r Main_Face_Grp_dont_FreezeTransformations ;
    //scale -r 0.3 0.3 0.3;
    setAttr "Main_Face_Grp_dont_FreezeTransformations.translateX" 3;
    setAttr "Main_Face_Grp_dont_FreezeTransformations.translateY" 16;

    """)


    # ############################# add selected layer #########################
    # mel.eval("""
    # layerEditorCreateLayer 1;
    # layerEditorLayerButtonTypeChange layer1;
    # select -r LineFunction Line6 Line5 ;
    # select -tgl Line4 ;
    # select -tgl Line2 Line3 ;
    # editDisplayLayerMembers -noRecurse layer1 `ls -selection`;
    #                       """)
    # mel.eval('select -cl ;')  

    ############################################################## tuple
    Face_grp_pos = cmds.xform(joint_Neck, query=True, translation=True, worldSpace=True)
    Face_grp_tuple = tuple(Face_grp_pos)

    jnt_ER_pos = cmds.xform(joint_ER, query=True, translation=True, worldSpace=True)
    jnt_ER_tuple = tuple(jnt_ER_pos)

    jnt_EL_pos = cmds.xform(joint_EL, query=True, translation=True, worldSpace=True)
    jnt_EL_tuple = tuple(jnt_EL_pos)

    jnt_MUL_pos = cmds.xform(Jnt_MUL, query=True, translation=True, worldSpace=True)
    jnt_MUL_tuple = tuple(jnt_MUL_pos)

    jnt_BW1_pos = cmds.xform(Jnt_BW1, query=True, translation=True, worldSpace=True)
    jnt_BW1_tuple = tuple(jnt_BW1_pos)

    jnt_BW2_pos = cmds.xform(Jnt_BW2, query=True, translation=True, worldSpace=True)
    jnt_BW2_tuple = tuple(jnt_BW2_pos)

    jnt_RCL_pos = cmds.xform(Jnt_RCL, query=True, translation=True, worldSpace=True)
    jnt_RCL_tuple = tuple(jnt_RCL_pos)

    jnt_BW3_pos = cmds.xform(Jnt_BW3, query=True, translation=True, worldSpace=True)
    jnt_BW3_tuple = tuple(jnt_BW3_pos)

    jnt_BW4_pos = cmds.xform(Jnt_BW4, query=True, translation=True, worldSpace=True)
    jnt_BW4_tuple = tuple(jnt_BW4_pos)    

    jnt_MDL_pos = cmds.xform(Jnt_MDL, query=True, translation=True, worldSpace=True)
    jnt_MDL_tuple = tuple(jnt_MDL_pos)    

    jnt_LCL_pos = cmds.xform(Jnt_LCL, query=True, translation=True, worldSpace=True)
    jnt_LCL_tuple = tuple(jnt_LCL_pos)

    jnt_BW5_pos = cmds.xform(Jnt_BW5, query=True, translation=True, worldSpace=True)
    jnt_BW5_tuple = tuple(jnt_BW5_pos)

    jnt_BW6_pos = cmds.xform(Jnt_BW6, query=True, translation=True, worldSpace=True)
    jnt_BW6_tuple = tuple(jnt_BW6_pos) 

    jnt_BW7_pos = cmds.xform(Jnt_BW7, query=True, translation=True, worldSpace=True)
    jnt_BW7_tuple = tuple(jnt_BW7_pos)

    jnt_BW8_pos = cmds.xform(Jnt_BW8, query=True, translation=True, worldSpace=True)
    jnt_BW8_tuple = tuple(jnt_BW8_pos) 

    ##############################################################
    ############################################################## Eye Build

    R_Eye_grp = cmds.group(n="R_Eye_Grp", empty=True)
    cmds.xform(R_Eye_grp, translation=jnt_ER_tuple)
    cmds.parent(R_Eye_grp, groupMain)
    R_Eye_Loc_grp = cmds.group(n="R_Eye_Loc_grp", empty=True)
    cmds.xform(R_Eye_Loc_grp, translation=jnt_ER_tuple)
    cmds.parent(R_Eye_Loc_grp, R_Eye_grp)
    R_Loc_ER = cmds.curve(name ="R_Loc_Ctrl", degree = 1,
                    knot = [0, 4.7999999999999998, 9.5999999999999996, 12.800000000000001, 17.600000000000001,
                            22.399999999999999, 25.600000000000001, 30.399999999999999, 35.200000000000003,
                            38.399999999999999, 43.200000000000003, 48, 51.200000000000003],
                    point = [(-0.64000000000000012, -2.5600000000000005, 0),
                            (-0.64000000000000012, -0.64000000000000012, 0),(-2.5600000000000005, -0.64000000000000012, 0),
                            (-2.5600000000000005, 0.64000000000000012, 0),(-0.64000000000000012, 0.64000000000000012, 0),
                            (-0.64000000000000012, 2.5600000000000005, 0),(0.64000000000000012, 2.5600000000000005, 0),
                            (0.64000000000000012, 0.64000000000000012, 0),(2.5600000000000005, 0.64000000000000012, 0),
                            (2.5600000000000005, -0.64000000000000012, 0),(0.64000000000000012, -0.64000000000000012, 0),
                            (0.64000000000000012, -2.5600000000000005, 0),(-0.64000000000000012, -2.5600000000000005, 0)])
    cmds.scale(0.2,0.2,0.2)
    cmds.listRelatives(R_Loc_ER, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_Loc_ER), True)
    cmds.setAttr("{0}.overrideColor".format(R_Loc_ER), Color4)
    cmds.xform(R_Loc_ER, translation=jnt_ER_tuple)
    cmds.parent(R_Loc_ER, R_Eye_Loc_grp)

    mel.eval("""
    setAttr "R_Eye_Loc_grp|R_Loc_Ctrl.translateZ" 4;
    FreezeTransformations;
    select -cl  ;
            """)

    L_Eye_grp = cmds.group(n="L_Eye_Grp", empty=True)
    cmds.xform(L_Eye_grp, translation=jnt_EL_tuple)
    cmds.parent(L_Eye_grp, groupMain)
    L_Eye_Loc_grp = cmds.group(n="L_Eye_Loc_grp", empty=True)
    cmds.xform(L_Eye_Loc_grp, translation=jnt_EL_tuple)
    cmds.parent(L_Eye_Loc_grp, L_Eye_grp)
    L_Loc_ER = cmds.curve(name ="L_Loc_Ctrl", degree = 1,
                    knot = [0, 4.7999999999999998, 9.5999999999999996, 12.800000000000001, 17.600000000000001,
                            22.399999999999999, 25.600000000000001, 30.399999999999999, 35.200000000000003,
                            38.399999999999999, 43.200000000000003, 48, 51.200000000000003],
                    point = [(-0.64000000000000012, -2.5600000000000005, 0),
                            (-0.64000000000000012, -0.64000000000000012, 0),(-2.5600000000000005, -0.64000000000000012, 0),
                            (-2.5600000000000005, 0.64000000000000012, 0),(-0.64000000000000012, 0.64000000000000012, 0),
                            (-0.64000000000000012, 2.5600000000000005, 0),(0.64000000000000012, 2.5600000000000005, 0),
                            (0.64000000000000012, 0.64000000000000012, 0),(2.5600000000000005, 0.64000000000000012, 0),
                            (2.5600000000000005, -0.64000000000000012, 0),(0.64000000000000012, -0.64000000000000012, 0),
                            (0.64000000000000012, -2.5600000000000005, 0),(-0.64000000000000012, -2.5600000000000005, 0)])
    cmds.scale(0.2,0.2,0.2)
    cmds.listRelatives(L_Loc_ER, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_Loc_ER), True)
    cmds.setAttr("{0}.overrideColor".format(L_Loc_ER), Color4)    
    cmds.xform(L_Loc_ER, translation=jnt_EL_tuple)
    cmds.parent(L_Loc_ER, L_Eye_Loc_grp)
    mel.eval("""
    setAttr "L_Eye_Loc_grp|L_Loc_Ctrl.translateZ" 4;
    FreezeTransformations;
    select -cl  ;
            """)    

    jnt_ER = cmds.joint(n="ERJ_R")
    cmds.xform(jnt_ER, worldSpace=True, translation = jnt_ER_tuple)
    cmds.parent(jnt_ER, R_Eye_Loc_grp)
    
    jnt_EL = cmds.joint(n="ERJ_L")
    cmds.xform(jnt_EL, worldSpace=True, translation = jnt_EL_tuple)
    cmds.parent(jnt_EL, L_Eye_Loc_grp)

    ############################################################ Parent Eye
    mel.eval("""
    select -r R_Eye_Loc_grp|R_Loc_Ctrl ;
    select -add ERJ_R ;
    parentConstraint -mo -weight 1;
    select -r L_Eye_Loc_grp|L_Loc_Ctrl ;
    select -add ERJ_L ;
    parentConstraint -mo -weight 1;
             
    select -r ERJ_R ;
    select -add EyeR ;
    parentConstraint -mo -weight 1;
    select -r ERJ_L ;
    select -add EyeL ;
    parentConstraint -mo -weight 1;

    select -r ERJ_R ;
    select -add ERJ_L ;
    toggleVisibilityAndKeepSelection `optionVar -query toggleVisibilityAndKeepSelectionBehaviour`;    
             """)
    
    ############################################################## set driven key eye
    mel.eval("""
    setAttr "Eye_Ctrl_L.translateX" 0;
    setAttr "L_Eye_Loc_grp.translateX" 0;
    setDrivenKeyframe -currentDriver Eye_Ctrl_L.translateX L_Eye_Loc_grp.translateX;
    setAttr "Eye_Ctrl_L.translateX" 1;
    setAttr "L_Eye_Loc_grp.translateX" 2;
    setDrivenKeyframe -currentDriver Eye_Ctrl_L.translateX L_Eye_Loc_grp.translateX;
    setAttr "Eye_Ctrl_L.translateX" -1;
    setAttr "L_Eye_Loc_grp.translateX" -2;
    setDrivenKeyframe -currentDriver Eye_Ctrl_L.translateX L_Eye_Loc_grp.translateX;

    setAttr "Eye_Ctrl_L.translateZ" 0;
    setAttr "L_Eye_Loc_grp.translateY" 0;
    setDrivenKeyframe -currentDriver Eye_Ctrl_L.translateZ L_Eye_Loc_grp.translateY;
    setAttr "Eye_Ctrl_L.translateZ" -1;
    setAttr "L_Eye_Loc_grp.translateY" 2;
    setDrivenKeyframe -currentDriver Eye_Ctrl_L.translateZ L_Eye_Loc_grp.translateY;
    setAttr "Eye_Ctrl_L.translateZ" 1;
    setAttr "L_Eye_Loc_grp.translateY" -2;
    setDrivenKeyframe -currentDriver Eye_Ctrl_L.translateZ L_Eye_Loc_grp.translateY;
             
    setAttr "Eye_Ctrl_R.translateX" 0;
    setAttr "R_Eye_Loc_grp.translateX" 0;
    setDrivenKeyframe -currentDriver Eye_Ctrl_R.translateX R_Eye_Loc_grp.translateX;
    setAttr "Eye_Ctrl_R.translateX" 1;
    setAttr "R_Eye_Loc_grp.translateX" 2;
    setDrivenKeyframe -currentDriver Eye_Ctrl_R.translateX R_Eye_Loc_grp.translateX;
    setAttr "Eye_Ctrl_R.translateX" -1;
    setAttr "R_Eye_Loc_grp.translateX" -2;
    setDrivenKeyframe -currentDriver Eye_Ctrl_R.translateX R_Eye_Loc_grp.translateX;

    setAttr "Eye_Ctrl_R.translateZ" 0;
    setAttr "R_Eye_Loc_grp.translateY" 0;
    setDrivenKeyframe -currentDriver Eye_Ctrl_R.translateZ R_Eye_Loc_grp.translateY;
    setAttr "Eye_Ctrl_R.translateZ" -1;
    setAttr "R_Eye_Loc_grp.translateY" 2;
    setDrivenKeyframe -currentDriver Eye_Ctrl_R.translateZ R_Eye_Loc_grp.translateY;
    setAttr "Eye_Ctrl_R.translateZ" 1;
    setAttr "R_Eye_Loc_grp.translateY" -2;
    setDrivenKeyframe -currentDriver Eye_Ctrl_R.translateZ R_Eye_Loc_grp.translateY;   

    setAttr "Eye_Ctrl_R.translateZ" 0;
    setAttr "Eye_Ctrl_L.translateZ" 0;
    setAttr "Eye_Ctrl_R.translateX" 0;
    setAttr "Eye_Ctrl_L.translateX" 0;                                                  
             """)
    
    ############################################################## P parentConstraint
    mel.eval("""
    select -r EyeR_parentConstraint1 ;
    select -add EyeL_parentConstraint1 ;
    select -add Main_Face_Grp_dont_FreezeTransformations ;
    parent;
             """)
    

    ############################################################## Mouth build
    ##############################################################
    Face_Grp = cmds.group(n="Face_Ctrl_Grp", empty=True)
    cmds.xform(Face_Grp, translation=Face_grp_tuple)
    cmds.parent(Face_Grp, "Main_Face_Grp_dont_FreezeTransformations")

    ############################ MUL
    MUL_grp = cmds.group(n="MUL_Grp", empty=True)
    cmds.xform(MUL_grp, translation=jnt_MUL_tuple)
    MUL_Jaw_grp = cmds.group(n="MUL_Jaw_grp", empty=True)
    cmds.xform(MUL_grp, translation=jnt_MUL_tuple)
    cmds.parent(MUL_Jaw_grp, MUL_grp)
    mel.eval("""
    select -r MUL_Jaw_grp ;
    FreezeTransformations;
    """)  
    cmds.CenterPivot(MUL_Jaw_grp)
    MUL_Ctrl_grp = cmds.group(n="MUL_Ctrl_grp", empty=True)
    cmds.xform(MUL_grp, translation=jnt_MUL_tuple)
    cmds.parent(MUL_Ctrl_grp, MUL_Jaw_grp)
    mel.eval("""
    select -r MUL_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(MUL_Ctrl_grp)
    MUL_Ctrl = cmds.curve(name ="Mid_Up_Lip_Ctrl", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.5,0.5,0.5)
    cmds.listRelatives(MUL_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(MUL_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(MUL_Ctrl), Color4)
    cmds.xform(MUL_Ctrl, translation=jnt_MUL_tuple)
    cmds.parent(MUL_Ctrl, MUL_Ctrl_grp)
    mel.eval("""
    select -r Mid_Up_Lip_Ctrl ;
    setAttr "Mid_Up_Lip_Ctrl.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(MUL_grp, Face_Grp)
    
    ############################ BW1
    BW1_grp = cmds.group(n="BW1_Grp", empty=True)
    cmds.xform(BW1_grp, translation=jnt_BW1_tuple)
    BW1_Jaw_grp = cmds.group(n="BW1_Jaw_grp", empty=True)
    cmds.xform(BW1_grp, translation=jnt_BW1_tuple)
    cmds.parent(BW1_Jaw_grp, BW1_grp)
    mel.eval("""
    select -r BW1_Jaw_grp ;
    FreezeTransformations;
    """) 
    cmds.CenterPivot()
    BW1_Ctrl_grp = cmds.group(n="BW1_Ctrl_grp", empty=True)
    cmds.xform(BW1_grp, translation=jnt_BW1_tuple)
    cmds.parent(BW1_Ctrl_grp, BW1_Jaw_grp)
    mel.eval("""
    select -r BW1_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(BW1_Ctrl_grp)
    BW1_Ctrl = cmds.curve(name ="BW1_Ctrl_R", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.5,0.5,0.5)
    cmds.listRelatives(BW1_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(BW1_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(BW1_Ctrl), Color4)
    cmds.xform(BW1_Ctrl, translation=jnt_BW1_tuple)
    cmds.parent(BW1_Ctrl, BW1_Ctrl_grp)
    mel.eval("""
    select -r BW1_Ctrl_R ;
    setAttr "BW1_Ctrl_R.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(BW1_grp, Face_Grp)

    ############################ BW2
    BW2_grp = cmds.group(n="BW2_Grp", empty=True)
    cmds.xform(BW2_grp, translation=jnt_BW2_tuple)
    BW2_Jaw_grp = cmds.group(n="BW2_Jaw_grp", empty=True)
    cmds.xform(BW2_grp, translation=jnt_BW2_tuple)
    cmds.parent(BW2_Jaw_grp, BW2_grp)
    mel.eval("""
    select -r BW2_Jaw_grp ;
    FreezeTransformations;
    """)     
    cmds.CenterPivot()
    BW2_Ctrl_grp = cmds.group(n="BW2_Ctrl_grp", empty=True)
    cmds.xform(BW2_grp, translation=jnt_BW2_tuple)
    cmds.parent(BW2_Ctrl_grp, BW2_Jaw_grp)
    mel.eval("""
    select -r BW2_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(BW2_Ctrl_grp)
    BW2_Ctrl = cmds.curve(name ="BW2_Ctrl_R", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.5,0.5,0.5)
    cmds.listRelatives(BW2_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(BW2_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(BW2_Ctrl), Color4)
    cmds.xform(BW2_Ctrl, translation=jnt_BW2_tuple)
    cmds.parent(BW2_Ctrl, BW2_Ctrl_grp)
    mel.eval("""
    select -r BW2_Ctrl_R ;
    setAttr "BW2_Ctrl_R.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(BW2_grp, Face_Grp)

    ############################ RCL
    RCL_grp = cmds.group(n="RCL_Grp", empty=True)
    cmds.xform(RCL_grp, translation=jnt_RCL_tuple)
    RCL_Jaw_grp = cmds.group(n="RCL_Jaw_grp", empty=True)
    cmds.xform(RCL_grp, translation=jnt_RCL_tuple)
    cmds.parent(RCL_Jaw_grp, RCL_grp)
    mel.eval("""
    select -r RCL_Jaw_grp ;
    FreezeTransformations;
    """)       
    cmds.CenterPivot()
    RCL_Ctrl_grp = cmds.group(n="RCL_Ctrl_grp", empty=True)
    cmds.xform(RCL_grp, translation=jnt_RCL_tuple)
    cmds.parent(RCL_Ctrl_grp, RCL_Jaw_grp)
    mel.eval("""
    select -r RCL_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(RCL_Ctrl_grp)
    RCL_Ctrl = cmds.curve(name ="RCL_Ctrl_R", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.5,0.5,0.5)
    cmds.listRelatives(RCL_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(RCL_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(RCL_Ctrl), Color4)
    cmds.xform(RCL_Ctrl, translation=jnt_RCL_tuple)
    cmds.parent(RCL_Ctrl, RCL_Ctrl_grp)
    mel.eval("""
    select -r RCL_Ctrl_R ;
    setAttr "RCL_Ctrl_R.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(RCL_grp, Face_Grp)

    ############################ BW3
    BW3_grp = cmds.group(n="BW3_Grp", empty=True)
    cmds.xform(BW3_grp, translation=jnt_BW3_tuple)
    BW3_Jaw_grp = cmds.group(n="BW3_Jaw_grp", empty=True)
    cmds.xform(BW3_grp, translation=jnt_BW3_tuple)
    cmds.parent(BW3_Jaw_grp, BW3_grp)
    mel.eval("""
    select -r BW3_Jaw_grp ;
    FreezeTransformations;
    """)      
    cmds.CenterPivot()
    BW3_Ctrl_grp = cmds.group(n="BW3_Ctrl_grp", empty=True)
    cmds.xform(BW3_grp, translation=jnt_BW3_tuple)
    cmds.parent(BW3_Ctrl_grp, BW3_Jaw_grp)
    mel.eval("""
    select -r BW3_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(BW3_Ctrl_grp)
    BW3_Ctrl = cmds.curve(name ="BW3_Ctrl_R", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.5,0.5,0.5)
    cmds.listRelatives(BW3_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(BW3_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(BW3_Ctrl), Color4)
    cmds.xform(BW3_Ctrl, translation=jnt_BW3_tuple)
    cmds.parent(BW3_Ctrl, BW3_Ctrl_grp)
    mel.eval("""
    select -r BW3_Ctrl_R ;
    setAttr "BW3_Ctrl_R.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(BW3_grp, Face_Grp)

    ############################ BW4
    BW4_grp = cmds.group(n="BW4_Grp", empty=True)
    cmds.xform(BW4_grp, translation=jnt_BW4_tuple)
    BW4_Jaw_grp = cmds.group(n="BW4_Jaw_grp", empty=True)
    cmds.xform(BW4_grp, translation=jnt_BW4_tuple)
    cmds.parent(BW4_Jaw_grp, BW4_grp)
    mel.eval("""
    select -r BW4_Jaw_grp ;
    FreezeTransformations;
    """)     
    cmds.CenterPivot()
    BW4_Ctrl_grp = cmds.group(n="BW4_Ctrl_grp", empty=True)
    cmds.xform(BW4_grp, translation=jnt_BW4_tuple)
    cmds.parent(BW4_Ctrl_grp, BW4_Jaw_grp)
    mel.eval("""
    select -r BW4_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(BW4_Ctrl_grp)
    BW4_Ctrl = cmds.curve(name ="BW4_Ctrl_R", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.5,0.5,0.5)
    cmds.listRelatives(BW4_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(BW4_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(BW4_Ctrl), Color4)
    cmds.xform(BW4_Ctrl, translation=jnt_BW4_tuple)
    cmds.parent(BW4_Ctrl, BW4_Ctrl_grp)
    mel.eval("""
    select -r BW4_Ctrl_R ;
    setAttr "BW4_Ctrl_R.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(BW4_grp, Face_Grp)

    ############################ MDL
    MDL_grp = cmds.group(n="MDL_Grp", empty=True)
    cmds.xform(MDL_grp, translation=jnt_MDL_tuple)
    MDL_Jaw_grp = cmds.group(n="MDL_Jaw_grp", empty=True)
    cmds.xform(MDL_grp, translation=jnt_MDL_tuple)
    cmds.parent(MDL_Jaw_grp, MDL_grp)
    mel.eval("""
    select -r MDL_Jaw_grp ;
    FreezeTransformations;
    """)       
    cmds.CenterPivot()
    MDL_Ctrl_grp = cmds.group(n="MDL_Ctrl_grp", empty=True)
    cmds.xform(MDL_grp, translation=jnt_MDL_tuple)
    cmds.parent(MDL_Ctrl_grp, MDL_Jaw_grp)
    cmds.CenterPivot(MDL_Ctrl_grp)
    mel.eval("""
    select -r MDL_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(MUL_Ctrl_grp)
    MDL_Ctrl = cmds.curve(name ="Mid_Down_Lip_Ctrl", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.5,0.5,0.5)
    cmds.listRelatives(MDL_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(MDL_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(MDL_Ctrl), Color4)
    cmds.xform(MDL_Ctrl, translation=jnt_MDL_tuple)
    cmds.parent(MDL_Ctrl, MDL_Ctrl_grp)
    mel.eval("""
    select -r Mid_Down_Lip_Ctrl ;
    setAttr "Mid_Down_Lip_Ctrl.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(MDL_grp, Face_Grp)

    ############################ BW5
    BW5_grp = cmds.group(n="BW5_Grp", empty=True)
    cmds.xform(BW5_grp, translation=jnt_BW5_tuple)
    BW5_Jaw_grp = cmds.group(n="BW5_Jaw_grp", empty=True)
    cmds.xform(BW5_grp, translation=jnt_BW5_tuple)
    cmds.parent(BW5_Jaw_grp, BW5_grp)
    mel.eval("""
    select -r BW5_Jaw_grp ;
    FreezeTransformations;
    """)       
    cmds.CenterPivot()
    BW5_Ctrl_grp = cmds.group(n="BW5_Ctrl_grp", empty=True)
    cmds.xform(BW5_grp, translation=jnt_BW5_tuple)
    cmds.parent(BW5_Ctrl_grp, BW5_Jaw_grp)
    mel.eval("""
    select -r BW5_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(BW5_Ctrl_grp)
    BW5_Ctrl = cmds.curve(name ="BW1_Ctrl_L", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.5,0.5,0.5)
    cmds.listRelatives(BW5_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(BW5_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(BW5_Ctrl), Color4)
    cmds.xform(BW5_Ctrl, translation=jnt_BW5_tuple)
    cmds.parent(BW5_Ctrl, BW5_Ctrl_grp)
    mel.eval("""
    select -r BW1_Ctrl_L ;
    setAttr "BW1_Ctrl_L.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(BW5_grp, Face_Grp)

    ############################ BW6
    BW6_grp = cmds.group(n="BW6_Grp", empty=True)
    cmds.xform(BW6_grp, translation=jnt_BW6_tuple)
    BW6_Jaw_grp = cmds.group(n="BW6_Jaw_grp", empty=True)
    cmds.xform(BW6_grp, translation=jnt_BW6_tuple)
    cmds.parent(BW6_Jaw_grp, BW6_grp)
    mel.eval("""
    select -r BW6_Jaw_grp ;
    FreezeTransformations;
    """)      
    cmds.CenterPivot()
    BW6_Ctrl_grp = cmds.group(n="BW6_Ctrl_grp", empty=True)
    cmds.xform(BW6_grp, translation=jnt_BW6_tuple)
    cmds.parent(BW6_Ctrl_grp, BW6_Jaw_grp)
    mel.eval("""
    select -r BW6_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(BW6_Ctrl_grp)
    BW6_Ctrl = cmds.curve(name ="BW2_Ctrl_L", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.5,0.5,0.5)
    cmds.listRelatives(BW6_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(BW6_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(BW6_Ctrl), Color4)
    cmds.xform(BW6_Ctrl, translation=jnt_BW6_tuple)
    cmds.parent(BW6_Ctrl, BW6_Ctrl_grp)
    mel.eval("""
    select -r BW2_Ctrl_L ;
    setAttr "BW2_Ctrl_L.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(BW6_grp, Face_Grp)

    ############################ BW7
    BW7_grp = cmds.group(n="BW7_Grp", empty=True)
    cmds.xform(BW7_grp, translation=jnt_BW7_tuple)
    BW7_Jaw_grp = cmds.group(n="BW7_Jaw_grp", empty=True)
    cmds.xform(BW7_grp, translation=jnt_BW7_tuple)
    cmds.parent(BW7_Jaw_grp, BW7_grp)
    mel.eval("""
    select -r BW7_Jaw_grp ;
    FreezeTransformations;
    """)      
    cmds.CenterPivot()
    BW7_Ctrl_grp = cmds.group(n="BW7_Ctrl_grp", empty=True)
    cmds.xform(BW7_grp, translation=jnt_BW7_tuple)
    cmds.parent(BW7_Ctrl_grp, BW7_Jaw_grp)
    mel.eval("""
    select -r BW7_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(BW7_Ctrl_grp)
    BW7_Ctrl = cmds.curve(name ="BW3_Ctrl_L", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.5,0.5,0.5)
    cmds.listRelatives(BW7_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(BW7_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(BW7_Ctrl), Color4)
    cmds.xform(BW7_Ctrl, translation=jnt_BW7_tuple)
    cmds.parent(BW7_Ctrl, BW7_Ctrl_grp)
    mel.eval("""
    select -r BW3_Ctrl_L ;
    setAttr "BW3_Ctrl_L.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(BW7_grp, Face_Grp)

    ############################ BW8
    BW8_grp = cmds.group(n="BW8_Grp", empty=True)
    cmds.xform(BW8_grp, translation=jnt_BW8_tuple)
    BW8_Jaw_grp = cmds.group(n="BW8_Jaw_grp", empty=True)
    cmds.xform(BW8_grp, translation=jnt_BW8_tuple)
    cmds.parent(BW8_Jaw_grp, BW8_grp)
    mel.eval("""
    select -r BW8_Jaw_grp ;
    FreezeTransformations;
    """)      
    cmds.CenterPivot()
    BW8_Ctrl_grp = cmds.group(n="BW8_Ctrl_grp", empty=True)
    cmds.xform(BW8_grp, translation=jnt_BW8_tuple)
    cmds.parent(BW8_Ctrl_grp, BW8_Jaw_grp)
    mel.eval("""
    select -r BW8_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(BW8_Ctrl_grp)
    BW8_Ctrl = cmds.curve(name ="BW4_Ctrl_L", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.5,0.5,0.5)
    cmds.listRelatives(BW8_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(BW8_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(BW8_Ctrl), Color4)
    cmds.xform(BW8_Ctrl, translation=jnt_BW8_tuple)
    cmds.parent(BW8_Ctrl, BW8_Ctrl_grp)
    mel.eval("""
    select -r BW4_Ctrl_L ;
    setAttr "BW4_Ctrl_L.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(BW8_grp, Face_Grp)

    ############################ LCL
    LCL_grp = cmds.group(n="LCL_Grp", empty=True)
    cmds.xform(LCL_grp, translation=jnt_LCL_tuple)
    LCL_Jaw_grp = cmds.group(n="LCL_Jaw_grp", empty=True)
    cmds.xform(LCL_grp, translation=jnt_LCL_tuple)
    cmds.parent(LCL_Jaw_grp, LCL_grp)
    mel.eval("""
    select -r LCL_Jaw_grp ;
    FreezeTransformations;
    """)     
    cmds.CenterPivot()
    LCL_Ctrl_grp = cmds.group(n="LCL_Ctrl_grp", empty=True)
    cmds.xform(LCL_grp, translation=jnt_LCL_tuple)
    cmds.parent(LCL_Ctrl_grp, LCL_Jaw_grp)
    mel.eval("""
    select -r LCL_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(LCL_Ctrl_grp)
    LCL_Ctrl = cmds.curve(name ="LCL_Ctrl_L", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.5,0.5,0.5)
    cmds.listRelatives(LCL_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(LCL_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(LCL_Ctrl), Color4)
    cmds.xform(LCL_Ctrl, translation=jnt_LCL_tuple)
    cmds.parent(LCL_Ctrl, LCL_Ctrl_grp)
    mel.eval("""
    select -r LCL_Ctrl_L ;
    setAttr "LCL_Ctrl_L.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(LCL_grp, Face_Grp)


    ############################################### set parent Mouth Ctrl
    mel.eval("""
    select -r Mid_Down_Lip_Ctrl ;
    select -tgl Neck|Mid_Up_Lip|Mid_Down_Lip ;
    parentConstraint -mo -weight 1;
             
    select -r Mid_Up_Lip_Ctrl ;
    select -tgl Neck|Mid_Up_Lip ;
    parentConstraint -mo -weight 1;
             
    select -r BW1_Ctrl_R ;
    select -tgl R_Between_1 ;
    parentConstraint -mo -weight 1;
             
    select -r BW2_Ctrl_R ;
    select -tgl R_Between_2 ;
    parentConstraint -mo -weight 1;
    
    select -r RCL_Ctrl_R ;
    select -tgl R_Corner_Lip ;
    parentConstraint -mo -weight 1;
             
    select -r BW3_Ctrl_R ;
    select -tgl R_Between_3 ;
    parentConstraint -mo -weight 1;
             
    select -r BW4_Ctrl_R ;
    select -tgl R_Between_4 ;
    parentConstraint -mo -weight 1;
             
    select -r BW1_Ctrl_L ;
    select -tgl L_Between_1 ;
    parentConstraint -mo -weight 1;
             
    select -r BW2_Ctrl_L ;
    select -tgl L_Between_2 ;
    parentConstraint -mo -weight 1;
             
    select -r LCL_Ctrl_L ;
    select -tgl L_Corner_Lip ;
    parentConstraint -mo -weight 1;
             
    select -r BW3_Ctrl_L ;
    select -tgl L_Between_3 ;
    parentConstraint -mo -weight 1;
        
    select -r BW4_Ctrl_L ;
    select -tgl L_Between_4 ;
    parentConstraint -mo -weight 1;
             """)
    
    ################################################################ set driven key mouth
    ###################### mouth translation #####################
    mel.eval("""
    setAttr "Mouth.translateZ" 0;
    setAttr "BW6_Ctrl_grp.translateY" 0;
    setAttr "MUL_Ctrl_grp.translateY" 0;
    setAttr "BW1_Ctrl_grp.translateY" 0;
    setAttr "BW2_Ctrl_grp.translateY" 0;
    setAttr "BW5_Ctrl_grp.translateY" 0;
    setAttr "LCL_Ctrl_grp.translateY" 0;
    setAttr "RCL_Ctrl_grp.translateY" 0;
    setAttr "BW7_Ctrl_grp.translateY" 0;
    setAttr "BW3_Ctrl_grp.translateY" 0;
    setAttr "BW8_Ctrl_grp.translateY" 0;
    setAttr "BW4_Ctrl_grp.translateY" 0;
    setAttr "MDL_Ctrl_grp.translateY" 0;
    setDrivenKeyframe -currentDriver Mouth.translateZ LCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW8_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW7_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW6_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW5_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ MDL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW4_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW3_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ RCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW2_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW1_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ MUL_Ctrl_grp.translateY;
                                
    setAttr "Mouth.translateZ" 2;
    setAttr "BW6_Ctrl_grp.translateY" -0.1;
    setAttr "MUL_Ctrl_grp.translateY" 0.1;
    setAttr "BW1_Ctrl_grp.translateY" 0.1;
    setAttr "BW2_Ctrl_grp.translateY" -0.1;
    setAttr "BW5_Ctrl_grp.translateY" 0.1;
    setAttr "LCL_Ctrl_grp.translateY" -0.5;
    setAttr "RCL_Ctrl_grp.translateY" -0.5;
    setAttr "BW3_Ctrl_grp.translateY" -1;
    setAttr "BW7_Ctrl_grp.translateY" -1;
    setAttr "BW4_Ctrl_grp.translateY" -1.25;
    setAttr "BW8_Ctrl_grp.translateY" -1.25;
    setAttr "MDL_Ctrl_grp.translateY" -1.3;
    setDrivenKeyframe -currentDriver Mouth.translateZ LCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW8_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW7_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW6_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW5_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ MDL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW4_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW3_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ RCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW2_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW1_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ MUL_Ctrl_grp.translateY;

    setAttr "Mouth.translateX" 0;
    setAttr "MUL_Ctrl_grp.translateX" 0;
    setAttr "LCL_Ctrl_grp.translateX" 0;
    setAttr "BW8_Ctrl_grp.translateX" 0;
    setAttr "BW7_Ctrl_grp.translateX" 0;
    setAttr "BW6_Ctrl_grp.translateX" 0;
    setAttr "BW5_Ctrl_grp.translateX" 0;
    setAttr "MDL_Ctrl_grp.translateX" 0;
    setAttr "BW4_Ctrl_grp.translateX" 0;
    setAttr "BW3_Ctrl_grp.translateX" 0;
    setAttr "RCL_Ctrl_grp.translateX" 0;
    setAttr "BW2_Ctrl_grp.translateX" 0;
    setAttr "BW1_Ctrl_grp.translateX" 0;
    setDrivenKeyframe -currentDriver Mouth.translateX LCL_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW8_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW7_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW6_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW5_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX MDL_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW4_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW3_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX RCL_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW2_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW1_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX MUL_Ctrl_grp.translateX;

    setAttr "Mouth.translateX" 1;
    setAttr "BW5_Ctrl_grp.translateX" 0.2;
    setAttr "BW8_Ctrl_grp.translateX" 0.2;
    setAttr "BW6_Ctrl_grp.translateX" 0.4;
    setAttr "BW7_Ctrl_grp.translateX" 0.4;
    setAttr "LCL_Ctrl_grp.translateX" 0.6;
    setAttr "BW1_Ctrl_grp.translateX" -0.2;
    setAttr "BW4_Ctrl_grp.translateX" -0.2;
    setAttr "RCL_Ctrl_grp.translateX" -0.2;
    setAttr "BW2_Ctrl_grp.translateX" -0.4;
    setAttr "BW3_Ctrl_grp.translateX" -0.4;
    setAttr "RCL_Ctrl_grp.translateX" -0.6;
    setDrivenKeyframe -currentDriver Mouth.translateX LCL_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW8_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW7_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW6_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW5_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX MDL_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW4_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW3_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX RCL_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW2_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW1_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX MUL_Ctrl_grp.translateX;
                
    setAttr "Mouth.translateX" -1;
    setAttr "BW5_Ctrl_grp.translateX" -0.3;
    setAttr "BW8_Ctrl_grp.translateX" -0.3;
    setAttr "BW6_Ctrl_grp.translateX" -0.6;
    setAttr "BW7_Ctrl_grp.translateX" -0.6;
    setAttr "LCL_Ctrl_grp.translateX" -0.9;
    setAttr "BW1_Ctrl_grp.translateX" 0.3;
    setAttr "BW4_Ctrl_grp.translateX" 0.3;
    setAttr "BW2_Ctrl_grp.translateX" 0.6;
    setAttr "BW3_Ctrl_grp.translateX" 0.6;
    setAttr "RCL_Ctrl_grp.translateX" 0.9;
    setDrivenKeyframe -currentDriver Mouth.translateX LCL_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW8_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW7_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW6_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW5_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX MDL_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW4_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW3_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX RCL_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW2_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW1_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX MUL_Ctrl_grp.translateX;

    selectKey -clear ;
    selectKey -add -k -f 0 -f 2 LCL_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 BW8_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 BW7_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 BW6_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 BW5_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 MDL_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 BW4_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 BW3_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 RCL_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 BW2_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 BW1_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 MUL_Ctrl_grp_translateY ;
    selectKey -add -k LCL_Ctrl_grp_translateX BW8_Ctrl_grp_translateX BW7_Ctrl_grp_translateX BW6_Ctrl_grp_translateX BW5_Ctrl_grp_translateX MDL_Ctrl_grp_translateX BW4_Ctrl_grp_translateX BW3_Ctrl_grp_translateX RCL_Ctrl_grp_translateX BW2_Ctrl_grp_translateX BW1_Ctrl_grp_translateX MUL_Ctrl_grp_translateX ;
    keyTangent -itt linear -ott linear;             

    setAttr "Mouth.translateZ" 0;
    setAttr "Mouth.translateX" 0;
             
    """)

    ######################## mouth reaction #########################
    mel.eval("""
    //---------------------------------------------------------------- happy             
    setAttr "Mouth.Happy" 0;
    setAttr "BW5_Ctrl_grp.translateY" 0;
    setAttr "BW8_Ctrl_grp.translateY" 0;
    setAttr "BW6_Ctrl_grp.translateY" 0;
    setAttr "BW7_Ctrl_grp.translateY" 0;
    setAttr "LCL_Ctrl_grp.translateY" 0;
    setAttr "BW4_Ctrl_grp.translateY" 0;
    setAttr "BW1_Ctrl_grp.translateY" 0;
    setAttr "BW2_Ctrl_grp.translateY" 0;
    setAttr "BW3_Ctrl_grp.translateY" 0;
    setAttr "RCL_Ctrl_grp.translateY" 0;             
    setDrivenKeyframe -currentDriver Mouth.Happy LCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW8_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW7_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW6_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW5_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy MDL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW4_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW3_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy RCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW2_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW1_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy MUL_Ctrl_grp.translateY;
                
    setAttr "Mouth.Happy" 10;
    setAttr "BW5_Ctrl_grp.translateY" 0.2;
    setAttr "BW8_Ctrl_grp.translateY" 0.2;
    setAttr "BW6_Ctrl_grp.translateY" 0.4;
    setAttr "BW7_Ctrl_grp.translateY" 0.4;
    setAttr "LCL_Ctrl_grp.translateY" 0.5;
    setAttr "BW4_Ctrl_grp.translateY" 0.2;
    setAttr "BW1_Ctrl_grp.translateY" 0.2;
    setAttr "BW2_Ctrl_grp.translateY" 0.4;
    setAttr "BW3_Ctrl_grp.translateY" 0.4;
    setAttr "RCL_Ctrl_grp.translateY" 0.5;
    setDrivenKeyframe -currentDriver Mouth.Happy LCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW8_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW7_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW6_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW5_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy MDL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW4_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW3_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy RCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW2_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW1_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy MUL_Ctrl_grp.translateY;

    //---------------------------------------------------------------- sad
    setAttr "Mouth.Sad" 0;
    setAttr "MUL_Ctrl_grp.translateY" 0;
    setAttr "LCL_Ctrl_grp.translateY" 0;
    setAttr "BW8_Ctrl_grp.translateY" 0;
    setAttr "BW7_Ctrl_grp.translateY" 0;
    setAttr "BW6_Ctrl_grp.translateY" 0;
    setAttr "BW5_Ctrl_grp.translateY" 0;
    setAttr "MDL_Ctrl_grp.translateY" 0;
    setAttr "BW4_Ctrl_grp.translateY" 0;
    setAttr "BW3_Ctrl_grp.translateY" 0;
    setAttr "RCL_Ctrl_grp.translateY" 0;
    setAttr "BW2_Ctrl_grp.translateY" 0;
    setAttr "BW1_Ctrl_grp.translateY" 0;
    setDrivenKeyframe -currentDriver Mouth.Sad LCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW8_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW7_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW6_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW5_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad MDL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW4_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW3_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad RCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW2_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW1_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad MUL_Ctrl_grp.translateY;

    setAttr "Mouth.Sad" 10;
    setAttr "BW5_Ctrl_grp.translateY" -0.2;
    setAttr "BW8_Ctrl_grp.translateY" -0.2;
    setAttr "BW6_Ctrl_grp.translateY" -0.4;
    setAttr "BW7_Ctrl_grp.translateY" -0.4;
    setAttr "LCL_Ctrl_grp.translateY" -0.5;
    setAttr "BW4_Ctrl_grp.translateY" -0.2;
    setAttr "BW1_Ctrl_grp.translateY" -0.2;
    setAttr "BW2_Ctrl_grp.translateY" -0.4;
    setAttr "BW3_Ctrl_grp.translateY" -0.4;
    setAttr "RCL_Ctrl_grp.translateY" -0.5;
    setDrivenKeyframe -currentDriver Mouth.Sad LCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW8_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW7_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW6_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW5_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad MDL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW4_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW3_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad RCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW2_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW1_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad MUL_Ctrl_grp.translateY;
    setAttr "Mouth.Happy" 0;
    setAttr "Mouth.Sad" 0;       
    """)


    ########################set driven key ######################
    mel.eval(""" 
    select -add R_Between_4_parentConstraint1 ;
    select -add R_Between_3_parentConstraint1 ;
    select -add R_Corner_Lip_parentConstraint1 ;
    select -add R_Between_2_parentConstraint1 ;
    select -add R_Between_1_parentConstraint1 ;
    select -add Mid_Down_Lip_parentConstraint1 ;
    select -add L_Between_4_parentConstraint1 ;
    select -add L_Between_3_parentConstraint1 ;
    select -add L_Corner_Lip_parentConstraint1 ;
    select -add L_Between_2_parentConstraint1 ;
    select -add L_Between_1_parentConstraint1 ;
    select -add Mid_Up_Lip_parentConstraint1 ;
    select -add Main_Face_Grp_dont_FreezeTransformations ;
    parent;                                                   
    """)

    mel.eval(""" 
        select -r L_Between_4 ;
        select -tgl L_Between_3 ;
        parent;
        select -r BW4_Ctrl_L ;
        select -add BW8_Ctrl_grp ;
        parent;
  
        select -cl ;
                """)  


def fixBuildFace(*arg):
    mel.eval("""
             
    select -r Main_Face_Grp_dont_FreezeTransformations R_Eye_Grp L_Eye_Grp Face_Ctrl_Grp ;
    doDelete;         

    parent;                 
    """)
    cmds.parent(Jnt_MUL, world=True)
    cmds.delete(Jnt_BW5)