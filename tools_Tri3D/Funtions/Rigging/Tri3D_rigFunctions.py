import pymel.core as pm
import maya.cmds as cmds
import os

from eyeLidSetupTool import EyeLidSetupUI

Tools = os.path.join(os.path.dirname(__file__), "Controller")

ctrlColor = 'ctrlColor'
########################################################################
########################################################################
toolWindowName='DynamicWheel'
toolLabel='Dynamic Wheel'


checkBox1='checkAutoName' 
checkBox2='checkAutoPosition' 
checkBox3='checkAutoBind'
checkBox4='checkAutoCons' 

optionMenu1='optionWheelDirection'
windowwidth = []
windowheight = []
dwidth = []
dheight = []
i=[]
o=[]
sel=[]
dyngrp = 'SystemDY'
createorder = ['_GRP','_Ctrl','_dyn_JNT','_dyn_driver_RG','_dyn_driven_PC','_dyn_bake_ADL']
typeorder = ['transform','joint','joint','transform','pointConstraint','addDoubleLinear']
clist = [] 
ctrlattr = 'dynamics_enable', 'link_dynamics_bake', 'link_dynamics_preroll'
drvnattr = 'cacheTranslate'
hideattr = ['.tx','.ty','.tz','.ry','.rz','.sx','.sy','.sz','.v','.radi']
direction = []
up = []
rxyz = []

def changestate(*arg):
    if pm.textField('textFieldName', query=1, enable=1):
        pm.textField('textFieldName', edit=1, enable=0)
    else:
        pm.textField('textFieldName', edit=1, enable=1)
    if pm.checkBox(checkBox3, query=1, enable=1):
        pm.checkBox(checkBox3, edit=1, enable=0)
        pm.checkBox(checkBox3, edit=1, v=0)
    else:
        pm.checkBox(checkBox3, edit=1, enable=1)
    if pm.checkBox(checkBox4, query=1, enable=1):
        pm.checkBox(checkBox4, edit=1, enable=0)
        pm.checkBox(checkBox4, edit=1, v=0)
    else:
        pm.checkBox(checkBox4, edit=1, enable=1)

def changestatebind(*arg):
    if pm.checkBox(checkBox4, query=1, v=1):
        pm.checkBox(checkBox4, edit=1, v=0)
    
def changestatecons(*arg):
    if pm.checkBox(checkBox3, query=1, v=1):
        pm.checkBox(checkBox3, edit=1, v=0)

