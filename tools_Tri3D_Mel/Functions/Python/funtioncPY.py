import maya.cmds as cmds

selection = cmds.ls(sl=True)

rs_objects = []
rf_objects = []
rm_objects = []

for obj in selection:
    if obj.startswith("Rs"): 
        rs_objects.append(obj)
    elif obj.startswith("Rf"): 
        rf_objects.append(obj)
    elif obj.startswith("Rm"): 
        rm_objects.append(obj)

if rf_objects and rs_objects and rm_objects:
    parent = rf_objects[0]
    middle = rs_objects[0]
    child = rm_objects[0]

    cmds.parentConstraint(parent, middle, child, mo=True)

