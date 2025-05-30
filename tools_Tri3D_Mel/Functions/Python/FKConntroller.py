import maya.cmds as cmds
# from Tri 3D
def create_controllers_from_selection():
    selected_objects = cmds.ls(selection=True)
    if not selected_objects:
        cmds.warning("Not Object Selected!")
        return

    parent_relationships = {}

    controllers = []
    for obj in selected_objects:
        # from Tri 3D
        # pos = cmds.xform(obj, query=True, translation=True, worldSpace=True)
        controller = cmds.circle(name=obj+"_Ctrl", normalX = 90)[0] 
        cmds.makeIdentity(controller, apply = True, rotate = True)
        cmds.setAttr(controller + ".overrideEnabled", 1)
        cmds.setAttr(controller + ".overrideRGBColors",1)
        cmds.setAttr(controller + ".overrideColorRGB", 1 ,1 ,0)
        group = cmds.group(n =obj + "_grp", empty = True)
        cmds.parent(controller, group)
        # cmds.xform(group, translation=pos, worldSpace=True)  # Set controller position
        cmds.matchTransform(group, obj)
        controllers.append(controller)
        
        parent = cmds.listRelatives(obj, parent=True)
        if parent:
            parent_relationships[obj] = parent[0]

    for obj, parent in parent_relationships.items():
        if obj in selected_objects and parent in selected_objects:
            cmds.parent(obj+"_grp", parent+"_Ctrl")

    for obj, controller in zip(selected_objects, controllers):
        cmds.parentConstraint(controller, obj, maintainOffset=True)

    cmds.select(cl=True)
    cmds.warning("Success!")


create_controllers_from_selection()