def createDynamicWheel(*arg):
    global sel,dyngrp,createorder,typeorder,clist,ctrlattr,drvnattr,sel,hideattr,ryxz
    direction = pm.optionMenu(optionMenu1, q=1, v=1)
    if direction == 'x':
        rxyz = [0,90,0]
    elif direction == 'y':
        rxyz = [-90,0,0]
    elif direction == 'z':
        rxyz = [0,0,0]
    elif direction == '-x':
        rxyz = [0,-90,0]
    elif direction == '-y':
        rxyz = [90,0,0]
    elif direction == '-z':
        rxyz = [0,180,0]
    sel = pm.ls(os=1,ap=1)
    selpos = sel 
    if pm.checkBox('checkAutoName',q=1,v=1)==0:
        if not pm.textField('textFieldName',q=1,tx=1)=='':
            sel = [pm.textField('textFieldName',q=1,tx=1)]
            dmynode = pm.createNode('mesh',n=sel[0]+'Shape')
            dmypar = pm.rename(pm.listRelatives(dmynode,p=1),sel[0])
        else:
            sel = []
    else:
        sel = pm.ls(os=1,ap=1)
    pm.select(cl=1)
    if not pm.objExists(dyngrp):
        pm.group(n=dyngrp,w=1)
    for i in sel:
        try:
            par = pm.listRelatives(i,p=1)[0]
            parsuffix = par.split('_')
            parsuffix.reverse()
        except:
            parsuffix = ['null']
        try:
            n = i.split('_')
            del n[len(n)-1]
            ii = '_'.join(n)
        except:
            ii=i
        clist = []
        if pm.objExists(i+'_Dyn_SETUP'):
            pm.delete(i+'_Dyn_SETUP')
        for o in range(len(createorder)):
            if pm.objExists(i+createorder[o]):
                pm.delete(i+createorder[o])
            if o == 0 and parsuffix[0] == 'GRP':
                clist.append(par)
                dupgrp = pm.rename(pm.duplicate(par),par+'_Dup')
                pm.rename(pm.listRelatives(dupgrp)[0],dupgrp.replace('GRP','Ctrl'))
                pm.parent(dupgrp,w=1)
                pm.parent(par,w=1)
                pm.setAttr(par+'.t',0,0,0)
                pm.setAttr(par+'.r',0,0,0)
            elif o == 1 and (pm.objectType(i,i='joint') or pm.objectType(pm.listRelatives(i)[0],i='nurbsCurve')):
                clist.append(i)
                pm.parent(i,w=1)
                pm.setAttr(i+'.t',0,0,0)
                pm.setAttr(i+'.r',0,0,0)
            elif o == 2 and (pm.objectType(i,i='joint') or pm.objectType(pm.listRelatives(i)[0],i='nurbsCurve')):
                clist.append(pm.createNode(typeorder[o], n=i+createorder[o]))
            else:
                clist.append(pm.createNode(typeorder[o], n=i+createorder[o]))
        clist.append(pm.spaceLocator(n=i+'_1_Loc'))
        clist.append(pm.spaceLocator(n=i+'_2_Loc'))
        bbox = pm.exactWorldBoundingBox(i)

        if pm.objectType(i,i='joint') or pm.objectType(i,i='nurbsCurve'):
            posctrl = pm.xform(dupgrp,q=1,ws=1,rp=1)
            pm.setAttr(clist[6]+'.ty',posctrl[1])
        elif pm.checkBox('checkAutoName',q=1,v=1)==0:
            pm.setAttr(clist[6]+'.ty',0)
            pm.setAttr(clist[7]+'.ty',0.5)
        else:
            pm.setAttr(clist[6]+'.ty',bbox[1])
            pm.setAttr(clist[7]+'.ty',(bbox[4]+bbox[1])/2)
        distnode = pm.createNode('distanceDimShape', n=i+'_DisShape')
        clist.append(pm.rename(pm.listRelatives(distnode,p=1)[0],i+'_Dis'))
        
        
        chkshp = pm.listRelatives(i)[0]
        if pm.objectType(chkshp,i='joint') or pm.objectType(chkshp,i='nurbsCurve'):
            pass
        else:
            crcl = pm.circle( nr=(1, 0, 0), c=(0, 0, 0), r=3 )
            crclshp = pm.listRelatives(crcl)
            pm.parent(crclshp,clist[1],add=1,s=1)
            pm.rename(crclshp,clist[1]+'Shape')
            pm.delete(crcl)
    
        pm.parent(clist[1],clist[0])
        pm.parent(clist[2],clist[1])
        pm.parent(clist[4],clist[3])
        pm.select(clist[3],clist[6],clist[7],clist[8])
        if pm.objExists(i+'_Dyn_SETUP'):
            pm.parent(clist[3],clist[6],clist[7],clist[8],i+'_Dyn_SETUP')
        else:
            pm.select(cl=1)
            pm.select(clist[3],clist[6],clist[7],clist[8])
            pm.group(n=i+'_Dyn_SETUP')
        if pm.objExists(dyngrp):
            pm.parent(i+'_Dyn_SETUP',dyngrp)
        else:
            pm.select(cl=1)
            pm.select(i+'_Dyn_SETUP')
            pm.group(n=dyngrp)
        
        pcon = pm.pointConstraint(clist[1],clist[3],mo=1)
        pcon = pm.rename(pcon,pcon.replace('RG_pointConstraint1','PC'))
        clist.append(pcon)
        
        
        pm.addAttr(clist[1], ln=ctrlattr[0],nn='Dynamic',at='float',hnv=1,min=0,hxv=1,max=1,k=1,h=0,dv=1)
        clist[3].addAttr(drvnattr, attributeType='double3')
        clist[3].addAttr(drvnattr+'X', p=drvnattr, attributeType='double',k=1)
        clist[3].addAttr(drvnattr+'Y', p=drvnattr, attributeType='double',k=1)
        clist[3].addAttr(drvnattr+'Z', p=drvnattr, attributeType='double',k=1)
        
        pm.connectAttr(clist[2]+'.parentInverseMatrix',clist[4]+'.constraintParentInverseMatrix',f=1)
        pm.connectAttr(clist[3]+'.parentMatrix[0]',clist[4]+'.target[0].targetParentMatrix',f=1)
        pm.connectAttr(clist[3]+'.cacheTranslate',clist[4]+'.target[0].targetTranslate',f=1)
        pm.connectAttr(clist[1]+'.rx',clist[5]+'.input1',f=1)
        pm.connectAttr(clist[2]+'.rx',clist[5]+'.input2',f=1)
        pm.connectAttr(clist[6]+'.worldPosition',clist[8]+'.startPoint',f=1)
        pm.connectAttr(clist[7]+'.worldPosition',clist[8]+'.endPoint',f=1)
    
        #Expression
        cmd = ('float $rotate = 0.0;\n'
            'vector $pos = <<{0}.tx, {0}.ty, {0}.tz>>;\n'
            '\n'
            'float $state = {1}.dynamics_enable;\n'
            'if ($state > 0.0001) $rotate = .I[4];\n'
            '\n'
            'if (frame > .I[5])\n'
            '{{\n'
            '    $rotate = {2}.rx;\n'
            '\n'
            '    if ($state > 0.0001)\n'
            '    {{\n'
            '        float $radius = {3}.distance;\n'
            '        float $distance = {4}.constraintTranslateZ;\n'
            '        $rotate += $state * -1 * 57.29578 * $distance / $radius;\n'
            '    }}\n'
            '}}\n'
            '\n'
            '{2}.rx = $rotate;\n'
            '{0}.cacheTranslate.cacheTranslateX = $pos.x;\n'
            '{0}.cacheTranslate.cacheTranslateY = $pos.y;\n'
            '{0}.cacheTranslate.cacheTranslateZ = $pos.z;\n')

        cmd = cmd.format(clist[3],clist[1],clist[2],clist[8],clist[4])
        if pm.objExists(i+'_dyn_EXP'):
            pm.delete(i+'_dyn_EXP')
        clist.append(pm.expression(n=i+'_dyn_EXP',s=cmd))
        if pm.checkBox(checkBox1,q=1,v=1)==0 and pm.checkBox(checkBox2,q=1,v=1)==1:
            posctrl = pm.xform(selpos[0],q=1,ws=1,rp=1)
            pm.setAttr(clist[0]+'.tx',posctrl[0])
            pm.setAttr(clist[0]+'.ty',posctrl[1])
            pm.setAttr(clist[0]+'.tz',posctrl[2])
            pm.setAttr(clist[0]+'.r',rxyz)
        elif pm.objectType(i,i='joint') or pm.objectType(pm.listRelatives(i)[0],i='nurbsCurve'):
            pass
        elif pm.checkBox(checkBox1,q=1,v=1)==1 and pm.checkBox(checkBox2,q=1,v=1)==1:
            posctrl = pm.xform(i,q=1,ws=1,rp=1)
            pm.setAttr(clist[0]+'.tx',posctrl[0])
            pm.setAttr(clist[0]+'.ty',posctrl[1])
            pm.setAttr(clist[0]+'.tz',posctrl[2])
            pm.setAttr(clist[0]+'.r',rxyz)
        else:
            pm.setAttr(clist[0]+'.r',rxyz)
        
        for h in range(0,2):
            for attr in hideattr:
                if pm.objExists(clist[1+h*1]+attr):
                    pm.setAttr(clist[1+h*1]+attr,e=1,l=1,k=0,cb=0)
        
        if pm.checkBox(checkBox3,q=1,v=1):
            if pm.objectType(i,i='joint') or pm.objectType(pm.listRelatives(i)[0],i='nurbsCurve'):
                if pm.checkBox('checkAutoPosition',q=1,v=1):
                    try:
                        con = pm.parentConstraint(dupgrp,clist[0],mo=0)
                        pm.delete(con,dupgrp)
                    except:
                        print('Bind Failed. Pass this process')
            else:
                try:
                    pm.skinCluster(clist[2],i,sm=0,nw=1,ibp=1,tsb=1,ih=1)
                except:
                    print('Bind Failed')
        elif pm.checkBox(checkBox4,q=1,v=1):
            if pm.objectType(i,i='joint') or pm.objectType(pm.listRelatives(i)[0],i='nurbsCurve'):
                if pm.checkBox('checkAutoPosition',q=1,v=1):
                    try:
                        con = pm.parentConstraint(dupgrp,clist[0],mo=0)
                        pm.delete(con,dupgrp)
                    except:
                        print('Constraint Failed, Pass this process')
            else:
                try:
                    pm.parentConstraint(clist[2],i,mo=1)
                    pm.scaleConstraint(clist[2],i,mo=1)
                except:
                    print('Constraint Failed')
        else:
            if pm.objectType(i,i='joint') or pm.objectType(pm.listRelatives(i)[0],i='nurbsCurve'):
                if pm.checkBox('checkAutoPosition',q=1,v=1):
                    try:
                        con = pm.parentConstraint(dupgrp,clist[0],mo=0)
                        pm.delete(con,dupgrp)
                    except:
                        print('Pass this process')
                else:
                    pm.setAttr(clist[0]+'.r',rxyz)
                    pm.delete(dupgrp)
            else:
                print('Pass this process')
            
        clist.append(i+'_Dyn_SETUP')
        #rename
        try:
            if pm.checkBox('checkAutoName',q=1,v=1)==1:
                for o in clist:
                    if pm.objectType(i,i='joint') or pm.objectType(pm.listRelatives(i)[0],i='nurbsCurve'):
                        pass
                    else:
                        pm.rename(o,o.replace(str(i),str(ii)))
        except:
            pass
        if pm.checkBox('checkAutoName',q=1,v=1)==0:
            pm.delete(dmypar)
        
        pm.select(clist[1])
        print(clist)
        print('done')
    cmds.setAttr(dyngrp + '.visibility', 0)
