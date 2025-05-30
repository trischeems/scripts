from maya import cmds

#AutoTwist
def AutoTwistFunc(Axis = 'X', SwitchVar = 0, *args):
    
    cmds.undoInfo(openChunk=True)

            
    #Conditions
    SwitchVar = SwitchVar
    print SwitchVar

    DiferentOrient = 0
    
    Axis = Axis
    print Axis
    
    #Some Variables
    JointsTwist = cmds.ls(sl=True)
    
    if len(JointsTwist) != 2:
        cmds.warning('Select 2 Joints before please :D') 
        
    else:   
        #Create joints and position them
        JointsForTwist = []
        
        for i in range (4):
            Duplicated = cmds.duplicate(JointsTwist[0], n = str(JointsTwist[0])+'_Twist_'+str(i), rc = True)
            cmds.delete(cmds.listRelatives(Duplicated, c = True))
            
            #New Twist joints list
            JointsForTwist.append(str(JointsTwist[0])+'_Twist_'+str(i))
            print JointsForTwist
            
            #If twist joints exists parent it 
            if cmds.objExists(str(JointsTwist[0])+'_Twist_'+str(i-1)):
                cmds.parent(str(JointsTwist[0])+'_Twist_'+str(i),str(JointsTwist[0])+'_Twist_'+str(i-1))
        
        #Position joints in correct the spot... 
        for j in JointsForTwist:
            cmds.setAttr(str(j)+'.translate'+str(Axis), cmds.getAttr(JointsTwist[1]+'.translate'+str(Axis))/3 )
        
        cmds.parent(JointsForTwist[0],JointsTwist[0] ) 
        cmds.xform(str(JointsForTwist[0]), t =(0,0,0))       
        
        if cmds.listRelatives(JointsTwist[0],p = True) != None:
            cmds.parent(JointsForTwist[0], cmds.listRelatives(JointsTwist[0],p = True))
        
        #Ik Handle and pole vector set up
        IkHandle = cmds.ikHandle (n=str(JointsTwist[0]+'TwistIKrp'), sj=JointsForTwist[0], ee= JointsForTwist[1], sol = 'ikRPsolver')
        cmds.parent(IkHandle[0], JointsTwist[0])
        cmds.setAttr(str(JointsTwist[0])+'TwistIKrp'+'.poleVectorZ', 0)
        cmds.setAttr(str(JointsTwist[0])+'TwistIKrp'+'.poleVectorX', 0)
        cmds.setAttr(str(JointsTwist[0])+'TwistIKrp'+'.poleVectorY', 0)
        cmds.setAttr(str(JointsTwist[0])+'TwistIKrp'+'.snapEnable', 0)
        
        
        #Locator Setup
        AimLoc = cmds.spaceLocator(n = str(JointsTwist[0])+'_loc')
        
        if SwitchVar == 0:
            cmds.xform(AimLoc, m = cmds.xform(JointsForTwist[0], q=1, m=1))
            cmds.parent(AimLoc,JointsForTwist[0])
            cmds.xform(AimLoc, t = (0,0,0), ra =(0,0,0))
            cmds.rotate( 0,0,0,AimLoc)
            cmds.orientConstraint(str(JointsTwist[0]), AimLoc, mo = True)
        
        else:
            cmds.delete(cmds.parentConstraint(JointsForTwist[-1], AimLoc, mo =0))
            cmds.parent(AimLoc, JointsForTwist[0])
            cmds.xform(AimLoc, ra =(0,0,0))
            cmds.orientConstraint(str(JointsTwist[1]), AimLoc, mo = True)
            
        #Connect Orient to Joints 
        
        MultiNode = cmds.shadingNode('multiplyDivide', asUtility=1, n  = 'Twist_'+str(JointsTwist[0]))
        cmds.setAttr(str(MultiNode)+'.operation', 2)
        cmds.setAttr(str(MultiNode)+'.input2X', 3)
        cmds.connectAttr(str(AimLoc[0])+'.rotate'+str(Axis), str(MultiNode)+'.input1.input1X')
        
        JointsForTwist.remove(JointsForTwist[0])
        
        for k in JointsForTwist:
            cmds.connectAttr(str(MultiNode)+'.output.outputX', str(k)+'.rotate'+str(Axis))
            
        cmds.undoInfo(closeChunk=True)


