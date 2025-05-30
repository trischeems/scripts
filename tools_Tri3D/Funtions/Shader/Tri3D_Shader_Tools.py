import maya.cmds as cdms
import maya.mel as mel


## Duplicate Shader with connect work #########################################
def duplicateShaderWithConnect(*arg):
    mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "duplicateWithConnections");')

def duplicateShaderSingle(*arg):
    mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "duplicateShadingNetwork");')