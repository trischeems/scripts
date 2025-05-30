import maya.cmds as cmds

def returnValue():
    loft = ""
    sel = cmds.ls(selection=True, long=True) or []
    for obj in sel:
        inputs_transform = cmds.listConnections(obj, s=True, d=False) or []
        shapes = cmds.listRelatives(obj, shapes=True, fullPath=True) or []
        for shape in shapes:
            inputs_shape = cmds.listConnections(shape, s=True, d=False) or []
            for inp in set(inputs_shape):
                loft = inp
    return loft