def deleteDynamicWheel(*arg):
    if pm.checkBox('checkAutoName',q=1,v=1)==0:
        if not pm.textField('textFieldName',q=1,tx=1)=='':
            sel = [pm.textField('textFieldName',q=1,tx=1)]
        else:
            sel = []
    else:
        sel = pm.ls(os=1,ap=1)
    pm.select(cl=1)
    for i in sel:
        if pm.checkBox('checkAutoName',q=1,v=1)==0:
            ii=i
        else:
            try:
                n = i.split('_')
                del n[len(n)-1]
                ii = '_'.join(n)
            except:
                ii=i
        if pm.objExists(ii+'_dyn_EXP'):
            pm.delete(ii+'_dyn_EXP')
        if pm.objExists(ii+'_GRP'):
            pm.delete(ii+'_GRP')
        if pm.objExists(ii+'_Dyn_SETUP'):
            pm.delete(ii+'_Dyn_SETUP')


buttonMenu1='createDynamic'
buttonMenu2='deleteDynamic'

labelButtonMenu1='Create '
labelButtonMenu2='Delete '

buttonMenu1Function=createDynamicWheel
buttonMenu2Function=deleteDynamicWheel
        

################################################################
def run_eye_lid_setup(*args):
    EyeLidSetupUI.mayaRun()


