parent_joint = cmds.ls(sl = True)[0]
def get_joint_hierarchy(joint):
    joints = [joint]
    children = cmds.listRelatives(joint, children=True, type='joint') or []
    for child in children:
        joints.extend(get_joint_hierarchy(child))
    return joints

joint_hierarchy = get_joint_hierarchy(parent_joint)

positions = [cmds.xform(jnt, query=True, worldSpace=True, translation=True) for jnt in joint_hierarchy]
curve = cmds.curve(point=positions, degree=3, name=(parent_joint + "_CM"))