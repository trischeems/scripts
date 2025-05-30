'''
09/10/18
RdMAutoArms v1.0
By Esteban Rodriguez

www.renderdemartes.com
info@renderdemartes.com

import RdMAutoArms
reload (RdMAutoArms)
'''


from maya import cmds


###JOINTS LOCATORS
jointsNum = 4

def LocatorsBtn(*args):

    cmds.undoInfo(openChunk=True)   

    
    for X in range (jointsNum):
    
        cmds.select (clear = True)
        
        cmds.CreateLocator ()
        cmds.move (2.5*X+1, 0, 0)
        cmds.select (clear = True)

    cmds.rename ("locator1","L_Clavicule_LOC")
    cmds.rename ("locator2","L_Shoulder_LOC")
    cmds.rename ("locator3","L_Elbow_LOC")
    cmds.rename ("locator4","L_Wrist_LOC")

    if cmds.objExists ('SpineEnd_JC'):
        
         cmds.parent ('L_Wrist_LOC','L_Elbow_LOC')
         cmds.parent ('L_Elbow_LOC','L_Shoulder_LOC')
         cmds.parent ('L_Shoulder_LOC','L_Clavicule_LOC')
         cmds.pointConstraint ('SpineEnd_JC','L_Clavicule_LOC')
         cmds.delete ('L_Clavicule_LOC_pointConstraint1')
         cmds.parent ('L_Shoulder_LOC', 'L_Elbow_LOC ','L_Wrist_LOC', w = True)
         
    cmds.select('L_Elbow_LOC')
    cmds.move(0,0,-0.4, r = True)     
    cmds.select (clear = True)

    cmds.undoInfo(closeChunk=True)   
    
def JointsBtn(*args):  

    cmds.undoInfo(openChunk=True)   


    cmds.rename ("L_Clavicule_LOC","locator1")
    cmds.rename ("L_Shoulder_LOC","locator2")
    cmds.rename ("L_Elbow_LOC","locator3")
    cmds.rename ("L_Wrist_LOC","locator4")

    
    
    cmds.select (cl=True)
    
    for X in range (1,jointsNum + 1):  
                
        cmds.joint (n = "L_arm_" + str(X))
        cmds.pointConstraint ("locator" + str (X) , "L_arm_" + str(X))
        cmds.delete ("L_arm_" + str(X) + "_pointConstraint1")
        cmds.delete ("locator" + str (X))
        cmds.setAttr ("L_arm_" + str(X) + ".displayLocalAxis", 1)   
    
        
    cmds.joint ()    
    cmds.select ("L_arm_1","L_arm_2","L_arm_3","L_arm_4")    
    cmds.joint(e= True, zso=True, oj= "xzy", sao = "zdown")
    cmds.delete ('joint1')
    
    cmds.select("L_arm_1")
    cmds.mirrorJoint (mirrorYZ = True, mirrorBehavior = True, searchReplace=('L_', 'R_') )
    
    cmds.select ("R_arm_4")
    cmds.joint ()    
    cmds.select ("R_arm_1","R_arm_2","R_arm_3","R_arm_4")    
    cmds.joint(e= True, zso=True, oj= "xzy", sao = "zup")
    cmds.delete ('joint1')

    
    cmds.select (clear = True) 
          
    cmds.undoInfo(closeChunk=True)   
             
 ###IK FK CHAIN

def IKFK(GlobalMultVar, *args):  

    cmds.undoInfo(openChunk=True)   

    for X in range (1,jointsNum + 1):  
                     
        cmds.setAttr ("L_arm_" + str(X) + ".displayLocalAxis", 0) 
        cmds.setAttr ("R_arm_" + str(X) + ".displayLocalAxis", 0)

    cmds.duplicate ("L_arm_2", rc = True)
    cmds.duplicate ("L_arm_2", rc = True)
    cmds.rename ("L_arm_5", "L_arm_01_IK")
    cmds.rename ("L_arm_6", "L_arm_02_IK")
    cmds.rename ("L_arm_7", "L_arm_03_IK")
    
    cmds.rename ("L_arm_8", "L_arm_01_FK")
    cmds.rename ("L_arm_9", "L_arm_02_FK")
    cmds.rename ("L_arm_10", "L_arm_03_FK")
   
    
    if cmds.objExists('R_arm_1'):
        
        print 'Mirror already aplied'
        cmds.duplicate ("R_arm_2", rc = True)
        cmds.duplicate ("R_arm_2", rc = True)
        cmds.rename ("R_arm_5", "R_arm_01_IK")
        cmds.rename ("R_arm_6", "R_arm_02_IK")
        cmds.rename ("R_arm_7", "R_arm_03_IK")
        
        cmds.rename ("R_arm_8", "R_arm_01_FK")
        cmds.rename ("R_arm_9", "R_arm_02_FK")
        cmds.rename ("R_arm_10", "R_arm_03_FK")
        
                 
    else:
        
        cmds.select("L_arm_1")
        cmds.mirrorJoint (mirrorYZ = True, mirrorBehavior = True, searchReplace=('L_', 'R_') )
    
    cmds.ikHandle (n="L_ArmIKrp", sj="L_arm_01_IK", ee= "L_arm_03_IK")
    cmds.ikHandle (n="R_ArmIKrp", sj="R_arm_01_IK", ee= "R_arm_03_IK")

    
#Controladores
############################
    GlobalMult  = GlobalMultVar*2
    
