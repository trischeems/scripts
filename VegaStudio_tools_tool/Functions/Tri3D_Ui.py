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
import pymel.core as pm

# link file funtions
import VegaStudio_tools_animation.Functions.Tri3D_functions as func
reload(func)
import VegaStudio_tools_animation.Functions.Animation.Tri3D_animation as anim
reload(anim)
import VegaStudio_tools_animation.Functions.Animation.Tri3D_animationFuntions as Funcanim
reload(Funcanim)


IMAGE_PATH = os.path.join(os.path.dirname(__file__), "Icons")

################################################################ window functions
def createUI():
    if cmds.window("triWin", exists=True):
        cmds.deleteUI("triWin")


    triWin = cmds.window("triWin", title="Vega Animation", sizeable=False, menuBar=True, resizeToFitChildren=True, w=300)
    cmds.windowPref("triWin", remove=True, w=300)
    cmds.menu(l="Modify")
    cmds.menuItem(l="Freeze Transformations", image= IMAGE_PATH + "/FreezeTransform.png", c=func.freezeOptions )



################################################################ UI UX
################################################################
    main_layout = cmds.columnLayout(adjustableColumn=True)
    tab_layout_main = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)



################################################################ Animation
################################################################
    cmds.setParent(tab_layout_main)
    cmds.columnLayout("Animation", w=300)
    cmds.setParent("Animation")
    cmds.frameLayout("Graph", w=300)
    cmds.rowColumnLayout("FunctionsKey_Layout", nc=5, w=300, backgroundColor=[0.284,0.352,0.352])
    cmds.symbolButton(image = IMAGE_PATH +"/ResetKey.png", w=60, h=22, c=Funcanim.resetKey)
    cmds.symbolButton(image = IMAGE_PATH +"/copyKey.png", w=60, h=22, c=Funcanim.copyKey)
    cmds.symbolButton(image = IMAGE_PATH +"/pasteKey.png", w=60, h=22, c=Funcanim.pasteKey)
    cmds.symbolButton(image = IMAGE_PATH +"/deleteKey.png", w=60, h=22, c=Funcanim.cutKey)
    cmds.symbolButton(image = IMAGE_PATH +"/Picker.png", w=60, h=22)

    cmds.setParent("Animation")
    cmds.rowColumnLayout("FunctionsGraph_Layout", nc=10, w=300, backgroundColor=[0.284,0.352,0.352])
    cmds.textField("timeChangeField", w=50, placeholderText="Enter_")
    cmds.symbolButton(image = IMAGE_PATH + "/moveKeyLe.png", w=30, h=30, c=Funcanim.moveKeyBUi)
    cmds.symbolButton(image = IMAGE_PATH + "/moveKeyRi.png", w=30, h=30, c=Funcanim.moveKeyFUi)
    cmds.symbolButton(image = IMAGE_PATH +"/autoTangent.png", w=30, h=30, c=Funcanim.TangentsAuto)
    cmds.symbolButton(image = IMAGE_PATH +"/splineTangent.png", w=30, h=30, c=Funcanim.TangentsSpline)
    cmds.symbolButton(image = IMAGE_PATH +"/clampedTangent.png", w=30, h=30, c=Funcanim.TangentsClamped)
    cmds.symbolButton(image = IMAGE_PATH +"/linearTangent.png", w=30, h=30, c=Funcanim.TangentsLinear)
    cmds.symbolButton(image = IMAGE_PATH +"/flatTangent.png", w=30, h=30, c=Funcanim.TangentsFlat)
    cmds.symbolButton(image = IMAGE_PATH + "/getGraphEditor.png", w=30, h=30, c=func.graphEditor)

    cmds.setParent("Animation")
    cmds.rowColumnLayout("Layer8", w=300, nc=1, backgroundColor=[0.284,0.352,0.352])
    cmds.button(l="Detach Window", w=300, c=anim.animWindow)
    cmds.button(l="Group", w=300, c=func.groupobj)
    cmds.button(l="DemoRig", w=300, c=func.DemoRig)

    ################################################################ move key pro
    cmds.setParent("Animation")
    cmds.frameLayout("Move Key Pro", w=300, cll=True, cl=False)
    cmds.columnLayout("Main_Layout", w=300, adj= 1)
    cmds.rowColumnLayout("Move_Pro", w=300, nc=4)
    cmds.button(l= 'Select', c= Funcanim.selectCtrl, w=50)
    cmds.textField('selectCtrl', w= 250, ed= 0, placeholderText="Select_Controller")
    cmds.button(l= 'Select', c= Funcanim.selectAll, w=50)
    cmds.textField('selectAll', w= 100, ed= 0, placeholderText="Select_Ctrl")

    cmds.setParent("Main_Layout")
    cmds.checkBox('UseSEK', l= 'On_Start_End', v= 0, cc= Funcanim.useSEK)
    cmds.rowColumnLayout("Button2", w=300, nc=4)
    cmds.button(l= 'Start Key', c= Funcanim.butt_startKey, w=50)
    cmds.textField('startKey', w= 100, ed= 0, tx= '')
    cmds.button(l= 'End Key', c= Funcanim.butt_endKey, w=50)
    cmds.textField('endKey', w= 100, ed= 0, tx= '')
    cmds.setParent("Main_Layout")
    cmds.intSliderGrp('numbersKey', f= 1, min= 1, v= 1, max= 999999)
    cmds.setParent("Main_Layout")
    cmds.rowColumnLayout("button select", w=300, nc=2)
    cmds.button('moveBackward', l= '<<< Move Back', c= Funcanim.butt_moveBackward, w=150)
    cmds.button('moveForward', l= 'Move Go >>>', c= Funcanim.butt_moveForward, w=150)


################################################################ copy right by Tri 3D
################################################################
    cmds.setParent(tab_layout_main)
    cmds.columnLayout("About", w=300)
    cmds.frameLayout("Click to button :", w=300)
    cmds.rowColumnLayout("Layer6", w=300, nc=5)
    # cmds.symbolButton(image=IMAGE_PATH +"/LogoGumroad.jpg", w=60, h=60, c=func.openWebMessFB)
    cmds.text("                   ")
    cmds.symbolButton(image=IMAGE_PATH +"/gumroad.png", w=60, h=60, c=func.openWebgumroad)
    cmds.text("                   ")

    cmds.symbolButton(image=IMAGE_PATH +"/Gmail_Icon.png", w=60, h=60, c=func.openGmail)
    cmds.setParent("About")
    cmds.rowColumnLayout("Layer7", w=300, nc=3)
    cmds.button("Copy   ", w=100, c=func.copyEmail)
    cmds.textField("Email", w=199, text="info.tri3d@gmail.com")
    cmds.setParent("About")
    cmds.columnLayout("duongdungrong", w=300)
    # cmds.button(l="I love VN", w=300, h=30, backgroundColor=[1,1,1])
    cmds.button(l="Update", w=300, h=30, backgroundColor=[1,0.774,0.108])
    cmds.button(l="Course Rigging", w=300, h=30, backgroundColor=[1,0.774,0.108], c=func.openWebRiggingCause)
    cmds.image(image=IMAGE_PATH +"/LogoVega.jpg", w=300)
    cmds.setParent(tab_layout_main)

    cmds.showWindow(triWin)



createUI()






