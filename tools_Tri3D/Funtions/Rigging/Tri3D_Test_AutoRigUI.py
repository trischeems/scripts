import maya.cmds as cmds
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
import os
import maya.mel as mel
import pymel.core as pm


# link file funtions
import tools_Tri3D.Funtions.Tri3D_functions as func
reload(func)
import tools_Tri3D.Funtions.Rigging.Tri3D_rigFunctions as Rig
reload(Rig)
import tools_Tri3D.Funtions.Curve.CurveBasic as Cur
reload(Cur)
import tools_Tri3D.Funtions.Rigging.Tri3D_Test_AutoRig as AutoRig
reload(AutoRig)

#IMAGE_PATH = os.path.join(os.path.dirname(__file__), "Icons")

################################################################ window functions
def createUI():
    if cmds.window("test", exists=True):
        cmds.deleteUI("test")


    test = cmds.window("test", title="tools_Tri3D Auto Rig", sizeable=False, resizeToFitChildren=True, w=300)
    cmds.windowPref(test, remove=True, w=400)

    ############################################################

    main_layout = cmds.columnLayout(adjustableColumn=True)

    
    cmds.setParent(main_layout)
    cmds.rowColumnLayout("test_Button", w=200, nc=4)
    cmds.text(l="", w=30)
    cmds.button(l="Create", w=100, c=AutoRig.execute_mel_script)
    cmds.text(l="", w=30)
    cmds.button(l="Mirror", w=100, c=AutoRig.mirrorAnddeleteRoot)
    cmds.text(l="", w=30)
    cmds.text(l="", w=30)
    cmds.text(l="", w=30)
    cmds.text(l="", w=30)
    cmds.text(l="", w=30)
    cmds.button(l="IK", w=100, c=AutoRig.createIK)
    cmds.text(l="", w=30)
    cmds.button(l="FK", w=100, c=AutoRig.mirrorAnddeleteRoot)




    cmds.showWindow(test)
createUI()