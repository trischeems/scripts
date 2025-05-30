import maya.cmds as cmds
import maya.mel as mel

def asFitResample(*args):
	cmds.warning("cc")


################################ Build IK Handle
def set_start_text(*args):
    selected_joint = cmds.ls(selection=True, type="joint")
    if selected_joint:
        cmds.textField("IK_Select_start", edit=True, text=selected_joint[0])

def set_end_text(*args):
    selected_joint = cmds.ls(selection=True, type="joint")
    if selected_joint:
        cmds.textField("IK_Select_end", edit=True, text=selected_joint[0])

def build_ik_handle(*args):
    start_joint = cmds.textField("IK_Select_start", query=True, text=True)
    end_joint = cmds.textField("IK_Select_end", query=True, text=True)
    
    if not start_joint or not end_joint:
        cmds.warning("Please select joint before build !")
        return
    
    ik_handle = cmds.ikHandle(startJoint=start_joint, endEffector=end_joint, solver="ikRPsolver")[0]
    cmds.rename(ik_handle, "IK_Handle_tools")
    cmds.setAttr("IK_Handle_tools.visibility", False)
    
    IK_Handle_Ctrl = cmds.curve(name = end_joint + "_Ctrl", d=1, 
                                p=[(1, 1, 1),(1,1,-1) ,(1, -1, -1) ,(1, -1, 1) ,(-1, -1, 1) ,
                                   (-1, 1, 1) ,(1, 1, 1) ,(1, -1, 1) ,(-1, -1, 1) ,
                                   (-1, -1, -1) ,(-1, 1, -1) ,(1, 1, -1) ,(1, -1, -1) ,
								   (-1, -1, -1) ,(-1, 1, -1) ,(-1, 1, 1)], 
                                        k = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    cmds.setAttr ('%s.overrideEnabled'%(IK_Handle_Ctrl), True)
    cmds.setAttr ('%s.overrideColor'%(IK_Handle_Ctrl), 13)
    cmds.delete(IK_Handle_Ctrl, constructionHistory=True)
    
    ctrl_grp = cmds.group(IK_Handle_Ctrl, name=end_joint + "_Ctrl_Grp", empty=True)
    cmds.parent(IK_Handle_Ctrl, ctrl_grp)
    
    cmds.matchTransform(ctrl_grp, end_joint)
    
    
    #cmds.parentConstraint(IK_Handle_Ctrl, ik_handle, maintainOffset=True)
    cmds.warning("Build done !")
    cmds.parent("IK_Handle_tools", IK_Handle_Ctrl)
    
def build_ik_spline(*args):
    start_joint = cmds.textField("IK_Select_start", query=True, text=True)
    end_joint = cmds.textField("IK_Select_end", query=True, text=True)
    
    if not start_joint or not end_joint:
        cmds.warning("Please select joint before build !")
        return
    
    ik_handle = cmds.ikHandle(startJoint=start_joint, endEffector=end_joint, solver="ikSplineSolver")[0]
    cmds.rename(ik_handle, "IK_Spline_tools")
    cmds.setAttr("IK_Spline_tools.visibility", False)
    
    IK_Handle_Ctrl = cmds.curve(name = end_joint + "_Ctrl", d=1, 
                                p=[(1, 1, 1),(1,1,-1) ,(1, -1, -1) ,(1, -1, 1) ,(-1, -1, 1) ,
                                   (-1, 1, 1) ,(1, 1, 1) ,(1, -1, 1) ,(-1, -1, 1) ,
                                   (-1, -1, -1) ,(-1, 1, -1) ,(1, 1, -1) ,(1, -1, -1) ,
								   (-1, -1, -1) ,(-1, 1, -1) ,(-1, 1, 1)], 
                                        k = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    cmds.setAttr ('%s.overrideEnabled'%(IK_Handle_Ctrl), True)
    cmds.setAttr ('%s.overrideColor'%(IK_Handle_Ctrl), 13)
    cmds.delete(IK_Handle_Ctrl, constructionHistory=True)
    
    ctrl_grp = cmds.group(IK_Handle_Ctrl, name=end_joint + "_Ctrl_Grp", empty=True)
    cmds.parent(IK_Handle_Ctrl, ctrl_grp)
    
    cmds.matchTransform(ctrl_grp, end_joint)
    
    
    #cmds.parentConstraint(IK_Handle_Ctrl, ik_handle, maintainOffset=True)
    cmds.warning("Build done !")
    cmds.parent("IK_Handle_tools", IK_Handle_Ctrl)