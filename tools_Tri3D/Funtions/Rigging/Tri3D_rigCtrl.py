import maya.mel as mel
import maya.cmds as cmds



selected = False
def main(*args):
    global selected
    if not selected:
        cmds.select("Main_Controller", replace=True)
        selected = True
        cmds.button("Main_Ctrl", edit=True, backgroundColor=(1, 1, 0))
        cmds.scriptJob(event=("SelectionChanged", main))
    else:
        cmds.select(clear=True)
        selected = False
        cmds.button("Main_Ctrl", edit=True, backgroundColor=[0.284,0.352,0.352])

def Root(*args):
    global selected
    if not selected:
        cmds.select("Root_Ctrl", replace=True)
        selected = True
        cmds.button("Root_Ctrl", edit=True, backgroundColor=(1, 1, 0))
    else:
        cmds.select(clear=True)
        selected = False
        cmds.button("Root_Ctrl", edit=True, backgroundColor=[0.284,0.352,0.352])


   










    






