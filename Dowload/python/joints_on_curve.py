import maya.cmds as cmds

def transferweightUI():
    clsjntwin = cmds.window( title="Add InBetween Joints", iconName='inBetween Joints', widthHeight=(250,110),s=0)
    cmds.columnLayout( adjustableColumn=True )
    addcurvefeild = cmds.textField("loadcurve",ed=0)
    curvefeild = cmds.button( label='Add Curve' ,c = addcurve)
    numofjnt = cmds.textField("numberofjointfeild",pht="Number of Joints")
    gobtn = cmds.button( label='Run',c=inbetweenjoints)
    closebtn = cmds.button( label='Close', command=('cmds.deleteUI(\"' + clsjntwin + '\", window=True)') )
    cmds.showWindow(clsjntwin)
    
def inbetweenjoints(*args):
    ladcurve=cmds.textField("loadcurve",q=True,text=True)
    numberofjoints=cmds.textField("numberofjointfeild",q=True,text=True)
    curveinfo=cmds.arclen(ladcurve,ch=1)
    curvelength=cmds.getAttr(curveinfo + ".arcLength")
    getUvalue=float(1.0/(int(numberofjoints)-1))
    newvalue=0
    cmds.select(cl=1)
    newjntstart=cmds.joint(n= "joint10")
    pathanimationstart=cmds.pathAnimation(newjntstart,c=ladcurve)
    startctrl=cmds.circle(n=newjntstart + "_Ctrl",r=0.5,nr=(0,1,0))
    startctrlgrp=cmds.group(n=newjntstart + "Ctrl_Grp")
    cmds.delete(cmds.pointConstraint(newjntstart,startctrlgrp))
    cmds.parentConstraint(startctrl,newjntstart,mo=1)
    cmds.select(cl=1)
    newjntstartlist=[]
    newgrpstartlist=[]
    newctrlstartlist=[]
    for eachnumberofjoints in range(1,int(numberofjoints)):
        newjnt=cmds.joint(n= "joint1" + str(eachnumberofjoints))
        newjntstartlist.append(newjnt)
        circlectrl=cmds.circle(n=newjnt + "_Ctrl",r=0.5,nr=(0,1,0))
        ctrlgrp=cmds.group(n=newjnt + "Ctrl_Grp")
        newctrlstartlist.append(circlectrl)
        newgrpstartlist.append(ctrlgrp)
        pathanimation=cmds.pathAnimation(newjnt,c=ladcurve)
        newvalue +=getUvalue
        cmds.setAttr(pathanimation + ".uValue",newvalue)
        cmds.delete(cmds.ls("addDoubleLinear*"))
        cmds.delete(pathanimation)
        cmds.setAttr(newjnt + ".jointOrientX",0)
        cmds.setAttr(newjnt + ".jointOrientY",0)
        cmds.setAttr(newjnt + ".jointOrientZ",0)
        cmds.delete(cmds.pointConstraint(newjnt,ctrlgrp))
        cmds.parentConstraint(circlectrl,newjnt,mo=1)
        cmds.select(clear=1)
    cmds.parent(newjntstartlist[0],newjntstart)
    cmds.parent(newgrpstartlist[0],startctrl)
    for each in range(0,len(newjntstartlist)-1):
        cmds.parent(newjntstartlist[each+1],newjntstartlist[each])
        cmds.parent(newgrpstartlist[each+1],newctrlstartlist[each])
    cmds.select(newjntstart,hi=1)
    cmds.joint(e=1,oj="xyz",secondaryAxisOrient="xup",zso=1)
    cmds.setAttr(newjntstartlist[-1] + ".jointOrientX",0)
    cmds.setAttr(newjntstartlist[-1] + ".jointOrientY",0)
    cmds.setAttr(newjntstartlist[-1] + ".jointOrientZ",0)

def addcurve(*args):
    lodcurve=cmds.ls(selection=1)
    addcurve =cmds.textField("loadcurve", edit=True, text=lodcurve[0])
    
transferweightUI()