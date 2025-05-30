import maya.cmds as cmds
import os
################################################################ import os
IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'Icons')

import VegaStudio_tools_animation.Functions.Animation.Tri3D_animationFuntions as Funcanim
reload(Funcanim)
import VegaStudio_tools_animation.Functions.Tri3D_functions as func
reload(func)
import VegaStudio_tools_animation.Functions.Animation.Tri3D_wdMK as MK
reload(MK)


############################################################################################### UI
def animWindow(*arg):                                                                                                                          
    if cmds.window("animWindow", exists=True):
        cmds.deleteUI("animWindow")
    anima = cmds.window("animWindow", title="tools_Animation Vega", sizeable=False, resizeToFitChildren=True, w=350)
    cmds.windowPref("animWindow", remove=True) 

    cmds.columnLayout("Key",adjustableColumn=True)
    cmds.rowColumnLayout("FunctionsKey", nc=5, w=350, backgroundColor=[0.284,0.352,0.352])
    cmds.symbolButton(image = IMAGE_PATH +"/ResetKey.png", w=70, h=25, c=Funcanim.resetKey)
    cmds.symbolButton(image = IMAGE_PATH +"/copyKey.png", w=70, h=25, c=Funcanim.copyKey)
    cmds.symbolButton(image = IMAGE_PATH +"/pasteKey.png", w=70, h=25, c=Funcanim.pasteKey)
    cmds.symbolButton(image = IMAGE_PATH +"/deleteKey.png", w=70, h=25, c=Funcanim.cutKey)
    cmds.symbolButton(image = IMAGE_PATH +"/Picker.png", w=70, h=25)

    cmds.setParent("Key")
    cmds.columnLayout("Graph", w=350)
    cmds.rowColumnLayout("FunctionsGraph", nc=10, w=350, backgroundColor=[0.284,0.352,0.352])
    cmds.textField("timeChangeField", w=60, placeholderText="Enter_",)
    cmds.symbolButton(image=IMAGE_PATH + "/moveKeyLe.png", w=30, h=30, c=Funcanim.moveKeyB)
    cmds.symbolButton(image=IMAGE_PATH + "/moveKeyRi.png", w=30, h=30, c=Funcanim.moveKeyF)
    cmds.button(l="MK_Pr", c=MK.wdMK)
    cmds.symbolButton(image=IMAGE_PATH + "/getGraphEditor.png", w=30, h=30, c=func.graphEditor)
    # cmds.symbolButton(image=IMAGE_PATH + "/play_hover.png", w=30, h=30, c=Funcanim.playButtonForward)

    cmds.setParent("Key")
    cmds.columnLayout("Graph_func", w=350)
    cmds.rowColumnLayout("FunctionsGraph_tools", nc=10, w=350, backgroundColor=[0.284,0.352,0.352])
    cmds.symbolButton(image = IMAGE_PATH +"/autoTangent.png", w=40, h=40, c=Funcanim.TangentsAuto)
    cmds.symbolButton(image = IMAGE_PATH +"/splineTangent.png", w=40, h=40, c=Funcanim.TangentsSpline)
    cmds.symbolButton(image = IMAGE_PATH +"/clampedTangent.png", w=40, h=40, c=Funcanim.TangentsClamped)
    cmds.symbolButton(image = IMAGE_PATH +"/linearTangent.png", w=40, h=40, c= Funcanim.TangentsLinear)
    cmds.symbolButton(image = IMAGE_PATH +"/flatTangent.png", w=40, h=40, c=Funcanim.TangentsFlat)
    cmds.symbolButton(image=IMAGE_PATH + "/postInfinityCycleOffset.png", w=40, h=40, c=Funcanim.postInfinityCycleOffset)
    cmds.symbolButton(image=IMAGE_PATH + "/preInfinityCycleOffset.png", w=40, h=40, c=Funcanim.preInfinityCycleOffset)
    cmds.showWindow(anima)