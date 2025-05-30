import maya.cmds as cmds
# from Tri 3D
parent_joint = cmds.ls(sl = True)[0]

ctrl_move = parent_joint + "_ctrl_main"
grp_path = parent_joint + "_Path_grp"
node_path = parent_joint + "_node"
loc_path_line = parent_joint + "_Loc_Path_Line"
n_parent = parent_joint + "Path_parent"
n_orient = parent_joint + "Path_orient"
pathCtrl = parent_joint + "_Path_Ctrl"
bsc_orient = parent_joint + "_bsc_orient_bake"

jointCtrl = []
jointEnd = []

cmds.setAttr((parent_joint + ".v"), 0)
cmds.setAttr((loc_path_line + ".v"), 0)
cmds.addAttr(parent_joint, ln = "Path", min = 0, max = 100, keyable = True)
def get_joint_hierarchy(joint):
    joints = [joint]
    children = cmds.listRelatives(joint, children=True, type='joint') or []
    for child in children:
        joints.extend(get_joint_hierarchy(child))
    return joints

joint_hierarchy = get_joint_hierarchy(parent_joint)

positions = [cmds.xform(jnt, query=True, worldSpace=True, translation=True) for jnt in joint_hierarchy]

groupMain = cmds.group(n = (parent_joint + "Main_grp"), empty = True)
groupLoc = cmds.group(n = (parent_joint + "_Loc"), empty = True)
groupLockAttr = cmds.group(n = (parent_joint + "_Lock_Attr_Ctrl"), empty = True)

cmds.parent(parent_joint, groupMain)
cmds.parent(ctrl_move, groupLoc)
cmds.parent(groupLoc, groupMain)
cmds.parent(grp_path, groupMain)
cmds.parent(loc_path_line, groupMain)
cmds.parent(groupLockAttr, groupMain)
cmds.matchTransform(groupLoc, parent_joint)

for obj in joint_hierarchy :
    group = cmds.group(obj, n = (obj + "_grp"), empty = True)
    ctrl = cmds.circle(obj, n = (obj + "_ctrl"), normalX = 90)
    # cmds.deleteHistory(ctrl, apply=True)
    cmds.parent(ctrl, group)
    cmds.matchTransform(group, obj)
    # cmds.parentConstraint(ctrl, obj)
    cmds.parent(group, ctrl_move)
    jointCtrl.append(ctrl)
    cmds.refresh()

# for i in range(len(positions) - 1):
#     current_pos = positions[i]
#     next_pos = positions[i + 1]
#     mid_pos = [(current_pos[j] + next_pos[j]) / 2 for j in range(3)]
#     new_positions.extend([current_pos, mid_pos])

# new_positions.append(positions[-1])
curve = cmds.curve(point=positions, degree=3, name=(parent_joint + "_CM"))

cvs = cmds.ls(curve + '.cv[*]', flatten=True)
num_E = len(jointCtrl)
if num_E > 3:
    cmds.addAttr(ctrl_move, ln = "Path", min = 0, max = (num_E - 3), keyable = True)
    for i, cv in enumerate(cvs):
        cmds.select(cv)
        cluster = cmds.cluster(name=("scl_" + str(i)))[1]
        cmds.setAttr((cluster + ".v"), 0)
        cmds.refresh()
        if i < len(jointCtrl):
            cmds.parent(cluster, jointCtrl[i])
    cmds.parent(curve, groupMain)
    cmds.select(cl= True)
    cmds.pathAnimation(loc_path_line,stu=0, etu=1, fa='z', ua='y', c = curve)
    namePath = cmds.rename("motionPath1", (parent_joint + "_mtp"))

    cmds.setAttr((namePath + ".uValue"), num_E)
    cmds.connectAttr((ctrl_move + ".Path"), (namePath + ".uValue"), f = True)
    cmds.delete("motionPath1_uValue")
    for obj in jointCtrl:
        cmds.addAttr(obj, ln = "Path", min = 0, max = (num_E - 3), proxy = (ctrl_move + ".Path"), keyable = True)
        cmds.addAttr(obj, ln = "OrientConstraint", min = 0, max = 1, proxy = (ctrl_move + ".OrientConstraint"), dv = 1, keyable = True)
    cmds.select(curve)
    cmds.setAttr((namePath + ".rx"), lock = True)

    cmds.connectAttr((groupLockAttr + ".tx"), (curve + ".tx"), f = True)
    cmds.connectAttr((groupLockAttr + ".ty"), (curve + ".ty"), f = True)
    cmds.connectAttr((groupLockAttr + ".tz"), (curve + ".tz"), f = True)
    cmds.connectAttr((groupLockAttr + ".rx"), (curve + ".rx"), f = True)
    cmds.connectAttr((groupLockAttr + ".ry"), (curve + ".ry"), f = True)
    cmds.connectAttr((groupLockAttr + ".rz"), (curve + ".rz"), f = True)
    cmds.connectAttr((groupLockAttr + ".sx"), (curve + ".sx"), f = True)
    cmds.connectAttr((groupLockAttr + ".sy"), (curve + ".sy"), f = True)
    cmds.connectAttr((groupLockAttr + ".sz"), (curve + ".sz"), f = True)

    cmds.addAttr(pathCtrl, ln = "Path", min = 0, max = (num_E - 3), proxy = (ctrl_move + ".Path"), keyable = True)
    cmds.parentConstraint(loc_path_line,grp_path, sr = ["x","y","z"], n = n_parent)
    cmds.orientConstraint(loc_path_line,grp_path, n = n_orient)

    cmds.connectAttr((ctrl_move + ".OrientConstraint"), (bsc_orient + ".blender"), f = True)
    cmds.connectAttr((n_orient + ".constraintRotateX"), (bsc_orient + ".color1R"), f = True)
    cmds.connectAttr((n_orient + ".constraintRotateY"), (bsc_orient + ".color1G"), f = True)
    cmds.connectAttr((n_orient + ".constraintRotateZ"), (bsc_orient + ".color1B"), f = True)
    
    cmds.connectAttr((bsc_orient + ".outputR"), (grp_path + ".rx"), f = True)
    cmds.connectAttr((bsc_orient + ".outputG"), (grp_path + ".ry"), f = True)
    cmds.connectAttr((bsc_orient + ".outputB"), (grp_path + ".rz"), f = True)

    print("Done")