############################
    
    #Clavicule
    
    cmds.circle (r= 3*GlobalMult,nr=(1, 0, 0), n= "L_clavicule_01_CC", ch= 0 )
    cmds.group  ("L_clavicule_01_CC", n="L_clavicule_01_GRP")
    cmds.parentConstraint ("L_arm_1", "L_clavicule_01_GRP"  )
    cmds.delete ("L_clavicule_01_GRP_parentConstraint1" )
    cmds.makeIdentity ("L_clavicule_01_CC", apply = True, t = True)
    cmds.setAttr("L_clavicule_01_CC" + "Shape.overrideEnabled", True )
    cmds.setAttr("L_clavicule_01_CC" + "Shape.overrideColor", 6 )

    cmds.duplicate ('L_clavicule_01_CC',n= "R_clavicule_01_CC")
    cmds.group  ("R_clavicule_01_CC", n="R_clavicule_01_GRP")
    cmds.parentConstraint ("R_arm_1", "R_clavicule_01_GRP"  )
    cmds.delete ("R_clavicule_01_GRP_parentConstraint1" )
    cmds.makeIdentity ("R_clavicule_01_CC", apply = True, t = True)
    cmds.setAttr("R_clavicule_01_CC" + "Shape.overrideEnabled", True )
    cmds.setAttr("R_clavicule_01_CC" + "Shape.overrideColor", 13 )

    #cmds.orientConstraint ('L_clavicule_01_CC','L_arm_1')
    #cmds.orientConstraint ('R_clavicule_01_CC','R_arm_1')
        
    #FK
    
    for P in range (1,jointsNum):    
       
        cmds.circle (r= 2*GlobalMult ,nr=(1, 0, 0), n= "L_armFK_0" +str(P) + "_CC", ch= 0 )
        cmds.group  ("L_armFK_0" +str(P) + "_CC", n="L_armFK_0" +str(P) + "_GRP")
        cmds.parentConstraint ("L_arm_0" +str(P) + "_FK", "L_armFK_0" +str(P) + "_GRP"  )
        cmds.delete ("L_armFK_0"+str(P)+ "_GRP_parentConstraint1" )
        cmds.makeIdentity ("L_armFK_0" +str(P) + "_CC", apply = True, t = True)
        cmds.setAttr("L_armFK_0" + str(P) + "_CCShape.overrideEnabled", True )
        cmds.setAttr("L_armFK_0" + str(P) + "_CCShape.overrideColor", 6 )
        
        cmds.circle (r= 2*GlobalMult ,nr=(1, 0, 0), n= "R_armFK_0" +str(P) + "_CC", ch= 0 )
        cmds.group  ("R_armFK_0" +str(P) + "_CC", n="R_armFK_0" +str(P) + "_GRP")
        cmds.parentConstraint ("R_arm_0" +str(P) + "_FK", "R_armFK_0" +str(P) + "_GRP"  )
        cmds.delete ("R_armFK_0"+str(P)+ "_GRP_parentConstraint1" )
        cmds.makeIdentity ("R_armFK_0" +str(P) + "_CC", apply = True, t = True)
        cmds.setAttr("R_armFK_0" + str(P) + "_CCShape.overrideEnabled", True )
        cmds.setAttr("R_armFK_0" + str(P) + "_CCShape.overrideColor", 13 )
        
    
    cmds.parent ("L_armFK_01_GRP", "L_clavicule_01_CC")
    cmds.parent ( "L_armFK_02_GRP","L_armFK_01_CC")
    cmds.parent ( "L_armFK_03_GRP","L_armFK_02_CC")
   
    cmds.parent ("R_armFK_01_GRP", "R_clavicule_01_CC")
    cmds.parent ( "R_armFK_02_GRP","R_armFK_01_CC")
    cmds.parent ( "R_armFK_03_GRP","R_armFK_02_CC")
    
    cmds.parentConstraint ("L_clavicule_01_CC","L_arm_1")
    cmds.parentConstraint ("L_armFK_01_CC","L_arm_01_FK")
    cmds.parentConstraint ("L_armFK_02_CC","L_arm_02_FK")
    cmds.parentConstraint ("L_armFK_03_CC","L_arm_03_FK")
    
    cmds.parentConstraint ("R_clavicule_01_CC","R_arm_1")
    cmds.parentConstraint ("R_armFK_01_CC","R_arm_01_FK")
    cmds.parentConstraint ("R_armFK_02_CC","R_arm_02_FK")
    cmds.parentConstraint ("R_armFK_03_CC","R_arm_03_FK")
        
        
    #IK
    
    cmds.curve(n="L_armIK_CC" , d=1, p=[(1, 1, 1),(1,1,-1) ,(1, -1, -1) ,(1, -1, 1) ,(-1, -1, 1) ,(-1, 1, 1) ,(1, 1, 1) ,(1, -1, 1) ,(-1, -1, 1) ,(-1, -1, -1) ,(-1, 1, -1) ,(1, 1, -1) ,(1, -1, -1) ,(-1, -1, -1) ,(-1, 1, -1) ,(-1, 1, 1)], k = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    cmds.group ("L_armIK_CC", n= "L_armIK_GRP")
    cmds.pointConstraint ("L_arm_03_IK", "L_armIK_GRP")
    cmds.delete ("L_armIK_GRP_pointConstraint1")
    cmds.orientConstraint ("L_arm_02_IK", "L_armIK_GRP")
    cmds.delete ("L_armIK_GRP_orientConstraint1")        
   
   
    cmds.curve(n="R_armIK_CC" , d=1, p=[(1, 1, 1),(1,1,-1) ,(1, -1, -1) ,(1, -1, 1) ,(-1, -1, 1) ,(-1, 1, 1) ,(1, 1, 1) ,(1, -1, 1) ,(-1, -1, 1) ,(-1, -1, -1) ,(-1, 1, -1) ,(1, 1, -1) ,(1, -1, -1) ,(-1, -1, -1) ,(-1, 1, -1) ,(-1, 1, 1)], k = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    cmds.group ("R_armIK_CC", n= "R_armIK_GRP")
    cmds.pointConstraint ("R_arm_03_IK", "R_armIK_GRP")
    cmds.delete ("R_armIK_GRP_pointConstraint1")
    cmds.orientConstraint ("R_arm_02_IK", "R_armIK_GRP")
    cmds.delete ("R_armIK_GRP_orientConstraint1")        
    
    cmds.parent ("L_ArmIKrp", "L_armIK_CC")
    cmds.parent ("R_ArmIKrp", "R_armIK_CC")
    
    cmds.orientConstraint ("L_armIK_CC","L_arm_03_IK", mo= True)
    cmds.orientConstraint ("R_armIK_CC","R_arm_03_IK", mo= True)

    cmds.scale(GlobalMult,GlobalMult,GlobalMult,'L_armIK_GRP', r = True)
    cmds.scale(GlobalMult,GlobalMult,GlobalMult,'R_armIK_GRP', r = True)
    
    cmds.setAttr ("L_armIK_CC.overrideEnabled", 1)
    cmds.setAttr ("R_armIK_CC.overrideEnabled", 1)

    cmds.setAttr ("L_armIK_CC.overrideColor", 6)
    cmds.setAttr ("R_armIK_CC.overrideColor", 13)    
    
    
    #Pole Vector

    cmds.polyPlane (n="L_PV_Plane", sh = 1, sw= 1)
    cmds.delete ("L_PV_Plane.vtx[3]")
    cmds.cluster ("L_PV_Plane.vtx[0]", n= "ShoulderCluster")
    cmds.cluster ("L_PV_Plane.vtx[1]" ,n= "ElbowCluster")
    cmds.cluster ("L_PV_Plane.vtx[2]", n= "WristCluster")
    
    cmds.pointConstraint ("L_arm_2","ShoulderClusterHandle")
    cmds.pointConstraint ("L_arm_3","ElbowClusterHandle")
    cmds.pointConstraint ("L_arm_4","WristClusterHandle")
    
    P01X = cmds.getAttr("L_arm_1.translateX")
    P01Y = cmds.getAttr("L_arm_1.translateY")
    P01Z = cmds.getAttr("L_arm_1.translateZ")    
    
    P02X = cmds.getAttr("L_arm_2.translateX") + P01X
    P02Y = cmds.getAttr("L_arm_2.translateY") + P01Y
    P02Z = cmds.getAttr("L_arm_2.translateZ") + P01Z
    
    P03X = cmds.getAttr("L_arm_3.translateX") + P02X
    P03Y = cmds.getAttr("L_arm_3.translateY") + P02Y
    P03Z = cmds.getAttr("L_arm_3.translateZ") + P02Z
    
    P04X = cmds.getAttr("L_arm_4.translateX") + P03X
    P04Y = cmds.getAttr("L_arm_4.translateY") + P03Y
    P04Z = cmds.getAttr("L_arm_4.translateZ") + P03Z
    
    cmds.moveVertexAlongDirection ("L_PV_Plane.vtx[1]", u= P02X+(P02X/2))
    PVposition = cmds.pointPosition ("L_PV_Plane.vtx[1]") 
    
    cmds.circle (n="L_PV01",nr=(0, 0, 1), r = GlobalMult)
    cmds.circle (n="L_PV02",nr=(0, 1, 0), r = GlobalMult)
    cmds.circle (n="L_PV03",nr=(1, 0, 0), r = GlobalMult)
    
    cmds.parent ("L_PV02Shape","L_PV01",r= True, s= True)
    cmds.parent ("L_PV03Shape","L_PV01",r= True, s= True)
    cmds.delete ("L_PV02","L_PV03")
    cmds.select ("L_PV01")
    cmds.group (n= "L_PV01_GRP", r= True)
    cmds.xform (t=PVposition)
    cmds.duplicate ("L_PV01_GRP", n= "R_PV_GRP")
    cmds.rename ("R_PV_GRP|L_PV01", "R_PV01")
    cmds.rename ("L_PV01_GRP", "L_PV0_GRP")
    cmds.move(0, 0, 0, ".scalePivot",".rotatePivot", absolute=True)
    cmds.setAttr ("R_PV_GRP.scaleX", -1)
    cmds.xform('R_PV_GRP', cp = True)
    
    
    cmds.select ("L_PV01","L_ArmIKrp")
    cmds.PoleVectorConstraint ()
    
    cmds.select ("R_PV01","R_ArmIKrp")
    cmds.PoleVectorConstraint ()
           
    cmds.setAttr("R_PV01Shape.overrideEnabled", True )
    cmds.setAttr("R_PV01Shape.overrideColor", 13 )
    cmds.setAttr("R_PV02Shape1.overrideEnabled", True )
    cmds.setAttr("R_PV02Shape1.overrideColor", 13 )     
    cmds.setAttr("R_PV03Shape1.overrideEnabled", True )
    cmds.setAttr("R_PV03Shape1.overrideColor", 13 )
    
    cmds.setAttr("L_PV01Shape.overrideEnabled", True )
    cmds.setAttr("L_PV01Shape.overrideColor", 6 )
    cmds.setAttr("L_PV02Shape.overrideEnabled", True )
    cmds.setAttr("L_PV02Shape.overrideColor", 6 )     
    cmds.setAttr("L_PV03Shape.overrideEnabled", True )
    cmds.setAttr("L_PV03Shape.overrideColor", 6 )
    
            
    #SwitchIKFK
    
    if cmds.objExists ("IK_FK_CC"):
        print "CurveControl IKFK  Exists"
    else:
        if cmds.objExists('makeTextCurves1'):
            cmds.rename ('makeTextCurves1','makeTextCurves1LOL')
        Texto = 'IK-FK'
        Color = 16
        Text = cmds.textCurves (n= Texto, t = Texto, o = True)    
        Lista= cmds.listRelatives (Text, ad = True)
        Shape = Lista[1]
        
        cmds.delete ('makeTextCurves1')
        
        for Curva in Lista:
            if cmds.objectType(str(Curva), isType='nurbsCurve'):
                curvaPapa = cmds.listRelatives(Curva, p = True)
                curvaAbuelo = cmds.listRelatives(curvaPapa, p = True)
                DobleCurva = cmds.listRelatives(curvaAbuelo)
                if len(DobleCurva)==2:
                    LetrasDobles.append (Curva)
                else:   
                    if not Shape == curvaPapa[0]:
                        cmds.makeIdentity (curvaAbuelo, a = True, t = True , r = True)
                        cmds.parent (Curva, Shape, r = True, s = True)
                    #Colores
                    cmds.setAttr (Curva+'.overrideEnabled', 1)
                    cmds.setAttr (Curva+'.overrideColor', Color)
                    
        cmds.parent (Shape,w=True)
        cmds.rename(Shape, 'IK_FK_CC')
        cmds.setAttr ("IK_FK_CC.overrideEnabled", 1)
        cmds.setAttr ("IK_FK_CC.overrideColor", 16)
        cmds.setAttr ('IK_FK_CC.rotateX', -90)
        cmds.xform(cp= True)
        cmds.setAttr ('IK_FK_CC.scaleX', GlobalMult)
        cmds.setAttr ('IK_FK_CC.scaleY', GlobalMult)
        cmds.setAttr ('IK_FK_CC.scaleZ', GlobalMult)
        cmds.makeIdentity(a=True, t = True, r = True, s=True)
        
    if cmds.objExists("IK_FK_CC.LeftArmIKFK")  :
        print 'existe Attr'  
    else:
        cmds.select ("IK_FK_CC")
        cmds.addAttr (ln= "LeftArmIKFK", min=0, max=1)
        cmds.setAttr ("IK_FK_CC.LeftArmIKFK", keyable = True)
        
    if cmds.objExists("IK_FK_CC.RightArmIKFK")  :
        print 'existe Attr'  
    else:
        cmds.select ("IK_FK_CC")
        cmds.addAttr (ln= "RightArmIKFK", min=0, max=1)
        cmds.setAttr ("IK_FK_CC.RightArmIKFK", keyable = True)
         
    
    cmds.expression (n="L_Arms_Switch", s = "L_arm_2.rotateX = (L_arm_01_FK.rotateX*IK_FK_CC.LeftArmIKFK)+(L_arm_01_IK.rotateX*(1-IK_FK_CC.LeftArmIKFK));\nL_arm_2.rotateY = (L_arm_01_FK.rotateY*IK_FK_CC.LeftArmIKFK)+(L_arm_01_IK.rotateY*(1-IK_FK_CC.LeftArmIKFK));\nL_arm_2.rotateZ = (L_arm_01_FK.rotateZ*IK_FK_CC.LeftArmIKFK)+(L_arm_01_IK.rotateZ*(1-IK_FK_CC.LeftArmIKFK));\nL_arm_3.rotateX = (L_arm_02_FK.rotateX*IK_FK_CC.LeftArmIKFK)+(L_arm_02_IK.rotateX*(1-IK_FK_CC.LeftArmIKFK));\nL_arm_3.rotateY = (L_arm_02_FK.rotateY*IK_FK_CC.LeftArmIKFK)+(L_arm_02_IK.rotateY*(1-IK_FK_CC.LeftArmIKFK));\nL_arm_3.rotateZ = (L_arm_02_FK.rotateZ*IK_FK_CC.LeftArmIKFK)+(L_arm_02_IK.rotateZ*(1-IK_FK_CC.LeftArmIKFK));\nL_arm_4.rotateX = (L_arm_03_FK.rotateX*IK_FK_CC.LeftArmIKFK)+(L_arm_03_IK.rotateX*(1-IK_FK_CC.LeftArmIKFK));\nL_arm_4.rotateY = (L_arm_03_FK.rotateY*IK_FK_CC.LeftArmIKFK)+(L_arm_03_IK.rotateY*(1-IK_FK_CC.LeftArmIKFK));\nL_arm_4.rotateZ = (L_arm_03_FK.rotateZ*IK_FK_CC.LeftArmIKFK)+(L_arm_03_IK.rotateZ*(1-IK_FK_CC.LeftArmIKFK));\nL_armFK_03_CC.visibility = IK_FK_CC.LeftArmIKFK;\nL_armFK_02_CC.visibility = IK_FK_CC.LeftArmIKFK;\nL_armFK_01_CC.visibility = IK_FK_CC.LeftArmIKFK;\nL_armIK_CC.visibility = (1-IK_FK_CC.LeftArmIKFK);")
    cmds.expression (n="R_Arms_Switch", s = "R_arm_2.rotateX = (R_arm_01_FK.rotateX*IK_FK_CC.RightArmIKFK)+(R_arm_01_IK.rotateX*(1-IK_FK_CC.RightArmIKFK));\nR_arm_2.rotateY = (R_arm_01_FK.rotateY*IK_FK_CC.RightArmIKFK)+(R_arm_01_IK.rotateY*(1-IK_FK_CC.RightArmIKFK));\nR_arm_2.rotateZ = (R_arm_01_FK.rotateZ*IK_FK_CC.RightArmIKFK)+(R_arm_01_IK.rotateZ*(1-IK_FK_CC.RightArmIKFK));\nR_arm_3.rotateX = (R_arm_02_FK.rotateX*IK_FK_CC.RightArmIKFK)+(R_arm_02_IK.rotateX*(1-IK_FK_CC.RightArmIKFK));\nR_arm_3.rotateY = (R_arm_02_FK.rotateY*IK_FK_CC.RightArmIKFK)+(R_arm_02_IK.rotateY*(1-IK_FK_CC.RightArmIKFK));\nR_arm_3.rotateZ = (R_arm_02_FK.rotateZ*IK_FK_CC.RightArmIKFK)+(R_arm_02_IK.rotateZ*(1-IK_FK_CC.RightArmIKFK));\nR_arm_4.rotateX = (R_arm_03_FK.rotateX*IK_FK_CC.RightArmIKFK)+(R_arm_03_IK.rotateX*(1-IK_FK_CC.RightArmIKFK));\nR_arm_4.rotateY = (R_arm_03_FK.rotateY*IK_FK_CC.RightArmIKFK)+(R_arm_03_IK.rotateY*(1-IK_FK_CC.RightArmIKFK));\nR_arm_4.rotateZ = (R_arm_03_FK.rotateZ*IK_FK_CC.RightArmIKFK)+(R_arm_03_IK.rotateZ*(1-IK_FK_CC.RightArmIKFK));\nR_armFK_03_CC.visibility = IK_FK_CC.RightArmIKFK;\nR_armFK_02_CC.visibility = IK_FK_CC.RightArmIKFK;\nR_armFK_01_CC.visibility = IK_FK_CC.RightArmIKFK;\nR_armIK_CC.visibility = (1-IK_FK_CC.RightArmIKFK);")
 

    cmds.setAttr ("IK_FK_CC.overrideEnabled", 1)
    cmds.setAttr ("IK_FK_CC.overrideColor", 18)    
    
    #Twist

    cmds.moveVertexAlongDirection ("L_PV_Plane.vtx[1]", u= -(P02X+(P02X/2)))
    V03position = cmds.pointPosition ("L_PV_Plane.vtx[2]")
    V02position = cmds.pointPosition ("L_PV_Plane.vtx[1]") 
    V01position = cmds.pointPosition ("L_PV_Plane.vtx[0]")     
    
    cmds.curve (n= "L_UpArmTwist",d=1, p=[(0,0,0),(10,0,0)], k = (0,1))
    cmds.curve (n= "L_DownArmTwist",d=1, p=[(0,0,0),(10,0,0)], k = (0,1))

        
    cmds.xform ("L_UpArmTwist.cv[0]" ,t=V01position)
    cmds.xform ("L_UpArmTwist.cv[1]" ,t=V02position)
    cmds.xform ("L_DownArmTwist.cv[0]" ,t=V02position)
    cmds.xform ("L_DownArmTwist.cv[1]" ,t=V03position)    
    
       
    cmds.duplicate ("L_UpArmTwist", n="R_UpArmTwist")
    cmds.duplicate ("L_DownArmTwist", n="R_DownArmTwist")  
    cmds.scale (-1,1,1, "R_UpArmTwist", a= True)
    cmds.scale (-1,1,1, "R_DownArmTwist", a= True)
    
    def FuckingSwitch (side):
    
        cmds.duplicate (str(side)+ "_arm_2", n= str(side)+"_UpArmTwist01")
        cmds.parent (str(side)+ "_UpArmTwist01", world = True)
        cmds.rename (str(side)+ "_UpArmTwist01|"+str(side)+"_arm_3",str(side)+ "_UpArmTwist03")
        cmds.duplicate (str(side)+ "_UpArmTwist03", n= str(side)+ "_DownArmTwist01")
        cmds.delete (str(side)+ "_UpArmTwist03|"+str(side)+"_arm_4") 
        cmds.rename (str(side)+ "_DownArmTwist01|"+str(side)+"_arm_4",str(side)+"_DownArmTwist03")
        cmds.parent (str(side)+ '_DownArmTwist01', w = True)
        
        
        cmds.duplicate (str(side)+ "_UpArmTwist03",n= str(side)+ "_UpArmTwist02")
        cmds.duplicate (str(side)+ "_DownArmTwist03",n= str(side)+ "_DownArmTwist02") 
          
        cmds.pointConstraint (str(side)+ "_UpArmTwist03",str(side)+ "_UpArmTwist01",str(side)+ "_UpArmTwist02", mo = False)
        cmds.pointConstraint (str(side)+ "_DownArmTwist03",str(side)+ "_DownArmTwist01",str(side)+ "_DownArmTwist02", mo = False)
        cmds.orientConstraint (str(side)+ "_UpArmTwist03",str(side)+ "_UpArmTwist01",str(side)+ "_UpArmTwist02", mo = True)
        cmds.orientConstraint (str(side)+ "_DownArmTwist03",str(side)+ "_DownArmTwist01",str(side)+ "_DownArmTwist02", mo = True)
        
        cmds.delete(str(side)+ "_UpArmTwist02_pointConstraint1",str(side)+ "_DownArmTwist02_pointConstraint1")
        cmds.delete(str(side)+ "_UpArmTwist02_orientConstraint1",str(side)+ "_DownArmTwist02_orientConstraint1")
        
        cmds.parent (str(side)+ "_UpArmTwist03",str(side)+ "_UpArmTwist02")
        cmds.parent (str(side)+ "_DownArmTwist03",str(side)+ "_DownArmTwist02")  
    
    FuckingSwitch("L")
    FuckingSwitch("R")
    
    cmds.group ("L_PV_Plane","ShoulderClusterHandle","ElbowClusterHandle","WristClusterHandle", n= "ExtrasAutoArms")
    cmds.setAttr ("ExtrasAutoArms.visibility", 0)
    cmds.duplicate ("L_PV_Plane", n="R_PV_Plane")
    cmds.setAttr ("R_PV_Plane.scaleX", -1)
    
    cmds.duplicate ("L_arm_2",n= "L_NoRot")
    cmds.duplicate ("R_arm_2",n= "R_NoRot")   
    cmds.delete ("L_NoRot|L_arm_3")
    cmds.delete ("R_NoRot|R_arm_3")
    
    cmds.duplicate("L_arm_2", n= "L_TwistShoulder_JJ" )
    cmds.parent ("L_TwistShoulder_JJ", world = True)
    cmds.rename ("L_TwistShoulder_JJ|L_arm_3","L_TwistElbow_JJ")    
    cmds.rename ("L_TwistElbow_JJ|L_arm_4","L_TwistWrist_JJ")
    
    cmds.duplicate("R_arm_2", n= "R_TwistShoulder_JJ" )
    cmds.parent ("R_TwistShoulder_JJ", world = True)
    cmds.rename ("R_TwistShoulder_JJ|R_arm_3","R_TwistElbow_JJ")    
    cmds.rename ("R_TwistElbow_JJ|R_arm_4","R_TwistWrist_JJ")
    
           
    cmds.ikHandle (n= "L_UpTwist_IK", sj="L_UpArmTwist01", ee="L_UpArmTwist03", sol = "ikSplineSolver", ccv= 0, pcv = 0, c="L_UpArmTwist" )
    cmds.ikHandle (n= "L_DownTwist_IK", sj="L_DownArmTwist01", ee="L_DownArmTwist03", sol = "ikSplineSolver", ccv= 0, pcv = 0, c="L_DownArmTwist" )
    cmds.ikHandle (n= "R_UpTwist_IK", sj="R_UpArmTwist01", ee="R_UpArmTwist03", sol = "ikSplineSolver", ccv= 0, pcv = 0, c="R_UpArmTwist" )
    cmds.ikHandle (n= "R_DownTwist_IK", sj="R_DownArmTwist01", ee="R_DownArmTwist03", sol = "ikSplineSolver", ccv= 0, pcv = 0, c="R_DownArmTwist" )
    
    
    
    #Twist Connections Stuff
    
    cmds.rebuildCurve ("L_UpArmTwist", s = 2, d = 1)
    cmds.rebuildCurve ("L_DownArmTwist", s = 2, d = 1)
    cmds.rebuildCurve ("R_UpArmTwist", s = 2, d = 1)
    cmds.rebuildCurve ("R_DownArmTwist", s = 2, d = 1)
    
    cmds.skinCluster("L_TwistShoulder_JJ","L_TwistElbow_JJ", "L_UpArmTwist", tsb= True, bm=0, sm=0, nw=1 )
    cmds.skinCluster("L_TwistElbow_JJ","L_TwistWrist_JJ", "L_DownArmTwist", tsb= True, bm=0, sm=0, nw=1 )
    cmds.skinCluster("R_TwistShoulder_JJ","R_TwistElbow_JJ", "R_UpArmTwist", tsb= True, bm=0, sm=0, nw=1 )
    cmds.skinCluster("R_TwistElbow_JJ","R_TwistWrist_JJ", "R_DownArmTwist", tsb= True, bm=0, sm=0, nw=1 )
    
    
    cmds.parentConstraint ("L_arm_2","L_TwistShoulder_JJ", mo = True)
    cmds.parentConstraint ("L_arm_3","L_TwistElbow_JJ", mo = True)
    cmds.parentConstraint ("L_arm_4","L_TwistWrist_JJ", mo = True)
    cmds.parentConstraint ("R_arm_2","R_TwistShoulder_JJ", mo = True)
    cmds.parentConstraint ("R_arm_3","R_TwistElbow_JJ", mo = True)
    cmds.parentConstraint ("R_arm_4","R_TwistWrist_JJ", mo = True)    
    
    
    #Advance Twist Controls
    
    cmds.setAttr ("L_UpTwist_IK.dTwistControlEnable", 1)
    cmds.setAttr ("L_UpTwist_IK.dWorldUpType", 4)
    cmds.setAttr ("L_UpTwist_IK.dForwardAxis", 0)
    cmds.setAttr ("L_UpTwist_IK.dWorldUpAxis", 1)
    
    cmds.setAttr ("R_UpTwist_IK.dTwistControlEnable", 1)
    cmds.setAttr ("R_UpTwist_IK.dWorldUpType", 4)
    cmds.setAttr ("R_UpTwist_IK.dForwardAxis", 0)
    cmds.setAttr ("R_UpTwist_IK.dWorldUpAxis", 1)
    
    cmds.setAttr ("L_DownTwist_IK.dTwistControlEnable", 1)
    cmds.setAttr ("L_DownTwist_IK.dWorldUpType", 4)
    cmds.setAttr ("L_DownTwist_IK.dForwardAxis", 0)
    cmds.setAttr ("L_DownTwist_IK.dWorldUpAxis", 1)

    
    cmds.setAttr ("R_DownTwist_IK.dTwistControlEnable", 1)
    cmds.setAttr ("R_DownTwist_IK.dWorldUpType", 4)
    cmds.setAttr ("R_DownTwist_IK.dForwardAxis", 0)
    cmds.setAttr ("R_DownTwist_IK.dWorldUpAxis", 1)
        
   
    cmds.connectAttr ("L_NoRot.xformMatrix", "L_UpTwist_IK.dWorldUpMatrix", f=True)
    cmds.connectAttr ("L_TwistElbow_JJ.xformMatrix", "L_UpTwist_IK.dWorldUpMatrixEnd", f=True )
    cmds.connectAttr ("R_NoRot.xformMatrix", "R_UpTwist_IK.dWorldUpMatrix", f=True)
    cmds.connectAttr ("R_TwistElbow_JJ.xformMatrix", "R_UpTwist_IK.dWorldUpMatrixEnd", f=True ) 
    
    cmds.connectAttr ("L_TwistElbow_JJ.xformMatrix", "L_DownTwist_IK.dWorldUpMatrix", f=True)
    cmds.connectAttr ("L_TwistWrist_JJ.xformMatrix", "L_DownTwist_IK.dWorldUpMatrixEnd", f=True )    
    cmds.connectAttr ("R_TwistElbow_JJ.xformMatrix", "R_DownTwist_IK.dWorldUpMatrix", f=True)
    cmds.connectAttr ("R_TwistWrist_JJ.xformMatrix", "R_DownTwist_IK.dWorldUpMatrixEnd", f=True )      
    
    cmds.setAttr ('L_UpArmTwist.inheritsTransform', 0)
    cmds.setAttr ('L_DownArmTwist.inheritsTransform', 0)
    cmds.setAttr ('R_UpArmTwist.inheritsTransform', 0)
    cmds.setAttr ('R_DownArmTwist.inheritsTransform', 0)
        
    cmds.select (clear = True)
            
    # Grouping and Organizing
    
    cmds.group ("L_armIK_GRP", "L_PV0_GRP", n="L_IKArm_GRP")
    cmds.group ("R_armIK_GRP", "R_PV_GRP", n="R_IKArm_GRP")
    cmds.group ("L_UpArmTwist", "L_DownArmTwist" , "L_UpTwist_IK", "L_DownTwist_IK","L_TwistShoulder_JJ","L_TwistElbow_JJ","L_TwistWrist_JJ","L_UpArmTwist01","L_DownArmTwist01", n = "L_TwistArm")
    cmds.group ("R_UpArmTwist", "R_DownArmTwist" , "R_UpTwist_IK", "R_DownTwist_IK","R_TwistShoulder_JJ","R_TwistElbow_JJ","R_TwistWrist_JJ","R_UpArmTwist01","R_DownArmTwist01", n = "R_TwistArm")
    cmds.group ("L_IKArm_GRP", "R_IKArm_GRP","L_clavicule_01_GRP","R_clavicule_01_GRP","L_arm_1","R_arm_1",n= "Connect this to the rest of the rig ARMS")
    cmds.group ("L_TwistArm", "R_TwistArm", "ExtrasAutoArms","Connect_this_to_the_rest_of_the_rig_ARMS", n="RdM_AutoARMS" )
    
           

    
#Lock and hide 
  
      
   #FK
   
    cmds.select ('L_armFK_03_CC','L_armFK_02_CC','L_armFK_01_CC','R_armFK_03_CC','R_armFK_02_CC','R_armFK_01_CC')
    FK = cmds.ls(sl=True)
   
    for T in FK:            
        cmds.setAttr(str(T)+'.translateX',lock = True, keyable = False, channelBox = False)
        cmds.setAttr(str(T)+'.translateY',lock = True, keyable = False, channelBox = False)
        cmds.setAttr(str(T)+'.translateZ',lock = True, keyable = False, channelBox = False)     
       
        cmds.setAttr(str(T)+'.scaleX',lock = True, keyable = False, channelBox = False)
        cmds.setAttr(str(T)+'.scaleY',lock = True, keyable = False, channelBox = False)
        cmds.setAttr(str(T)+'.scaleZ',lock = True, keyable = False, channelBox = False)

       
        cmds.setAttr(str(T)+'.visibility',lock = True, keyable = False, channelBox = False)
   
   #IK, Clavicule
   
    cmds.select ('L_armIK_CC', 'R_armIK_CC','R_clavicule_01_CC ','L_clavicule_01_CC')
    IK = cmds.ls(sl=True)
   
    for T in IK:            

        cmds.setAttr(str(T)+'.scaleX',lock = True, keyable = False, channelBox = False)
        cmds.setAttr(str(T)+'.scaleY',lock = True, keyable = False, channelBox = False)
        cmds.setAttr(str(T)+'.scaleZ',lock = True, keyable = False, channelBox = False)

       
        cmds.setAttr(str(T)+'.visibility',lock = True, keyable = False, channelBox = False)
   
   
   #Pole Vector   

    cmds.select ('L_PV01', 'R_PV01')
    PV = cmds.ls(sl=True)   

    for T in PV:   
             
        cmds.setAttr(str(T)+'.rotateX',lock = True, keyable = False, channelBox = False)
        cmds.setAttr(str(T)+'.rotateY',lock = True, keyable = False, channelBox = False)
        cmds.setAttr(str(T)+'.rotateZ',lock = True, keyable = False, channelBox = False)     
       
        cmds.setAttr(str(T)+'.scaleX',lock = True, keyable = False, channelBox = False)
        cmds.setAttr(str(T)+'.scaleY',lock = True, keyable = False, channelBox = False)
        cmds.setAttr(str(T)+'.scaleZ',lock = True, keyable = False, channelBox = False)

       
        cmds.setAttr(str(T)+'.visibility',lock = True, keyable = False, channelBox = False)

        # Borrar lo malo
    cmds.delete('L_UpArmTwist', 'L_DownArmTwist', 'L_UpTwist_IK', 'L_DownTwist_IK', 'R_UpArmTwist', 'R_DownArmTwist',
                'R_UpTwist_IK', 'R_DownTwist_IK')
    cmds.delete('R_TwistShoulder_JJ_parentConstraint1', 'R_TwistElbow_JJ_parentConstraint1',
                'R_TwistWrist_JJ_parentConstraint1', 'L_TwistWrist_JJ_parentConstraint1',
                'L_TwistElbow_JJ_parentConstraint1', 'L_TwistShoulder_JJ_parentConstraint1')
    cmds.delete('L_TwistShoulder_JJ', 'R_TwistShoulder_JJ', 'L_UpArmTwist01', 'R_UpArmTwist01')

    # Acomodar todo del lado izquierdo
    cmds.parent('L_TwistWrist_JJ', 'L_TwistElbow_JJ')
    cmds.parent('L_TwistElbow_JJ', 'L_DownArmTwist02', 'L_arm_3')

    cmds.delete('L_DownArmTwist03', 'L_DownArmTwist01')

    cmds.makeIdentity('L_TwistElbow_JJ', apply=True, t=1, r=1)

    # IKSc
    cmds.select('L_TwistElbow_JJ', 'L_TwistWrist_JJ')
    cmds.ikHandle(sol='ikSCsolver', n='L_TwistIKSc')
    cmds.parent('L_TwistIKSc', 'L_arm_4')

    # Orient for Twist
    OrientTemp = cmds.orientConstraint('L_TwistElbow_JJ', 'L_arm_4', 'L_DownArmTwist02', mo=0)
    cmds.delete(OrientTemp)

    cmds.makeIdentity('L_DownArmTwist02', apply=True, t=1, r=1)

    # ConnectionEditor
    cmds.shadingNode('multiplyDivide', asUtility=1, n='L_TwistMult')
    cmds.connectAttr('L_TwistElbow_JJ.rotate.rotateX', 'L_TwistMult.input1.input1X')
    cmds.setAttr('L_TwistMult.input2X', 0.5)
    cmds.connectAttr('L_TwistMult.output.outputX', 'L_DownArmTwist02.rotate.rotateX')

    # Duplicar para R
    # Acomodar todo del lado izquierdo
    cmds.parent('R_TwistWrist_JJ', 'R_TwistElbow_JJ')
    cmds.parent('R_TwistElbow_JJ', 'R_DownArmTwist02', 'R_arm_3')

    cmds.delete('R_DownArmTwist03', 'R_DownArmTwist01')

    cmds.makeIdentity('R_TwistElbow_JJ', apply=True, t=1, r=1)

    # IKSc
    cmds.select('R_TwistElbow_JJ', 'R_TwistWrist_JJ')
    cmds.ikHandle(sol='ikSCsolver', n='R_TwistIKSc')
    cmds.parent('R_TwistIKSc', 'R_arm_4')

    # Orient for Twist
    OrientTemp = cmds.orientConstraint('R_TwistElbow_JJ', 'R_arm_4', 'R_DownArmTwist02', mo=0)
    cmds.delete(OrientTemp)

    cmds.makeIdentity('R_DownArmTwist02', apply=True, t=1, r=1)

    # ConnectionEditor
    cmds.shadingNode('multiplyDivide', asUtility=1, n='R_TwistMult')
    cmds.connectAttr('R_TwistElbow_JJ.rotate.rotateX', 'R_TwistMult.input1.input1X')
    cmds.setAttr('R_TwistMult.input2X', 0.5)
    cmds.connectAttr('R_TwistMult.output.outputX', 'R_DownArmTwist02.rotate.rotateX')

    cmds.select('L_DownArmTwist02', 'L_arm_1', 'R_DownArmTwist02', 'R_arm_1', 'R_arm_2', 'L_arm_2', 'L_arm_3',
                'R_arm_3')
    cmds.sets(n='BindThisToArms')

    print 'DONE'
      
    cmds.undoInfo(closeChunk=True)   