def scalePoCurve(*arg):
    selected = cmds.ls(sl=True)
    value_scale = float(cmds.textField("scale_curve_value", query=True, text=True))
    selected_curve = pm.selected()[0]
    pivot_point = selected_curve.getPivots(worldSpace=True)[0]
    scale_factor = value_scale  
    for obj in selected:
        for cv in selected_curve.cv:
            vertex_position = pm.xform(cv, query=True, translation=True, worldSpace=True)
            scaled_position = [
                pivot_point[0] + (vertex_position[0] - pivot_point[0]) * scale_factor,
                pivot_point[1] + (vertex_position[1] - pivot_point[1]) * scale_factor,
                pivot_point[2] + (vertex_position[2] - pivot_point[2]) * scale_factor,
            ]
            pm.xform(cv, translation=scaled_position, worldSpace=True)
            
def scaleNeCurve(*arg):
    selected = cmds.ls(sl=True)
    value_scale = float(cmds.textField("scale_curve_value", query=True, text=True))
    selected_curve = pm.selected()[0]
    pivot_point = selected_curve.getPivots(worldSpace=True)[0]
    scale_factor =  - value_scale 
    for obj in selected:  
        for cv in selected_curve.cv:
            vertex_position = pm.xform(cv, query=True, translation=True, worldSpace=True)
            scaled_position = [
                pivot_point[0] + (vertex_position[0] - pivot_point[0]) / scale_factor,
                pivot_point[1] + (vertex_position[1] - pivot_point[1]) / scale_factor,
                pivot_point[2] + (vertex_position[2] - pivot_point[2]) / scale_factor,
            ]
            pm.xform(cv, translation=scaled_position, worldSpace=True)


################################################################ set color
def setColor():
    selColor = cmds.colorIndexSliderGrp(ctrlColor, query = 1, value = 1)
    selCtrl = cmds.ls(selection = 1)
    for ctrl in selCtrl:
        cmds.setAttr(ctrl + ".overrideEnabled", 1)
        cmds.setAttr(ctrl + ".overrideColor", (selColor - 1))  

def hideManipulator():
    selPanel = cmds.getPanel(withFocus = 1)
    cmds. modelEditor(selPanel, edit = 1,  selectionHiliteDisplay = 0, manipulators = 0)
    setColor() 

def showManipulator():
    selPanel = cmds.getPanel(withFocus = 1)
    cmds.modelEditor(selPanel, edit = 1,  selectionHiliteDisplay = 1, manipulators = 1)         
