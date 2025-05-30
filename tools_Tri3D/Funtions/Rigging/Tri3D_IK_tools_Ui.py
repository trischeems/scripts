import maya.cmds as cmds 
import os

import tools_Tri3D.Funtions.Rigging.Tri3D_IK_tools_functions as tf
reload(tf)

IMP = os.path.join(os.path.dirname(__file__), "Icons")

def IK_tools(*arg):
    if cmds.window("IK_tools_wd", exists=True):
        cmds.deleteUI("IK_tools_wd")
    IK_tools_wd = cmds.window("IK_tools_wd", sizeable=False, wh=[500,180], title="Tri3D IK_tools", menuBar=True)
    cmds.windowPref("IK_tools_wd", remove=True, h=500)

    main_layout = cmds.formLayout()
    cmds.image(image=IMP + "/bg.jpg", w=500)
    # cmds.frame("ReSample", w=150, h=150)
    resample_button = cmds.symbolButton(image=IMP + "/resample.png", w=110, h=35, c=tf.asFitResample)

    ######### build IK ################
    IK_button = cmds.symbolButton(image=IMP + "/IK_Icons.png", w=60, h=60)
    Select_IK_start= cmds.symbolButton(image=IMP + "/Select_start.png", w=60, h=30, c=tf.set_start_text)
    Select_IK_end= cmds.symbolButton(image=IMP + "/Select_end.png", w=60, h=30, c=tf.set_end_text)
    Build_IK_handle= cmds.symbolButton(image=IMP + "/Build_handle.png", w=80, h=30, c=tf.build_ik_handle) 
    Build_IK_Spline= cmds.symbolButton(image=IMP + "/Build_spline.png", w=80, h=30, c=tf.build_ik_spline) 
    IK_textField_start = cmds.textField("IK_Select_start", w=150, h=25, editable=False)
    IK_textField_end = cmds.textField("IK_Select_end", w=150, h=25, editable=False)
    cmds.radioCollection("IK_Build")
    # rd_IK_Handle = cmds.radioButton(l="IK Handle", w=75)
    # rd_IK_Spline = cmds.radioButton("rd_IK_Spline",l="IK Spline", w=75 )
    ######### build FK ################
    FK_button= cmds.symbolButton(image=IMP + "/FK_Icons.png", w=60, h=60)
    Select_FK= cmds.symbolButton(image=IMP + "/Select.png", w=60, h=30)
    Build_FK= cmds.symbolButton(image=IMP + "/Build.png", w=60, h=30) 
    FK_textField = cmds.textField("FK_Select_joint", w=150, h=25, editable=False)


######### form layout ################
    cmds.formLayout(main_layout, edit=True, attachForm=[
        #### Button 
        (resample_button, 'top', 10),
        (resample_button, 'left', 290),


        #### Build IK
        (IK_button, 'top', 13),
        (IK_button, 'left', 5),   

        (IK_textField_start, 'top', 15),
        (IK_textField_start, 'left', 120),  

        (Select_IK_start, 'top', 12),
        (Select_IK_start, 'left', 60),  

        (Select_IK_end, 'top', 41),
        (Select_IK_end, 'left', 60), 

        (IK_textField_end, 'top', 43),
        (IK_textField_end, 'left', 120), 

        (Build_IK_handle, 'top', 70),
        (Build_IK_handle, 'left', 118), 

        (Build_IK_Spline, 'top', 70),
        (Build_IK_Spline, 'left', 195), 

        # (rd_IK_Handle, 'top', 76),
        # (rd_IK_Handle, 'left', 120), 

        # (rd_IK_Spline, 'top', 76),
        # (rd_IK_Spline, 'left', 200), 


        ####### Build FK
        (FK_button, 'top', 110),
        (FK_button, 'left', 5),

        (FK_textField, 'top', 113),
        (FK_textField, 'left', 120),  

        (Select_FK, 'top', 110),
        (Select_FK, 'left', 60),  

        (Build_FK, 'top', 136),
        (Build_FK, 'left', 60)


        ])

    cmds.showWindow(IK_tools_wd)


            