import pymel.core as pm
import maya.cmds as cmds

ctrlColor = 'ctrlColor'
toolWindowName='DynamicWheel'
toolLabel='Dynamic Wheel'
select = cmds.ls(sl=True)
optionMenu1='optionWheelDirection'
windowwidth = []
windowheight = []
dwidth = []
dheight = []
i=[]
o=[]
sel=[]
dyngrp = 'SystemDY_' + select[0]
createorder = ['_Grp_Dyn','_Ctrl_Dyn','_dyn_JNT','_dyn_driver_RG','_dyn_driven_PC','_dyn_bake_ADL']
typeorder = ['transform','joint','joint','transform','pointConstraint','addDoubleLinear']
clist = [] 
ctrlattr = 'dynamics_enable', 'link_dynamics_bake', 'link_dynamics_preroll'
drvnattr = 'cacheTranslate'
hideattr = ['.tx','.ty','.tz','.ry','.rz','.sx','.sy','.sz','.radi']
direction = []
up = []
rxyz = []

def createDynamicWheel(*arg):
    global sel,dyngrp,createorder,typeorder,clist,ctrlattr,drvnattr,sel,hideattr,ryxz
    # if direction == 'x':
    # rxyz = [0,90,0]
    # elif direction == 'y':
    #     rxyz = [-90,0,0]
    # elif direction == 'z':
    rxyz = [0,0,0]
    # elif direction == '-x':
    #     rxyz = [0,-90,0]
    # elif direction == '-y':
    #     rxyz = [90,0,0]
    # elif direction == '-z':
    #     rxyz = [0,180,0]
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
        if pm.objExists(i+'_dynamic_set_grp'):
            pm.delete(i+'_dynamic_set_grp')
        for o in range(len(createorder)):
            if pm.objExists(i+createorder[o]):
                pm.delete(i+createorder[o])
            if o == 0 and parsuffix[0] == 'grp':
                clist.append(par)
                dupgrp = pm.rename(pm.duplicate(par),par+'_Dup')
                pm.rename(pm.listRelatives(dupgrp)[0],dupgrp.replace('grp','Ctrl'))
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

        else:
            pm.setAttr(clist[6]+'.ty',bbox[1])
            pm.setAttr(clist[7]+'.ty',(bbox[4]+bbox[1])/2)
        distnode = pm.createNode('distanceDimShape', n=i+'_DisShape')
        clist.append(pm.rename(pm.listRelatives(distnode,p=1)[0],i+'_Dis'))
        
        
        chkshp = pm.listRelatives(i)[0]
        if pm.objectType(chkshp,i='joint') or pm.objectType(chkshp,i='nurbsCurve'):
            pass
        # else:
            # crcl = pm.circle( nr=(1, 0, 0), c=(0, 0, 0), r=3 )
            # crclshp = pm.listRelatives(crcl)
            # pm.parent(crclshp,clist[1],add=1,s=1)
            # pm.rename(crcl,clist[1]+'_Ctrl_Dyn')
            # cmds.matchTransform(crcl,clist[1])
            # pm.delete(crcl)
    
        pm.parent(clist[1],clist[0])
        pm.parent(clist[2],clist[1])
        pm.parent(clist[4],clist[3])
        pm.select(clist[3],clist[6],clist[7],clist[8])
        if pm.objExists(i+'_dynamic_set_grp'):
            pm.parent(clist[3],clist[6],clist[7],clist[8],i+'_dynamic_set_grp')
        else:
            pm.select(cl=1)
            pm.select(clist[3],clist[6],clist[7],clist[8])
            pm.group(n=i+'_dynamic_set_grp')
        if pm.objExists(dyngrp):
            pm.parent(i+'_dynamic_set_grp',dyngrp)
        else:
            pm.select(cl=1)
            pm.select(i+'_dynamic_set_grp')
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
        if pm.objExists(i+'_dyn_expression'):
            pm.delete(i+'_dyn_expression')
        clist.append(pm.expression(n=i+'_dyn_expression',s=cmd))
        posctrl = pm.xform(i,q=1,ws=1,rp=1)
        pm.setAttr(clist[0]+'.tx',posctrl[0])
        pm.setAttr(clist[0]+'.ty',posctrl[1])
        pm.setAttr(clist[0]+'.tz',posctrl[2])
        pm.setAttr(clist[0]+'.r',rxyz)
        for h in range(0,2):
            for attr in hideattr:
                if pm.objExists(clist[1+h*1]+attr):
                    pm.setAttr(clist[1+h*1]+attr,e=1,l=1,k=0,cb=0)

        if pm.objectType(i,i='joint') or pm.objectType(pm.listRelatives(i)[0],i='nurbsCurve'):
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

        clist.append(i+'_dynamic_set_grp')
        try:
            for o in clist:
                if pm.objectType(i,i='joint') or pm.objectType(pm.listRelatives(i)[0],i='nurbsCurve'):
                    pass
                else:
                    pm.rename(o,o.replace(str(i),str(ii)))
        except:
            pass
        pm.select(clist[1])
        print(clist)
        print('done')
    cmds.setAttr(dyngrp + '.visibility', 0)
    cmds.setAttr(i + ".v",0)


createDynamicWheel()
