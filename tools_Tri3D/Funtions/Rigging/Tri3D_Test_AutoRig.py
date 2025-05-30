import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm


selected_obj = cmds.ls(sl=True)

#####################################
#####################################
joint_Root = "Root"
joint_Spine1 = "Spine1"
joint_Chest = "Chest"
joint_Neck = "Neck"
joint_Head = "HeadEnd"

joint_LScapula = "L_Scapula"
joint_LShoulder = "L_Shoulder"
joint_LElbow = "L_Elbow"
joint_LWrist = "L_Wrist"
joint_LHip = "L_Hip"
joint_LKnee = "L_Knee"
joint_LAnkle = "L_Ankle"
joint_LToes = "L_Toes"
joint_LToesEnd = "L_ToesEnd"

joint_RScapula = "R_Scapula"
joint_RShoulder = "R_Shoulder"
joint_RElbow = "R_Elbow"
joint_RWrist = "R_Wrist"
joint_RHip = "R_Hip"
joint_RKnee = "R_Knee"
joint_RAnkle = "R_Ankle"
joint_RToes = "R_Toes"
joint_RToesEnd = "R_ToesEnd"

joint_LHand = "L_Hand"
joint_LMiddleFinger1 = "L_MiddleFinger1"
joint_LMiddleFinger2 = "L_MiddleFinger2"
joint_LMiddleFinger3 = "L_MiddleFinger3"
joint_LThumbFinger1 = "L_ThumbFinger1"
joint_LThumbFinger2 = "L_ThumbFinger2"
joint_LThumbFinger3 = "L_ThumbFinger3"
joint_LIndexFinger1 = "L_IndexFinger1"
joint_LIndexFinger2 = "L_IndexFinger2"
joint_LIndexFinger3 = "L_IndexFinger3"
joint_LPinkyFinger1 = "L_PinkyFinger1"
joint_LPinkyFinger2 = "L_PinkyFinger2"
joint_LPinkyFinger3 = "L_PinkyFinger3"
joint_LRingFinger1 = "L_RingFinger1"
joint_LRingFinger2 = "L_RingFinger2"
joint_LRingFinger3 = "L_RingFinger3"

joint_RHand = "R_Hand"
joint_RMiddleFinger1 = "R_MiddleFinger1"
joint_RMiddleFinger2 = "R_MiddleFinger2"
joint_RMiddleFinger3 = "R_MiddleFinger3"
joint_RThumbFinger1 = "R_ThumbFinger1"
joint_RThumbFinger2 = "R_ThumbFinger2"
joint_RThumbFinger3 = "R_ThumbFinger3"
joint_RIndexFinger1 = "R_IndexFinger1"
joint_RIndexFinger2 = "R_IndexFinger2"
joint_RIndexFinger3 = "R_IndexFinger3"
joint_RPinkyFinger1 = "R_PinkyFinger1"
joint_RPinkyFinger2 = "R_PinkyFinger2"
joint_RPinkyFinger3 = "R_PinkyFinger3"
joint_RRingFinger1 = "R_RingFinger1"
joint_RRingFinger2 = "R_RingFinger2"
joint_RRingFinger3 = "R_RingFinger3"

joint_ER = "EyeR"
joint_EL = "EyeL"

Jnt_MUL ="Mid_Up_Lip"
Jnt_MDL ="Mid_Down_Lip"
Jnt_RCL = "R_Corner_Lip"
Jnt_BW1 = "R_Between_1"
Jnt_BW2 = "R_Between_2"
Jnt_BW3 = "R_Between_3"
Jnt_BW4 = "R_Between_4"

Jnt_LCL = "L_Corner_Lip"
Jnt_BW5 = "L_Between_1"
Jnt_BW6 = "L_Between_2"
Jnt_BW7 = "L_Between_3"
Jnt_BW8 = "L_Between_4"

Jnt_RIB = "R_InnerBrow"
Jnt_ROB = "R_OuterBrow"
Jnt_LIB = "L_InnerBrow"
Jnt_LOB = "L_OuterBrow"
Jnt_Jaw = "Jaw_Jnt"

Jnt_TG1 ="Tongue1_jnt"
Jnt_TG2 ="Tongue2_jnt"
Jnt_TG3 ="Tongue3_jnt"
Jnt_TG4 ="Tongue4_jnt"
####################################
####################################
Color1 = 18 # blue
Color2 = 13 # red
Color3 = 17 # yellow
Color4 = 14 # green
Color5 = 21 # orange
ColorCurve1 = 3 # xam
ColorCurve2 = 18 # xanh
ColorCurve3 = 17 # vang

####################################
####################################



def createBone(*args):
    mel_script = """

    
createNode joint -n "Root";
	setAttr ".t" -type "double3" 1.9709482123356974e-016 9.8285101990184387 -0.17717208138029261 ;
	setAttr -l on ".tx";
	setAttr ".r" -type "double3" 2.2263882770244617e-014 2.8624992133171654e-014 -3.1805546814635116e-015 ;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.999999999999972 8.0332256276735148 89.999999999999972 ;

createNode joint -n "Spine1" -p "Root";
	setAttr ".t" -type "double3" 1.7561552005093688 0 -7.5302564402681654e-016 ;
	setAttr -l on ".tz";
	setAttr ".r" -type "double3" 6.7940406962849691e-016 2.5057725739659384e-014 -8.587497639951495e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 3.1062237164616149 ;

createNode joint -n "R_Hip" -p "Root";
	setAttr ".t" -type "double3" -0.19968944689688328 -0.082240221781533229 -0.81968660714779118 ;
	//setAttr ".ro" 2;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.57203838694888565 178.21077998921388 2.8717939465701359 ;

createNode joint -n "R_Knee" -p "R_Hip";
	setAttr ".t" -type "double3" 4.9741246355670858 2.3314683517128287e-015 2.1538326677728037e-014 ;
	//setAttr ".ro" 2;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -9.4300858589301857 ;

createNode joint -n "R_Ankle" -p "R_Knee";
	setAttr ".t" -type "double3" 3.8301794911694191 -5.3290705182007514e-015 7.9936057773011271e-015 ;
	//setAttr ".ro" 3;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.4247604049611355 1.7303887114620087 4.2486823290117313 ;
	setAttr ".pa" -type "double3" 3.1147589914174403 -1.2104724556304993 -11.405913270501992 ;

createNode joint -n "R_Toes" -p "R_Ankle";
	setAttr ".t" -type "double3" 0.66611707946596899 1.3424176194153703 -3.9968028886505635e-015 ;
	//setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.093327476095577511 -0.68753961284705734 82.269656827073391 ;
	setAttr ".pa" -type "double3" -0.00019030234564052423 0.00053514845282692043 25.864574245063647 ;

createNode joint -n "R_ToesEnd" -p "R_Toes";
	setAttr ".t" -type "double3" 0.62690099391694121 3.8857805861880479e-016 1.7763568394002505e-015 ;
	//setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 179.99991330031264 1.3815119899922174e-005 -15.357691910328654 ;

createNode joint -n "Chest" -p "Spine1";
	setAttr ".t" -type "double3" 1.4259059316898739 -4.4408920985006262e-016 -6.236054395364479e-016 ;
	setAttr -l on ".tz";
	setAttr ".r" -type "double3" -2.5330783029728389e-014 -2.2486456079175096e-013 1.7015967545829819e-013 ;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 12.854441538903254 ;

createNode joint -n "Neck" -p "Chest";
	setAttr ".t" -type "double3" 1.1676556525613471 3.9968028886505635e-015 4.5826128503804045e-015 ;
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	//setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 2.3956597842176279 ;
	setAttr ".pa" -type "double3" -1.7940447748746266e-016 6.8425179703803005e-015 0 ;

createNode joint -n "R_Scapula" -p "Chest";
	setAttr ".t" -type "double3" 0.76420093764430419 0.27528914379522496 -0.43653594851735028 ;
	//setAttr ".ro" 2;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 57.954651186638614 90.021230553569026 50.020358430320435 ;

createNode joint -n "R_Shoulder" -p "R_Scapula";

	setAttr ".t" -type "double3" 1.0925408230395581 -4.163336342344337e-015 -3.730349362740526e-014 ;
	//setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.00030235216143521706 -0.011608264598945518 -2.9840096586893488 ;
	setAttr ".pa" -type "double3" -4.1293130717023516e-007 0 0 ;

createNode joint -n "R_Elbow" -p "R_Shoulder";
	setAttr ".t" -type "double3" 2.6142519042768337 -1.2906342661267445e-015 -1.0125233984581428e-013 ;
	//setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 6.3821889474816276 ;

createNode joint -n "R_Wrist" -p "R_Elbow";
	setAttr ".t" -type "double3" 2.2826034776256066 3.219646771412954e-015 6.0573768223548541e-013 ;
	//setAttr ".ro" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -3.3801837498864455 ;

createNode joint -n "R_Hand" ;
	setAttr ".t" -type "double3" -6.729 13.713 -0.161 ;
    setAttr ".r" -type "double3" 90 0 180;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.069474194567568717 4.7753179570062354 -0.8344806599264869 ;
	setAttr ".pa" -type "double3" -2.490303168013669e-017 3.8068719241856406 -4.0949047407001542 ;
	FreezeTransformations;
    
createNode joint -n "R_MiddleFinger1" -p "R_Hand";
	setAttr ".t" -type "double3" 0.96324153450077432 0.0039656713481192873 7.9936057773011271e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.069474194567568717 4.7753179570062354 -0.8344806599264869 ;
	setAttr ".pa" -type "double3" -2.490303168013669e-017 3.8068719241856406 -4.0949047407001542 ;

createNode joint -n "R_MiddleFinger2" -p "R_MiddleFinger1";
	setAttr ".t" -type "double3" 0.31064094986492652 5.2589196886110301e-011 -9.1482377229112899e-012 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.036678948879720293 -2.5199985860300922 -0.0025734866816321577 ;
	setAttr ".pa" -type "double3" 0 0 2.5199999009299203 ;

createNode joint -n "R_MiddleFinger3" -p "R_MiddleFinger2";
	setAttr ".t" -type "double3" 0.17127015324651573 -7.2164496600635175e-016 -4.7961634663806763e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.053454832775707894 -3.6712936380785144 -0.0014021136048479931 ;
	setAttr ".pa" -type "double3" 0 0 3.6712939054552742 ;

createNode joint -n "R_ThumbFinger1" -p "R_Hand";
	setAttr ".t" -type "double3" 0.20402275375960777 0.14485585120260247 -0.10091871133417207 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -52.264000000000024 19.323320728472126 38.439955900417992 ;
	setAttr ".pa" -type "double3" -34.462082586865911 -8.7285733235282201 -1.7903981777634761 ;

createNode joint -n "R_ThumbFinger2" -p "R_ThumbFinger1";
	setAttr ".t" -type "double3" 0.35088249761039381 1.5418475385331476e-009 2.0206218920293395e-009 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;

createNode joint -n "R_ThumbFinger3" -p "R_ThumbFinger2";
	setAttr ".t" -type "double3" 0.1686858927156254 0 2.7533531010703882e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;

createNode joint -n "R_IndexFinger1" -p "R_Hand";
	setAttr ".t" -type "double3" 0.86087833292390137 0.23966045955925147 -0.017444365616485769 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.90355498164830117 3.1740263719529995 15.899115832802362 ;
	setAttr ".pa" -type "double3" 0.065532877363568762 20.527688987272207 -2.5422327562497964 ;

createNode joint -n "R_IndexFinger2" -p "R_IndexFinger1";
	setAttr ".t" -type "double3" 0.26385832488508587 2.1458834709164876e-011 1.0187051202592556e-010 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;

createNode joint -n "R_IndexFinger3" -p "R_IndexFinger2";
	setAttr ".t" -type "double3" 0.17551941301193974 -7.1054273576010019e-015 -4.7961634663806763e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.6418340242699812 -5.7596206078048544 0.066225387225899435 ;
	setAttr ".pa" -type "double3" 0 0 5.7600000490223469 ;

createNode joint -n "R_PinkyFinger1" -p "R_Hand";
	setAttr ".t" -type "double3" 0.886 -0.474 -0.098 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -2.9521670012571231 7.9169505597481988 -15.886024859268939 ;
	setAttr ".pa" -type "double3" -0.21586850671656455 -15.856897343794616 -7.9762775885025459 ;

createNode joint -n "R_PinkyFinger2" -p "R_PinkyFinger1";
	setAttr ".t" -type "double3" 0.23273224634690681 -6.4392935428259079e-015 -9.0594198809412774e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.26683083078458442 -0.71917589712374974 -0.0344391239165893 ;
	setAttr ".pa" -type "double3" 0 0 0.71999997359174039 ;

createNode joint -n "R_PinkyFinger3" -p "R_PinkyFinger2";
	setAttr ".t" -type "double3" 0.14230168593650916 -5.773159728050814e-015 -4.9737991503207013e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.1588765498905533 -5.7546090601920987 -0.24956300887639274 ;
	setAttr ".pa" -type "double3" 0 0 5.7599997887354624 ;

createNode joint -n "R_RingFinger1" -p "R_Hand";
	setAttr ".t" -type "double3" 0.92 -0.229 -0.042 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.18874659568729768 1.4381831520375543 -2.8370412493246802 ;
	setAttr ".pa" -type "double3" -0.07133019936876682 -2.835223641928581 -1.4417652325251511 ;

createNode joint -n "R_RingFinger2" -p "R_RingFinger1";
	setAttr ".t" -type "double3" 0.28952412379075909 1.0658141036401503e-014 -1.2612133559741778e-013 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.28317914938276145 2.1599955702211711 0.0043909097713010735 ;
	setAttr ".pa" -type "double3" 0 0 -2.1600000310934706 ;


createNode joint -n "R_RingFinger3" -p "R_RingFinger2";
	setAttr ".t" -type "double3" 0.1750602747689598 -4.1078251911130792e-015 1.3500311979441904e-013 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.56783371127762794 -4.3198948128062415 -0.030192099090909089 ;
	setAttr ".pa" -type "double3" 0 0 4.3200001190538568 ;

createNode joint -n "HeadEnd" -p "Neck";
	setAttr ".t" -type "double3" 3.032 -0.269 0 ;
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;


    """

    pm.mel.eval(mel_script)
    cmds.textField("Import_biped_Text", edit=True, text="Done Import !")
    
    cmds.checkBox("Import_CheckBox", enable=True, edit=True, value=True)

def deleteImportBone(*arg):
    mel_script = """
    select -r Root ;
	doDelete;
    select -r R_Hand ;
    doDelete;
    select -r L_Hand ;
	doDelete;
	"""
    pm.mel.eval(mel_script)
    cmds.textField("Import_biped_Text", edit=True, text="Delete Import !")
    #cmds.textField("Done_Setup_CheckBox", edit=True, text="Delete Import")
    #cmds.textField("Mirror_Checkbox", edit=True, text="Delete Import")


def DoneSetupBone(*args):
    mel_script = """
channelBoxCommand -unlock;
CBunlockAttr "R_RingFinger3.tx";
CBunlockAttr "Root.tx";
CBunlockAttr "Spine1.tx";
CBunlockAttr "Chest.tx";
CBunlockAttr "Neck.tx";
CBunlockAttr "HeadEnd.tx";
CBunlockAttr "R_Scapula.tx";
CBunlockAttr "R_Shoulder.tx";
CBunlockAttr "R_Elbow.tx";
CBunlockAttr "R_Wrist.tx";
CBunlockAttr "R_Hip.tx";
CBunlockAttr "R_Knee.tx";
CBunlockAttr "R_Ankle.tx";
CBunlockAttr "R_Toes.tx";
CBunlockAttr "R_ToesEnd.tx";
CBunlockAttr "R_Hand.tx";
CBunlockAttr "R_MiddleFinger1.tx";
CBunlockAttr "R_MiddleFinger2.tx";
CBunlockAttr "R_MiddleFinger3.tx";
CBunlockAttr "R_ThumbFinger1.tx";
CBunlockAttr "R_ThumbFinger2.tx";
CBunlockAttr "R_ThumbFinger3.tx";
CBunlockAttr "R_IndexFinger1.tx";
CBunlockAttr "R_IndexFinger2.tx";
CBunlockAttr "R_IndexFinger3.tx";
CBunlockAttr "R_PinkyFinger1.tx";
CBunlockAttr "R_PinkyFinger2.tx";
CBunlockAttr "R_PinkyFinger3.tx";
CBunlockAttr "R_RingFinger1.tx";
CBunlockAttr "R_RingFinger2.tx";
CBunlockAttr "R_RingFinger3.ty";
CBunlockAttr "Root.ty";
CBunlockAttr "Spine1.ty";
CBunlockAttr "Chest.ty";
CBunlockAttr "Neck.ty";
CBunlockAttr "HeadEnd.ty";
CBunlockAttr "R_Scapula.ty";
CBunlockAttr "R_Shoulder.ty";
CBunlockAttr "R_Elbow.ty";
CBunlockAttr "R_Wrist.ty";
CBunlockAttr "R_Hip.ty";
CBunlockAttr "R_Knee.ty";
CBunlockAttr "R_Ankle.ty";
CBunlockAttr "R_Toes.ty";
CBunlockAttr "R_ToesEnd.ty";
CBunlockAttr "R_Hand.ty";
CBunlockAttr "R_MiddleFinger1.ty";
CBunlockAttr "R_MiddleFinger2.ty";
CBunlockAttr "R_MiddleFinger3.ty";
CBunlockAttr "R_ThumbFinger1.ty";
CBunlockAttr "R_ThumbFinger2.ty";
CBunlockAttr "R_ThumbFinger3.ty";
CBunlockAttr "R_IndexFinger1.ty";
CBunlockAttr "R_IndexFinger2.ty";
CBunlockAttr "R_IndexFinger3.ty";
CBunlockAttr "R_PinkyFinger1.ty";
CBunlockAttr "R_PinkyFinger2.ty";
CBunlockAttr "R_PinkyFinger3.ty";
CBunlockAttr "R_RingFinger1.ty";
CBunlockAttr "R_RingFinger2.ty";
CBunlockAttr "R_RingFinger3.tz";
CBunlockAttr "Root.tz";
CBunlockAttr "Spine1.tz";
CBunlockAttr "Chest.tz";
CBunlockAttr "Neck.tz";
CBunlockAttr "HeadEnd.tz";
CBunlockAttr "R_Scapula.tz";
CBunlockAttr "R_Shoulder.tz";
CBunlockAttr "R_Elbow.tz";
CBunlockAttr "R_Wrist.tz";
CBunlockAttr "R_Hip.tz";
CBunlockAttr "R_Knee.tz";
CBunlockAttr "R_Ankle.tz";
CBunlockAttr "R_Toes.tz";
CBunlockAttr "R_ToesEnd.tz";
CBunlockAttr "R_Hand.tz";
CBunlockAttr "R_MiddleFinger1.tz";
CBunlockAttr "R_MiddleFinger2.tz";
CBunlockAttr "R_MiddleFinger3.tz";
CBunlockAttr "R_ThumbFinger1.tz";
CBunlockAttr "R_ThumbFinger2.tz";
CBunlockAttr "R_ThumbFinger3.tz";
CBunlockAttr "R_IndexFinger1.tz";
CBunlockAttr "R_IndexFinger2.tz";
CBunlockAttr "R_IndexFinger3.tz";
CBunlockAttr "R_PinkyFinger1.tz";
CBunlockAttr "R_PinkyFinger2.tz";
CBunlockAttr "R_PinkyFinger3.tz";
CBunlockAttr "R_RingFinger1.tz";
CBunlockAttr "R_RingFinger2.tz";
CBunlockAttr "R_RingFinger3.rx";
CBunlockAttr "Root.rx";
CBunlockAttr "Spine1.rx";
CBunlockAttr "Chest.rx";
CBunlockAttr "Neck.rx";
CBunlockAttr "HeadEnd.rx";
CBunlockAttr "R_Scapula.rx";
CBunlockAttr "R_Shoulder.rx";
CBunlockAttr "R_Elbow.rx";
CBunlockAttr "R_Wrist.rx";
CBunlockAttr "R_Hip.rx";
CBunlockAttr "R_Knee.rx";
CBunlockAttr "R_Ankle.rx";
CBunlockAttr "R_Toes.rx";
CBunlockAttr "R_ToesEnd.rx";
CBunlockAttr "R_Hand.rx";
CBunlockAttr "R_MiddleFinger1.rx";
CBunlockAttr "R_MiddleFinger2.rx";
CBunlockAttr "R_MiddleFinger3.rx";
CBunlockAttr "R_ThumbFinger1.rx";
CBunlockAttr "R_ThumbFinger2.rx";
CBunlockAttr "R_ThumbFinger3.rx";
CBunlockAttr "R_IndexFinger1.rx";
CBunlockAttr "R_IndexFinger2.rx";
CBunlockAttr "R_IndexFinger3.rx";
CBunlockAttr "R_PinkyFinger1.rx";
CBunlockAttr "R_PinkyFinger2.rx";
CBunlockAttr "R_PinkyFinger3.rx";
CBunlockAttr "R_RingFinger1.rx";
CBunlockAttr "R_RingFinger2.rx";
CBunlockAttr "R_RingFinger3.ry";
CBunlockAttr "Root.ry";
CBunlockAttr "Spine1.ry";
CBunlockAttr "Chest.ry";
CBunlockAttr "Neck.ry";
CBunlockAttr "HeadEnd.ry";
CBunlockAttr "R_Scapula.ry";
CBunlockAttr "R_Shoulder.ry";
CBunlockAttr "R_Elbow.ry";
CBunlockAttr "R_Wrist.ry";
CBunlockAttr "R_Hip.ry";
CBunlockAttr "R_Knee.ry";
CBunlockAttr "R_Ankle.ry";
CBunlockAttr "R_Toes.ry";
CBunlockAttr "R_ToesEnd.ry";
CBunlockAttr "R_Hand.ry";
CBunlockAttr "R_MiddleFinger1.ry";
CBunlockAttr "R_MiddleFinger2.ry";
CBunlockAttr "R_MiddleFinger3.ry";
CBunlockAttr "R_ThumbFinger1.ry";
CBunlockAttr "R_ThumbFinger2.ry";
CBunlockAttr "R_ThumbFinger3.ry";
CBunlockAttr "R_IndexFinger1.ry";
CBunlockAttr "R_IndexFinger2.ry";
CBunlockAttr "R_IndexFinger3.ry";
CBunlockAttr "R_PinkyFinger1.ry";
CBunlockAttr "R_PinkyFinger2.ry";
CBunlockAttr "R_PinkyFinger3.ry";
CBunlockAttr "R_RingFinger1.ry";
CBunlockAttr "R_RingFinger2.ry";
CBunlockAttr "R_RingFinger3.rz";
CBunlockAttr "Root.rz";
CBunlockAttr "Spine1.rz";
CBunlockAttr "Chest.rz";
CBunlockAttr "Neck.rz";
CBunlockAttr "HeadEnd.rz";
CBunlockAttr "R_Scapula.rz";
CBunlockAttr "R_Shoulder.rz";
CBunlockAttr "R_Elbow.rz";
CBunlockAttr "R_Wrist.rz";
CBunlockAttr "R_Hip.rz";
CBunlockAttr "R_Knee.rz";
CBunlockAttr "R_Ankle.rz";
CBunlockAttr "R_Toes.rz";
CBunlockAttr "R_ToesEnd.rz";
CBunlockAttr "R_Hand.rz";
CBunlockAttr "R_MiddleFinger1.rz";
CBunlockAttr "R_MiddleFinger2.rz";
CBunlockAttr "R_MiddleFinger3.rz";
CBunlockAttr "R_ThumbFinger1.rz";
CBunlockAttr "R_ThumbFinger2.rz";
CBunlockAttr "R_ThumbFinger3.rz";
CBunlockAttr "R_IndexFinger1.rz";
CBunlockAttr "R_IndexFinger2.rz";
CBunlockAttr "R_IndexFinger3.rz";
CBunlockAttr "R_PinkyFinger1.rz";
CBunlockAttr "R_PinkyFinger2.rz";
CBunlockAttr "R_PinkyFinger3.rz";
CBunlockAttr "R_RingFinger1.rz";
CBunlockAttr "R_RingFinger2.rz";
CBunlockAttr "R_RingFinger3.sx";
CBunlockAttr "Root.sx";
CBunlockAttr "Spine1.sx";
CBunlockAttr "Chest.sx";
CBunlockAttr "Neck.sx";
CBunlockAttr "HeadEnd.sx";
CBunlockAttr "R_Scapula.sx";
CBunlockAttr "R_Shoulder.sx";
CBunlockAttr "R_Elbow.sx";
CBunlockAttr "R_Wrist.sx";
CBunlockAttr "R_Hip.sx";
CBunlockAttr "R_Knee.sx";
CBunlockAttr "R_Ankle.sx";
CBunlockAttr "R_Toes.sx";
CBunlockAttr "R_ToesEnd.sx";
CBunlockAttr "R_Hand.sx";
CBunlockAttr "R_MiddleFinger1.sx";
CBunlockAttr "R_MiddleFinger2.sx";
CBunlockAttr "R_MiddleFinger3.sx";
CBunlockAttr "R_ThumbFinger1.sx";
CBunlockAttr "R_ThumbFinger2.sx";
CBunlockAttr "R_ThumbFinger3.sx";
CBunlockAttr "R_IndexFinger1.sx";
CBunlockAttr "R_IndexFinger2.sx";
CBunlockAttr "R_IndexFinger3.sx";
CBunlockAttr "R_PinkyFinger1.sx";
CBunlockAttr "R_PinkyFinger2.sx";
CBunlockAttr "R_PinkyFinger3.sx";
CBunlockAttr "R_RingFinger1.sx";
CBunlockAttr "R_RingFinger2.sx";
CBunlockAttr "R_RingFinger3.sy";
CBunlockAttr "Root.sy";
CBunlockAttr "Spine1.sy";
CBunlockAttr "Chest.sy";
CBunlockAttr "Neck.sy";
CBunlockAttr "HeadEnd.sy";
CBunlockAttr "R_Scapula.sy";
CBunlockAttr "R_Shoulder.sy";
CBunlockAttr "R_Elbow.sy";
CBunlockAttr "R_Wrist.sy";
CBunlockAttr "R_Hip.sy";
CBunlockAttr "R_Knee.sy";
CBunlockAttr "R_Ankle.sy";
CBunlockAttr "R_Toes.sy";
CBunlockAttr "R_ToesEnd.sy";
CBunlockAttr "R_Hand.sy";
CBunlockAttr "R_MiddleFinger1.sy";
CBunlockAttr "R_MiddleFinger2.sy";
CBunlockAttr "R_MiddleFinger3.sy";
CBunlockAttr "R_ThumbFinger1.sy";
CBunlockAttr "R_ThumbFinger2.sy";
CBunlockAttr "R_ThumbFinger3.sy";
CBunlockAttr "R_IndexFinger1.sy";
CBunlockAttr "R_IndexFinger2.sy";
CBunlockAttr "R_IndexFinger3.sy";
CBunlockAttr "R_PinkyFinger1.sy";
CBunlockAttr "R_PinkyFinger2.sy";
CBunlockAttr "R_PinkyFinger3.sy";
CBunlockAttr "R_RingFinger1.sy";
CBunlockAttr "R_RingFinger2.sy";
CBunlockAttr "R_RingFinger3.sz";
CBunlockAttr "Root.sz";
CBunlockAttr "Spine1.sz";
CBunlockAttr "Chest.sz";
CBunlockAttr "Neck.sz";
CBunlockAttr "HeadEnd.sz";
CBunlockAttr "R_Scapula.sz";
CBunlockAttr "R_Shoulder.sz";
CBunlockAttr "R_Elbow.sz";
CBunlockAttr "R_Wrist.sz";
CBunlockAttr "R_Hip.sz";
CBunlockAttr "R_Knee.sz";
CBunlockAttr "R_Ankle.sz";
CBunlockAttr "R_Toes.sz";
CBunlockAttr "R_ToesEnd.sz";
CBunlockAttr "R_Hand.sz";
CBunlockAttr "R_MiddleFinger1.sz";
CBunlockAttr "R_MiddleFinger2.sz";
CBunlockAttr "R_MiddleFinger3.sz";
CBunlockAttr "R_ThumbFinger1.sz";
CBunlockAttr "R_ThumbFinger2.sz";
CBunlockAttr "R_ThumbFinger3.sz";
CBunlockAttr "R_IndexFinger1.sz";
CBunlockAttr "R_IndexFinger2.sz";
CBunlockAttr "R_IndexFinger3.sz";
CBunlockAttr "R_PinkyFinger1.sz";
CBunlockAttr "R_PinkyFinger2.sz";
CBunlockAttr "R_PinkyFinger3.sz";
CBunlockAttr "R_RingFinger1.sz";
CBunlockAttr "R_RingFinger2.sz";
CBunlockAttr "R_RingFinger3.v";
CBunlockAttr "Root.v";
CBunlockAttr "Spine1.v";
CBunlockAttr "Chest.v";
CBunlockAttr "Neck.v";
CBunlockAttr "HeadEnd.v";
CBunlockAttr "R_Scapula.v";
CBunlockAttr "R_Shoulder.v";
CBunlockAttr "R_Elbow.v";
CBunlockAttr "R_Wrist.v";
CBunlockAttr "R_Hip.v";
CBunlockAttr "R_Knee.v";
CBunlockAttr "R_Ankle.v";
CBunlockAttr "R_Toes.v";
CBunlockAttr "R_ToesEnd.v";
CBunlockAttr "R_Hand.v";
CBunlockAttr "R_MiddleFinger1.v";
CBunlockAttr "R_MiddleFinger2.v";
CBunlockAttr "R_MiddleFinger3.v";
CBunlockAttr "R_ThumbFinger1.v";
CBunlockAttr "R_ThumbFinger2.v";
CBunlockAttr "R_ThumbFinger3.v";
CBunlockAttr "R_IndexFinger1.v";
CBunlockAttr "R_IndexFinger2.v";
CBunlockAttr "R_IndexFinger3.v";
CBunlockAttr "R_PinkyFinger1.v";
CBunlockAttr "R_PinkyFinger2.v";
CBunlockAttr "R_PinkyFinger3.v";
CBunlockAttr "R_RingFinger1.v";
CBunlockAttr "R_RingFinger2.v";
CBunlockAttr "R_RingFinger3.radi";
CBunlockAttr "Root.radi";
CBunlockAttr "Spine1.radi";
CBunlockAttr "Chest.radi";
CBunlockAttr "Neck.radi";
CBunlockAttr "HeadEnd.radi";
CBunlockAttr "R_Scapula.radi";
CBunlockAttr "R_Shoulder.radi";
CBunlockAttr "R_Elbow.radi";
CBunlockAttr "R_Wrist.radi";
CBunlockAttr "R_Hip.radi";
CBunlockAttr "R_Knee.radi";
CBunlockAttr "R_Ankle.radi";
CBunlockAttr "R_Toes.radi";
CBunlockAttr "R_ToesEnd.radi";
CBunlockAttr "R_Hand.radi";
CBunlockAttr "R_MiddleFinger1.radi";
CBunlockAttr "R_MiddleFinger2.radi";
CBunlockAttr "R_MiddleFinger3.radi";
CBunlockAttr "R_ThumbFinger1.radi";
CBunlockAttr "R_ThumbFinger2.radi";
CBunlockAttr "R_ThumbFinger3.radi";
CBunlockAttr "R_IndexFinger1.radi";
CBunlockAttr "R_IndexFinger2.radi";
CBunlockAttr "R_IndexFinger3.radi";
CBunlockAttr "R_PinkyFinger1.radi";
CBunlockAttr "R_PinkyFinger2.radi";
CBunlockAttr "R_PinkyFinger3.radi";
CBunlockAttr "R_RingFinger1.radi";
CBunlockAttr "R_RingFinger2.radi";

    """

    pm.mel.eval(mel_script)
    
    cmds.textField("Done_Setup_Bone", edit=True, text="Done Setup !")
    cmds.checkBox("Done_Setup_CheckBox", edit=True, value=True)


def mirrorBone(*arg):
    mel_script = """
select -r R_Scapula ;
mirrorJoint -mirrorYZ -mirrorBehavior -searchReplace "R_" "L_";
select -r R_Hip ;
mirrorJoint -mirrorYZ -mirrorBehavior -searchReplace "R_" "L_";
select -r R_Hand ;
mirrorJoint -mirrorYZ -mirrorBehavior -searchReplace "R_" "L_";
    """

    pm.mel.eval(mel_script)
    
    cmds.textField("Mirror_Text", edit=True, text="Done Mirror !")
    cmds.checkBox("Mirror_Checkbox", edit=True, value=True)


##################################################################### Build Auto
##################################################################### 

def buildAutoRig(*arg):

    ##################################################################### Build Controller
    Main_Grp = cmds.group(n="Basic_Rig_Tri3D", empty=True)

    Basic_Grp = cmds.group(n="System", empty=True)
    mel.eval("""
    setAttr -lock true -keyable false -channelBox false "System.tx";
    setAttr -lock true -keyable false -channelBox false "System.ty";
    setAttr -lock true -keyable false -channelBox false "System.tz";
    setAttr -lock true -keyable false -channelBox false "System.rx";
    setAttr -lock true -keyable false -channelBox false "System.ry";
    setAttr -lock true -keyable false -channelBox false "System.rz";
    setAttr -lock true -keyable false -channelBox false "System.v";

  
                   
    """)
    cmds.refresh(cv =1)
    cmds.parent(Basic_Grp, Main_Grp)

    Controller_grp = cmds.group(n="Controller", empty=True)
    cmds.parent(Controller_grp, Basic_Grp)

    SW_grp = cmds.group(n="IK_FK_SW_Grp", empty=True)
    cmds.parent(SW_grp, Controller_grp)

    Skeleton_grp = cmds.group(n="Skeleton", empty=True)
    cmds.parent(Skeleton_grp, Basic_Grp)

    IK_FK_System = cmds.group(n="IK_FK_System", empty=True)                                
    cmds.parent(IK_FK_System, Basic_Grp)

    Hip_grp = cmds.group(n="Hip_Ctrl_Grp", empty=True)                                
    cmds.parent(Hip_grp, Controller_grp)

    Hand_grp = cmds.group(n="Hand_Ctrl_Grp", empty=True)                                
    cmds.parent(Hand_grp, Controller_grp)

    Constraint_grp = cmds.group(n="Constraint_Grp", empty=True)
    cmds.parent(Constraint_grp, Basic_Grp)

    IK_Root_Crl_Grp = cmds.group(n="IK_Root_Grp", empty=True)
    cmds.parent(IK_Root_Crl_Grp, Controller_grp)

    ################################ Scale Ctrl
    Scale_Ctrl = cmds.curve(n="Scale", d=1, p=[(0, 0, 1.19),
        (0.6, 0, -0.6),
        (-0.6, 0, -0.6),
        (0, 0, 1.19),
        (0, 0.6, -0.6),
        (0, 0, -0.6),
        (0, -0.6, -0.6)])
    
    cmds.refresh(cv =1)
    mel.eval("""
    setAttr "Scale.visibility" 0;
    setAttr -lock true -keyable false -channelBox false "Scale.tx";
    setAttr -lock true -keyable false -channelBox false "Scale.ty";
    setAttr -lock true -keyable false -channelBox false "Scale.tz";
    setAttr -lock true -keyable false -channelBox false "Scale.rx";
    setAttr -lock true -keyable false -channelBox false "Scale.ry";
    setAttr -lock true -keyable false -channelBox false "Scale.rz";
    setAttr -lock true -keyable false -channelBox false "Scale.v";
    connectAttr -f Scale.scale System.scale;              
    """)
    cmds.parent(Scale_Ctrl, Main_Grp)

    cmds.refresh(cv =1)
    ################################ Main Ctrl
    Main_ctrl_grp = cmds.group(n="Main_Ctrl_Grp", empty=True)
    cmds.parent(Main_ctrl_grp, Controller_grp)

    Main_Controller = cmds.circle(n="Main_Controller", nr=(0, 1, 0), r=4)[0]
    cmds.addAttr(Main_Controller, longName='______________________', attributeType='enum', en='____________', keyable=True)
    mel.eval('setAttr -lock true "Main_Controller.______________________";')
    cmds.addAttr(Main_Controller, longName = 'Scale_Rig', attributeType = 'float', min = -100, max = 100, keyable=True) 
    cmds.listRelatives(Main_Controller, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Main_Controller), True)
    cmds.setAttr("{0}.overrideColor".format(Main_Controller), Color4)
    cmds.parent(Main_Controller, Main_ctrl_grp)


    cmds.refresh(cv =1)
    ################################ Body_Ctrl
    Body_Controller = cmds.xform(joint_Root, query=True, translation=True, worldSpace=True)
    Body_Controller_tuple = tuple(Body_Controller)
    Body_grp = cmds.group(n="Body_Ctrl_Grp", empty=True)
    cmds.xform(Body_grp, worldSpace=True, translation=Body_Controller_tuple)
    Body_Ctrl =cmds.curve(name="Body_Ctrl", d=1, p=[
    (-2.18, 0, 0.43), (-2.77, 0, 0.55), (-2.77, 0, 1.09), (-3.9, 0, 0),
    (-2.77, 0, -1.09), (-2.77, 0, -0.55), (-2.18, 0, -0.43), (-2.03, 0, -0.86),
    (-1.83, 0, -1.25), (-1.56, 0, -1.56), (-1.25, 0, -1.83), (-0.86, 0, -2.03),
    (-0.43, 0, -2.18), (-0.55, 0, -2.77), (-1.09, 0, -2.77), (0, 0, -3.9),
    (1.09, 0, -2.77), (0.55, 0, -2.77), (0.43, 0, -2.18), (0.86, 0, -2.03),
    (1.25, 0, -1.83), (1.56, 0, -1.56), (1.83, 0, -1.25), (2.03, 0, -0.86),
    (2.18, 0, -0.43), (2.77, 0, -0.55), (2.77, 0, -1.09), (3.9, 0, 0),
    (2.77, 0, 1.09), (2.77, 0, 0.55), (2.18, 0, 0.43), (2.03, 0, 0.86),
    (1.83, 0, 1.25), (1.56, 0, 1.56), (1.25, 0, 1.83), (0.86, 0, 2.03),
    (0.43, 0, 2.18), (0.55, 0, 2.77), (1.09, 0, 2.77), (0, 0, 3.9),
    (-1.09, 0, 2.77), (-0.55, 0, 2.77), (-0.43, 0, 2.18), (-0.86, 0, 2.03),
    (-1.25, 0, 1.83), (-1.56, 0, 1.56), (-1.83, 0, 1.25), (-2.03, 0, 0.86),
    (-2.18, 0, 0.43)])
    cmds.scale(1, 1, 1)
    cmds.addAttr(Body_Ctrl, longName='______________________', attributeType='enum', en='____________', keyable=True)    
    mel.eval('setAttr -lock true "Body_Ctrl.______________________";')
    cmds.addAttr(Body_Ctrl, longName = 'FK_IK', attributeType = 'float', min = 1, max = 10, keyable=True) 
    cmds.listRelatives(Body_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Body_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(Body_Ctrl), Color3) 
    cmds.xform(Body_Ctrl, worldSpace=True, translation=Body_Controller_tuple)
    cmds.parent(Body_Ctrl, Body_grp)
    cmds.makeIdentity(Body_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.parent(Body_grp, Controller_grp)
    
    cmds.refresh(cv =1)
	################################ Root Ctrl
    jointRoot = cmds.xform(joint_Root, query=True, translation=True, worldSpace=True)
    jointRoot_tuple = tuple(jointRoot)
    Root_grp = cmds.group(n="Root_Ctrl_Grp", empty=True)
    cmds.xform(Root_grp, worldSpace=True, translation=jointRoot_tuple)
    Root_Ctrl =cmds.curve(name="Root_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.listRelatives(Root_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Root_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(Root_Ctrl), Color1)
    cmds.xform(Root_Ctrl, worldSpace=True, translation=jointRoot_tuple)
    #cmds.makeIdentity(Root_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.parent(Root_Ctrl, Root_grp)
    cmds.matchTransform(Root_grp, joint_Root, rot=True)
    cmds.parent(Root_grp, Controller_grp)

    cmds.refresh(cv =1)
    ################################IK  Root Ctrl
    IK_Root_grp = cmds.group(n="IK_Root_Ctrl_Grp", empty=True)
    cmds.xform(IK_Root_grp, worldSpace=True, translation=jointRoot_tuple)
    IK_Root_Ctrl =cmds.curve(name="IK_Root_Ctrl", d=1, p=[
    (0.26, -2.1, -2.1), (0.26, 2.1, -2.1), (0.26, 2.1, 2.1), (-0.26, 2.1, 2.1), 
    (-0.26, 2.1, -2.1), (0.26, 2.1, -2.1), (0.26, 2.1, 2.1), (0.26, -2.1, 2.1), 
    (0.26, -2.1, -2.1), (-0.26, -2.1, -2.1), (-0.26, 2.1, -2.1), (-0.26, 2.1, 2.1), 
    (-0.26, -2.1, 2.1), (-0.26, -2.1, -2.1), (-0.26, -2.1, 2.1), (0.26, -2.1, 2.1)])
    cmds.listRelatives(IK_Root_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(IK_Root_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(IK_Root_Ctrl), Color2)
    cmds.xform(IK_Root_Ctrl, worldSpace=True, translation=jointRoot_tuple)
    cmds.parent(IK_Root_Ctrl, IK_Root_grp)
    cmds.matchTransform(IK_Root_grp, joint_Root, rot=True)
    cmds.parent(IK_Root_grp, IK_Root_Crl_Grp)
    joint_Root_Ctrl = cmds.joint(n="Root_Ctrl_Jnt", radius=2)
    cmds.parent(joint_Root_Ctrl, IK_Root_Ctrl)
    cmds.makeIdentity(joint_Root_Ctrl, apply=True, translate=True, rotate=True, scale=True)
            
    cmds.refresh(cv =1)
    ################################ Spine1
    JointSpine = cmds.xform(joint_Spine1, query=True, translation=True, worldSpace=True)
    JointSpine_tuple = tuple(JointSpine)
    Spine_grp = cmds.group(n="Spine_Ctrl_Grp", empty=True)
    cmds.xform(Spine_grp, worldSpace=True, translation=JointSpine_tuple)
    Spine_Ctrl =cmds.curve(name="Spine_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.listRelatives(Spine_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Spine_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(Spine_Ctrl), Color1)
    cmds.xform(Spine_Ctrl, worldSpace=True, translation=JointSpine_tuple)
    cmds.parent(Spine_Ctrl, Spine_grp)
    cmds.makeIdentity(Spine_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(Spine_grp, joint_Spine1, rot=True)
    cmds.parent(Spine_grp, Root_Ctrl)
    
    cmds.refresh(cv =1)
    ################################ Chest
    jointChest = cmds.xform(joint_Chest, query=True, translation=True, worldSpace=True)
    jointChest_tuple = tuple(jointChest)
    Chest_grp = cmds.group(n="Chest_Ctrl_Grp", empty=True)
    cmds.xform(Chest_grp, worldSpace=True, translation=jointChest_tuple)
    Chest_Ctrl =cmds.curve(name="Chest_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.listRelatives(Chest_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Chest_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(Chest_Ctrl), Color1)
    cmds.xform(Chest_Ctrl, worldSpace=True, translation=jointChest_tuple)
    cmds.parent(Chest_Ctrl, Chest_grp)
    cmds.makeIdentity(Chest_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(Chest_grp, joint_Chest, rot=True)
    cmds.parent(Chest_grp, Spine_Ctrl)

    cmds.refresh(cv =1)
    ################################IK  Chest Ctrl
    IK_Chest_grp = cmds.group(n="IK_Chest_Ctrl_Grp", empty=True)
    cmds.xform(IK_Chest_grp, worldSpace=True, translation=jointChest_tuple)
    IK_Chest_Ctrl =cmds.curve(name="IK_Chest_Ctrl", d=1, p=[
    (0.26, -2.1, -2.1), (0.26, 2.1, -2.1), (0.26, 2.1, 2.1), (-0.26, 2.1, 2.1),
    (-0.26, 2.1, -2.1), (0.26, 2.1, -2.1), (0.26, 2.1, 2.1), (0.26, -2.1, 2.1),
    (0.26, -2.1, -2.1), (-0.26, -2.1, -2.1), (-0.26, 2.1, -2.1), (-0.26, 2.1, 2.1),
    (-0.26, -2.1, 2.1), (-0.26, -2.1, -2.1), (-0.26, -2.1, 2.1), (0.26, -2.1, 2.1)])
    cmds.listRelatives(IK_Chest_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(IK_Chest_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(IK_Chest_Ctrl), Color2)
    cmds.xform(IK_Chest_Ctrl, worldSpace=True, translation=jointChest_tuple)
    cmds.parent(IK_Chest_Ctrl, IK_Chest_grp)
    cmds.matchTransform(IK_Chest_grp, joint_Chest, rot=True)
    cmds.parent(IK_Chest_grp, IK_Root_Crl_Grp)    
    joint_Chest_Ctrl = cmds.joint(n="Chest_Ctrl_Jnt", radius=2)
    cmds.parent(joint_Chest_Ctrl, IK_Chest_Ctrl)
    cmds.makeIdentity(joint_Chest_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.refresh(cv =1)
    ################################ Neck
    jointNeck = cmds.xform(joint_Neck, query=True, translation=True, worldSpace=True)
    jointNeck_tuple = tuple(jointNeck)
    Neck_grp = cmds.group(n="Neck_Ctrl_Grp", empty=True)
    cmds.xform(Neck_grp, worldSpace=True, translation=jointNeck_tuple)
    Neck_Ctrl =cmds.curve(name="Neck_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.5, 0.5, 0.5)
    cmds.addAttr(Neck_Ctrl, longName = 'Global', attributeType = 'float', min = 1, max = 10, keyable=True) 
    cmds.listRelatives(Neck_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Neck_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(Neck_Ctrl), Color1)
    cmds.xform(Neck_Ctrl, worldSpace=True, translation=jointNeck_tuple)
    cmds.parent(Neck_Ctrl, Neck_grp)
    cmds.makeIdentity(Neck_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(Neck_grp, joint_Neck, rot=True)
    cmds.parent(Neck_grp, Controller_grp)

    cmds.refresh(cv =1)
    ################################ L_Hip
    jointLHip = cmds.xform(joint_LHip, query=True, translation=True, worldSpace=True)
    joint_LHip_tuple = tuple(jointLHip)
    L_Hip_grp = cmds.group(n="L_Hip_Ctrl_Grp", empty=True)
    cmds.xform(L_Hip_grp, worldSpace=True, translation=joint_LHip_tuple)
    L_Hip_Ctrl =cmds.curve(name="L_Hip_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.5, 0.5, 0.5)
    cmds.listRelatives(L_Hip_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_Hip_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_Hip_Ctrl), Color1)
    cmds.xform(L_Hip_Ctrl, worldSpace=True, translation=joint_LHip_tuple)
    cmds.parent(L_Hip_Ctrl, L_Hip_grp)
    cmds.makeIdentity(L_Hip_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_Hip_grp, joint_LHip, rot=True)
    cmds.parent(L_Hip_grp, Hip_grp)

    cmds.refresh(cv =1)
    ################################ L_Knee
    jointLKnee = cmds.xform(joint_LKnee, query=True, translation=True, worldSpace=True)
    joint_LKnee_tuple = tuple(jointLKnee)
    L_Knee_grp = cmds.group(n="L_Knee_Ctrl_Grp", empty=True)
    cmds.xform(L_Knee_grp, worldSpace=True, translation=joint_LKnee_tuple)
    L_Knee_Ctrl =cmds.curve(name="L_Knee_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.4, 0.4, 0.4)
    cmds.listRelatives(L_Knee_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_Knee_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_Knee_Ctrl), Color1)
    cmds.xform(L_Knee_Ctrl, worldSpace=True, translation=joint_LKnee_tuple)
    cmds.parent(L_Knee_Ctrl, L_Knee_grp)
    cmds.makeIdentity(L_Knee_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_Knee_grp, joint_LKnee, rot=True)
    cmds.parent(L_Knee_grp, L_Hip_Ctrl)
    
    cmds.refresh(cv =1)
	################################ L_Ankle
    jointLAnkle = cmds.xform(joint_LAnkle, query=True, translation=True, worldSpace=True)
    joint_LAnkle_tuple = tuple(jointLAnkle)
    L_Ankle_grp = cmds.group(n="L_Ankle_Ctrl_Grp", empty=True)
    cmds.xform(L_Ankle_grp, worldSpace=True, translation=joint_LAnkle_tuple)
    L_Ankle_Ctrl =cmds.curve(name="L_Ankle_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.4, 0.4, 0.4)
    cmds.listRelatives(L_Ankle_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_Ankle_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_Ankle_Ctrl), Color1)
    cmds.xform(L_Ankle_Ctrl, worldSpace=True, translation=joint_LAnkle_tuple)
    cmds.parent(L_Ankle_Ctrl, L_Ankle_grp)
    cmds.makeIdentity(L_Ankle_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_Ankle_grp, joint_LAnkle, rot=True)
    cmds.parent(L_Ankle_grp, L_Knee_Ctrl)
    
    cmds.refresh(cv =1)
    ###################################################################### IK FK SW L
    L_IKFKROOTGRP = cmds.xform(joint_LAnkle, query=True, translation=True, worldSpace=True)
    L_IKFKROOTGRP_tuple = tuple(L_IKFKROOTGRP)
    L_IKFKROOT_grp = cmds.group(n="L_IKFKFOOT_Grp", empty=True)
    cmds.parent(L_IKFKROOT_grp, SW_grp)
    cmds.parentConstraint(L_Ankle_Ctrl, L_IKFKROOT_grp)
    cmds.xform(L_IKFKROOT_grp, worldSpace=True, translation=L_IKFKROOTGRP_tuple)
    L_IKFKROOT_Ctrl =cmds.curve(name="L_IK_FK_Foot_Ctrl", d=1, p=[
    (0, 0, 0),(0, 1.1, 0),(-0.09, 1.1, 0),(-0.17, 1.13, 0),(-0.25, 1.16, 0),(-0.32, 1.2, 0),(-0.39, 1.26, 0),
    (-0.44, 1.32, 0),(-0.49, 1.4, 0),(-0.52, 1.48, 0),(-0.54, 1.56, 0),(-0.55, 1.65, 0),
    (-0.54, 1.73, 0),(-0.52, 1.82, 0),(-0.49, 1.89, 0),(-0.44, 1.97, 0),(-0.39, 2.04, 0),
    (-0.32, 2.09, 0),(-0.25, 2.13, 0),(-0.17, 2.17, 0),(-0.09, 2.19, 0),(0, 2.2, 0),
    (0.09, 2.19, 0),(0.17, 2.17, 0),(0.25, 2.13, 0),(0.32, 2.09, 0),(0.39, 2.04, 0),
    (0.44, 1.97, 0),(0.49, 1.89, 0),(0.52, 1.82, 0),(0.54, 1.73, 0),(0.55, 1.65, 0),
    (0.54, 1.56, 0),(0.52, 1.48, 0),(0.49, 1.4, 0),(0.44, 1.32, 0),(0.39, 1.26, 0),
    (0.32, 1.2, 0),(0.25, 1.16, 0),(0.17, 1.13, 0),(0.17, 1.13, 0),(0.09, 1.1, 0),(0, 1.1, 0)])
    # cmds.scale(0.1, 0.1, 0.1, L_IKFKROOT_Ctrl)
    cmds.listRelatives(L_IKFKROOT_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_IKFKROOT_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_IKFKROOT_Ctrl), Color3)
    cmds.parent(L_IKFKROOT_Ctrl, L_IKFKROOT_grp)
    attributes = ['translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ']
    [cmds.setAttr('{}.{}'.format(L_IKFKROOT_Ctrl, attr), 0) for attr in attributes]
    # mel.eval('FreezeTransformations;')
    # cmds.matchTransform(L_IKFKROOT_grp, joint_LAnkle, rot=True)

	################################ L_Toes
    jointLToes = cmds.xform(joint_LToes, query=True, translation=True, worldSpace=True)
    joint_LToes_tuple = tuple(jointLToes)
    L_Toes_grp = cmds.group(n="L_Toes_Ctrl_Grp", empty=True)
    cmds.xform(L_Toes_grp, worldSpace=True, translation=joint_LToes_tuple)
    L_Toes_Ctrl =cmds.curve(name="L_Toes_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.3, 0.3, 0.3)
    cmds.listRelatives(L_Toes_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_Toes_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_Toes_Ctrl), Color1)
    cmds.xform(L_Toes_Ctrl, worldSpace=True, translation=joint_LToes_tuple)
    cmds.parent(L_Toes_Ctrl, L_Toes_grp)
    cmds.makeIdentity(L_Toes_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_Toes_grp, joint_LToes, rot=True)
    cmds.parent(L_Toes_grp, L_Ankle_Ctrl)

    cmds.refresh(cv =1)
	################################ L_Spacula
    jointLScapula = cmds.xform(joint_LScapula, query=True, translation=True, worldSpace=True)
    joint_LScapula_tuple = tuple(jointLScapula)
    L_Scapula_grp = cmds.group(n="L_Scapula_Ctrl_Grp", empty=True)
    cmds.xform(L_Scapula_grp, worldSpace=True, translation=joint_LScapula_tuple)
    L_Scapula_Ctrl =cmds.curve(name="L_Scapula_Ctrl", d=1, p=[
    (-0.84, -1.33, -0.84), (-0.82, -1.29, -1.09), (-0.8, -1.21, -1.33), (-0.77, -1.07, -1.56),
    (-0.9, -1.07, -1.43), (-1.03, -1.07, -1.3), (-1.12, -0.91, -1.39), (-1.19, -0.71, -1.45),
    (-1.24, -0.48, -1.51), (-1.27, -0.25, -1.54), (-1.28, 0, -1.55), (-1.27, 0.25, -1.54),
    (-1.24, 0.48, -1.51), (-1.19, 0.71, -1.45), (-1.12, 0.91, -1.39), (-1.03, 1.07, -1.3),
    (-0.9, 1.07, -1.43), (-0.77, 1.07, -1.56), (-0.8, 1.21, -1.33), (-0.82, 1.29, -1.09),
    (-0.84, 1.33, -0.84), (-1.09, 1.29, -0.82), (-1.33, 1.21, -0.8), (-1.56, 1.07, -0.77),
    (-1.43, 1.07, -0.9), (-1.3, 1.07, -1.03), (-1.39, 0.91, -1.12), (-1.45, 0.71, -1.19),
    (-1.51, 0.48, -1.24), (-1.54, 0.25, -1.27), (-1.55, 0, -1.28), (-1.54, -0.25, -1.27),
    (-1.51, -0.48, -1.24), (-1.45, -0.71, -1.19), (-1.39, -0.91, -1.12), (-1.3, -1.07, -1.03),
    (-1.43, -1.07, -0.9), (-1.56, -1.07, -0.77), (-1.33, -1.21, -0.8), (-1.09, -1.29, -0.82),
    (-0.84, -1.33, -0.84)])
    cmds.scale(0.8, 0.8, 0.8)
    cmds.listRelatives(L_Scapula_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_Scapula_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_Scapula_Ctrl), Color3)
    cmds.xform(L_Scapula_Ctrl, worldSpace=True, translation=joint_LScapula_tuple)
    cmds.parent(L_Scapula_Ctrl, L_Scapula_grp)
    cmds.makeIdentity(L_Scapula_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_Scapula_grp, joint_LScapula, rot=True)
    cmds.parent(L_Scapula_grp, Hand_grp)

    cmds.refresh(cv =1)
    ################################ L_Shoulder
    jointLShoulder = cmds.xform(joint_LShoulder, query=True, translation=True, worldSpace=True)
    joint_LShoulder_tuple = tuple(jointLShoulder)
    L_Shoulder_All_grp = cmds.group(n="L_Shoulder_Grp", empty=True)
    cmds.parent(L_Shoulder_All_grp, Hand_grp)
    cmds.makeIdentity(L_Shoulder_All_grp, apply=True, translate=True, rotate=True, scale=True)
    L_Shoulder_grp = cmds.group(n="L_Shoulder_Ctrl_Grp", empty=True)
    cmds.xform(L_Shoulder_grp, worldSpace=True, translation=joint_LShoulder_tuple)
    L_Shoulder_Ctrl =cmds.curve(name="L_Shoulder_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.5, 0.5, 0.5)
    cmds.listRelatives(L_Shoulder_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_Shoulder_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_Shoulder_Ctrl), Color1)
    cmds.xform(L_Shoulder_Ctrl, worldSpace=True, translation=joint_LShoulder_tuple)
    cmds.parent(L_Shoulder_Ctrl, L_Shoulder_grp)
    cmds.makeIdentity(L_Shoulder_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_Shoulder_grp, joint_LShoulder, rot=True)
    cmds.parent(L_Shoulder_grp, L_Shoulder_All_grp)
    cmds.makeIdentity(L_Shoulder_grp, apply=True, translate=True, rotate=True, scale=True)

    cmds.refresh(cv =1)
    ################################ L_Elbow
    jointLElbow = cmds.xform(joint_LElbow, query=True, translation=True, worldSpace=True)
    joint_LElbow_tuple = tuple(jointLElbow)
    L_Elbow_grp = cmds.group(n="L_Elbow_Ctrl_Grp", empty=True)
    cmds.xform(L_Elbow_grp, worldSpace=True, translation=joint_LElbow_tuple)
    L_Elbow_Ctrl =cmds.curve(name="L_Elbow_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.4, 0.4, 0.4)
    cmds.listRelatives(L_Elbow_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_Elbow_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_Elbow_Ctrl), Color1)
    cmds.xform(L_Elbow_Ctrl, worldSpace=True, translation=joint_LElbow_tuple)
    cmds.parent(L_Elbow_Ctrl, L_Elbow_grp)
    cmds.makeIdentity(L_Elbow_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_Elbow_grp, joint_LElbow, rot=True)
    cmds.parent(L_Elbow_grp, L_Shoulder_Ctrl)
    
    cmds.refresh(cv =1)
    ################################ L_Wrist
    jointLWrist = cmds.xform(joint_LWrist, query=True, translation=True, worldSpace=True)
    joint_LWrist_tuple = tuple(jointLWrist)
    L_Wrist_grp = cmds.group(n="L_Wrist_Ctrl_Grp", empty=True)
    cmds.xform(L_Wrist_grp, worldSpace=True, translation=joint_LWrist_tuple)
    L_Wrist_Ctrl =cmds.curve(name="L_Wrist_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.3, 0.3, 0.3, L_Wrist_Ctrl)
    cmds.listRelatives(L_Wrist_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_Wrist_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_Wrist_Ctrl), Color1)
    cmds.xform(L_Wrist_Ctrl, worldSpace=True, translation=joint_LWrist_tuple)
    cmds.parent(L_Wrist_Ctrl, L_Wrist_grp)
    cmds.makeIdentity(L_Wrist_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_Wrist_grp, joint_LWrist, rot=True)
    cmds.parent(L_Wrist_grp, L_Elbow_Ctrl)

    cmds.refresh(cv =1)
    ################################ R_Hip
    jointRHip = cmds.xform(joint_RHip, query=True, translation=True, worldSpace=True)
    joint_RHip_tuple = tuple(jointRHip)
    R_Hip_grp = cmds.group(n="R_Hip_Ctrl_Grp", empty=True)
    cmds.xform(R_Hip_grp, worldSpace=True, translation=joint_RHip_tuple)
    R_Hip_Ctrl =cmds.curve(name="R_Hip_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.5, 0.5, 0.5)
    cmds.listRelatives(R_Hip_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_Hip_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_Hip_Ctrl), Color1)
    cmds.xform(R_Hip_Ctrl, worldSpace=True, translation=joint_RHip_tuple)
    cmds.parent(R_Hip_Ctrl, R_Hip_grp)
    cmds.makeIdentity(R_Hip_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_Hip_grp, joint_RHip, rot=True)
    cmds.parent(R_Hip_grp, Hip_grp)

    cmds.refresh(cv =1)
    ################################ R_Knee
    jointRKnee = cmds.xform(joint_RKnee, query=True, translation=True, worldSpace=True)
    joint_RKnee_tuple = tuple(jointRKnee)
    R_Knee_grp = cmds.group(n="R_Knee_Ctrl_Grp", empty=True)
    cmds.xform(R_Knee_grp, worldSpace=True, translation=joint_RKnee_tuple)
    R_Knee_Ctrl =cmds.curve(name="R_Knee_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.4, 0.4, 0.4)
    cmds.listRelatives(R_Knee_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_Knee_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_Knee_Ctrl), Color1)
    cmds.xform(R_Knee_Ctrl, worldSpace=True, translation=joint_RKnee_tuple)
    cmds.parent(R_Knee_Ctrl, R_Knee_grp)
    cmds.makeIdentity(R_Knee_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_Knee_grp, joint_RKnee, rot=True)
    cmds.parent(R_Knee_grp, R_Hip_Ctrl)
    
    cmds.refresh(cv =1)
	################################ R_Ankle
    jointRAnkle = cmds.xform(joint_RAnkle, query=True, translation=True, worldSpace=True)
    joint_RAnkle_tuple = tuple(jointRAnkle)
    R_Ankle_grp = cmds.group(n="R_Ankle_Ctrl_Grp", empty=True)
    cmds.xform(R_Ankle_grp, worldSpace=True, translation=joint_RAnkle_tuple)
    R_Ankle_Ctrl =cmds.curve(name="R_Ankle_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.4, 0.4, 0.4)
    cmds.listRelatives(R_Ankle_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_Ankle_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_Ankle_Ctrl), Color1)
    cmds.xform(R_Ankle_Ctrl, worldSpace=True, translation=joint_RAnkle_tuple)
    cmds.parent(R_Ankle_Ctrl, R_Ankle_grp)
    cmds.makeIdentity(R_Ankle_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_Ankle_grp, joint_RAnkle, rot=True)
    cmds.parent(R_Ankle_grp, R_Knee_Ctrl)

    cmds.refresh(cv =1)
    ###################################################################### IK FK SW R
    R_IKFKROOTGRP = cmds.xform(joint_RAnkle, query=True, translation=True, worldSpace=True)
    R_IKFKROOTGRP_tuple = tuple(R_IKFKROOTGRP)
    R_IKFKROOT_grp = cmds.group(n="R_IKFKFOOT_Grp", empty=True)
    cmds.parent(R_IKFKROOT_grp, SW_grp)
    cmds.parentConstraint(R_Ankle_Ctrl, R_IKFKROOT_grp)
    cmds.xform(R_IKFKROOT_grp, worldSpace=True, translation=R_IKFKROOTGRP_tuple)
    R_IKFKROOT_Ctrl =cmds.curve(name="R_IK_FK_Foot_Ctrl", d=1, p=[
    (0, 0, 0),(0, -1.08, 0),(-0.09, -1.09, 0),(-0.17, -1.11, 0),(-0.25, -1.14, 0),(-0.32, -1.18, 0),
    (-0.38, -1.24, 0),(-0.44, -1.3, 0),(-0.48, -1.38, 0),(-0.51, -1.45, 0),(-0.53, -1.53, 0),
    (-0.54, -1.62, 0),(-0.53, -1.71, 0),(-0.51, -1.79, 0),(-0.48, -1.86, 0),(-0.44, -1.94, 0),
    (-0.38, -2, 0),(-0.32, -2.06, 0),(-0.25, -2.1, 0),(-0.17, -2.13, 0),(-0.09, -2.15, 0),
    (0, -2.16, 0),(0.09, -2.15, 0),(0.17, -2.13, 0),(0.25, -2.1, 0),(0.32, -2.06, 0),
    (0.38, -2, 0),(0.44, -1.94, 0),(0.48, -1.86, 0),(0.51, -1.79, 0),(0.53, -1.71, 0),
    (0.54, -1.62, 0),(0.53, -1.53, 0),(0.51, -1.45, 0),(0.48, -1.38, 0),(0.44, -1.3, 0),(0.38, -1.24, 0),
    (0.32, -1.18, 0),(0.25, -1.14, 0),(0.17, -1.11, 0),(0.17, -1.11, 0),(0.09, -1.09, 0),(0, -1.08, 0)])
    #cmds.scale(0.054, 0.054, 0.054, R_IKFKROOT_Ctrl)
    cmds.listRelatives(R_IKFKROOT_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_IKFKROOT_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_IKFKROOT_Ctrl), Color3)
    cmds.parent(R_IKFKROOT_Ctrl, R_IKFKROOT_grp)
    attributes = ['translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ']
    [cmds.setAttr('{}.{}'.format(R_IKFKROOT_Ctrl, attr), 0) for attr in attributes]
    # mel.eval('FreezeTransformations;')
    # cmds.matchTransform(R_IKFKROOT_grp, joint_LAnkle, rot=True)

    cmds.refresh(cv =1)
	################################ R_Toes
    jointRToes = cmds.xform(joint_RToes, query=True, translation=True, worldSpace=True)
    joint_RToes_tuple = tuple(jointRToes)
    R_Toes_grp = cmds.group(n="R_Toes_Ctrl_Grp", empty=True)
    cmds.xform(R_Toes_grp, worldSpace=True, translation=joint_RToes_tuple)
    R_Toes_Ctrl =cmds.curve(name="R_Toes_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.3, 0.3, 0.3)
    cmds.listRelatives(R_Toes_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_Toes_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_Toes_Ctrl), Color1)
    cmds.xform(R_Toes_Ctrl, worldSpace=True, translation=joint_RToes_tuple)
    cmds.parent(R_Toes_Ctrl, R_Toes_grp)
    cmds.makeIdentity(R_Toes_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_Toes_grp, joint_RToes, rot=True)
    cmds.parent(R_Toes_grp, R_Ankle_Ctrl)

    cmds.refresh(cv =1)
	################################ R_Spacula
    jointRScapula = cmds.xform(joint_RScapula, query=True, translation=True, worldSpace=True)
    joint_RScapula_tuple = tuple(jointRScapula)
    R_Scapula_grp = cmds.group(n="R_Scapula_Ctrl_Grp", empty=True)
    cmds.xform(R_Scapula_grp, worldSpace=True, translation=joint_RScapula_tuple)
    R_Scapula_Ctrl =cmds.curve(name="R_Scapula_Ctrl", d=1, p=[
    (0.84, -1.33, 0.84), (0.82, -1.29, 1.09), (0.8, -1.21, 1.33), (0.77, -1.07, 1.56),
    (0.9, -1.07, 1.43), (1.03, -1.07, 1.3), (1.12, -0.91, 1.39), (1.19, -0.71, 1.45),
    (1.24, -0.48, 1.51), (1.27, -0.25, 1.54), (1.28, 0, 1.55), (1.27, 0.25, 1.54),
    (1.24, 0.48, 1.51), (1.19, 0.71, 1.45), (1.12, 0.91, 1.39), (1.03, 1.07, 1.3),
    (0.9, 1.07, 1.43), (0.77, 1.07, 1.56), (0.8, 1.21, 1.33), (0.82, 1.29, 1.09),
    (0.84, 1.33, 0.84), (1.09, 1.29, 0.82), (1.33, 1.21, 0.8), (1.56, 1.07, 0.77),
    (1.43, 1.07, 0.9), (1.3, 1.07, 1.03), (1.39, 0.91, 1.12), (1.45, 0.71, 1.19),
    (1.51, 0.48, 1.24), (1.54, 0.25, 1.27), (1.55, 0, 1.28), (1.54, -0.25, 1.27),
    (1.51, -0.48, 1.24), (1.45, -0.71, 1.19), (1.39, -0.91, 1.12), (1.3, -1.07, 1.03),
    (1.43, -1.07, 0.9), (1.56, -1.07, 0.77), (1.33, -1.21, 0.8), (1.09, -1.29, 0.82),
    (0.84, -1.33, 0.84)])
    cmds.scale(0.8, 0.8, 0.8)
    cmds.listRelatives(R_Scapula_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_Scapula_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_Scapula_Ctrl), Color3)
    cmds.xform(R_Scapula_Ctrl, worldSpace=True, translation=joint_RScapula_tuple)
    cmds.parent(R_Scapula_Ctrl, R_Scapula_grp)
    cmds.makeIdentity(R_Scapula_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_Scapula_grp, joint_RScapula, rot=True)
    cmds.parent(R_Scapula_grp, Hand_grp)

    cmds.refresh(cv =1)
    ################################ R_Shoulder
    jointRShoulder = cmds.xform(joint_RShoulder, query=True, translation=True, worldSpace=True)
    joint_RShoulder_tuple = tuple(jointRShoulder)
    R_Shoulder_All_grp = cmds.group(n="R_Shoulder_Grp", empty=True)
    cmds.parent(R_Shoulder_All_grp, Hand_grp)
    cmds.makeIdentity(R_Shoulder_All_grp, apply=True, translate=True, rotate=True, scale=True)
    R_Shoulder_grp = cmds.group(n="R_Shoulder_Ctrl_Grp", empty=True)
    cmds.xform(R_Shoulder_grp, worldSpace=True, translation=joint_RShoulder_tuple)
    R_Shoulder_Ctrl =cmds.curve(name="R_Shoulder_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.5, 0.5, 0.5)
    cmds.listRelatives(R_Shoulder_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_Shoulder_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_Shoulder_Ctrl), Color1)
    cmds.xform(R_Shoulder_Ctrl, worldSpace=True, translation=joint_RShoulder_tuple)
    cmds.parent(R_Shoulder_Ctrl, R_Shoulder_grp)
    cmds.makeIdentity(R_Shoulder_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_Shoulder_grp, joint_RShoulder, rot=True)
    cmds.parent(R_Shoulder_grp, R_Shoulder_All_grp)
    cmds.makeIdentity(R_Shoulder_grp, apply=True, translate=True, rotate=True, scale=True)
    #cmds.parentConstraint(R_Shoulder_grp, R_Shoulder_All_grp)

    cmds.refresh(cv =1)
    ################################ R_Elbow
    jointRElbow = cmds.xform(joint_RElbow, query=True, translation=True, worldSpace=True)
    joint_RElbow_tuple = tuple(jointRElbow)
    R_Elbow_grp = cmds.group(n="R_Elbow_Ctrl_Grp", empty=True)
    cmds.xform(R_Elbow_grp, worldSpace=True, translation=joint_RElbow_tuple)
    R_Elbow_Ctrl =cmds.curve(name="R_Elbow_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.4, 0.4, 0.4)
    cmds.listRelatives(R_Elbow_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_Elbow_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_Elbow_Ctrl), Color1)
    cmds.xform(R_Elbow_Ctrl, worldSpace=True, translation=joint_RElbow_tuple)
    cmds.parent(R_Elbow_Ctrl, R_Elbow_grp)
    cmds.makeIdentity(R_Elbow_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_Elbow_grp, joint_RElbow, rot=True)
    cmds.parent(R_Elbow_grp, R_Shoulder_Ctrl)
    
    cmds.refresh(cv =1)
    ################################ R_Wrist
    jointRWrist = cmds.xform(joint_RWrist, query=True, translation=True, worldSpace=True)
    joint_RWrist_tuple = tuple(jointRWrist)
    R_Wrist_grp = cmds.group(n="R_Wrist_Ctrl_Grp", empty=True)
    cmds.xform(R_Wrist_grp, worldSpace=True, translation=joint_RWrist_tuple)
    R_Wrist_Ctrl =cmds.curve(name="R_Wrist_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.3, 0.3, 0.3, R_Wrist_Ctrl)
    cmds.listRelatives(R_Wrist_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_Wrist_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_Wrist_Ctrl), Color1)
    cmds.xform(R_Wrist_Ctrl, worldSpace=True, translation=joint_RWrist_tuple)
    cmds.parent(R_Wrist_Ctrl, R_Wrist_grp)
    cmds.makeIdentity(R_Wrist_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_Wrist_grp, joint_RWrist, rot=True)
    cmds.parent(R_Wrist_grp, R_Elbow_Ctrl)


    cmds.refresh(cv =1)
    ################################ L_Hand
    jointLHand = cmds.xform(joint_LHand, query=True, translation=True, worldSpace=True)
    joint_LHand_tuple = tuple(jointLHand)
    L_Hand_grp = cmds.group(n="L_Hand_CtrL_Grp", empty=True)
    cmds.xform(L_Hand_grp, worldSpace=True, translation=joint_LHand_tuple)
    L_Hand_Ctrl =cmds.curve(name="L_Hand_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.1, 0.1, 0.1, L_Hand_Ctrl)
    cmds.listRelatives(L_Hand_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_Hand_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_Hand_Ctrl), Color1)
    L_IKFK_Ctrl =cmds.curve(name="L_IKFK_Hand_Ctrl", d=1, p=[
    (-1.35, 0.85, 0),(-1.48, 0.85, 0),(-1.74, 0.8, 0),(-2.07, 0.62, 0),(-2.3, 0.33, 0),(-2.37, 0, 0),(-2.3, -0.33, 0),
    (-2.07, -0.62, 0),(-1.74, -0.8, 0),(-1.48, -0.85, 0),(-1.35, -0.85, 0)])
    #cmds.scale(0.1, 0.1, 0.1, L_IKFK_Ctrl)
    cmds.listRelatives(L_IKFK_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_IKFK_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_IKFK_Ctrl), Color3)
    cmds.xform(L_Hand_Ctrl, worldSpace=True, translation=joint_LHand_tuple)
    cmds.xform(L_IKFK_Ctrl, worldSpace=True, translation=joint_LHand_tuple)
    cmds.parent(L_IKFK_Ctrl, L_Hand_Ctrl)
    cmds.parent(L_Hand_Ctrl, L_Hand_grp)
    cmds.makeIdentity(L_Hand_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.makeIdentity(L_IKFK_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_Hand_grp, joint_LHand, rot=True)
    cmds.parent(L_Hand_grp, Hand_grp)
    # cmds.parentConstraint(L_Wrist_Ctrl, L_Hand_grp)
        
    cmds.refresh(cv =1)
    ################################ L_ThumbFinger1
    jointLThumbFinger1 = cmds.xform(joint_LThumbFinger1, query=True, translation=True, worldSpace=True)
    joint_LThumbFinger1_tuple = tuple(jointLThumbFinger1)
    L_ThumbFinger1_grp = cmds.group(n="L_ThumbFinger1_CtrL_Grp", empty=True)
    cmds.xform(L_ThumbFinger1_grp, worldSpace=True, translation=joint_LThumbFinger1_tuple)
    L_ThumbFinger1_Ctrl =cmds.curve(name="L_ThumbFinger1_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, L_ThumbFinger1_Ctrl)
    cmds.listRelatives(L_ThumbFinger1_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_ThumbFinger1_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_ThumbFinger1_Ctrl), Color1)
    cmds.xform(L_ThumbFinger1_Ctrl, worldSpace=True, translation=joint_LThumbFinger1_tuple)
    cmds.parent(L_ThumbFinger1_Ctrl, L_ThumbFinger1_grp)
    cmds.makeIdentity(L_ThumbFinger1_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_ThumbFinger1_grp, joint_LThumbFinger1, rot=True)
    cmds.parent(L_ThumbFinger1_grp, L_Hand_Ctrl)  
            
    cmds.refresh(cv =1)
    ################################ L_ThumbFinger2
    jointLThumbFinger2 = cmds.xform(joint_LThumbFinger2, query=True, translation=True, worldSpace=True)
    joint_LThumbFinger2_tuple = tuple(jointLThumbFinger2)
    L_ThumbFinger2_grp = cmds.group(n="L_ThumbFinger2_CtrL_Grp", empty=True)
    cmds.xform(L_ThumbFinger2_grp, worldSpace=True, translation=joint_LThumbFinger2_tuple)
    L_ThumbFinger2_Ctrl =cmds.curve(name="L_ThumbFinger2_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, L_ThumbFinger2_Ctrl)
    cmds.listRelatives(L_ThumbFinger2_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_ThumbFinger2_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_ThumbFinger2_Ctrl), Color1)
    cmds.xform(L_ThumbFinger2_Ctrl, worldSpace=True, translation=joint_LThumbFinger2_tuple)
    cmds.parent(L_ThumbFinger2_Ctrl, L_ThumbFinger2_grp)
    cmds.makeIdentity(L_ThumbFinger2_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_ThumbFinger2_grp, joint_LThumbFinger2, rot=True)
    cmds.parent(L_ThumbFinger2_grp, L_ThumbFinger1_Ctrl)  

    cmds.refresh(cv =1)
    ################################ L_ThumbFinger3
    jointLThumbFinger3 = cmds.xform(joint_LThumbFinger3, query=True, translation=True, worldSpace=True)
    joint_LThumbFinger3_tuple = tuple(jointLThumbFinger3)
    L_ThumbFinger3_grp = cmds.group(n="L_ThumbFinger3_CtrL_Grp", empty=True)
    cmds.xform(L_ThumbFinger3_grp, worldSpace=True, translation=joint_LThumbFinger3_tuple)
    L_ThumbFinger3_Ctrl =cmds.curve(name="L_ThumbFinger3_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, L_ThumbFinger3_Ctrl)
    cmds.listRelatives(L_ThumbFinger3_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_ThumbFinger3_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_ThumbFinger3_Ctrl), Color1)
    cmds.xform(L_ThumbFinger3_Ctrl, worldSpace=True, translation=joint_LThumbFinger3_tuple)
    cmds.parent(L_ThumbFinger3_Ctrl, L_ThumbFinger3_grp)
    cmds.makeIdentity(L_ThumbFinger3_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_ThumbFinger3_grp, joint_LThumbFinger3, rot=True)
    cmds.parent(L_ThumbFinger3_grp, L_ThumbFinger2_Ctrl)  

    cmds.refresh(cv =1)
    ################################ L_MiddleFinger1
    jointLMiddleFinger1 = cmds.xform(joint_LMiddleFinger1, query=True, translation=True, worldSpace=True)
    joint_LMiddleFinger1_tuple = tuple(jointLMiddleFinger1)
    L_MiddleFinger1_grp = cmds.group(n="L_MiddleFinger1_CtrL_Grp", empty=True)
    cmds.xform(L_MiddleFinger1_grp, worldSpace=True, translation=joint_LMiddleFinger1_tuple)
    L_MiddleFinger1_Ctrl =cmds.curve(name="L_MiddleFinger1_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, L_MiddleFinger1_Ctrl)
    cmds.listRelatives(L_MiddleFinger1_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_MiddleFinger1_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_MiddleFinger1_Ctrl), Color1)
    cmds.xform(L_MiddleFinger1_Ctrl, worldSpace=True, translation=joint_LMiddleFinger1_tuple)
    cmds.parent(L_MiddleFinger1_Ctrl, L_MiddleFinger1_grp)
    cmds.makeIdentity(L_MiddleFinger1_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_MiddleFinger1_grp, joint_LMiddleFinger1, rot=True)
    cmds.parent(L_MiddleFinger1_grp, L_Hand_Ctrl)  
        
    cmds.refresh(cv =1)
    ################################ L_MiddleFinger2
    jointLMiddleFinger2 = cmds.xform(joint_LMiddleFinger2, query=True, translation=True, worldSpace=True)
    joint_LMiddleFinger2_tuple = tuple(jointLMiddleFinger2)
    L_MiddleFinger2_grp = cmds.group(n="L_MiddleFinger2_CtrL_Grp", empty=True)
    cmds.xform(L_MiddleFinger2_grp, worldSpace=True, translation=joint_LMiddleFinger2_tuple)
    L_MiddleFinger2_Ctrl =cmds.curve(name="L_MiddleFinger2_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, L_MiddleFinger2_Ctrl)
    cmds.listRelatives(L_MiddleFinger2_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_MiddleFinger2_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_MiddleFinger2_Ctrl), Color1)
    cmds.xform(L_MiddleFinger2_Ctrl, worldSpace=True, translation=joint_LMiddleFinger2_tuple)
    cmds.parent(L_MiddleFinger2_Ctrl, L_MiddleFinger2_grp)
    cmds.makeIdentity(L_MiddleFinger2_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_MiddleFinger2_grp, joint_LMiddleFinger2, rot=True)
    cmds.parent(L_MiddleFinger2_grp, L_MiddleFinger1_Ctrl) 
        
    cmds.refresh(cv =1)
    ################################ L_MiddleFinger3
    jointLMiddleFinger3 = cmds.xform(joint_LMiddleFinger3, query=True, translation=True, worldSpace=True)
    joint_LMiddleFinger3_tuple = tuple(jointLMiddleFinger3)
    L_MiddleFinger3_grp = cmds.group(n="L_MiddleFinger3_CtrL_Grp", empty=True)
    cmds.xform(L_MiddleFinger3_grp, worldSpace=True, translation=joint_LMiddleFinger3_tuple)
    L_MiddleFinger3_Ctrl =cmds.curve(name="L_MiddleFinger3_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, L_MiddleFinger3_Ctrl)
    cmds.listRelatives(L_MiddleFinger3_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_MiddleFinger3_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_MiddleFinger3_Ctrl), Color1)
    cmds.xform(L_MiddleFinger3_Ctrl, worldSpace=True, translation=joint_LMiddleFinger3_tuple)
    cmds.parent(L_MiddleFinger3_Ctrl, L_MiddleFinger3_grp)
    cmds.makeIdentity(L_MiddleFinger3_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_MiddleFinger3_grp, joint_LMiddleFinger3, rot=True)
    cmds.parent(L_MiddleFinger3_grp, L_MiddleFinger2_Ctrl) 
        
    cmds.refresh(cv =1)
    ################################ L_IndexFinger1
    jointLIndexFinger1 = cmds.xform(joint_LIndexFinger1, query=True, translation=True, worldSpace=True)
    joint_LIndexFinger1_tuple = tuple(jointLIndexFinger1)
    L_IndexFinger1_grp = cmds.group(n="L_IndexFinger1_CtrL_Grp", empty=True)
    cmds.xform(L_IndexFinger1_grp, worldSpace=True, translation=joint_LIndexFinger1_tuple)
    L_IndexFinger1_Ctrl =cmds.curve(name="L_IndexFinger1_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, L_IndexFinger1_Ctrl)
    cmds.listRelatives(L_IndexFinger1_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_IndexFinger1_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_IndexFinger1_Ctrl), Color1)
    cmds.xform(L_IndexFinger1_Ctrl, worldSpace=True, translation=joint_LIndexFinger1_tuple)
    cmds.parent(L_IndexFinger1_Ctrl, L_IndexFinger1_grp)
    cmds.makeIdentity(L_IndexFinger1_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_IndexFinger1_grp, joint_LIndexFinger1, rot=True)
    cmds.parent(L_IndexFinger1_grp, L_Hand_Ctrl) 
        
    cmds.refresh(cv =1)
    ################################ L_IndexFinger2
    jointLIndexFinger2 = cmds.xform(joint_LIndexFinger2, query=True, translation=True, worldSpace=True)
    joint_LIndexFinger2_tuple = tuple(jointLIndexFinger2)
    L_IndexFinger2_grp = cmds.group(n="L_IndexFinger2_CtrL_Grp", empty=True)
    cmds.xform(L_IndexFinger2_grp, worldSpace=True, translation=joint_LIndexFinger2_tuple)
    L_IndexFinger2_Ctrl =cmds.curve(name="L_IndexFinger2_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, L_IndexFinger2_Ctrl)
    cmds.listRelatives(L_IndexFinger2_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_IndexFinger2_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_IndexFinger2_Ctrl), Color1)
    cmds.xform(L_IndexFinger2_Ctrl, worldSpace=True, translation=joint_LIndexFinger2_tuple)
    cmds.parent(L_IndexFinger2_Ctrl, L_IndexFinger2_grp)
    cmds.makeIdentity(L_IndexFinger2_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_IndexFinger2_grp, joint_LIndexFinger2, rot=True)
    cmds.parent(L_IndexFinger2_grp, L_IndexFinger1_Ctrl) 
        
    cmds.refresh(cv =1)
    ################################ L_IndexFinger3
    jointLIndexFinger3 = cmds.xform(joint_LIndexFinger3, query=True, translation=True, worldSpace=True)
    joint_LIndexFinger3_tuple = tuple(jointLIndexFinger3)
    L_IndexFinger3_grp = cmds.group(n="L_IndexFinger3_CtrL_Grp", empty=True)
    cmds.xform(L_IndexFinger3_grp, worldSpace=True, translation=joint_LIndexFinger3_tuple)
    L_IndexFinger3_Ctrl =cmds.curve(name="L_IndexFinger3_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, L_IndexFinger3_Ctrl)
    cmds.listRelatives(L_IndexFinger3_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_IndexFinger3_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_IndexFinger3_Ctrl), Color1)
    cmds.xform(L_IndexFinger3_Ctrl, worldSpace=True, translation=joint_LIndexFinger3_tuple)
    cmds.parent(L_IndexFinger3_Ctrl, L_IndexFinger3_grp)
    cmds.makeIdentity(L_IndexFinger3_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_IndexFinger3_grp, joint_LIndexFinger3, rot=True)
    cmds.parent(L_IndexFinger3_grp, L_IndexFinger2_Ctrl) 
        
    cmds.refresh(cv =1)
    ################################ L_RingFinger1
    jointLRingFinger1 = cmds.xform(joint_LRingFinger1, query=True, translation=True, worldSpace=True)
    joint_LRingFinger1_tuple = tuple(jointLRingFinger1)
    L_RingFinger1_grp = cmds.group(n="L_RingFinger1_CtrL_Grp", empty=True)
    cmds.xform(L_RingFinger1_grp, worldSpace=True, translation=joint_LRingFinger1_tuple)
    L_RingFinger1_Ctrl =cmds.curve(name="L_RingFinger1_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, L_RingFinger1_Ctrl)
    cmds.listRelatives(L_RingFinger1_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_RingFinger1_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_RingFinger1_Ctrl), Color1)
    cmds.xform(L_RingFinger1_Ctrl, worldSpace=True, translation=joint_LRingFinger1_tuple)
    cmds.parent(L_RingFinger1_Ctrl, L_RingFinger1_grp)
    cmds.makeIdentity(L_RingFinger1_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_RingFinger1_grp, joint_LRingFinger1, rot=True)
    cmds.parent(L_RingFinger1_grp, L_Hand_Ctrl) 
        
    cmds.refresh(cv =1)
    ################################ L_RingFinger2
    jointLRingFinger2 = cmds.xform(joint_LRingFinger2, query=True, translation=True, worldSpace=True)
    joint_LRingFinger2_tuple = tuple(jointLRingFinger2)
    L_RingFinger2_grp = cmds.group(n="L_RingFinger2_CtrL_Grp", empty=True)
    cmds.xform(L_RingFinger2_grp, worldSpace=True, translation=joint_LRingFinger2_tuple)
    L_RingFinger2_Ctrl =cmds.curve(name="L_RingFinger2_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, L_RingFinger2_Ctrl)
    cmds.listRelatives(L_RingFinger2_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_RingFinger2_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_RingFinger2_Ctrl), Color1)
    cmds.xform(L_RingFinger2_Ctrl, worldSpace=True, translation=joint_LRingFinger2_tuple)
    cmds.parent(L_RingFinger2_Ctrl, L_RingFinger2_grp)
    cmds.makeIdentity(L_RingFinger2_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_RingFinger2_grp, joint_LRingFinger2, rot=True)
    cmds.parent(L_RingFinger2_grp, L_RingFinger1_Ctrl) 

    cmds.refresh(cv =1)
    ################################ L_RingFinger3
    jointLRingFinger3 = cmds.xform(joint_LRingFinger3, query=True, translation=True, worldSpace=True)
    joint_LRingFinger3_tuple = tuple(jointLRingFinger3)
    L_RingFinger3_grp = cmds.group(n="L_RingFinger3_CtrL_Grp", empty=True)
    cmds.xform(L_RingFinger3_grp, worldSpace=True, translation=joint_LRingFinger3_tuple)
    L_RingFinger3_Ctrl =cmds.curve(name="L_RingFinger3_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, L_RingFinger3_Ctrl)
    cmds.listRelatives(L_RingFinger3_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_RingFinger3_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_RingFinger3_Ctrl), Color1)
    cmds.xform(L_RingFinger3_Ctrl, worldSpace=True, translation=joint_LRingFinger3_tuple)
    cmds.parent(L_RingFinger3_Ctrl, L_RingFinger3_grp)
    cmds.makeIdentity(L_RingFinger3_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_RingFinger3_grp, joint_LRingFinger3, rot=True)
    cmds.parent(L_RingFinger3_grp, L_RingFinger2_Ctrl) 

    cmds.refresh(cv =1)
    ################################ L_PinkyFinger1
    jointLPinkyFinger1 = cmds.xform(joint_LPinkyFinger1, query=True, translation=True, worldSpace=True)
    joint_LPinkyFinger1_tuple = tuple(jointLPinkyFinger1)
    L_PinkyFinger1_grp = cmds.group(n="L_PinkyFinger1_CtrL_Grp", empty=True)
    cmds.xform(L_PinkyFinger1_grp, worldSpace=True, translation=joint_LPinkyFinger1_tuple)
    L_PinkyFinger1_Ctrl =cmds.curve(name="L_PinkyFinger1_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, L_PinkyFinger1_Ctrl)
    cmds.listRelatives(L_PinkyFinger1_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_PinkyFinger1_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_PinkyFinger1_Ctrl), Color1)
    cmds.xform(L_PinkyFinger1_Ctrl, worldSpace=True, translation=joint_LPinkyFinger1_tuple)
    cmds.parent(L_PinkyFinger1_Ctrl, L_PinkyFinger1_grp)
    cmds.makeIdentity(L_PinkyFinger1_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_PinkyFinger1_grp, joint_LPinkyFinger1, rot=True)
    cmds.parent(L_PinkyFinger1_grp, L_Hand_Ctrl) 

    cmds.refresh(cv =1)
    ################################ L_PinkyFinger2
    jointLPinkyFinger2 = cmds.xform(joint_LPinkyFinger2, query=True, translation=True, worldSpace=True)
    joint_LPinkyFinger2_tuple = tuple(jointLPinkyFinger2)
    L_PinkyFinger2_grp = cmds.group(n="L_PinkyFinger2_CtrL_Grp", empty=True)
    cmds.xform(L_PinkyFinger2_grp, worldSpace=True, translation=joint_LPinkyFinger2_tuple)
    L_PinkyFinger2_Ctrl =cmds.curve(name="L_PinkyFinger2_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, L_PinkyFinger2_Ctrl)
    cmds.listRelatives(L_PinkyFinger2_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_PinkyFinger2_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_PinkyFinger2_Ctrl), Color1)
    cmds.xform(L_PinkyFinger2_Ctrl, worldSpace=True, translation=joint_LPinkyFinger2_tuple)
    cmds.parent(L_PinkyFinger2_Ctrl, L_PinkyFinger2_grp)
    cmds.makeIdentity(L_PinkyFinger2_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_PinkyFinger2_grp, joint_LPinkyFinger2, rot=True)
    cmds.parent(L_PinkyFinger2_grp, L_PinkyFinger1_Ctrl) 

    cmds.refresh(cv =1)
    ################################ L_PinkyFinger3
    jointLPinkyFinger3 = cmds.xform(joint_LPinkyFinger3, query=True, translation=True, worldSpace=True)
    joint_LPinkyFinger3_tuple = tuple(jointLPinkyFinger3)
    L_PinkyFinger3_grp = cmds.group(n="L_PinkyFinger3_CtrL_Grp", empty=True)
    cmds.xform(L_PinkyFinger3_grp, worldSpace=True, translation=joint_LPinkyFinger3_tuple)
    L_PinkyFinger3_Ctrl =cmds.curve(name="L_PinkyFinger3_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, L_PinkyFinger3_Ctrl)
    cmds.listRelatives(L_PinkyFinger3_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_PinkyFinger3_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_PinkyFinger3_Ctrl), Color1)
    cmds.xform(L_PinkyFinger3_Ctrl, worldSpace=True, translation=joint_LPinkyFinger3_tuple)
    cmds.parent(L_PinkyFinger3_Ctrl, L_PinkyFinger3_grp)
    cmds.makeIdentity(L_PinkyFinger3_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(L_PinkyFinger3_grp, joint_LPinkyFinger3, rot=True)
    cmds.parent(L_PinkyFinger3_grp, L_PinkyFinger2_Ctrl) 


    cmds.refresh(cv =1)
    ################################ R_Hand
    jointRHand = cmds.xform(joint_RHand, query=True, translation=True, worldSpace=True)
    joint_RHand_tuple = tuple(jointRHand)
    R_Hand_grp = cmds.group(n="R_Hand_Ctrl_Grp", empty=True)
    cmds.xform(R_Hand_grp, worldSpace=True, translation=joint_RHand_tuple)
    R_Hand_Ctrl =cmds.curve(name="R_Hand_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.1, 0.1, 0.1, R_Hand_Ctrl)
    cmds.listRelatives(R_Hand_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_Hand_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_Hand_Ctrl), Color1)
    R_IKFK_Ctrl =cmds.curve(name="R_IKFK_Hand_Ctrl", d=1, p=[
    (1.35, 0.85, 0),(1.48, 0.85, 0),(1.74, 0.8, 0),
    (2.07, 0.62, 0),(2.3, 0.33, 0),(2.37, 0, 0),(2.3, -0.33, 0),
    (2.07, -0.62, 0),(1.74, -0.8, 0),(1.48, -0.85, 0),(1.35, -0.85, 0)])
    #cmds.scale(0.1, 0.1, 0.1, R_IKFK_Ctrl)
    cmds.listRelatives(R_IKFK_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_IKFK_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_IKFK_Ctrl), Color3)
    cmds.xform(R_Hand_Ctrl, worldSpace=True, translation=joint_RHand_tuple)
    cmds.xform(R_IKFK_Ctrl, worldSpace=True, translation=joint_RHand_tuple)
    cmds.parent(R_IKFK_Ctrl, R_Hand_Ctrl)
    cmds.parent(R_Hand_Ctrl, R_Hand_grp)
    cmds.makeIdentity(R_Hand_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.makeIdentity(R_IKFK_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_Hand_grp, joint_RHand, rot=True)
    cmds.parent(R_Hand_grp, Hand_grp)
    # cmds.parentConstraint(R_Wrist_Ctrl, R_Hand_grp)

    cmds.refresh(cv =1)
    ################################ R_ThumbFinger1
    jointRThumbFinger1 = cmds.xform(joint_RThumbFinger1, query=True, translation=True, worldSpace=True)
    joint_RThumbFinger1_tuple = tuple(jointRThumbFinger1)
    R_ThumbFinger1_grp = cmds.group(n="R_ThumbFinger1_Ctrl_Grp", empty=True)
    cmds.xform(R_ThumbFinger1_grp, worldSpace=True, translation=joint_RThumbFinger1_tuple)
    R_ThumbFinger1_Ctrl =cmds.curve(name="R_ThumbFinger1_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, R_ThumbFinger1_Ctrl)
    cmds.listRelatives(R_ThumbFinger1_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_ThumbFinger1_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_ThumbFinger1_Ctrl), Color1)
    cmds.xform(R_ThumbFinger1_Ctrl, worldSpace=True, translation=joint_RThumbFinger1_tuple)
    cmds.parent(R_ThumbFinger1_Ctrl, R_ThumbFinger1_grp)
    cmds.makeIdentity(R_ThumbFinger1_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_ThumbFinger1_grp, joint_RThumbFinger1, rot=True)
    cmds.parent(R_ThumbFinger1_grp, R_Hand_Ctrl)  
            
    cmds.refresh(cv =1)
    ################################ R_ThumbFinger2
    jointRThumbFinger2 = cmds.xform(joint_RThumbFinger2, query=True, translation=True, worldSpace=True)
    joint_RThumbFinger2_tuple = tuple(jointRThumbFinger2)
    R_ThumbFinger2_grp = cmds.group(n="R_ThumbFinger2_Ctrl_Grp", empty=True)
    cmds.xform(R_ThumbFinger2_grp, worldSpace=True, translation=joint_RThumbFinger2_tuple)
    R_ThumbFinger2_Ctrl =cmds.curve(name="R_ThumbFinger2_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, R_ThumbFinger2_Ctrl)
    cmds.listRelatives(R_ThumbFinger2_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_ThumbFinger2_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_ThumbFinger2_Ctrl), Color1)
    cmds.xform(R_ThumbFinger2_Ctrl, worldSpace=True, translation=joint_RThumbFinger2_tuple)
    cmds.parent(R_ThumbFinger2_Ctrl, R_ThumbFinger2_grp)
    cmds.makeIdentity(R_ThumbFinger2_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_ThumbFinger2_grp, joint_RThumbFinger2, rot=True)
    cmds.parent(R_ThumbFinger2_grp, R_ThumbFinger1_Ctrl)  

    cmds.refresh(cv =1)
    ################################ R_ThumbFinger3
    jointRThumbFinger3 = cmds.xform(joint_RThumbFinger3, query=True, translation=True, worldSpace=True)
    joint_RThumbFinger3_tuple = tuple(jointRThumbFinger3)
    R_ThumbFinger3_grp = cmds.group(n="R_ThumbFinger3_Ctrl_Grp", empty=True)
    cmds.xform(R_ThumbFinger3_grp, worldSpace=True, translation=joint_RThumbFinger3_tuple)
    R_ThumbFinger3_Ctrl =cmds.curve(name="R_ThumbFinger3_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, R_ThumbFinger3_Ctrl)
    cmds.listRelatives(R_ThumbFinger3_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_ThumbFinger3_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_ThumbFinger3_Ctrl), Color1)
    cmds.xform(R_ThumbFinger3_Ctrl, worldSpace=True, translation=joint_RThumbFinger3_tuple)
    cmds.parent(R_ThumbFinger3_Ctrl, R_ThumbFinger3_grp)
    cmds.makeIdentity(R_ThumbFinger3_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_ThumbFinger3_grp, joint_RThumbFinger3, rot=True)
    cmds.parent(R_ThumbFinger3_grp, R_ThumbFinger2_Ctrl)  

    cmds.refresh(cv =1)
    ################################ R_MiddleFinger1
    jointRMiddleFinger1 = cmds.xform(joint_RMiddleFinger1, query=True, translation=True, worldSpace=True)
    joint_RMiddleFinger1_tuple = tuple(jointRMiddleFinger1)
    R_MiddleFinger1_grp = cmds.group(n="R_MiddleFinger1_Ctrl_Grp", empty=True)
    cmds.xform(R_MiddleFinger1_grp, worldSpace=True, translation=joint_RMiddleFinger1_tuple)
    R_MiddleFinger1_Ctrl =cmds.curve(name="R_MiddleFinger1_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, R_MiddleFinger1_Ctrl)
    cmds.listRelatives(R_MiddleFinger1_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_MiddleFinger1_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_MiddleFinger1_Ctrl), Color1)
    cmds.xform(R_MiddleFinger1_Ctrl, worldSpace=True, translation=joint_RMiddleFinger1_tuple)
    cmds.parent(R_MiddleFinger1_Ctrl, R_MiddleFinger1_grp)
    cmds.makeIdentity(R_MiddleFinger1_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_MiddleFinger1_grp, joint_RMiddleFinger1, rot=True)
    cmds.parent(R_MiddleFinger1_grp, R_Hand_Ctrl)  
        
    cmds.refresh(cv =1)
    ################################ R_MiddleFinger2
    jointRMiddleFinger2 = cmds.xform(joint_RMiddleFinger2, query=True, translation=True, worldSpace=True)
    joint_RMiddleFinger2_tuple = tuple(jointRMiddleFinger2)
    R_MiddleFinger2_grp = cmds.group(n="R_MiddleFinger2_Ctrl_Grp", empty=True)
    cmds.xform(R_MiddleFinger2_grp, worldSpace=True, translation=joint_RMiddleFinger2_tuple)
    R_MiddleFinger2_Ctrl =cmds.curve(name="R_MiddleFinger2_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, R_MiddleFinger2_Ctrl)
    cmds.listRelatives(R_MiddleFinger2_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_MiddleFinger2_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_MiddleFinger2_Ctrl), Color1)
    cmds.xform(R_MiddleFinger2_Ctrl, worldSpace=True, translation=joint_RMiddleFinger2_tuple)
    cmds.parent(R_MiddleFinger2_Ctrl, R_MiddleFinger2_grp)
    cmds.makeIdentity(R_MiddleFinger2_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_MiddleFinger2_grp, joint_RMiddleFinger2, rot=True)
    cmds.parent(R_MiddleFinger2_grp, R_MiddleFinger1_Ctrl) 
        
    cmds.refresh(cv =1)
    ################################ R_MiddleFinger3
    jointRMiddleFinger3 = cmds.xform(joint_RMiddleFinger3, query=True, translation=True, worldSpace=True)
    joint_RMiddleFinger3_tuple = tuple(jointRMiddleFinger3)
    R_MiddleFinger3_grp = cmds.group(n="R_MiddleFinger3_Ctrl_Grp", empty=True)
    cmds.xform(R_MiddleFinger3_grp, worldSpace=True, translation=joint_RMiddleFinger3_tuple)
    R_MiddleFinger3_Ctrl =cmds.curve(name="R_MiddleFinger3_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, R_MiddleFinger3_Ctrl)
    cmds.listRelatives(R_MiddleFinger3_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_MiddleFinger3_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_MiddleFinger3_Ctrl), Color1)
    cmds.xform(R_MiddleFinger3_Ctrl, worldSpace=True, translation=joint_RMiddleFinger3_tuple)
    cmds.parent(R_MiddleFinger3_Ctrl, R_MiddleFinger3_grp)
    cmds.makeIdentity(R_MiddleFinger3_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_MiddleFinger3_grp, joint_RMiddleFinger3, rot=True)
    cmds.parent(R_MiddleFinger3_grp, R_MiddleFinger2_Ctrl) 
        
    cmds.refresh(cv =1)
    ################################ R_IndexFinger1
    jointRIndexFinger1 = cmds.xform(joint_RIndexFinger1, query=True, translation=True, worldSpace=True)
    joint_RIndexFinger1_tuple = tuple(jointRIndexFinger1)
    R_IndexFinger1_grp = cmds.group(n="R_IndexFinger1_Ctrl_Grp", empty=True)
    cmds.xform(R_IndexFinger1_grp, worldSpace=True, translation=joint_RIndexFinger1_tuple)
    R_IndexFinger1_Ctrl =cmds.curve(name="R_IndexFinger1_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, R_IndexFinger1_Ctrl)
    cmds.listRelatives(R_IndexFinger1_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_IndexFinger1_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_IndexFinger1_Ctrl), Color1)
    cmds.xform(R_IndexFinger1_Ctrl, worldSpace=True, translation=joint_RIndexFinger1_tuple)
    cmds.parent(R_IndexFinger1_Ctrl, R_IndexFinger1_grp)
    cmds.makeIdentity(R_IndexFinger1_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_IndexFinger1_grp, joint_RIndexFinger1, rot=True)
    cmds.parent(R_IndexFinger1_grp, R_Hand_Ctrl) 
        
    cmds.refresh(cv =1)
    ################################ R_IndexFinger2
    jointRIndexFinger2 = cmds.xform(joint_RIndexFinger2, query=True, translation=True, worldSpace=True)
    joint_RIndexFinger2_tuple = tuple(jointRIndexFinger2)
    R_IndexFinger2_grp = cmds.group(n="R_IndexFinger2_Ctrl_Grp", empty=True)
    cmds.xform(R_IndexFinger2_grp, worldSpace=True, translation=joint_RIndexFinger2_tuple)
    R_IndexFinger2_Ctrl =cmds.curve(name="R_IndexFinger2_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, R_IndexFinger2_Ctrl)
    cmds.listRelatives(R_IndexFinger2_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_IndexFinger2_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_IndexFinger2_Ctrl), Color1)
    cmds.xform(R_IndexFinger2_Ctrl, worldSpace=True, translation=joint_RIndexFinger2_tuple)
    cmds.parent(R_IndexFinger2_Ctrl, R_IndexFinger2_grp)
    cmds.makeIdentity(R_IndexFinger2_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_IndexFinger2_grp, joint_RIndexFinger2, rot=True)
    cmds.parent(R_IndexFinger2_grp, R_IndexFinger1_Ctrl) 
        
    cmds.refresh(cv =1)
    ################################ R_IndexFinger3
    jointRIndexFinger3 = cmds.xform(joint_RIndexFinger3, query=True, translation=True, worldSpace=True)
    joint_RIndexFinger3_tuple = tuple(jointRIndexFinger3)
    R_IndexFinger3_grp = cmds.group(n="R_IndexFinger3_Ctrl_Grp", empty=True)
    cmds.xform(R_IndexFinger3_grp, worldSpace=True, translation=joint_RIndexFinger3_tuple)
    R_IndexFinger3_Ctrl =cmds.curve(name="R_IndexFinger3_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, R_IndexFinger3_Ctrl)
    cmds.listRelatives(R_IndexFinger3_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_IndexFinger3_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_IndexFinger3_Ctrl), Color1)
    cmds.xform(R_IndexFinger3_Ctrl, worldSpace=True, translation=joint_RIndexFinger3_tuple)
    cmds.parent(R_IndexFinger3_Ctrl, R_IndexFinger3_grp)
    cmds.makeIdentity(R_IndexFinger3_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_IndexFinger3_grp, joint_RIndexFinger3, rot=True)
    cmds.parent(R_IndexFinger3_grp, R_IndexFinger2_Ctrl) 
        
    cmds.refresh(cv =1)
    ################################ R_RingFinger1
    jointRRingFinger1 = cmds.xform(joint_RRingFinger1, query=True, translation=True, worldSpace=True)
    joint_RRingFinger1_tuple = tuple(jointRRingFinger1)
    R_RingFinger1_grp = cmds.group(n="R_RingFinger1_Ctrl_Grp", empty=True)
    cmds.xform(R_RingFinger1_grp, worldSpace=True, translation=joint_RRingFinger1_tuple)
    R_RingFinger1_Ctrl =cmds.curve(name="R_RingFinger1_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, R_RingFinger1_Ctrl)
    cmds.listRelatives(R_RingFinger1_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_RingFinger1_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_RingFinger1_Ctrl), Color1)
    cmds.xform(R_RingFinger1_Ctrl, worldSpace=True, translation=joint_RRingFinger1_tuple)
    cmds.parent(R_RingFinger1_Ctrl, R_RingFinger1_grp)
    cmds.makeIdentity(R_RingFinger1_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_RingFinger1_grp, joint_RRingFinger1, rot=True)
    cmds.parent(R_RingFinger1_grp, R_Hand_Ctrl) 
        
    cmds.refresh(cv =1)
    ################################ R_RingFinger2
    jointRRingFinger2 = cmds.xform(joint_RRingFinger2, query=True, translation=True, worldSpace=True)
    joint_RRingFinger2_tuple = tuple(jointRRingFinger2)
    R_RingFinger2_grp = cmds.group(n="R_RingFinger2_Ctrl_Grp", empty=True)
    cmds.xform(R_RingFinger2_grp, worldSpace=True, translation=joint_RRingFinger2_tuple)
    R_RingFinger2_Ctrl =cmds.curve(name="R_RingFinger2_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, R_RingFinger2_Ctrl)
    cmds.listRelatives(R_RingFinger2_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_RingFinger2_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_RingFinger2_Ctrl), Color1)
    cmds.xform(R_RingFinger2_Ctrl, worldSpace=True, translation=joint_RRingFinger2_tuple)
    cmds.parent(R_RingFinger2_Ctrl, R_RingFinger2_grp)
    cmds.makeIdentity(R_RingFinger2_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_RingFinger2_grp, joint_RRingFinger2, rot=True)
    cmds.parent(R_RingFinger2_grp, R_RingFinger1_Ctrl) 

    cmds.refresh(cv =1)
    ################################ R_RingFinger3
    jointRRingFinger3 = cmds.xform(joint_RRingFinger3, query=True, translation=True, worldSpace=True)
    joint_RRingFinger3_tuple = tuple(jointRRingFinger3)
    R_RingFinger3_grp = cmds.group(n="R_RingFinger3_Ctrl_Grp", empty=True)
    cmds.xform(R_RingFinger3_grp, worldSpace=True, translation=joint_RRingFinger3_tuple)
    R_RingFinger3_Ctrl =cmds.curve(name="R_RingFinger3_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, R_RingFinger3_Ctrl)
    cmds.listRelatives(R_RingFinger3_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_RingFinger3_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_RingFinger3_Ctrl), Color1)
    cmds.xform(R_RingFinger3_Ctrl, worldSpace=True, translation=joint_RRingFinger3_tuple)
    cmds.parent(R_RingFinger3_Ctrl, R_RingFinger3_grp)
    cmds.makeIdentity(R_RingFinger3_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_RingFinger3_grp, joint_RRingFinger3, rot=True)
    cmds.parent(R_RingFinger3_grp, R_RingFinger2_Ctrl) 

    cmds.refresh(cv =1)
    ################################ R_PinkyFinger1
    jointRPinkyFinger1 = cmds.xform(joint_RPinkyFinger1, query=True, translation=True, worldSpace=True)
    joint_RPinkyFinger1_tuple = tuple(jointRPinkyFinger1)
    R_PinkyFinger1_grp = cmds.group(n="R_PinkyFinger1_Ctrl_Grp", empty=True)
    cmds.xform(R_PinkyFinger1_grp, worldSpace=True, translation=joint_RPinkyFinger1_tuple)
    R_PinkyFinger1_Ctrl =cmds.curve(name="R_PinkyFinger1_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, R_PinkyFinger1_Ctrl)
    cmds.listRelatives(R_PinkyFinger1_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_PinkyFinger1_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_PinkyFinger1_Ctrl), Color1)
    cmds.xform(R_PinkyFinger1_Ctrl, worldSpace=True, translation=joint_RPinkyFinger1_tuple)
    cmds.parent(R_PinkyFinger1_Ctrl, R_PinkyFinger1_grp)
    cmds.makeIdentity(R_PinkyFinger1_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_PinkyFinger1_grp, joint_RPinkyFinger1, rot=True)
    cmds.parent(R_PinkyFinger1_grp, R_Hand_Ctrl) 

    cmds.refresh(cv =1)
    ################################ R_PinkyFinger2
    jointRPinkyFinger2 = cmds.xform(joint_RPinkyFinger2, query=True, translation=True, worldSpace=True)
    joint_RPinkyFinger2_tuple = tuple(jointRPinkyFinger2)
    R_PinkyFinger2_grp = cmds.group(n="R_PinkyFinger2_Ctrl_Grp", empty=True)
    cmds.xform(R_PinkyFinger2_grp, worldSpace=True, translation=joint_RPinkyFinger2_tuple)
    R_PinkyFinger2_Ctrl =cmds.curve(name="R_PinkyFinger2_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, R_PinkyFinger2_Ctrl)
    cmds.listRelatives(R_PinkyFinger2_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_PinkyFinger2_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_PinkyFinger2_Ctrl), Color1)
    cmds.xform(R_PinkyFinger2_Ctrl, worldSpace=True, translation=joint_RPinkyFinger2_tuple)
    cmds.parent(R_PinkyFinger2_Ctrl, R_PinkyFinger2_grp)
    cmds.makeIdentity(R_PinkyFinger2_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_PinkyFinger2_grp, joint_RPinkyFinger2, rot=True)
    cmds.parent(R_PinkyFinger2_grp, R_PinkyFinger1_Ctrl) 

    cmds.refresh(cv =1)
    ################################ R_PinkyFinger3
    jointRPinkyFinger3 = cmds.xform(joint_RPinkyFinger3, query=True, translation=True, worldSpace=True)
    joint_RPinkyFinger3_tuple = tuple(jointRPinkyFinger3)
    R_PinkyFinger3_grp = cmds.group(n="R_PinkyFinger3_Ctrl_Grp", empty=True)
    cmds.xform(R_PinkyFinger3_grp, worldSpace=True, translation=joint_RPinkyFinger3_tuple)
    R_PinkyFinger3_Ctrl =cmds.curve(name="R_PinkyFinger3_Ctrl", d=1, p=[
    (0, 2, 0), (0, 1.85, -0.76), (0, 1.41, -1.41), (0, 0.76, -1.85),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, 0, 0), (0, 2, 0), (0, 1.85, 0.76),
    (0, 1.41, 1.41), (0, 0.76, 1.85), (0, 0, 2), (0, 0, 0),
    (0, 0, -2), (0, -0.76, -1.85), (0, -1.41, -1.41), (0, -1.85, -0.76),
    (0, -2, 0), (0, -1.85, 0.76), (0, -1.41, 1.41), (0, -0.76, 1.85),
    (0, 0, 2)])
    cmds.scale(0.08, 0.08, 0.08, R_PinkyFinger3_Ctrl)
    cmds.listRelatives(R_PinkyFinger3_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_PinkyFinger3_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_PinkyFinger3_Ctrl), Color1)
    cmds.xform(R_PinkyFinger3_Ctrl, worldSpace=True, translation=joint_RPinkyFinger3_tuple)
    cmds.parent(R_PinkyFinger3_Ctrl, R_PinkyFinger3_grp)
    cmds.makeIdentity(R_PinkyFinger3_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.matchTransform(R_PinkyFinger3_grp, joint_RPinkyFinger3, rot=True)
    cmds.parent(R_PinkyFinger3_grp, R_PinkyFinger2_Ctrl) 

    cmds.refresh(cv =1)
    ################################ R_IK Foot Ctrl 
    R_IK_Foot_Controller = cmds.xform(joint_RAnkle, query=True, translation=True, worldSpace=True)
    R_IK_Foot_Controller_tuple = tuple(R_IK_Foot_Controller)
    R_IK_Foot_Controller_Grp = cmds.group(n="R_IK_Foot_Grp", empty=True)
    cmds.xform(R_IK_Foot_Controller_Grp, worldSpace=True, translation=R_IK_Foot_Controller_tuple)
    R_IK_Foot_Controller_Ctrl =cmds.curve(name="R_IK_Foot_Ctrl", d=1, p=[
    (0.5, -0.09, 1.48),(0.5, 0.23, -0.5),(-0.5, 0.23, -0.5),(-0.5, -0.97, -0.69),
    (0.5, -0.97, -0.69),(0.5, 0.23, -0.5),(-0.5, 0.23, -0.5),(-0.5, -0.09, 1.48),
    (0.5, -0.09, 1.48),(0.5, -0.95, 2.32),(0.5, -0.97, -0.69),(-0.5, -0.97, -0.69),
    (-0.5, -0.95, 2.32),(0.5, -0.95, 2.32),(-0.5, -0.95, 2.32),(-0.5, -0.09, 1.48)])
    cmds.scale(1, 1, 1)

    cmds.refresh(cv =1)
    R_Heel_ctrl_Grp = cmds.group(n="R_Heel_Ctrl_Grp", empty=True)
    R_Heel_Ctrl = cmds.circle(n="R_Heel_Ctrl", nr=(0, 1, 0), r=0.5)[0]
    cmds.listRelatives(R_Heel_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_Heel_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_Heel_Ctrl), Color5) 
    cmds.parent(R_Heel_Ctrl, R_Heel_ctrl_Grp)
    R_Toe_ctrl_Grp = cmds.group(n="R_Toe_Ctrl_Grp", empty=True)
    R_Toe_Ctrl = cmds.circle(n="R_Toe_Ctrl", nr=(0, 1, 0), r=0.5)[0]
    cmds.listRelatives(R_Toe_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_Toe_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_Toe_Ctrl), Color5) 
    cmds.parent(R_Toe_Ctrl, R_Toe_ctrl_Grp)
    cmds.parent(R_Toe_ctrl_Grp, R_Heel_Ctrl)
    cmds.parent(R_Heel_ctrl_Grp, R_IK_Foot_Controller_Ctrl)   

    cmds.refresh(cv =1)
    cmds.addAttr(R_IK_Foot_Controller_Ctrl, longName='______________________', attributeType='enum', en='____________', keyable=True)
    mel.eval('setAttr -lock true "R_IK_Foot_Ctrl.______________________";')
    cmds.addAttr(R_IK_Foot_Controller_Ctrl, longName = 'Heel', attributeType = 'float', min = 1, max = 10, keyable=True) 
    cmds.addAttr(R_IK_Foot_Controller_Ctrl, longName = 'Toe', attributeType = 'float', min = 1, max = 10, keyable=True) 
    cmds.listRelatives(R_IK_Foot_Controller_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_IK_Foot_Controller_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_IK_Foot_Controller_Ctrl), Color2) 
    cmds.xform(R_IK_Foot_Controller_Ctrl, worldSpace=True, translation=R_IK_Foot_Controller_tuple)
    cmds.parent(R_IK_Foot_Controller_Ctrl, R_IK_Foot_Controller_Grp)
    cmds.makeIdentity(R_IK_Foot_Controller_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    mel.eval("""
    setAttr "R_Heel_Ctrl_Grp.rotateZ" -90;
    setAttr "R_Heel_Ctrl_Grp.translateY" -1;
    setAttr "R_Heel_Ctrl_Grp.translateZ" -0.7;
    setAttr "R_Toe_Ctrl_Grp.translateZ" 3;
    select -r R_Heel_Ctrl ;
    select -tgl R_Toe_Ctrl ;
    DeleteHistory;

             """)
    cmds.refresh(cv =1)
    cmds.parent(R_IK_Foot_Controller_Grp, Hip_grp)

    ################################ L_IK Foot Ctrl 
    L_IK_Foot_Controller = cmds.xform(joint_LAnkle, query=True, translation=True, worldSpace=True)
    L_IK_Foot_Controller_tuple = tuple(L_IK_Foot_Controller)
    L_IK_Foot_Controller_Grp = cmds.group(n="L_IK_Foot_Grp", empty=True)
    cmds.xform(L_IK_Foot_Controller_Grp, worldSpace=True, translation=L_IK_Foot_Controller_tuple)
    L_IK_Foot_Controller_Ctrl =cmds.curve(name="L_IK_Foot_Ctrl", d=1, p=[
    (0.5, -0.09, 1.48),(0.5, 0.23, -0.5),(-0.5, 0.23, -0.5),(-0.5, -0.97, -0.69),
    (0.5, -0.97, -0.69),(0.5, 0.23, -0.5),(-0.5, 0.23, -0.5),(-0.5, -0.09, 1.48),
    (0.5, -0.09, 1.48),(0.5, -0.95, 2.32),(0.5, -0.97, -0.69),(-0.5, -0.97, -0.69),
    (-0.5, -0.95, 2.32),(0.5, -0.95, 2.32),(-0.5, -0.95, 2.32),(-0.5, -0.09, 1.48)])
    cmds.scale(1, 1, 1)
    
    cmds.refresh(cv =1)
    L_Heel_ctrl_Grp = cmds.group(n="L_Heel_Ctrl_Grp", empty=True)
    L_Heel_Ctrl = cmds.circle(n="L_Heel_Ctrl", nr=(0, 1, 0), r=0.5)[0]
    cmds.listRelatives(L_Heel_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_Heel_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_Heel_Ctrl), Color5) 
    cmds.parent(L_Heel_Ctrl, L_Heel_ctrl_Grp)
    L_Toe_ctrl_Grp = cmds.group(n="L_Toe_Ctrl_Grp", empty=True)
    L_Toe_Ctrl = cmds.circle(n="L_Toe_Ctrl", nr=(0, 1, 0), r=0.5)[0]
    cmds.listRelatives(L_Toe_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_Toe_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_Toe_Ctrl), Color5)     
    cmds.parent(L_Toe_Ctrl, L_Toe_ctrl_Grp)
    cmds.parent(L_Toe_ctrl_Grp, L_Heel_Ctrl)   
    cmds.parent(L_Heel_ctrl_Grp, L_IK_Foot_Controller_Ctrl)   

    cmds.refresh(cv =1)
    cmds.addAttr(L_IK_Foot_Controller_Ctrl, longName='______________________', attributeType='enum', en='____________', keyable=True)
    mel.eval('setAttr -lock true "L_IK_Foot_Ctrl.______________________";')
    cmds.addAttr(L_IK_Foot_Controller_Ctrl, longName = 'Heel', attributeType = 'float', min = 1, max = 10, keyable=True) 
    cmds.addAttr(L_IK_Foot_Controller_Ctrl, longName = 'Toe', attributeType = 'float', min = 1, max = 10, keyable=True) 
    cmds.listRelatives(L_IK_Foot_Controller_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_IK_Foot_Controller_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_IK_Foot_Controller_Ctrl), Color2) 
    cmds.xform(L_IK_Foot_Controller_Ctrl, worldSpace=True, translation=L_IK_Foot_Controller_tuple)
    cmds.parent(L_IK_Foot_Controller_Ctrl, L_IK_Foot_Controller_Grp)
    cmds.makeIdentity(L_IK_Foot_Controller_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    mel.eval("""
    setAttr "L_Heel_Ctrl_Grp.rotateZ" -90;
    setAttr "L_Heel_Ctrl_Grp.translateY" -1;
    setAttr "L_Heel_Ctrl_Grp.translateZ" -0.7;
    setAttr "L_Toe_Ctrl_Grp.translateZ" 3;
    select -r L_Heel_Ctrl ;
    select -tgl L_Toe_Ctrl ;
    DeleteHistory;
             """)
    cmds.parent(L_IK_Foot_Controller_Grp, Hip_grp)
    
    cmds.refresh(cv =1)
    ################################ L_IK Hand Ctrl 
    L_IK_Hand_Controller = cmds.xform(joint_LWrist, query=True, translation=True, worldSpace=True)
    L_IK_Hand_Controller_tuple = tuple(L_IK_Hand_Controller)
    L_IK_Hand_Controller_Grp = cmds.group(n="L_IK_Hand_Grp", empty=True)
    cmds.xform(L_IK_Hand_Controller_Grp, worldSpace=True, translation=L_IK_Hand_Controller_tuple)
    L_IK_Hand_Controller_Ctrl =cmds.curve(name="L_IK_Hand_Ctrl", d=1, p=[
    (1, 1, 1),(1,1,-1) ,(1, -1, -1) ,(1, -1, 1) ,(-1, -1, 1) ,(-1, 1, 1) ,(1, 1, 1) ,
    (1, -1, 1) ,(-1, -1, 1) ,(-1, -1, -1) ,(-1, 1, -1) ,(1, 1, -1) ,
    (1, -1, -1) ,(-1, -1, -1) ,(-1, 1, -1) ,(-1, 1, 1)],
    k = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    cmds.scale(0.5, 0.5, 0.5)
    #cmds.addAttr(L_IK_Hand_Controller_Ctrl, longName='______________________', attributeType='enum', en='____________', keyable=True)
    #mel.eval('setAttr -lock true "L_IK_Hand_Ctrl.______________________";')
    #cmds.addAttr(L_IK_Hand_Controller_Ctrl, longName = 'Heel', attributeType = 'float', min = 1, max = 10, keyable=True) 
    #cmds.addAttr(L_IK_Hand_Controller_Ctrl, longName = 'Toe', attributeType = 'float', min = 1, max = 10, keyable=True) 
    cmds.listRelatives(L_IK_Hand_Controller_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_IK_Hand_Controller_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_IK_Hand_Controller_Ctrl), Color2) 
    cmds.xform(L_IK_Hand_Controller_Ctrl, worldSpace=True, translation=L_IK_Hand_Controller_tuple)
    cmds.parent(L_IK_Hand_Controller_Ctrl, L_IK_Hand_Controller_Grp)
    cmds.makeIdentity(L_IK_Hand_Controller_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.parent(L_IK_Hand_Controller_Grp, Hand_grp)
        
    cmds.refresh(cv =1)
    ################################ R_IK Hand Ctrl 
    R_IK_Hand_Controller = cmds.xform(joint_RWrist, query=True, translation=True, worldSpace=True)
    R_IK_Hand_Controller_tuple = tuple(R_IK_Hand_Controller)
    R_IK_Hand_Controller_Grp = cmds.group(n="R_IK_Hand_Grp", empty=True)
    cmds.xform(R_IK_Hand_Controller_Grp, worldSpace=True, translation=R_IK_Hand_Controller_tuple)
    R_IK_Hand_Controller_Ctrl =cmds.curve(name="R_IK_Hand_Ctrl", d=1, p=[
    (1, 1, 1),(1,1,-1) ,(1, -1, -1) ,(1, -1, 1) ,(-1, -1, 1) ,(-1, 1, 1) ,(1, 1, 1) ,
    (1, -1, 1) ,(-1, -1, 1) ,(-1, -1, -1) ,(-1, 1, -1) ,(1, 1, -1) ,
    (1, -1, -1) ,(-1, -1, -1) ,(-1, 1, -1) ,(-1, 1, 1)],
    k = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    cmds.scale(0.5, 0.5, 0.5)
    #cmds.addAttr(R_IK_Hand_Controller_Ctrl, longName='______________________', attributeType='enum', en='____________', keyable=True)
    #mel.eval('setAttr -lock true "R_IK_Hand_Ctrl.______________________";')
    #cmds.addAttr(R_IK_Hand_Controller_Ctrl, longName = 'Heel', attributeType = 'float', min = 1, max = 10, keyable=True) 
    #cmds.addAttr(R_IK_Hand_Controller_Ctrl, longName = 'Toe', attributeType = 'float', min = 1, max = 10, keyable=True) 
    cmds.listRelatives(R_IK_Hand_Controller_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_IK_Hand_Controller_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_IK_Hand_Controller_Ctrl), Color2) 
    cmds.xform(R_IK_Hand_Controller_Ctrl, worldSpace=True, translation=R_IK_Hand_Controller_tuple)
    cmds.parent(R_IK_Hand_Controller_Ctrl, R_IK_Hand_Controller_Grp)
    cmds.makeIdentity(R_IK_Hand_Controller_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    cmds.parent(R_IK_Hand_Controller_Grp, Hand_grp)

    cmds.refresh(cv =1)
    ################################################################ Knee Foot
    R_Loc_Ctrl_xf = cmds.xform(joint_RKnee, query=True, translation=True, worldSpace=True)
    R_Loc_Ctrl_tuple = tuple(R_Loc_Ctrl_xf) 
    R_Loc_Ctrl_Grp = cmds.group(n="R_Loc_Ctrl_Grp", empty=True)
    cmds.xform(R_Loc_Ctrl_Grp, ws=True, translation=R_Loc_Ctrl_tuple)
    cmds.makeIdentity(R_Loc_Ctrl_Grp, apply=True, translate=True, rotate=True, scale=True)
    R_Loc_Ctrl = cmds.curve(name ="R_Loc_Ctrl", degree = 1,\
                    knot = [0, 1, 2, 3, 4, 5, 6, 7],\
                    point = [(-2, 0, 0),\
                            (2, 0, 0),\
                            (0, 0, 0),\
                            (0, 0, 2),\
                            (0, 0, -2),\
                            (0, 0, 0),\
                            (0, 2, 0),\
                            (0, -2, 0)]\
                )
    cmds.scale(0.3,0.3,0.3)
    cmds.listRelatives(R_Loc_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_Loc_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_Loc_Ctrl), Color2)  
    cmds.xform(R_Loc_Ctrl, ws=True, translation=R_Loc_Ctrl_tuple)   
    cmds.parent(R_Loc_Ctrl, R_Loc_Ctrl_Grp)
    cmds.parent(R_Loc_Ctrl_Grp, R_IK_Foot_Controller_Grp)
    cmds.makeIdentity(R_Loc_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    mel.eval('setAttr "R_Loc_Ctrl_Grp.translateZ" 4;')

    cmds.refresh(cv =1)
    L_Loc_Ctrl_xf = cmds.xform(joint_LKnee, query=True, translation=True, worldSpace=True)
    L_Loc_Ctrl_tuple = tuple(L_Loc_Ctrl_xf) 
    L_Loc_Ctrl_Grp = cmds.group(n="L_Loc_Ctrl_Grp", empty=True)
    cmds.xform(L_Loc_Ctrl_Grp, ws=True, translation=L_Loc_Ctrl_tuple)
    cmds.makeIdentity(L_Loc_Ctrl_Grp, apply=True, translate=True, rotate=True, scale=True)
    L_Loc_Ctrl = cmds.curve(name ="L_Loc_Ctrl", degree = 1,\
                    knot = [0, 1, 2, 3, 4, 5, 6, 7],\
                    point = [(-2, 0, 0),\
                            (2, 0, 0),\
                            (0, 0, 0),\
                            (0, 0, 2),\
                            (0, 0, -2),\
                            (0, 0, 0),\
                            (0, 2, 0),\
                            (0, -2, 0)]\
                )
    cmds.scale(0.3,0.3,0.3)
    cmds.listRelatives(L_Loc_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_Loc_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_Loc_Ctrl), Color2)  
    cmds.xform(L_Loc_Ctrl, ws=True, translation=L_Loc_Ctrl_tuple)   
    cmds.parent(L_Loc_Ctrl, L_Loc_Ctrl_Grp)
    cmds.parent(L_Loc_Ctrl_Grp, L_IK_Foot_Controller_Grp)
    cmds.makeIdentity(L_Loc_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    mel.eval('setAttr "L_Loc_Ctrl_Grp.translateZ" 4;')

    cmds.refresh(cv =1)
    ############################################################# Elbow Hand
    R_ElbowFL_Ctrl_xf = cmds.xform(joint_RElbow, query=True, translation=True, worldSpace=True)
    R_ElbowFL_Ctrl_tuple = tuple(R_ElbowFL_Ctrl_xf) 
    R_ElbowFL_Ctrl_Grp = cmds.group(n="R_ElbowFL_Ctrl_Grp", empty=True)
    cmds.xform(R_ElbowFL_Ctrl_Grp, ws=True, translation=R_ElbowFL_Ctrl_tuple)
    cmds.makeIdentity(R_ElbowFL_Ctrl_Grp, apply=True, translate=True, rotate=True, scale=True)
    R_ElbowFL_Ctrl = cmds.curve(name ="R_ElbowFL_Ctrl", degree = 1,\
                    knot = [0, 1, 2, 3, 4, 5, 6, 7],\
                    point = [(-2, 0, 0),\
                            (2, 0, 0),\
                            (0, 0, 0),\
                            (0, 0, 2),\
                            (0, 0, -2),\
                            (0, 0, 0),\
                            (0, 2, 0),\
                            (0, -2, 0)]\
                )
    cmds.scale(0.3,0.3,0.3)
    cmds.listRelatives(R_ElbowFL_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_ElbowFL_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(R_ElbowFL_Ctrl), Color2)  
    cmds.xform(R_ElbowFL_Ctrl, ws=True, translation=R_ElbowFL_Ctrl_tuple)   
    cmds.parent(R_ElbowFL_Ctrl, R_ElbowFL_Ctrl_Grp)
    cmds.parent(R_ElbowFL_Ctrl_Grp, R_IK_Hand_Controller_Grp)
    cmds.makeIdentity(R_ElbowFL_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    mel.eval('setAttr "R_ElbowFL_Ctrl_Grp.translateZ" -4;')


    cmds.refresh(cv =1)
    L_ElbowFL_Ctrl_xf = cmds.xform(joint_LElbow, query=True, translation=True, worldSpace=True)
    L_ElbowFL_Ctrl_tuple = tuple(L_ElbowFL_Ctrl_xf) 
    L_ElbowFL_Ctrl_Grp = cmds.group(n="L_ElbowFL_Ctrl_Grp", empty=True)
    cmds.xform(L_ElbowFL_Ctrl_Grp, ws=True, translation=L_ElbowFL_Ctrl_tuple)
    cmds.makeIdentity(L_ElbowFL_Ctrl_Grp, apply=True, translate=True, rotate=True, scale=True)
    L_ElbowFL_Ctrl = cmds.curve(name ="L_ElbowFL_Ctrl", degree = 1,\
                    knot = [0, 1, 2, 3, 4, 5, 6, 7],\
                    point = [(-2, 0, 0),\
                            (2, 0, 0),\
                            (0, 0, 0),\
                            (0, 0, 2),\
                            (0, 0, -2),\
                            (0, 0, 0),\
                            (0, 2, 0),\
                            (0, -2, 0)]\
                )
    cmds.scale(0.3,0.3,0.3)
    cmds.listRelatives(L_ElbowFL_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_ElbowFL_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(L_ElbowFL_Ctrl), Color2)  
    cmds.xform(L_ElbowFL_Ctrl, ws=True, translation=L_ElbowFL_Ctrl_tuple)   
    cmds.parent(L_ElbowFL_Ctrl, L_ElbowFL_Ctrl_Grp)
    cmds.parent(L_ElbowFL_Ctrl_Grp, L_IK_Hand_Controller_Grp)
    cmds.makeIdentity(L_ElbowFL_Ctrl, apply=True, translate=True, rotate=True, scale=True)
    mel.eval('setAttr "L_ElbowFL_Ctrl_Grp.translateZ" -4;')




    cmds.refresh(cv =1)
    ################################################################################ creat joint IK FK Root
    ################################ IK Root


    mel.eval("""
    select -r Root ;
    duplicate -rr;
    select -r Root1|R_Hip ;
    delete;
    //select -r Root1|L_Hip ;
    //delete;
    select -r Root1|Spine1|Chest|Neck Root1|Spine1|Chest|R_Scapula ;
    delete;
    rename "Root1" "IK_Root";
    select -r IK_Root|Spine1 ;
    rename "IK_Root|Spine1" "IK_Spine";
    select -r IK_Spine|Chest ;
    rename "IK_Spine|Chest" "IK_Chest";
    select -r IK_Root|L_Hip ;
    delete;
    select -r IK_Chest|L_Scapula ;
    delete;
    CBunlockAttr "IK_Chest.tz";
    CBunlockAttr "IK_Root.tz";
    CBunlockAttr "IK_Spine.tz";
    CBunlockAttr "IK_Chest.rx";
    CBunlockAttr "IK_Root.rx";
    CBunlockAttr "IK_Spine.rx";
    CBunlockAttr "IK_Chest.ry";
    CBunlockAttr "IK_Root.ry";
    CBunlockAttr "IK_Spine.ry";
    CBunlockAttr "IK_Chest.tx";
    CBunlockAttr "IK_Root.tx";
    CBunlockAttr "IK_Spine.tx";
    CBunlockAttr "IK_Chest.ty";
    CBunlockAttr "IK_Root.ty";
    CBunlockAttr "IK_Spine.ty";
    CBunlockAttr "IK_Chest.tz";
    CBunlockAttr "IK_Root.tz";
    CBunlockAttr "IK_Spine.tz";
                      """)
    cmds.parent("IK_Root", "Skeleton")
    
    # IK_Root = cmds.xform(joint_Root, query=True, translation=True, worldSpace=True)
    # IK_Root_tuple = tuple(IK_Root)
    # IK_Spine = cmds.xform(joint_Spine1, query=True, translation=True, worldSpace=True)
    # IK_Spine_tuple = tuple(IK_Spine)
    # IK_Chest = cmds.xform(joint_Chest, query=True, translation=True, worldSpace=True)
    # IK_Chest_tuple = tuple(IK_Chest)
    # IK_Root = cmds.xform(joint_Root, query=True, translation=True, worldSpace=True)
    # IK_Root_tuple = tuple(IK_Root)
    # IK_Spine = cmds.xform(joint_Spine1, query=True, translation=True, worldSpace=True)
    # IK_Spine_tuple = tuple(IK_Spine)
    # IK_Chest = cmds.xform(joint_Chest, query=True, translation=True, worldSpace=True)
    # IK_Chest_tuple = tuple(IK_Chest)

    # IK_Root_jnt = cmds.joint(n="IK_Root")
    # cmds.parent(IK_Root_jnt, Skeleton_grp)
    # cmds.xform(IK_Root_jnt, worldSpace=True, translation=IK_Root_tuple)
    # #cmds.matchTransform(IK_Root_jnt, joint_Root, pos=True, rot=True)

    # IK_Spine_jnt = cmds.joint(n="IK_Spine")
    # cmds.xform(IK_Spine_jnt, worldSpace=True, translation=IK_Spine_tuple)
    # #cmds.matchTransform(IK_Spine_jnt, joint_Spine1, pos=True, rot=True)

    # IK_Chest_jnt = cmds.joint(n="IK_Chest")
    # cmds.xform(IK_Chest_jnt, worldSpace=True, translation=IK_Chest_tuple)
    # #cmds.matchTransform(IK_Chest_jnt, joint_Chest, pos=True, rot=True)  
    # mel.eval("""
    # select -r IK_Root ;
    # FreezeTransformations;
    # joint -e  -oj xyz -secondaryAxisOrient yup -ch -zso;
    # select -r IK_Chest ;
    # setAttr "IK_Chest.jointOrientY" 0;
    # setAttr "IK_Chest.jointOrientX" 0;
    # setAttr "IK_Chest.jointOrientZ" 0;
    #          """)
    ################################ FK Root
    # FK_Root = cmds.xform(joint_Root, query=True, translation=True, worldSpace=True)
    # FK_Root_tuple = tuple(FK_Root)
    # FK_Spine = cmds.xform(joint_Spine1, query=True, translation=True, worldSpace=True)
    # FK_Spine_tuple = tuple(FK_Spine)
    # FK_Chest = cmds.xform(joint_Chest, query=True, translation=True, worldSpace=True)
    # FK_Chest_tuple = tuple(FK_Chest)

    cmds.refresh(cv =1)
    FK_Root_jnt = cmds.joint(n="FK_Root")
    cmds.parent(FK_Root_jnt, Skeleton_grp)
    cmds.matchTransform(FK_Root_jnt, joint_Root, pos=True, rot=True)

    FK_Spine_jnt = cmds.joint(n="FK_Spine")
    cmds.matchTransform(FK_Spine_jnt, joint_Spine1, pos=True, rot=True)
    
    FK_Chest_jnt = cmds.joint(n="FK_Chest")
    cmds.matchTransform(FK_Chest_jnt, joint_Chest, pos=True, rot=True)  
    ################################################################################ ParentConstraint
    cmds.refresh(cv =1)
    mel.eval("""
    //--------------------------------------- constraint root         
    select -r IK_Root ;
    select -add FK_Root ;
    select -add Root ;
    parentConstraint -mo -weight 1; 

    select -r IK_Spine ;
    select -add FK_Spine ;
    select -add Spine1 ;
    parentConstraint -mo -weight 1;              

    select -r IK_Chest ;
    select -add FK_Chest ;
    select -add Chest ;
    parentConstraint -mo -weight 1; 
             
    setAttr "Root_parentConstraint1.IK_RootW0" 0;
    setAttr "Spine1_parentConstraint1.IK_SpineW0" 0;
    setAttr "Chest_parentConstraint1.IK_ChestW0" 0;  
                    
    select -r Root L_Hand R_Hand ;
    parent Root Skeleton ;
    parent L_Hand Skeleton ;
    parent R_Hand Skeleton ; 
             
    select -r R_Scapula_Ctrl ;
    select -add R_Shoulder_Grp ;
    parentConstraint -mo -weight 1;
    select -r L_Scapula_Ctrl ;
    select -add L_Shoulder_Grp ;
    parentConstraint -mo -weight 1;
             
    select -r Body_Ctrl ;
    select -add Root_Ctrl_Grp ;
    parentConstraint -mo -weight 1;
             
    select -r Main_Controller ;
    select -add Body_Ctrl_Grp ;
    parentConstraint -mo -weight 1;
             
    select -r Root_Ctrl ;
    select -add L_Hip_Ctrl_Grp ;
    parentConstraint -mo -weight 1;
             
    select -r Root_Ctrl ;
    select -add R_Hip_Ctrl_Grp ;
    parentConstraint -mo -weight 1;
             
    select -r Chest_Ctrl ;
    select -add Neck_Ctrl_Grp ;
    parentConstraint -mo -weight 1;       

    select -r Chest_Ctrl ;
    select -add R_Scapula_Ctrl_Grp ;
    parentConstraint -mo -weight 1; 
             
    select -r Chest_Ctrl ;
    select -add L_Scapula_Ctrl_Grp ;
    parentConstraint -mo -weight 1; 

                          
             """)
    

    ###################################################################### Create joint IK FK
    cmds.refresh(cv =1)
    mel.eval("""
    select -r L_Hip ;
    duplicate -rr;
    select -r L_Hip1 ;
    searchReplaceNames "L" "IK_L" "hierarchy";
    rename "IK_L_Hip1" "IK_L_Hip";

    select -r L_Hip ;
    duplicate -rr;
    select -r L_Hip1 ;
    searchReplaceNames "L" "FK_L" "hierarchy";
    rename "FK_L_Hip1" "FK_L_Hip";

    select -r R_Hip ;
    duplicate -rr;
    select -r R_Hip1 ;
    searchReplaceNames "R" "IK_R" "hierarchy";
    rename "IK_R_Hip1" "IK_R_Hip";

    select -r R_Hip ;
    duplicate -rr;
    select -r R_Hip1 ;
    searchReplaceNames "R" "FK_R" "hierarchy";
    rename "FK_R_Hip1" "FK_R_Hip";
             
    select -r L_Shoulder ;
    duplicate -rr;
    select -r L_Shoulder1 ;
    searchReplaceNames "L" "IK_L" "hierarchy";
    rename "IK_L_Shoulder1" "IK_L_Shoulder";
             
    select -r L_Shoulder ;
    duplicate -rr;
    select -r L_Shoulder1 ;
    searchReplaceNames "L" "FK_L" "hierarchy";
    rename "FK_L_Shoulder1" "FK_L_Shoulder";   

    select -r R_Shoulder ;
    duplicate -rr;
    select -r R_Shoulder1 ;
    searchReplaceNames "R" "IK_R" "hierarchy";
    rename "IK_R_Shoulder1" "IK_R_Shoulder";
             
    select -r R_Shoulder ;
    duplicate -rr;
    select -r R_Shoulder1 ;
    searchReplaceNames "R" "FK_R" "hierarchy";
    rename "FK_R_Shoulder1" "FK_R_Shoulder";                       
             """)
    ################################################################################## IK_Handle_Foot
    # mel.eval("""
    # select -r IK_L_Hip ;
    # select -add IK_L_Ankle ;
    # ikHandle;
    # select -r IK_L_Ankle ;
    # select -add IK_L_Toes ;
    # ikHandle;
    # select -add IK_L_Toes ;
    # select -add IK_L_ToesEnd ;
    # ikHandle;
    # rename "ikHandle1" "L_ikHandle_Ankle";
    # rename "ikHandle2" "L_ikHandle_Tiptoe";
    # rename "ikHandle3" "L_ikHandle_Toe";

    # select -r IK_R_Hip ;
    # select -add IK_R_Ankle ;
    # ikHandle;
    # select -r IK_R_Ankle ;
    # select -add IK_R_Toes ;
    # ikHandle;
    # select -add IK_R_Toes ;
    # select -add IK_R_ToesEnd ;
    # ikHandle;
    # rename "ikHandle1" "R_ikHandle_Ankle";
    # rename "ikHandle2" "R_ikHandle_Tiptoe";
    # rename "ikHandle3" "R_ikHandle_Toe";
    #          """)
    cmds.refresh(cv =1)
    L_Heel_Grp = cmds.group(n="L_Heel_Grp", empty=True)
    cmds.parent(L_Heel_Grp, IK_FK_System)
    L_Toe_Grp = cmds.group(n="L_Toe_Grp", empty=True)
    cmds.parent(L_Toe_Grp, L_Heel_Grp)

    R_Heel_Grp = cmds.group(n="R_Heel_Grp", empty=True)
    cmds.parent(R_Heel_Grp, IK_FK_System)
    R_Toe_Grp = cmds.group(n="R_Toe_Grp", empty=True)
    cmds.parent(R_Toe_Grp, R_Heel_Grp)

    left_hip = 'IK_L_Hip'
    left_ankle = 'IK_L_Ankle'
    left_toes = 'IK_L_Toes'
    left_toes_end = 'IK_L_ToesEnd'
    left_ankle_ik = cmds.ikHandle(startJoint=left_hip, endEffector=left_ankle)[0]
    left_tiptoe_ik = cmds.ikHandle(startJoint=left_ankle, endEffector=left_toes)[0]
    left_toe_ik = cmds.ikHandle(startJoint=left_toes, endEffector=left_toes_end)[0]
    cmds.rename(left_ankle_ik, "L_ikHandle_Ankle")
    cmds.rename(left_tiptoe_ik, "L_ikHandle_Tiptoe")
    cmds.rename(left_toe_ik, "L_ikHandle_Toe")

    cmds.refresh(cv =1)
    right_hip = 'IK_R_Hip'
    right_ankle = 'IK_R_Ankle'
    right_toes = 'IK_R_Toes'
    right_toes_end = 'IK_R_ToesEnd'
    right_ankle_ik = cmds.ikHandle(startJoint=right_hip, endEffector=right_ankle)[0]
    right_tiptoe_ik = cmds.ikHandle(startJoint=right_ankle, endEffector=right_toes)[0]
    right_toe_ik = cmds.ikHandle(startJoint=right_toes, endEffector=right_toes_end)[0]
    cmds.rename(right_ankle_ik, "R_ikHandle_Ankle")
    cmds.rename(right_tiptoe_ik, "R_ikHandle_Tiptoe")
    cmds.rename(right_toe_ik, "R_ikHandle_Toe")

    cmds.parent("R_ikHandle_Ankle", R_Toe_Grp)
    cmds.parent("R_ikHandle_Tiptoe", R_Toe_Grp)
    cmds.parent("R_ikHandle_Toe", R_Toe_Grp)

    cmds.parent("L_ikHandle_Ankle", L_Toe_Grp)
    cmds.parent("L_ikHandle_Tiptoe", L_Toe_Grp)
    cmds.parent("L_ikHandle_Toe", L_Toe_Grp)

    cmds.refresh(cv =1)
    ################################################################ IK Handle Hand
    left_Shoulder = 'IK_L_Shoulder'
    left_Hand = 'IK_L_Wrist'
    left_Hand_IK = cmds.ikHandle(startJoint=left_Shoulder, endEffector=left_Hand)[0]
    cmds.rename(left_Hand_IK, "L_ikHandle_Hand")
    cmds.parent("L_ikHandle_Hand", L_IK_Hand_Controller_Ctrl)

    Right_Shoulder = 'IK_R_Shoulder'
    Right_Hand = 'IK_R_Wrist'
    Right_Hand_IK = cmds.ikHandle(startJoint=Right_Shoulder, endEffector=Right_Hand)[0]
    cmds.rename(Right_Hand_IK, "R_ikHandle_Hand")
    cmds.parent("R_ikHandle_Hand", R_IK_Hand_Controller_Ctrl)

    cmds.refresh(cv =1)
    ################################################################## IK Loc Foot
    mel.eval("""
    select -r R_ElbowFL_Ctrl ;
    select -add R_ikHandle_Hand ;
    poleVectorConstraint -weight 1;
    select -r L_ElbowFL_Ctrl ;
    select -add L_ikHandle_Hand ;
    poleVectorConstraint -weight 1;
    
    select -r R_Loc_Ctrl ;
    select -add R_ikHandle_Ankle ;
    poleVectorConstraint -weight 1;
    select -r L_Loc_Ctrl ;
    select -add L_ikHandle_Ankle ;
    poleVectorConstraint -weight 1;
             
    select -r L_IK_Foot_Ctrl ;
    select -add L_Loc_Ctrl_Grp ;
    parentConstraint -mo -weight 1;

    select -r R_IK_Foot_Ctrl ;
    select -add R_Loc_Ctrl_Grp ;
    parentConstraint -mo -weight 1;             
    """)

    cmds.refresh(cv =1)
    ################################################################ IK Root and bindSkin ik root

    mel.eval("""
    select -r IK_Root ;
    select -add IK_Chest ;
    ikHandle -sol ikSplineSolver;
    select -r curve1 ;
    rename "curve1" "IK_Curve_Root";
             
    select -r Root_Ctrl_Jnt ;
    select -add Chest_Ctrl_Jnt ;         
    select -add IK_Curve_Root ; 
    SmoothBindSkin;
           
             """)
    # setAttr "IK_Chest.rotateZ" 0;
    # shadingNode -asUtility curveInfo;
    # shadingNode -asUtility multiplyDivide;
    # rename "curveInfo1" "Curve_Root";
    # rename "multiplyDivide1" "Mul_Root";
    # connectAttr -f IK_Curve_RootShape.worldSpace[0] Curve_Root.inputCurve;
    # connectAttr -f Curve_Root.arcLength Mul_Root.input1X;

    # connectAttr -f Mul_Root.outputX |Basic_Rig_Tri3D|Skeleton|IK_Root.scaleX;
    # connectAttr -f Mul_Root.outputX IK_Spine.scaleX;
    # connectAttr -f Mul_Root.outputX IK_Chest.scaleX;
    # setAttr "Mul_Root.operation" 2;
    # setAttr "Mul_Root.input2X" 3.182; 
    cmds.refresh(cv =1)
    ################################################################ Parent Constraint Joint
    mel.eval("""

    select -r IK_R_Hip ;
    select -add FK_R_Hip ;
    select -add R_Hip ;
    parentConstraint -mo -weight 1;

    select -r IK_R_Knee ;
    select -add FK_R_Knee ;
    select -add R_Knee ;
    parentConstraint -mo -weight 1;

    select -r IK_R_Ankle ;
    select -add FK_R_Ankle ;
    select -add R_Ankle ;
    parentConstraint -mo -weight 1;

    select -r IK_R_Toes ;
    select -add FK_R_Toes ;
    select -add R_Toes ;
    parentConstraint -mo -weight 1;

    select -r IK_R_ToesEnd ;
    select -add FK_R_ToesEnd ;
    select -add R_ToesEnd ;
    parentConstraint -mo -weight 1;


    select -r IK_L_Hip ;
    select -add FK_L_Hip ;
    select -add L_Hip ;
    parentConstraint -mo -weight 1;

    select -r IK_L_Knee ;
    select -add FK_L_Knee ;
    select -add L_Knee ;
    parentConstraint -mo -weight 1;

    select -r IK_L_Ankle ;
    select -add FK_L_Ankle ;
    select -add L_Ankle ;
    parentConstraint -mo -weight 1;

    select -r IK_L_Toes ;
    select -add FK_L_Toes ;
    select -add L_Toes ;
    parentConstraint -mo -weight 1;

    select -r IK_L_ToesEnd ;
    select -add FK_L_ToesEnd ;
    select -add L_ToesEnd ;
    parentConstraint -mo -weight 1;                         

    //----------------------------------------------------- Hand
    select -r IK_R_Shoulder ;
    select -add FK_R_Shoulder ;
    select -add R_Shoulder ;
    parentConstraint -mo -weight 1;

    select -r IK_R_Elbow ;
    select -add FK_R_Elbow ;
    select -add R_Elbow ;
    parentConstraint -mo -weight 1;

    select -r IK_R_Wrist ;
    select -add FK_R_Wrist ;
    select -add R_Wrist ;
    parentConstraint -mo -weight 1;                                       

    select -r IK_L_Shoulder ;
    select -add FK_L_Shoulder ;
    select -add L_Shoulder ;
    parentConstraint -mo -weight 1;

    select -r IK_L_Elbow ;
    select -add FK_L_Elbow ;
    select -add L_Elbow ;
    parentConstraint -mo -weight 1;

    select -r IK_L_Wrist ;
    select -add FK_L_Wrist ;
    select -add L_Wrist ;
    parentConstraint -mo -weight 1;  

    //------------------------------------------------- FK hand
    select -r R_Shoulder_Ctrl ;
    select -tgl FK_R_Shoulder ;
    parentConstraint -mo -weight 1;

    select -r R_Elbow_Ctrl ;
    select -tgl FK_R_Elbow ;
    parentConstraint -mo -weight 1;

    select -r R_Wrist_Ctrl ;
    select -tgl FK_R_Wrist ;
    parentConstraint -mo -weight 1;                                                   

    select -r L_Shoulder_Ctrl ;
    select -tgl FK_L_Shoulder ;
    parentConstraint -mo -weight 1;

    select -r L_Elbow_Ctrl ;
    select -tgl FK_L_Elbow ;
    parentConstraint -mo -weight 1;                                       
                
    select -r L_Wrist_Ctrl ;
    select -tgl FK_L_Wrist ;
    parentConstraint -mo -weight 1;             
             """)
    cmds.refresh(cv =1)
    ###################################################################### root parent
    mel.eval("""
                      
    select -r Main_Controller ;
    select -add R_IK_Foot_Grp ;
    parentConstraint -mo -weight 1;  
    select -r Main_Controller ;
    select -add L_IK_Foot_Grp ;
    parentConstraint -mo -weight 1; 
             
    //-------------------------------------------------------- neck IK
    select -r IK_Chest_Ctrl ;
    select -add Neck_Ctrl_Grp ;
    parentConstraint -mo -weight 1; 
    
    //-------------------------------------------------------- neck parent
    select -r Neck_Ctrl ;
    select -tgl Neck ;
    parentConstraint -mo -weight 1;         
             """)

    
    cmds.refresh(cv =1)
    ###################################################################### finger Parent Constraint
    mel.eval("""
    //------------------------------------ R_Hand
    select -r R_Hand_Ctrl ;
    select -add R_Hand ;
    parentConstraint -mo -weight 1; 
    
    select -r R_ThumbFinger1_Ctrl ;
    select -add R_ThumbFinger1 ;
    parentConstraint -mo -weight 1;
              
    select -r R_ThumbFinger2_Ctrl ;
    select -add R_ThumbFinger2 ;
    parentConstraint -mo -weight 1; 
    
    select -r R_ThumbFinger3_Ctrl ;
    select -add R_ThumbFinger3 ;
    parentConstraint -mo -weight 1;  

              
    select -r R_IndexFinger1_Ctrl ;
    select -add R_IndexFinger1 ;
    parentConstraint -mo -weight 1; 
    
    select -r R_IndexFinger2_Ctrl ;
    select -add R_IndexFinger2 ;
    parentConstraint -mo -weight 1; 

    select -r R_IndexFinger3_Ctrl ;
    select -add R_IndexFinger3 ;
    parentConstraint -mo -weight 1; 
    
    select -r R_MiddleFinger1_Ctrl ;
    select -add R_MiddleFinger1 ;
    parentConstraint -mo -weight 1;
              
    select -r R_MiddleFinger2_Ctrl ;
    select -add R_MiddleFinger2 ;
    parentConstraint -mo -weight 1; 
    
    select -r R_MiddleFinger3_Ctrl ;
    select -add R_MiddleFinger3 ;
    parentConstraint -mo -weight 1;  

              
    select -r R_RingFinger1_Ctrl ;
    select -add R_RingFinger1 ;
    parentConstraint -mo -weight 1; 
    
    select -r R_RingFinger2_Ctrl ;
    select -add R_RingFinger2 ;
    parentConstraint -mo -weight 1; 

    select -r R_RingFinger3_Ctrl ;
    select -add R_RingFinger3 ;
    parentConstraint -mo -weight 1; 
    
    select -r R_PinkyFinger1_Ctrl ;
    select -add R_PinkyFinger1 ;
    parentConstraint -mo -weight 1;
              
    select -r R_PinkyFinger2_Ctrl ;
    select -add R_PinkyFinger2 ;
    parentConstraint -mo -weight 1; 
    
    select -r R_PinkyFinger3_Ctrl ;
    select -add R_PinkyFinger3 ;
    parentConstraint -mo -weight 1;  
    

     
    //------------------------------------ L_Hand
    select -r L_Hand_Ctrl ;
    select -add L_Hand ;
    parentConstraint -mo -weight 1; 
    
    select -r L_ThumbFinger1_Ctrl ;
    select -add L_ThumbFinger1 ;
    parentConstraint -mo -weight 1;
              
    select -r L_ThumbFinger2_Ctrl ;
    select -add L_ThumbFinger2 ;
    parentConstraint -mo -weight 1; 
    
    select -r L_ThumbFinger3_Ctrl ;
    select -add L_ThumbFinger3 ;
    parentConstraint -mo -weight 1;  

              
    select -r L_IndexFinger1_Ctrl ;
    select -add L_IndexFinger1 ;
    parentConstraint -mo -weight 1; 
    
    select -r L_IndexFinger2_Ctrl ;
    select -add L_IndexFinger2 ;
    parentConstraint -mo -weight 1; 

    select -r L_IndexFinger3_Ctrl ;
    select -add L_IndexFinger3 ;
    parentConstraint -mo -weight 1; 
    
    select -r L_MiddleFinger1_Ctrl ;
    select -add L_MiddleFinger1 ;
    parentConstraint -mo -weight 1;
              
    select -r L_MiddleFinger2_Ctrl ;
    select -add L_MiddleFinger2 ;
    parentConstraint -mo -weight 1; 
    
    select -r L_MiddleFinger3_Ctrl ;
    select -add L_MiddleFinger3 ;
    parentConstraint -mo -weight 1;  

              
    select -r L_RingFinger1_Ctrl ;
    select -add L_RingFinger1 ;
    parentConstraint -mo -weight 1; 
    
    select -r L_RingFinger2_Ctrl ;
    select -add L_RingFinger2 ;
    parentConstraint -mo -weight 1; 

    select -r L_RingFinger3_Ctrl ;
    select -add L_RingFinger3 ;
    parentConstraint -mo -weight 1; 
    
    select -r L_PinkyFinger1_Ctrl ;
    select -add L_PinkyFinger1 ;
    parentConstraint -mo -weight 1;
              
    select -r L_PinkyFinger2_Ctrl ;
    select -add L_PinkyFinger2 ;
    parentConstraint -mo -weight 1; 
    
    select -r L_PinkyFinger3_Ctrl ;
    select -add L_PinkyFinger3 ;
    parentConstraint -mo -weight 1; 
    

    """)
    cmds.refresh(cv =1)
    ###################################################################### parent Elbow Hand
    mel.eval("""
    select -r L_IK_Hand_Ctrl ;
    select -tgl L_ElbowFL_Ctrl_Grp ;
    parentConstraint -mo -weight 1;

    select -r R_IK_Hand_Ctrl ;
    select -tgl R_ElbowFL_Ctrl_Grp ;
    parentConstraint -mo -weight 1;
             """)
    

    cmds.refresh(cv =1)
    ###################################################################### Lock attr IK FK FOOT SW
    mel.eval("""
    setAttr -lock true -keyable false -channelBox false "L_IK_FK_Foot_Ctrl.tx";
    setAttr -lock true -keyable false -channelBox false "R_IKFK_Hand_Ctrl.tx";
    setAttr -lock true -keyable false -channelBox false "L_IKFK_Hand_Ctrl.tx";
    setAttr -lock true -keyable false -channelBox false "R_IK_FK_Foot_Ctrl.tx";
    setAttr -lock true -keyable false -channelBox false "L_IK_FK_Foot_Ctrl.ty";
    setAttr -lock true -keyable false -channelBox false "R_IKFK_Hand_Ctrl.ty";
    setAttr -lock true -keyable false -channelBox false "L_IKFK_Hand_Ctrl.ty";
    setAttr -lock true -keyable false -channelBox false "R_IK_FK_Foot_Ctrl.ty";
    setAttr -lock true -keyable false -channelBox false "L_IK_FK_Foot_Ctrl.tz";
    setAttr -lock true -keyable false -channelBox false "R_IKFK_Hand_Ctrl.tz";
    setAttr -lock true -keyable false -channelBox false "L_IKFK_Hand_Ctrl.tz";
    setAttr -lock true -keyable false -channelBox false "R_IK_FK_Foot_Ctrl.tz";
    setAttr -lock true -keyable false -channelBox false "L_IK_FK_Foot_Ctrl.rx";
    setAttr -lock true -keyable false -channelBox false "R_IKFK_Hand_Ctrl.rx";
    setAttr -lock true -keyable false -channelBox false "L_IKFK_Hand_Ctrl.rx";
    setAttr -lock true -keyable false -channelBox false "R_IK_FK_Foot_Ctrl.rx";
    setAttr -lock true -keyable false -channelBox false "L_IK_FK_Foot_Ctrl.ry";
    setAttr -lock true -keyable false -channelBox false "R_IKFK_Hand_Ctrl.ry";
    setAttr -lock true -keyable false -channelBox false "L_IKFK_Hand_Ctrl.ry";
    setAttr -lock true -keyable false -channelBox false "R_IK_FK_Foot_Ctrl.ry";
    setAttr -lock true -keyable false -channelBox false "L_IK_FK_Foot_Ctrl.rz";
    setAttr -lock true -keyable false -channelBox false "R_IKFK_Hand_Ctrl.rz";
    setAttr -lock true -keyable false -channelBox false "L_IKFK_Hand_Ctrl.rz";
    setAttr -lock true -keyable false -channelBox false "R_IK_FK_Foot_Ctrl.rz";
    setAttr -lock true -keyable false -channelBox false "L_IK_FK_Foot_Ctrl.sx";
    setAttr -lock true -keyable false -channelBox false "R_IKFK_Hand_Ctrl.sx";
    setAttr -lock true -keyable false -channelBox false "L_IKFK_Hand_Ctrl.sx";
    setAttr -lock true -keyable false -channelBox false "R_IK_FK_Foot_Ctrl.sx";
    setAttr -lock true -keyable false -channelBox false "L_IK_FK_Foot_Ctrl.sy";
    setAttr -lock true -keyable false -channelBox false "R_IKFK_Hand_Ctrl.sy";
    setAttr -lock true -keyable false -channelBox false "L_IKFK_Hand_Ctrl.sy";
    setAttr -lock true -keyable false -channelBox false "R_IK_FK_Foot_Ctrl.sy";
    setAttr -lock true -keyable false -channelBox false "L_IK_FK_Foot_Ctrl.sz";
    setAttr -lock true -keyable false -channelBox false "R_IKFK_Hand_Ctrl.sz";
    setAttr -lock true -keyable false -channelBox false "L_IKFK_Hand_Ctrl.sz";
    setAttr -lock true -keyable false -channelBox false "R_IK_FK_Foot_Ctrl.sz";
    setAttr -lock true -keyable false -channelBox false "L_IK_FK_Foot_Ctrl.v";
    setAttr -lock true -keyable false -channelBox false "R_IKFK_Hand_Ctrl.v";
    setAttr -lock true -keyable false -channelBox false "L_IKFK_Hand_Ctrl.v";
    setAttr -lock true -keyable false -channelBox false "R_IK_FK_Foot_Ctrl.v";
             
    setAttr -lock true -keyable false -channelBox false "Constraint_Grp.tx";
    setAttr -lock true -keyable false -channelBox false "IK_FK_System.tx";
    setAttr -lock true -keyable false -channelBox false "Constraint_Grp.ty";
    setAttr -lock true -keyable false -channelBox false "IK_FK_System.ty";
    setAttr -lock true -keyable false -channelBox false "Constraint_Grp.tz";
    setAttr -lock true -keyable false -channelBox false "IK_FK_System.tz";
    setAttr -lock true -keyable false -channelBox false "Constraint_Grp.rx";
    setAttr -lock true -keyable false -channelBox false "IK_FK_System.rx";
    setAttr -lock true -keyable false -channelBox false "Constraint_Grp.ry";
    setAttr -lock true -keyable false -channelBox false "IK_FK_System.ry";
    setAttr -lock true -keyable false -channelBox false "Constraint_Grp.rz";
    setAttr -lock true -keyable false -channelBox false "IK_FK_System.rz";
    setAttr -lock true -keyable false -channelBox false "Constraint_Grp.sx";
    setAttr -lock true -keyable false -channelBox false "IK_FK_System.sx";
    setAttr -lock true -keyable false -channelBox false "Constraint_Grp.sy";
    setAttr -lock true -keyable false -channelBox false "IK_FK_System.sy";
    setAttr -lock true -keyable false -channelBox false "Constraint_Grp.sz";
    setAttr -lock true -keyable false -channelBox false "IK_FK_System.sz";  

    setAttr -lock true -keyable false -channelBox false "Root_Ctrl.tx";
    setAttr -lock true -keyable false -channelBox false "Root_Ctrl.ty";
    setAttr -lock true -keyable false -channelBox false "Root_Ctrl.tz";
    setAttr -lock true -keyable false -channelBox false "Root_Ctrl.sx";
    setAttr -lock true -keyable false -channelBox false "Root_Ctrl.sy";
    setAttr -lock true -keyable false -channelBox false "Root_Ctrl.sz";
    setAttr -lock true -keyable false -channelBox false "Root_Ctrl.v";
             
    setAttr -lock true -keyable false -channelBox false "L_Shoulder_Ctrl.v";
    setAttr -lock true -keyable false -channelBox false "L_Hip_Ctrl.v";
    setAttr -lock true -keyable false -channelBox false "R_Hip_Ctrl.v";
    setAttr -lock true -keyable false -channelBox false "R_Shoulder_Ctrl.v";
             
    setAttr -lock true -keyable false -channelBox false "Main_Controller.sx";
    setAttr -lock true -keyable false -channelBox false "Main_Controller.sy";
    setAttr -lock true -keyable false -channelBox false "Main_Controller.sz";
    setAttr -keyable false -channelBox true "Main_Controller.Scale_Rig";

             """)
    

    cmds.refresh(cv =1)
    ################################################################## set attributes  Hand Foot Ctrl 

        ##################### Foot      
    cmds.addAttr(R_IKFKROOT_Ctrl, longName = 'IK_FK', attributeType = 'float', min = -2 , max = 10, keyable=True) 
    cmds.addAttr(R_IKFKROOT_Ctrl, longName = 'Knee_Follow', attributeType = 'float', min = 1, max = 2, keyable=True) 
    cmds.addAttr(L_IKFKROOT_Ctrl, longName = 'IK_FK', attributeType = 'float', min = -2 , max = 10, keyable=True) 
    cmds.addAttr(L_IKFKROOT_Ctrl, longName = 'Knee_Follow', attributeType = 'float', min = 1, max = 2, keyable=True) 

        ##################### Hand
    cmds.addAttr(L_IKFK_Ctrl, longName = 'FK_IK', attributeType = 'float', min = -2 , max = 10, keyable=True) 
    cmds.addAttr(L_IKFK_Ctrl, longName = 'Elbow_Follow', attributeType = 'float', min = 1, max = 2, keyable=True) 
    cmds.addAttr(L_IKFK_Ctrl, longName = '_________________', attributeType='enum', en='____________', keyable=True) 
    mel.eval('setAttr -lock true "L_IKFK_Hand_Ctrl._________________";')
    cmds.addAttr(L_IKFK_Ctrl, longName = 'Thump', attributeType = 'float', min = -2 , max = 10, keyable=True) 
    cmds.addAttr(L_IKFK_Ctrl, longName = 'Index', attributeType = 'float', min = -2 , max = 10, keyable=True) 
    cmds.addAttr(L_IKFK_Ctrl, longName = 'Middle', attributeType = 'float', min = -2 , max = 10, keyable=True) 
    cmds.addAttr(L_IKFK_Ctrl, longName = 'Ring', attributeType = 'float', min = -2 , max = 10, keyable=True) 
    cmds.addAttr(L_IKFK_Ctrl, longName = 'Pinky', attributeType = 'float', min = -2 , max = 10, keyable=True) 

    cmds.addAttr(R_IKFK_Ctrl, longName = 'FK_IK', attributeType = 'float', min = -2 , max = 10, keyable=True) 
    cmds.addAttr(R_IKFK_Ctrl, longName = 'Elbow_Follow', attributeType = 'float', min = 1, max = 2, keyable=True) 
    cmds.addAttr(R_IKFK_Ctrl, longName = '_________________', attributeType='enum', en='____________', keyable=True) 
    mel.eval('setAttr -lock true "R_IKFK_Hand_Ctrl._________________";')
    cmds.addAttr(R_IKFK_Ctrl, longName = 'Thump', attributeType = 'float', min = -2 , max = 10, keyable=True) 
    cmds.addAttr(R_IKFK_Ctrl, longName = 'Index', attributeType = 'float', min = -2 , max = 10, keyable=True) 
    cmds.addAttr(R_IKFK_Ctrl, longName = 'Middle', attributeType = 'float', min = -2 , max = 10, keyable=True) 
    cmds.addAttr(R_IKFK_Ctrl, longName = 'Ring', attributeType = 'float', min = -2 , max = 10, keyable=True) 
    cmds.addAttr(R_IKFK_Ctrl, longName = 'Pinky', attributeType = 'float', min = -2 , max = 10, keyable=True) 





    cmds.refresh(cv =1)
    ###################################################################### set driven Key
    mel.eval("""
    //---------------------------------------------------------------- set driven Key parentConstraint Foot
    setAttr "R_IK_FK_Foot_Ctrl.IK_FK" 0;
    setAttr "R_ToesEnd_parentConstraint1.IK_R_ToesEndW0" 1;
    setAttr "R_ToesEnd_parentConstraint1.FK_R_ToesEndW1" 0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_ToesEnd_parentConstraint1.IK_R_ToesEndW0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_ToesEnd_parentConstraint1.FK_R_ToesEndW1;
    setAttr "R_IK_FK_Foot_Ctrl.IK_FK" 10;
    setAttr "R_ToesEnd_parentConstraint1.IK_R_ToesEndW0" 0;
    setAttr "R_ToesEnd_parentConstraint1.FK_R_ToesEndW1" 1;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_ToesEnd_parentConstraint1.IK_R_ToesEndW0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_ToesEnd_parentConstraint1.FK_R_ToesEndW1;

    setAttr "R_IK_FK_Foot_Ctrl.IK_FK" 0;
    setAttr "R_Toes_parentConstraint1.IK_R_ToesW0" 1;
    setAttr "R_Toes_parentConstraint1.FK_R_ToesW1" 0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_Toes_parentConstraint1.IK_R_ToesW0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_Toes_parentConstraint1.FK_R_ToesW1;
    setAttr "R_IK_FK_Foot_Ctrl.IK_FK" 10;
    setAttr "R_Toes_parentConstraint1.IK_R_ToesW0" 0;
    setAttr "R_Toes_parentConstraint1.FK_R_ToesW1" 1;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_Toes_parentConstraint1.IK_R_ToesW0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_Toes_parentConstraint1.FK_R_ToesW1;
             
    setAttr "R_IK_FK_Foot_Ctrl.IK_FK" 0;
    setAttr "R_Ankle_parentConstraint1.IK_R_AnkleW0" 1;
    setAttr "R_Ankle_parentConstraint1.FK_R_AnkleW1" 0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_Ankle_parentConstraint1.IK_R_AnkleW0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_Ankle_parentConstraint1.FK_R_AnkleW1;
    setAttr "R_IK_FK_Foot_Ctrl.IK_FK" 10;
    setAttr "R_Ankle_parentConstraint1.IK_R_AnkleW0" 0;
    setAttr "R_Ankle_parentConstraint1.FK_R_AnkleW1" 1;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_Ankle_parentConstraint1.IK_R_AnkleW0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_Ankle_parentConstraint1.FK_R_AnkleW1;     
             
    setAttr "R_IK_FK_Foot_Ctrl.IK_FK" 0;
    setAttr "R_Knee_parentConstraint1.IK_R_KneeW0" 1;
    setAttr "R_Knee_parentConstraint1.FK_R_KneeW1" 0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_Knee_parentConstraint1.IK_R_KneeW0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_Knee_parentConstraint1.FK_R_KneeW1;
    setAttr "R_IK_FK_Foot_Ctrl.IK_FK" 10;
    setAttr "R_Knee_parentConstraint1.IK_R_KneeW0" 0;
    setAttr "R_Knee_parentConstraint1.FK_R_KneeW1" 1;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_Knee_parentConstraint1.IK_R_KneeW0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_Knee_parentConstraint1.FK_R_KneeW1;  
             
    setAttr "R_IK_FK_Foot_Ctrl.IK_FK" 0;
    setAttr "R_Hip_parentConstraint1.IK_R_HipW0" 1;
    setAttr "R_Hip_parentConstraint1.FK_R_HipW1" 0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_Hip_parentConstraint1.IK_R_HipW0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_Hip_parentConstraint1.FK_R_HipW1;
    setAttr "R_IK_FK_Foot_Ctrl.IK_FK" 10;
    setAttr "R_Hip_parentConstraint1.IK_R_HipW0" 0;
    setAttr "R_Hip_parentConstraint1.FK_R_HipW1" 1;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_Hip_parentConstraint1.IK_R_HipW0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_Hip_parentConstraint1.FK_R_HipW1; 
    setAttr "R_IK_FK_Foot_Ctrl.IK_FK" 0;   

    setAttr "L_IK_FK_Foot_Ctrl.IK_FK" 0;
    setAttr "L_ToesEnd_parentConstraint1.IK_L_ToesEndW0" 1;
    setAttr "L_ToesEnd_parentConstraint1.FK_L_ToesEndW1" 0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_ToesEnd_parentConstraint1.IK_L_ToesEndW0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_ToesEnd_parentConstraint1.FK_L_ToesEndW1;
    setAttr "L_IK_FK_Foot_Ctrl.IK_FK" 10;
    setAttr "L_ToesEnd_parentConstraint1.IK_L_ToesEndW0" 0;
    setAttr "L_ToesEnd_parentConstraint1.FK_L_ToesEndW1" 1;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_ToesEnd_parentConstraint1.IK_L_ToesEndW0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_ToesEnd_parentConstraint1.FK_L_ToesEndW1;

    setAttr "L_IK_FK_Foot_Ctrl.IK_FK" 0;
    setAttr "L_Toes_parentConstraint1.IK_L_ToesW0" 1;
    setAttr "L_Toes_parentConstraint1.FK_L_ToesW1" 0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_Toes_parentConstraint1.IK_L_ToesW0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_Toes_parentConstraint1.FK_L_ToesW1;
    setAttr "L_IK_FK_Foot_Ctrl.IK_FK" 10;
    setAttr "L_Toes_parentConstraint1.IK_L_ToesW0" 0;
    setAttr "L_Toes_parentConstraint1.FK_L_ToesW1" 1;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_Toes_parentConstraint1.IK_L_ToesW0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_Toes_parentConstraint1.FK_L_ToesW1;
             
    setAttr "L_IK_FK_Foot_Ctrl.IK_FK" 0;
    setAttr "L_Ankle_parentConstraint1.IK_L_AnkleW0" 1;
    setAttr "L_Ankle_parentConstraint1.FK_L_AnkleW1" 0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_Ankle_parentConstraint1.IK_L_AnkleW0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_Ankle_parentConstraint1.FK_L_AnkleW1;
    setAttr "L_IK_FK_Foot_Ctrl.IK_FK" 10;
    setAttr "L_Ankle_parentConstraint1.IK_L_AnkleW0" 0;
    setAttr "L_Ankle_parentConstraint1.FK_L_AnkleW1" 1;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_Ankle_parentConstraint1.IK_L_AnkleW0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_Ankle_parentConstraint1.FK_L_AnkleW1;     
             
    setAttr "L_IK_FK_Foot_Ctrl.IK_FK" 0;
    setAttr "L_Knee_parentConstraint1.IK_L_KneeW0" 1;
    setAttr "L_Knee_parentConstraint1.FK_L_KneeW1" 0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_Knee_parentConstraint1.IK_L_KneeW0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_Knee_parentConstraint1.FK_L_KneeW1;
    setAttr "L_IK_FK_Foot_Ctrl.IK_FK" 10;
    setAttr "L_Knee_parentConstraint1.IK_L_KneeW0" 0;
    setAttr "L_Knee_parentConstraint1.FK_L_KneeW1" 1;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_Knee_parentConstraint1.IK_L_KneeW0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_Knee_parentConstraint1.FK_L_KneeW1;  
             
    setAttr "L_IK_FK_Foot_Ctrl.IK_FK" 0;
    setAttr "L_Hip_parentConstraint1.IK_L_HipW0" 1;
    setAttr "L_Hip_parentConstraint1.FK_L_HipW1" 0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_Hip_parentConstraint1.IK_L_HipW0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_Hip_parentConstraint1.FK_L_HipW1;
    setAttr "L_IK_FK_Foot_Ctrl.IK_FK" 10;
    setAttr "L_Hip_parentConstraint1.IK_L_HipW0" 0;
    setAttr "L_Hip_parentConstraint1.FK_L_HipW1" 1;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_Hip_parentConstraint1.IK_L_HipW0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_Hip_parentConstraint1.FK_L_HipW1; 
    setAttr "L_IK_FK_Foot_Ctrl.IK_FK" 0;   

    //---------------------------------------------------------------- set driven key IK FK Foot
    setAttr "R_IK_FK_Foot_Ctrl.IK_FK" 0;
    setAttr "R_Hip_Ctrl_Grp.visibility" 0;
    setAttr "R_IK_Foot_Grp.visibility" 1;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_Hip_Ctrl_Grp.visibility;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_IK_Foot_Grp.visibility;
    setAttr "R_IK_FK_Foot_Ctrl.IK_FK" 10;
    setAttr "R_Hip_Ctrl_Grp.visibility" 1;
    setAttr "R_IK_Foot_Grp.visibility" 0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_Hip_Ctrl_Grp.visibility;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_IK_Foot_Grp.visibility;
    setAttr "R_IK_FK_Foot_Ctrl.IK_FK" 0;
             
    setAttr "L_IK_FK_Foot_Ctrl.IK_FK" 0;
    setAttr "L_Hip_Ctrl_Grp.visibility" 0;
    setAttr "L_IK_Foot_Grp.visibility" 1;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_Hip_Ctrl_Grp.visibility;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_IK_Foot_Grp.visibility;
    setAttr "L_IK_FK_Foot_Ctrl.IK_FK" 10;
    setAttr "L_Hip_Ctrl_Grp.visibility" 1;
    setAttr "L_IK_Foot_Grp.visibility" 0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_Hip_Ctrl_Grp.visibility;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_IK_Foot_Grp.visibility;
    setAttr "L_IK_FK_Foot_Ctrl.IK_FK" 0;             
             
    //------------------------------------------------------------- root IK FK
    setAttr "Body_Ctrl.FK_IK" 1;
    setAttr "Root_parentConstraint1.IK_RootW0" 0;
    setAttr "Root_parentConstraint1.FK_RootW1" 1;
    setAttr "Spine1_parentConstraint1.IK_SpineW0" 0;
    setAttr "Spine1_parentConstraint1.FK_SpineW1" 1; 
    setAttr "Chest_parentConstraint1.IK_ChestW0" 0;
    setAttr "Chest_parentConstraint1.FK_ChestW1" 1;                         
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK Root_parentConstraint1.IK_RootW0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK Root_parentConstraint1.FK_RootW1;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK Spine1_parentConstraint1.IK_SpineW0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK Spine1_parentConstraint1.FK_SpineW1;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK Chest_parentConstraint1.IK_ChestW0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK Chest_parentConstraint1.FK_ChestW1;
    setAttr "Body_Ctrl.FK_IK" 10;
    setAttr "Root_parentConstraint1.IK_RootW0" 1;
    setAttr "Root_parentConstraint1.FK_RootW1" 0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK Root_parentConstraint1.IK_RootW0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK Root_parentConstraint1.FK_RootW1;
    setAttr "Spine1_parentConstraint1.IK_SpineW0" 1;
    setAttr "Spine1_parentConstraint1.FK_SpineW1" 0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK Spine1_parentConstraint1.IK_SpineW0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK Spine1_parentConstraint1.FK_SpineW1;
    setAttr "Chest_parentConstraint1.IK_ChestW0" 1;
    setAttr "Chest_parentConstraint1.FK_ChestW1" 0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK Chest_parentConstraint1.IK_ChestW0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK Chest_parentConstraint1.FK_ChestW1;
    setAttr "Body_Ctrl.FK_IK" 1;
             
    //---------------------------------------------------------------- Neck Ctrl Grp
    setAttr "Body_Ctrl.FK_IK" 1;
    setAttr "Neck_Ctrl_Grp_parentConstraint1.Chest_CtrlW0" 1;
    setAttr "Neck_Ctrl_Grp_parentConstraint1.IK_Chest_CtrlW1" 0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK Neck_Ctrl_Grp_parentConstraint1.Chest_CtrlW0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK Neck_Ctrl_Grp_parentConstraint1.IK_Chest_CtrlW1;
    setAttr "Body_Ctrl.FK_IK" 10;
    setAttr "Neck_Ctrl_Grp_parentConstraint1.Chest_CtrlW0" 0;
    setAttr "Neck_Ctrl_Grp_parentConstraint1.IK_Chest_CtrlW1" 1;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK Neck_Ctrl_Grp_parentConstraint1.Chest_CtrlW0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK Neck_Ctrl_Grp_parentConstraint1.IK_Chest_CtrlW1;
    setAttr "Body_Ctrl.FK_IK" 1;                            
             """)
    
    cmds.refresh(cv =1)
    ################################################################# Parent Constraint FK Foot
    mel.eval("""
    select -r L_Hip_Ctrl ;
    select -tgl FK_L_Hip ;
    parentConstraint -mo -weight 1;

    select -r L_Knee_Ctrl ;
    select -tgl FK_L_Knee ;
    parentConstraint -mo -weight 1;

    select -r L_Ankle_Ctrl ;
    select -tgl FK_L_Ankle ;
    parentConstraint -mo -weight 1;

    select -r L_Toes_Ctrl ;
    select -tgl FK_L_Toes ;
    parentConstraint -mo -weight 1;
             
    select -r R_Hip_Ctrl ;
    select -tgl FK_R_Hip ;
    parentConstraint -mo -weight 1;

    select -r R_Knee_Ctrl ;
    select -tgl FK_R_Knee ;
    parentConstraint -mo -weight 1;

    select -r R_Ankle_Ctrl ;
    select -tgl FK_R_Ankle ;
    parentConstraint -mo -weight 1;

    select -r R_Toes_Ctrl ;
    select -tgl FK_R_Toes ;
    parentConstraint -mo -weight 1;
             
    //---------------------------------------------------- Parent IK ctrl vs Ik handle
    select -r R_Toe_Ctrl ;
    select -tgl R_Heel_Grp ;
    parentConstraint -mo -weight 1;
             
    select -r L_Toe_Ctrl ;
    select -tgl L_Heel_Grp ;
    parentConstraint -mo -weight 1;              
    //--------------------------------------------------- Parent Ankle vs IK FK
    select -r L_IK_Foot_Ctrl ;
    select -add L_IKFKFOOT_Grp ;
    parentConstraint -mo -weight 1;

    select -r R_IK_Foot_Ctrl ;
    select -add R_IKFKFOOT_Grp ;
    parentConstraint -mo -weight 1;
    
    //---------------------------------------------------- Parent FK Root
    select -r Root_Ctrl ;
    select -add FK_Root ;
    
    parentConstraint -mo -weight 1;
    select -r Spine_Ctrl ;
    select -tgl FK_Spine ;
    performParentConstraint 0;
    
    parentConstraint -mo -weight 1;
    select -r Chest_Ctrl ;
    select -tgl FK_Chest ;
    performParentConstraint 0;
    parentConstraint -mo -weight 1;
         
             
    //---------------------------------------------------------------- set driven key IK FK Foot ctrl grp
    setAttr "L_IK_FK_Foot_Ctrl.IK_FK" 0;
    setAttr "L_IKFKFOOT_Grp_parentConstraint1.L_Ankle_CtrlW0" 0;
    setAttr "L_IKFKFOOT_Grp_parentConstraint1.L_IK_Foot_CtrlW1" 1;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_IKFKFOOT_Grp_parentConstraint1.L_Ankle_CtrlW0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_IKFKFOOT_Grp_parentConstraint1.L_IK_Foot_CtrlW1;
    setAttr "L_IK_FK_Foot_Ctrl.IK_FK" 10;
    setAttr "L_IKFKFOOT_Grp_parentConstraint1.L_Ankle_CtrlW0" 1;
    setAttr "L_IKFKFOOT_Grp_parentConstraint1.L_IK_Foot_CtrlW1" 0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_IKFKFOOT_Grp_parentConstraint1.L_Ankle_CtrlW0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.IK_FK L_IKFKFOOT_Grp_parentConstraint1.L_IK_Foot_CtrlW1;

    setAttr "R_IK_FK_Foot_Ctrl.IK_FK" 0;
    setAttr "R_IKFKFOOT_Grp_parentConstraint1.R_Ankle_CtrlW0" 0;
    setAttr "R_IKFKFOOT_Grp_parentConstraint1.R_IK_Foot_CtrlW1" 1;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_IKFKFOOT_Grp_parentConstraint1.R_Ankle_CtrlW0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_IKFKFOOT_Grp_parentConstraint1.R_IK_Foot_CtrlW1;
    setAttr "R_IK_FK_Foot_Ctrl.IK_FK" 10;
    setAttr "R_IKFKFOOT_Grp_parentConstraint1.R_Ankle_CtrlW0" 1;
    setAttr "R_IKFKFOOT_Grp_parentConstraint1.R_IK_Foot_CtrlW1" 0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_IKFKFOOT_Grp_parentConstraint1.R_Ankle_CtrlW0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.IK_FK R_IKFKFOOT_Grp_parentConstraint1.R_IK_Foot_CtrlW1;
    setAttr "R_IK_FK_Foot_Ctrl.IK_FK" 0;
    setAttr "L_IK_FK_Foot_Ctrl.IK_FK" 0;

             """)
    cmds.refresh(cv =1)
    ######################################################## parent hand
    mel.eval("""
    select -r Main_Controller ;
    select -add L_IK_Hand_Grp ;
    parentConstraint -mo -weight 1; 
 
    select -r L_Wrist_Ctrl ;
    select -add L_Hand_CtrL_Grp ;
    parentConstraint -mo -weight 1; 

    select -r L_IK_Hand_Ctrl ;
    select -add L_Hand_CtrL_Grp ;
    parentConstraint -mo -weight 1;                                             

    select -r Main_Controller ;
    select -add R_IK_Hand_Grp ;
    parentConstraint -mo -weight 1; 
        
    select -r R_Wrist_Ctrl ;
    select -add R_Hand_Ctrl_Grp ;
    parentConstraint -mo -weight 1; 

    select -r R_IK_Hand_Ctrl ;
    select -add R_Hand_Ctrl_Grp ;
    parentConstraint -mo -weight 1; 

    select -r IK_Chest_Ctrl ;
    select -add R_Scapula_Ctrl_Grp ;
    parentConstraint -mo -weight 1;          
             
    select -r IK_Chest_Ctrl ;
    select -add L_Scapula_Ctrl_Grp ;
    parentConstraint -mo -weight 1;
             
    //--------------------------------------------------------Set drieven key
    setAttr "R_IKFK_Hand_Ctrl.FK_IK" 0;
    setAttr "R_Hand_Ctrl_Grp_parentConstraint1.R_Wrist_CtrlW0" 1;
    setAttr "R_Hand_Ctrl_Grp_parentConstraint1.R_IK_Hand_CtrlW1" 0;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_Hand_Ctrl_Grp_parentConstraint1.R_Wrist_CtrlW0;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_Hand_Ctrl_Grp_parentConstraint1.R_IK_Hand_CtrlW1;
    setAttr "R_IKFK_Hand_Ctrl.FK_IK" 10;
    setAttr "R_Hand_Ctrl_Grp_parentConstraint1.R_Wrist_CtrlW0" 0;
    setAttr "R_Hand_Ctrl_Grp_parentConstraint1.R_IK_Hand_CtrlW1" 1;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_Hand_Ctrl_Grp_parentConstraint1.R_Wrist_CtrlW0;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_Hand_Ctrl_Grp_parentConstraint1.R_IK_Hand_CtrlW1;

    setAttr "L_IKFK_Hand_Ctrl.FK_IK" 0;
    setAttr "L_Hand_CtrL_Grp_parentConstraint1.L_Wrist_CtrlW0" 1;
    setAttr "L_Hand_CtrL_Grp_parentConstraint1.L_IK_Hand_CtrlW1" 0;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_Hand_CtrL_Grp_parentConstraint1.L_Wrist_CtrlW0;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_Hand_CtrL_Grp_parentConstraint1.L_IK_Hand_CtrlW1;
    setAttr "L_IKFK_Hand_Ctrl.FK_IK" 10;
    setAttr "L_Hand_CtrL_Grp_parentConstraint1.L_Wrist_CtrlW0" 0;
    setAttr "L_Hand_CtrL_Grp_parentConstraint1.L_IK_Hand_CtrlW1" 1;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_Hand_CtrL_Grp_parentConstraint1.L_Wrist_CtrlW0;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_Hand_CtrL_Grp_parentConstraint1.L_IK_Hand_CtrlW1;
             
    setAttr "L_IKFK_Hand_Ctrl.FK_IK" 0;
    setAttr "L_IK_Hand_Grp.visibility" 0;
    setAttr "L_Shoulder_Grp.visibility" 1;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_IK_Hand_Grp.visibility;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_Shoulder_Grp.visibility;
    setAttr "L_IKFK_Hand_Ctrl.FK_IK" 10;
    setAttr "L_IK_Hand_Grp.visibility" 1;
    setAttr "L_Shoulder_Grp.visibility" 0;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_IK_Hand_Grp.visibility;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_Shoulder_Grp.visibility;

    setAttr "R_IKFK_Hand_Ctrl.FK_IK" 0;
    setAttr "R_IK_Hand_Grp.visibility" 0;
    setAttr "R_Shoulder_Grp.visibility" 1;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_IK_Hand_Grp.visibility;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_Shoulder_Grp.visibility;
    setAttr "R_IKFK_Hand_Ctrl.FK_IK" 10;
    setAttr "R_IK_Hand_Grp.visibility" 1;
    setAttr "R_Shoulder_Grp.visibility" 0;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_IK_Hand_Grp.visibility;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_Shoulder_Grp.visibility;
    
    //------------------------------------------------------ Set parent hand IK FK
    setAttr "R_IKFK_Hand_Ctrl.FK_IK" 0;
    setAttr "R_Wrist_parentConstraint1.IK_R_WristW0" 0;
    setAttr "R_Wrist_parentConstraint1.FK_R_WristW1" 1;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_Wrist_parentConstraint1.IK_R_WristW0;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_Wrist_parentConstraint1.FK_R_WristW1;
    setAttr "R_IKFK_Hand_Ctrl.FK_IK" 10;
    setAttr "R_Wrist_parentConstraint1.IK_R_WristW0" 1;
    setAttr "R_Wrist_parentConstraint1.FK_R_WristW1" 0;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_Wrist_parentConstraint1.IK_R_WristW0;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_Wrist_parentConstraint1.FK_R_WristW1;
            
    setAttr "R_IKFK_Hand_Ctrl.FK_IK" 0;
    setAttr "R_Elbow_parentConstraint1.IK_R_ElbowW0" 0;
    setAttr "R_Elbow_parentConstraint1.FK_R_ElbowW1" 1;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_Elbow_parentConstraint1.IK_R_ElbowW0;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_Elbow_parentConstraint1.FK_R_ElbowW1;
    setAttr "R_IKFK_Hand_Ctrl.FK_IK" 10;
    setAttr "R_Elbow_parentConstraint1.IK_R_ElbowW0" 1;
    setAttr "R_Elbow_parentConstraint1.FK_R_ElbowW1" 0;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_Elbow_parentConstraint1.IK_R_ElbowW0;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_Elbow_parentConstraint1.FK_R_ElbowW1;

    setAttr "R_IKFK_Hand_Ctrl.FK_IK" 0;
    setAttr "R_Shoulder_parentConstraint1.IK_R_ShoulderW0" 0;
    setAttr "R_Shoulder_parentConstraint1.FK_R_ShoulderW1" 1;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_Shoulder_parentConstraint1.IK_R_ShoulderW0;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_Shoulder_parentConstraint1.FK_R_ShoulderW1;
    setAttr "R_IKFK_Hand_Ctrl.FK_IK" 10;
    setAttr "R_Shoulder_parentConstraint1.IK_R_ShoulderW0" 1;
    setAttr "R_Shoulder_parentConstraint1.FK_R_ShoulderW1" 0;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_Shoulder_parentConstraint1.IK_R_ShoulderW0;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.FK_IK R_Shoulder_parentConstraint1.FK_R_ShoulderW1;
                  
    setAttr "L_IKFK_Hand_Ctrl.FK_IK" 0;
    setAttr "L_Wrist_parentConstraint1.IK_L_WristW0" 0;
    setAttr "L_Wrist_parentConstraint1.FK_L_WristW1" 1;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_Wrist_parentConstraint1.IK_L_WristW0;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_Wrist_parentConstraint1.FK_L_WristW1;
    setAttr "L_IKFK_Hand_Ctrl.FK_IK" 10;
    setAttr "L_Wrist_parentConstraint1.IK_L_WristW0" 1;
    setAttr "L_Wrist_parentConstraint1.FK_L_WristW1" 0;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_Wrist_parentConstraint1.IK_L_WristW0;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_Wrist_parentConstraint1.FK_L_WristW1;
            
    setAttr "L_IKFK_Hand_Ctrl.FK_IK" 0;
    setAttr "L_Elbow_parentConstraint1.IK_L_ElbowW0" 0;
    setAttr "L_Elbow_parentConstraint1.FK_L_ElbowW1" 1;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_Elbow_parentConstraint1.IK_L_ElbowW0;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_Elbow_parentConstraint1.FK_L_ElbowW1;
    setAttr "L_IKFK_Hand_Ctrl.FK_IK" 10;
    setAttr "L_Elbow_parentConstraint1.IK_L_ElbowW0" 1;
    setAttr "L_Elbow_parentConstraint1.FK_L_ElbowW1" 0;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_Elbow_parentConstraint1.IK_L_ElbowW0;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_Elbow_parentConstraint1.FK_L_ElbowW1;

    setAttr "L_IKFK_Hand_Ctrl.FK_IK" 0;
    setAttr "L_Shoulder_parentConstraint1.IK_L_ShoulderW0" 0;
    setAttr "L_Shoulder_parentConstraint1.FK_L_ShoulderW1" 1;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_Shoulder_parentConstraint1.IK_L_ShoulderW0;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_Shoulder_parentConstraint1.FK_L_ShoulderW1;
    setAttr "L_IKFK_Hand_Ctrl.FK_IK" 10;
    setAttr "L_Shoulder_parentConstraint1.IK_L_ShoulderW0" 1;
    setAttr "L_Shoulder_parentConstraint1.FK_L_ShoulderW1" 0;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_Shoulder_parentConstraint1.IK_L_ShoulderW0;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.FK_IK L_Shoulder_parentConstraint1.FK_L_ShoulderW1;
    
    //---------------------------------------------------------------- parent scapula
    select -r R_Scapula_Ctrl ;
    select -tgl R_Scapula ;
    parentConstraint -mo -weight 1; 
    select -r L_Scapula_Ctrl ;
    select -tgl L_Scapula ;
    parentConstraint -mo -weight 1;

    //---------------------------------------------------------------- driven key root
    select -r ikHandle1 ;
    rename "ikHandle1" "ikHandle_Root";
    select -r ikHandle_Root ;
    setAttr "ikHandle_Root.dTwistControlEnable" 1;
    setAttr "ikHandle_Root.dWorldUpType" 4;
    setAttr "ikHandle_Root.dWorldUpVectorX" 0;
    setAttr "ikHandle_Root.dWorldUpVectorY" 1;
    setAttr "ikHandle_Root.dWorldUpVectorZ" 0;
    setAttr "ikHandle_Root.dWorldUpVectorEndX" 0;
    setAttr "ikHandle_Root.dWorldUpVectorEndY" 1;
    setAttr "ikHandle_Root.dWorldUpVectorEndZ" 0;
    select -r ikHandle_Root ;
    connectAttr -f IK_Root_Ctrl.worldMatrix[0] ikHandle_Root.dWorldUpMatrix;
    connectAttr -f IK_Chest_Ctrl.worldMatrix[0] ikHandle_Root.dWorldUpMatrixEnd; 

    //---------------------------------------------------------------- driven elbow
    setAttr "R_IKFK_Hand_Ctrl.Elbow_Follow" 1;
    setAttr "R_ElbowFL_Ctrl_Grp_parentConstraint1.R_IK_Hand_CtrlW0" 0;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Elbow_Follow R_ElbowFL_Ctrl_Grp_parentConstraint1.R_IK_Hand_CtrlW0;
    setAttr "R_IKFK_Hand_Ctrl.Elbow_Follow" 2;
    setAttr "R_ElbowFL_Ctrl_Grp_parentConstraint1.R_IK_Hand_CtrlW0" 1;
    setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Elbow_Follow R_ElbowFL_Ctrl_Grp_parentConstraint1.R_IK_Hand_CtrlW0;
             
    setAttr "L_IKFK_Hand_Ctrl.Elbow_Follow" 1;
    setAttr "L_ElbowFL_Ctrl_Grp_parentConstraint1.L_IK_Hand_CtrlW0" 0;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Elbow_Follow L_ElbowFL_Ctrl_Grp_parentConstraint1.L_IK_Hand_CtrlW0;
    setAttr "L_IKFK_Hand_Ctrl.Elbow_Follow" 2;
    setAttr "L_ElbowFL_Ctrl_Grp_parentConstraint1.L_IK_Hand_CtrlW0" 1;
    setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Elbow_Follow L_ElbowFL_Ctrl_Grp_parentConstraint1.L_IK_Hand_CtrlW0;
    setAttr "L_IKFK_Hand_Ctrl.Elbow_Follow" 1;
    setAttr "R_IKFK_Hand_Ctrl.Elbow_Follow" 1;


    //---------------------------------------------------------------- driven key knee
    setAttr "L_IK_FK_Foot_Ctrl.Knee_Follow" 2;
    setAttr "L_Loc_Ctrl_Grp_parentConstraint1.L_IK_Foot_CtrlW0" 1;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.Knee_Follow L_Loc_Ctrl_Grp_parentConstraint1.L_IK_Foot_CtrlW0;
    setAttr "L_IK_FK_Foot_Ctrl.Knee_Follow" 1;
    setAttr "L_Loc_Ctrl_Grp_parentConstraint1.L_IK_Foot_CtrlW0" 0;
    setDrivenKeyframe -currentDriver L_IK_FK_Foot_Ctrl.Knee_Follow L_Loc_Ctrl_Grp_parentConstraint1.L_IK_Foot_CtrlW0;
             
    setAttr "R_IK_FK_Foot_Ctrl.Knee_Follow" 2;
    setAttr "R_Loc_Ctrl_Grp_parentConstraint1.R_IK_Foot_CtrlW0" 1;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.Knee_Follow R_Loc_Ctrl_Grp_parentConstraint1.R_IK_Foot_CtrlW0;
    setAttr "R_IK_FK_Foot_Ctrl.Knee_Follow" 1;
    setAttr "R_Loc_Ctrl_Grp_parentConstraint1.R_IK_Foot_CtrlW0" 0;
    setDrivenKeyframe -currentDriver R_IK_FK_Foot_Ctrl.Knee_Follow R_Loc_Ctrl_Grp_parentConstraint1.R_IK_Foot_CtrlW0;
             
    //---------------------------------------------------------------- driven key scapula 
    setAttr "Body_Ctrl.FK_IK" 1;
    setAttr "R_Scapula_Ctrl_Grp_parentConstraint1.Chest_CtrlW0" 1;
    setAttr "R_Scapula_Ctrl_Grp_parentConstraint1.IK_Chest_CtrlW1" 0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK R_Scapula_Ctrl_Grp_parentConstraint1.Chest_CtrlW0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK R_Scapula_Ctrl_Grp_parentConstraint1.IK_Chest_CtrlW1;
    setAttr "L_Scapula_Ctrl_Grp_parentConstraint1.Chest_CtrlW0" 1;
    setAttr "L_Scapula_Ctrl_Grp_parentConstraint1.IK_Chest_CtrlW1" 0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK L_Scapula_Ctrl_Grp_parentConstraint1.Chest_CtrlW0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK L_Scapula_Ctrl_Grp_parentConstraint1.IK_Chest_CtrlW1;
    setAttr "Body_Ctrl.FK_IK" 10;
    setAttr "R_Scapula_Ctrl_Grp_parentConstraint1.Chest_CtrlW0" 0;
    setAttr "R_Scapula_Ctrl_Grp_parentConstraint1.IK_Chest_CtrlW1" 1;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK R_Scapula_Ctrl_Grp_parentConstraint1.Chest_CtrlW0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK R_Scapula_Ctrl_Grp_parentConstraint1.IK_Chest_CtrlW1;
    setAttr "L_Scapula_Ctrl_Grp_parentConstraint1.Chest_CtrlW0" 0;
    setAttr "L_Scapula_Ctrl_Grp_parentConstraint1.IK_Chest_CtrlW1" 1;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK L_Scapula_Ctrl_Grp_parentConstraint1.Chest_CtrlW0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK L_Scapula_Ctrl_Grp_parentConstraint1.IK_Chest_CtrlW1;
    setAttr "Body_Ctrl.FK_IK" 1;
             
    //---------------------------------------------------------------- IK FK Root trl visibility
    setAttr "Body_Ctrl.FK_IK" 1;
    setAttr "Root_Ctrl_Grp.visibility" 1;
    setAttr "IK_Root_Grp.visibility" 0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK IK_Root_Grp.visibility; 
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK Root_Ctrl_Grp.visibility;
    setAttr "Body_Ctrl.FK_IK" 10;
    setAttr "IK_Root_Grp.visibility" 1;
    setAttr "Root_Ctrl_Grp.visibility" 0;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK IK_Root_Grp.visibility;
    setDrivenKeyframe -currentDriver Body_Ctrl.FK_IK Root_Ctrl_Grp.visibility;
    setAttr "Body_Ctrl.FK_IK" 1;
             
    //---------------------------------------------------------------- set driven key heel
    setAttr "L_IK_Foot_Ctrl.Heel" 1;
    setAttr "L_Heel_Ctrl_Grp.rotateY" 0;
    setDrivenKeyframe -currentDriver L_IK_Foot_Ctrl.Heel L_Heel_Ctrl_Grp.rotateY;
    setAttr "L_IK_Foot_Ctrl.Heel" 10;
    setAttr "L_Heel_Ctrl_Grp.rotateY" -30;
    setDrivenKeyframe -currentDriver L_IK_Foot_Ctrl.Heel L_Heel_Ctrl_Grp.rotateY;
    setAttr "L_IK_Foot_Ctrl.Heel" 1;
    selectKey -add -k -f 1 -f 10 L_Heel_Ctrl_Grp_rotateY ;
    keyTangent -itt linear -ott linear;
             
    setAttr "L_IK_Foot_Ctrl.Toe" 1;
    setAttr "L_Toe_Ctrl_Grp.rotateY" 0;
    setDrivenKeyframe -currentDriver L_IK_Foot_Ctrl.Toe L_Toe_Ctrl_Grp.rotateY;
    setAttr "L_IK_Foot_Ctrl.Toe" 10;
    setAttr "L_Toe_Ctrl_Grp.rotateY" 30;
    setDrivenKeyframe -currentDriver L_IK_Foot_Ctrl.Toe L_Toe_Ctrl_Grp.rotateY;

    setAttr "R_IK_Foot_Ctrl.Heel" 1;
    setAttr "R_Heel_Ctrl_Grp.rotateY" 0;
    setDrivenKeyframe -currentDriver R_IK_Foot_Ctrl.Heel R_Heel_Ctrl_Grp.rotateY;
    setAttr "R_IK_Foot_Ctrl.Heel" 10;
    setAttr "R_Heel_Ctrl_Grp.rotateY" -30;
    setDrivenKeyframe -currentDriver R_IK_Foot_Ctrl.Heel R_Heel_Ctrl_Grp.rotateY;
    setAttr "R_IK_Foot_Ctrl.Heel" 1;
    selectKey -add -k -f 1 -f 10 R_Heel_Ctrl_Grp_rotateY ;
    keyTangent -itt linear -ott linear;
             
    setAttr "R_IK_Foot_Ctrl.Toe" 1;
    setAttr "R_Toe_Ctrl_Grp.rotateY" 0;
    setDrivenKeyframe -currentDriver R_IK_Foot_Ctrl.Toe R_Toe_Ctrl_Grp.rotateY;
    setAttr "R_IK_Foot_Ctrl.Toe" 10;
    setAttr "R_Toe_Ctrl_Grp.rotateY" 30;
    setDrivenKeyframe -currentDriver R_IK_Foot_Ctrl.Toe R_Toe_Ctrl_Grp.rotateY;             
    setAttr "R_IK_Foot_Ctrl.Toe" 1;
    setAttr "L_IK_Foot_Ctrl.Toe" 1;
    
    select -r R_Toe_Ctrl_Grp ;
    select -add L_Toe_Ctrl_Grp ;
    selectKey -clear ;
    selectKey -add -k -f 1 -f 10 R_Toe_Ctrl_Grp_rotateY ;
    selectKey -add -k -f 1 -f 10 L_Toe_Ctrl_Grp_rotateY ;
    keyTangent -itt linear -ott linear;

         

    //---------------------------------------------------------------- Scale_Rig
    setAttr "Main_Controller.Scale_Rig" 1;
    setAttr "Scale.scaleZ" 1;
    setAttr "Scale.scaleX" 1;
    setAttr "Scale.scaleY" 1;
    setDrivenKeyframe -currentDriver Main_Controller.Scale_Rig Scale.scaleX;
    setDrivenKeyframe -currentDriver Main_Controller.Scale_Rig Scale.scaleY;
    setDrivenKeyframe -currentDriver Main_Controller.Scale_Rig Scale.scaleZ;
    setAttr "Main_Controller.Scale_Rig" -100;
    setAttr "Scale.scaleZ" -100;
    setAttr "Scale.scaleX" -100;
    setAttr "Scale.scaleY" -100;
    setDrivenKeyframe -currentDriver Main_Controller.Scale_Rig Scale.scaleX;
    setDrivenKeyframe -currentDriver Main_Controller.Scale_Rig Scale.scaleY;
    setDrivenKeyframe -currentDriver Main_Controller.Scale_Rig Scale.scaleZ;
    setAttr "Main_Controller.Scale_Rig" 100;
    setAttr "Scale.scaleZ" 100;
    setAttr "Scale.scaleX" 100;
    setAttr "Scale.scaleY" 100;
    setDrivenKeyframe -currentDriver Main_Controller.Scale_Rig Scale.scaleX;
    setDrivenKeyframe -currentDriver Main_Controller.Scale_Rig Scale.scaleY;
    setDrivenKeyframe -currentDriver Main_Controller.Scale_Rig Scale.scaleZ;
    selectKey -add -k Scale_scaleX Scale_scaleY Scale_scaleZ ;
    keyTangent -itt linear -ott linear;
    setAttr "Main_Controller.Scale_Rig" 1;

    //---------------------------------------------------------------- hide IK FK                   
    select -r IK_FK_System ;
    toggleVisibilityAndKeepSelection `optionVar -query toggleVisibilityAndKeepSelectionBehaviour`;
    select -r IK_L_Hip FK_L_Hip IK_R_Hip FK_R_Hip ;
    toggleVisibilityAndKeepSelection `optionVar -query toggleVisibilityAndKeepSelectionBehaviour`;
    select -r IK_L_Shoulder FK_L_Shoulder ;
    toggleVisibilityAndKeepSelection `optionVar -query toggleVisibilityAndKeepSelectionBehaviour`;         
    select -r IK_R_Shoulder FK_R_Shoulder ;
    select -add IK_Root FK_Root Chest_Ctrl_Jnt Root_Ctrl_Jnt L_ikHandle_Hand R_ikHandle_Hand ;
    toggleVisibilityAndKeepSelection `optionVar -query toggleVisibilityAndKeepSelectionBehaviour`;

    setAttr "L_IKFK_Hand_Ctrl.FK_IK" 0;
    setAttr "R_IKFK_Hand_Ctrl.FK_IK" 0;
             """)
    
    #cmds.ikHandle("ikHandle_Root", edit=True, forwardAxis=4, UpAxis=9)
    cmds.refresh(cv =1)
    ##################################################### move parent constraint to grp
    mel.eval("""
    select -r R_Wrist_parentConstraint1 ;
    select -add R_Elbow_parentConstraint1 ;
    select -add R_Shoulder_parentConstraint1 ;
    select -add FK_R_Wrist_parentConstraint1 ;
    select -add FK_R_Elbow_parentConstraint1 ;
    select -add FK_R_Shoulder_parentConstraint1 ;
    select -add L_Wrist_parentConstraint1 ;
    select -add L_Elbow_parentConstraint1 ;
    select -add L_Shoulder_parentConstraint1 ;
    select -add FK_L_Wrist_parentConstraint1 ;
    select -add FK_L_Elbow_parentConstraint1 ;
    select -add FK_L_Shoulder_parentConstraint1 ;
    select -add R_ToesEnd_parentConstraint1 ;
    select -add R_Toes_parentConstraint1 ;
    select -add R_Ankle_parentConstraint1 ;
    select -add R_Knee_parentConstraint1 ;
    select -add R_Hip_parentConstraint1 ;
    select -add L_ToesEnd_parentConstraint1 ;
    select -add L_Toes_parentConstraint1 ;
    select -add L_Ankle_parentConstraint1 ;
    select -add L_Knee_parentConstraint1 ;
    select -add L_Hip_parentConstraint1 ;
    select -add FK_L_Toes_parentConstraint1 ;
    select -add FK_L_Ankle_parentConstraint1 ;
    select -add FK_L_Knee_parentConstraint1 ;
    select -add FK_L_Hip_parentConstraint1 ;
    select -add FK_R_Toes_parentConstraint1 ;
    select -add FK_R_Ankle_parentConstraint1 ;
    select -add FK_R_Knee_parentConstraint1 ;
    select -add FK_R_Hip_parentConstraint1 ;
    select -add L_MiddleFinger3_parentConstraint1 ;
    select -add L_MiddleFinger2_parentConstraint1 ;
    select -add L_MiddleFinger1_parentConstraint1 ;
    select -add L_ThumbFinger3_parentConstraint1 ;
    select -add L_ThumbFinger2_parentConstraint1 ;
    select -add L_ThumbFinger1_parentConstraint1 ;
    select -add L_IndexFinger3_parentConstraint1 ;
    select -add L_IndexFinger2_parentConstraint1 ;
    select -add L_IndexFinger1_parentConstraint1 ;
    select -add L_PinkyFinger3_parentConstraint1 ;
    select -add L_PinkyFinger2_parentConstraint1 ;
    select -add L_PinkyFinger1_parentConstraint1 ;
    select -add L_RingFinger3_parentConstraint1 ;
    select -add L_RingFinger2_parentConstraint1 ;
    select -add L_RingFinger1_parentConstraint1 ;
    select -add L_Hand_parentConstraint1 ;
    select -add R_MiddleFinger3_parentConstraint1 ;
    select -add R_MiddleFinger2_parentConstraint1 ;
    select -add R_MiddleFinger1_parentConstraint1 ;
    select -add R_ThumbFinger3_parentConstraint1 ;
    select -add R_ThumbFinger2_parentConstraint1 ;
    select -add R_ThumbFinger1_parentConstraint1 ;
    select -add R_IndexFinger3_parentConstraint1 ;
    select -add R_IndexFinger2_parentConstraint1 ;
    select -add R_IndexFinger1_parentConstraint1 ;
    select -add R_PinkyFinger3_parentConstraint1 ;
    select -add R_PinkyFinger2_parentConstraint1 ;
    select -add R_PinkyFinger1_parentConstraint1 L_ikHandle_Ankle_poleVectorConstraint1 L_Heel_Grp_parentConstraint1 R_ikHandle_Ankle_poleVectorConstraint1 R_Heel_Grp_parentConstraint1;
    select -add R_RingFinger3_parentConstraint1 R_ElbowFL_Ctrl_Grp_parentConstraint1 L_ElbowFL_Ctrl_Grp_parentConstraint1;
    select -add R_RingFinger2_parentConstraint1 R_Loc_Ctrl_Grp_parentConstraint1 L_Loc_Ctrl_Grp_parentConstraint1;
    select -add R_RingFinger1_parentConstraint1 FK_Chest_parentConstraint1 FK_Spine_parentConstraint1 FK_Root_parentConstraint1;
    select -add R_Hand_parentConstraint1 L_ikHandle_Hand_poleVectorConstraint1 R_ikHandle_Hand_poleVectorConstraint1;
    select -add R_Shoulder_Grp_parentConstraint1;
    select -add R_Hip_Ctrl_Grp_parentConstraint1 R_IK_Foot_Grp_parentConstraint1 L_IK_Foot_Grp_parentConstraint1 ;
    select -add Root_parentConstraint1 Body_Ctrl_Grp_parentConstraint1 Root_Ctrl_Grp_parentConstraint1 Neck_Ctrl_Grp_parentConstraint1 L_Hip_Ctrl_Grp_parentConstraint1 L_IKFKFOOT_Grp_parentConstraint1 R_IKFKFOOT_Grp_parentConstraint1 ;
    select -add Spine1_parentConstraint1 R_IK_Hand_Grp_parentConstraint1 L_IK_Hand_Grp_parentConstraint1 R_Hand_Ctrl_Grp_parentConstraint1 L_Hand_CtrL_Grp_parentConstraint1 R_Scapula_Ctrl_Grp_parentConstraint1 L_Shoulder_Grp_parentConstraint1 L_Scapula_Ctrl_Grp_parentConstraint1 ;
    select -add Chest_parentConstraint1 L_Scapula_parentConstraint1 R_Scapula_parentConstraint1 Neck_parentConstraint1;
    select -add Constraint_Grp ;
    parent;
             
    select -r ikHandle_Root ;
    select -add IK_Curve_Root ;
    doGroup 0 1 1;
    select -r group1 ;
    rename "group1" "IK_Root";
    select -r |IK_Root ;
    select -add IK_FK_System ;
    parent;      
                    
    setAttr "Constraint_Grp.visibility" 0;
    setAttr -lock true -keyable false -channelBox false "Constraint_Grp.v";
    setAttr -lock true -keyable false -channelBox false "IK_FK_System.v";  
    setAttr "R_Heel_Grp.visibility" 0;
    setAttr "L_Heel_Grp.visibility" 0;           
             """)
    mel.eval('select -cl ;')    



################################################################
################################################################ face rig 

    cmds.refresh(cv =1)
################################## Eye 
def rightEye(*arg):
    selected_object = cmds.ls(sl=True)
    for obj in selected_object :
        Eye_Joint_R = cmds.joint(n="EyeR")
        cmds.matchTransform(Eye_Joint_R, obj , rot=True, pos=True)
        cmds.parent(Eye_Joint_R, joint_Neck)
    cmds.textField("RE_Text", edit=True, text="Right Eye Done !")
    cmds.checkBox("RE_CheckBox", enable=True, edit=True, value=True)
def dltRE(*arg):
    cmds.delete(joint_ER)
    cmds.textField("RE_Text", edit=True, text=" Delete !")

def leftEye(*arg):
    selected_object = cmds.ls(sl=True)
    for obj in selected_object :
        Eye_Joint_L = cmds.joint(n="EyeL")
        cmds.matchTransform(Eye_Joint_L, obj , rot=True, pos=True)
        cmds.parent(Eye_Joint_L, joint_Neck)
    cmds.textField("LE_Text", edit=True, text="Left Eye Done !")
    cmds.checkBox("LE_CheckBox", enable=True, edit=True, value=True)
def dltLE(*arg):
    cmds.delete(joint_EL)
    cmds.textField("LE_Text", edit=True, text=" Delete !")


################################### mouths
def MidUpLip(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="Mid_Up_Lip",position=vertex_pos)
    cmds.parent(joint, world=True)
    cmds.textField("MUL_Text", edit=True, text="Mid Up Lip Done !")
    cmds.checkBox("MUL_CheckBox", enable=True, edit=True, value=True)
def dltMUL(*arg):
    cmds.delete(Jnt_MUL)
    cmds.textField("MUL_Text", edit=True, text=" Delete !")


def MidBW1(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="R_Between_1",position=vertex_pos)
    cmds.parent(joint, Jnt_MUL)
    cmds.textField("RB1_Text", edit=True, text="R Between 1 Done !")
    cmds.checkBox("RB1_CheckBox", enable=True, edit=True, value=True)
def dltBW1(*arg):
    cmds.delete(Jnt_BW1)
    cmds.textField("RB1_Text", edit=True, text=" Delete !")


def MidBW2(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="R_Between_2",position=vertex_pos)
    cmds.parent(joint, Jnt_BW1)
    cmds.textField("RB2_Text", edit=True, text="R Between 2 Done !")
    cmds.checkBox("RB2_CheckBox", enable=True, edit=True, value=True)
def dltBW2(*arg):
    cmds.delete(Jnt_BW2)
    cmds.textField("RB2_Text", edit=True, text=" Delete !")


def R_Corner_Lip(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="R_Corner_Lip",position=vertex_pos)
    cmds.parent(joint, Jnt_BW2)
    cmds.textField("RCL_Text", edit=True, text="Right Corner Lip Done !")
    cmds.checkBox("RCL_CheckBox", enable=True, edit=True, value=True)
def dltRCL(*arg):
    cmds.delete(Jnt_RCL)
    cmds.textField("RCL_Text", edit=True, text=" Delete !")


def MidBW3(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="R_Between_3",position=vertex_pos)
    cmds.parent(joint, Jnt_RCL)
    cmds.textField("RB3_Text", edit=True, text="R Between 3 Done !")
    cmds.checkBox("RB3_CheckBox", enable=True, edit=True, value=True)
def dltBW3(*arg):
    cmds.delete(Jnt_BW3)
    cmds.textField("RB3_Text", edit=True, text=" Delete !")


def MidBW4(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="R_Between_4",position=vertex_pos)
    cmds.parent(joint, Jnt_BW3)
    cmds.textField("RB4_Text", edit=True, text="R Between 4 Done !")
    cmds.checkBox("RB4_CheckBox", enable=True, edit=True, value=True)
def dltBW4(*arg):
    cmds.delete(Jnt_BW4)
    cmds.textField("RB4_Text", edit=True, text=" Delete !")


def MidDownLip(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="Mid_Down_Lip",position=vertex_pos)
    cmds.parent(joint, Jnt_MUL)
    cmds.textField("MDL_Text", edit=True, text="Mid Down Lip Done !")
    cmds.checkBox("MDL_CheckBox", enable=True, edit=True, value=True)
def dltMDL(*arg):
    cmds.delete(Jnt_MDL)
    cmds.textField("MDL_Text", edit=True, text=" Delete !")


def InnerBrow(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="R_InnerBrow",position=vertex_pos)
    cmds.parent(joint, joint_Neck)
    cmds.textField("RIB_Text", edit=True, text="Mid Down Lip Done !")
    cmds.checkBox("RIB_CheckBox", enable=True, edit=True, value=True)
def dltRIB(*arg):
    cmds.delete(Jnt_RIB)
    cmds.textField("RIB_Text", edit=True, text=" Delete !")


def OuterBrow(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="R_OuterBrow",position=vertex_pos)
    cmds.parent(joint, joint_Neck)
    cmds.textField("LIB_Text", edit=True, text="Mid Down Lip Done !")
    cmds.checkBox("LIB_CheckBox", enable=True, edit=True, value=True)    
def dltROB(*arg):
    cmds.delete(Jnt_ROB)
    cmds.textField("LIB_Text", edit=True, text=" Delete !")


def jawJnt(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="Jaw_Jnt",position=vertex_pos)
    cmds.parent(joint, joint_Neck)
    cmds.textField("Jaw_Text", edit=True, text="Jaw Done !")
    cmds.checkBox("Jaw_CheckBox", enable=True, edit=True, value=True)
    mel.eval("""
    polyPlane -w 1 -h 1 -sx 1 -sy 1 -ax 0 1 0 -cuv 2 -ch 1;
    setAttr "pPlane1.scaleZ" 3;
    setAttr "pPlane1.scaleX" 3;
    select -r pPlane1 ;
    select -tgl Jaw_Jnt ;
    parent;
    setAttr "pPlane1.rotateZ" 0;
    setAttr "pPlane1.translateX" 0;
    setAttr "pPlane1.translateY" 0;
    setAttr "pPlane1.translateZ" 0;
    setAttr "pPlane1.rotateX" 0;
    setAttr "pPlane1.rotateY" 0;
    select -r Jaw_Jnt ;                                       
    """) 
def dltJaw(*arg):
    cmds.delete(Jnt_Jaw)
    cmds.textField("Jaw_Text", edit=True, text=" Delete !")

def MirrorMouth(*arg):
    mel.eval("""
    select -r R_OuterBrow ;
    select -tgl R_InnerBrow ;
    parent;

    select -r R_InnerBrow ; 
    mirrorJoint -mirrorYZ -mirrorBehavior -searchReplace "R" "L";
                     
    select -r R_Between_1 ;
    mirrorJoint -mirrorYZ -mirrorBehavior -searchReplace "R" "L";
             
    select -r Mid_Up_Lip ;
    select -tgl Neck ;
    parent;
             
             
             """)
    
    cmds.textField("MR_Text", edit=True, text="Mirror Done !")
    cmds.checkBox("MR_CheckBox", edit=True, value=True) 
def Jnt_TOG1(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="Tongue1_jnt",position=vertex_pos)
    cmds.parent(joint, joint_Neck)

def Jnt_TOG2(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="Tongue2_jnt",position=vertex_pos)
    cmds.parent(joint, "Tongue1_jnt")

def Jnt_TOG3(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="Tongue3_jnt",position=vertex_pos)
    cmds.parent(joint, "Tongue2_jnt")

def Jnt_TOG4(*arg):
    selected_verts = cmds.ls(selection=True, flatten=True)
    vertex_pos = cmds.pointPosition(selected_verts[0])
    joint = cmds.joint(n="Tongue4_jnt",position=vertex_pos)
    cmds.parent(joint, "Tongue3_jnt")
    cmds.checkBox("Tongue_checkbox", enable=True, edit=True, value=True)    
def dltTG1(*arg):
    cmds.delete(Jnt_TG1)
 



def buildFace(*arg):
    groupMain = cmds.group(name="Main_Face_Grp_dont_FreezeTransformations", empty=True)
    Main_Functions = cmds.curve(name="Main_Face",d=1, p=[
        (-0.43, 0, -0.86),
        (0.43, 0, -0.86),
        (0.43, 0, 0.71),
        (-0.43, 0, 0.71),
        (-0.43, 0, -0.86)])
    
    # mel.eval("""
    # setAttr "Main_Face.overrideEnabled" 1;
    # changeObjColor Main_Face.overrideColor AttributeEditor|MainAttributeEditorLayout|formLayout92|AEmenuBarLayout|AErootLayout|AEStackLayout|AErootLayoutPane|AEbaseFormLayout|AEcontrolFormLayout|AttrEdtransformFormLayout|scrollLayout3|columnLayout33|frameLayout50|columnLayout37|frameLayout56|columnLayout48|columnLayout51|objIndexColorSlider;
    # updateLayerColor Main_Face.overrideColor AttributeEditor|MainAttributeEditorLayout|formLayout92|AEmenuBarLayout|AErootLayout|AEStackLayout|AErootLayoutPane|AEbaseFormLayout|AEcontrolFormLayout|AttrEdtransformFormLayout|scrollLayout3|columnLayout33|frameLayout50|columnLayout37|frameLayout56|columnLayout48|columnLayout51|objIndexColorSlider;
    # """)

    mel.eval('setAttr -lock true -keyable false -channelBox false "Main_Face.v";')
    Functions = cmds.curve(name="LineFunction",d=1, p=[        
        (-0.4, 0, 0.45),
        (0.4, 0, 0.45),
        (0.4, 0, 0.68),
        (-0.4, 0, 0.68),
        (-0.4, 0, 0.45)])

    mel.eval("""
    curve -d 2 -p -0.08 0 0.65 -p -0.08 0 0.56 -p -0.08 0 0.48 -p -0.06 0 0.48 -p -0.05 0 0.48 -p -0.03 0 0.54 -p -0.01 0 0.6 -p 0 0 0.62 -p 0 0 0.62 -p 0.01 0 0.61 -p 0.01 0 0.6 -p 0.03 0 0.54 -p 0.05 0 0.48 -p 0.07 0 0.48 -p 0.08 0 0.48 -p 0.08 0 0.56 -p 0.08 0 0.65 -p 0.07 0 0.65 -p 0.06 0 0.65 -p 0.06 0 0.58 -p 0.06 0 0.51 -p 0.04 0 0.58 -p 0.01 0 0.65 -p 0 0 0.65 -p -0.01 0 0.65 -p -0.03 0 0.58 -p -0.06 0 0.5 -p -0.06 0 0.58 -p -0.06 0 0.65 -p -0.07 0 0.65 -p -0.08 0 0.65;
                          """)
    cmds.CenterPivot()    
    mel.eval("""    
    select -r LineFunction ;
    //setAttr "curveShape2.template" 1;
             """)
    cmds.parent(Functions, Main_Functions)
    cmds.listRelatives(Main_Functions, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Main_Functions), True)
    cmds.setAttr("{0}.overrideColor".format(Main_Functions), ColorCurve2)  
    cmds.parent(Main_Functions, groupMain)

    Ctrl_grp = cmds.group(name="Ctrl_Grp", empty=True)
    cmds.parent(Ctrl_grp, Main_Functions)
    Line_grp = cmds.group(name="Line_grp", empty=True)
    cmds.parent(Line_grp, Main_Functions)
    Line2 = cmds.curve(name="Line2",d=1, p=[(-0.14, 0, -0.14),
        (0.14, 0, -0.14),
        (0.14, 0, 0.14),
        (-0.14, 0, 0.14),
        (-0.14, 0, -0.14)])
    gr4 = cmds.group(n="BR", empty=True)
    Func4 = cmds.curve(name="Bow_Ctrl_R", d=1, p=[        
        (0, 0, -0.36),(0.12, 0, -0.36),
        (0.24, 0, -0.24),(0.36, 0, -0.12),(0.36, 0, 0),(0.36, 0, 0.12),(0.24, 0, 0.24),
        (0.12, 0, 0.36),(0, 0, 0.36),(-0.12, 0, 0.36),(-0.24, 0, 0.24),(-0.36, 0, 0.12),
        (-0.36, 0, 0),(-0.36, 0, -0.12),(-0.24, 0, -0.24),(-0.12, 0, -0.36),(0, 0, -0.36)])
    cmds.parent(Func4, gr4)
    cmds.parent(gr4, Line2) 
    mel.eval("""
    setAttr "BR.scaleZ" 0.140;
    setAttr "BR.scaleX" 0.140;
    setAttr "BR.scaleY" 0.140;
             """)   
             
    cmds.parent(Line2, Line_grp)     
    mel.eval("""
    setAttr "Line2.translateX" -0.216;
    setAttr "Line2.translateZ" -0.646;

    select -r Line2 ;
    //setAttr "curveShape4.template" 1;

             """)
    cmds.listRelatives(Line2, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Line2), True)
    cmds.setAttr("{0}.overrideColor".format(Line2), ColorCurve1)  

    Line3 = cmds.curve(name="Line3",d=1, p=[(-0.14, 0, -0.14),
        (0.14, 0, -0.14),
        (0.14, 0, 0.14),
        (-0.14, 0, 0.14),
        (-0.14, 0, -0.14)])
    gr3 = cmds.group(n="BL", empty=True)
    Func3 = cmds.curve(name="Bow_Ctrl_L", d=1, p=[        
        (0, 0, -0.36),(0.12, 0, -0.36),
        (0.24, 0, -0.24),(0.36, 0, -0.12),(0.36, 0, 0),(0.36, 0, 0.12),(0.24, 0, 0.24),
        (0.12, 0, 0.36),(0, 0, 0.36),(-0.12, 0, 0.36),(-0.24, 0, 0.24),(-0.36, 0, 0.12),
        (-0.36, 0, 0),(-0.36, 0, -0.12),(-0.24, 0, -0.24),(-0.12, 0, -0.36),(0, 0, -0.36)])
    cmds.parent(Func3, gr3)
    cmds.parent(gr3, Line3) 
    mel.eval("""
    setAttr "BL.scaleZ" 0.140;
    setAttr "BL.scaleX" 0.140;
    setAttr "BL.scaleY" 0.140;
             """)  
    
    cmds.parent(Line3, Line_grp)        
    mel.eval("""
    setAttr "Line3.translateX" 0.216;
    setAttr "Line3.translateZ" -0.646;
    setAttr -lock true -keyable false -channelBox false "Line3.v";    
    select -r Line3 ;

             """)
    cmds.listRelatives(Line3, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Line3), True)
    cmds.setAttr("{0}.overrideColor".format(Line3), ColorCurve1)  

 
    
    Line4 = cmds.curve(name="Line4",d=1, p=[(-0.14, 0, -0.14),
        (0.14, 0, -0.14),
        (0.14, 0, 0.14),
        (-0.14, 0, 0.14),
        (-0.14, 0, -0.14)])
    gr1 = cmds.group(n="ER", empty=True)
    Func1 = cmds.curve(name="Eye_Ctrl_R", d=1, p=[        
        (0, 0, -0.36),(0.12, 0, -0.36),
        (0.24, 0, -0.24),(0.36, 0, -0.12),(0.36, 0, 0),(0.36, 0, 0.12),(0.24, 0, 0.24),
        (0.12, 0, 0.36),(0, 0, 0.36),(-0.12, 0, 0.36),(-0.24, 0, 0.24),(-0.36, 0, 0.12),
        (-0.36, 0, 0),(-0.36, 0, -0.12),(-0.24, 0, -0.24),(-0.12, 0, -0.36),(0, 0, -0.36)])
    cmds.parent(Func1, gr1)
    cmds.parent(gr1, Line4) 
    mel.eval("""
    setAttr "ER.scaleZ" 0.140;
    setAttr "ER.scaleX" 0.140;
    setAttr "ER.scaleY" 0.140;
             """)   
             
    cmds.parent(Line4, Line_grp)    
    mel.eval("""
    setAttr "Line4.translateX" -0.216;
    setAttr "Line4.translateZ" -0.264;
    setAttr -lock true -keyable false -channelBox false "Line4.v";
    select -r Line4 ;

             """)
    cmds.listRelatives(Line4, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Line4), True)
    cmds.setAttr("{0}.overrideColor".format(Line4), ColorCurve1)  

    Line5 = cmds.curve(name="Line5",d=1, p=[(-0.14, 0, -0.14),
        (0.14, 0, -0.14),
        (0.14, 0, 0.14),
        (-0.14, 0, 0.14),
        (-0.14, 0, -0.14)])
    gr2 = cmds.group(n="EL", empty=True)
    Func2 = cmds.curve(name="Eye_Ctrl_L", d=1, p=[        
        (0, 0, -0.36),(0.12, 0, -0.36),
        (0.24, 0, -0.24),(0.36, 0, -0.12),(0.36, 0, 0),(0.36, 0, 0.12),(0.24, 0, 0.24),
        (0.12, 0, 0.36),(0, 0, 0.36),(-0.12, 0, 0.36),(-0.24, 0, 0.24),(-0.36, 0, 0.12),
        (-0.36, 0, 0),(-0.36, 0, -0.12),(-0.24, 0, -0.24),(-0.12, 0, -0.36),(0, 0, -0.36)])
    cmds.parent(Func2, gr2)
    cmds.parent(gr2, Line5) 
    mel.eval("""
    setAttr "EL.scaleZ" 0.140;
    setAttr "EL.scaleX" 0.140;
    setAttr "EL.scaleY" 0.140;
             """)   
    cmds.parent(Line5, Line_grp)    
    mel.eval("""
    setAttr "Line5.translateX" 0.216;
    setAttr "Line5.translateZ" -0.264;
    setAttr -lock true -keyable false -channelBox false "Line5.v";
    select -r Line5 ;

             """)
    cmds.listRelatives(Line5, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Line5), True)
    cmds.setAttr("{0}.overrideColor".format(Line5), ColorCurve1)  


    Line6 = cmds.curve(name="Line6",d=1, p=[(-0.14, 0, -0.14),
        (0.14, 0, -0.14),
        (0.14, 0, 0.14),
        (-0.14, 0, 0.14),
        (-0.14, 0, -0.14)])
    gr5 = cmds.group(n="MM", empty=True)
    Func5 = cmds.curve(name="Mouth", d=1, p=[        
        (0, 0, -0.36),(0.12, 0, -0.36),
        (0.24, 0, -0.24),(0.36, 0, -0.12),(0.36, 0, 0),(0.36, 0, 0.12),(0.24, 0, 0.24),
        (0.12, 0, 0.36),(0, 0, 0.36),(-0.12, 0, 0.36),(-0.24, 0, 0.24),(-0.36, 0, 0.12),
        (-0.36, 0, 0),(-0.36, 0, -0.12),(-0.24, 0, -0.24),(-0.12, 0, -0.36),(0, 0, -0.36)])
    cmds.parent(Func5, gr5) 
    cmds.parent(Line6, Line_grp)     
    mel.eval("""
    setAttr "Line6.scaleZ" 1.5;
    setAttr "Line6.scaleX" 1.5;
    setAttr "Line6.scaleY" 1.5;
    setAttr "Line6.translateZ" 0.20;
    select -r Line6 ;

             """)
    cmds.listRelatives(Line6, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Line6), True)
    cmds.setAttr("{0}.overrideColor".format(Line6), ColorCurve1)  
    cmds.parent(gr5, Line6) 
    mel.eval("""
    setAttr "MM.scaleZ" 0.140;
    setAttr "MM.scaleX" 0.140;
    setAttr "MM.scaleY" 0.140;
    setAttr "MM.translateZ" -0.14;
    
             """)  


    mel.eval("""
    setAttr -keyable false -channelBox true "Main_Face.tx";
    setAttr -keyable false -channelBox true "Main_Face.ty";
    setAttr -keyable false -channelBox true "Main_Face.tz";
    setAttr -keyable false -channelBox true "Main_Face.rx";
    setAttr -keyable false -channelBox true "Main_Face.ry";
    setAttr -keyable false -channelBox true "Main_Face.rz";
    setAttr -keyable false -channelBox true "Main_Face.sx";
    setAttr -keyable false -channelBox true "Main_Face.sy";
    setAttr -keyable false -channelBox true "Main_Face.sz";
             """)
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_R.ty";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_R.sz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_R.sx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_R.sy";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_R.ry";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_R.rx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_R.rz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_R.v";')
    cmds.transformLimits(Func4, tx=(-1, 1), ty=(0, 0), tz=(-1, 1), rx=(0, 0), ry=(0, 0), rz=(0, 0), sx=(1, 1), sy=(1, 1), sz=(1, 1), etx=(True, True), ety=(True, True), etz=(True, True))
    cmds.listRelatives(Func4, shapes=True)
    cmds.addAttr(Func4, longName='______________________', attributeType='enum', en='____________', keyable=True)
    mel.eval('setAttr -lock true "Bow_Ctrl_R.______________________";')
    # cmds.addAttr(Func4, longName = 'Blink', attributeType = 'float', min = 0, max = 10, keyable=True) 
    # cmds.addAttr(Func4, longName = 'Iris', attributeType = 'float', min = 0, max = 10, keyable=True) 
    # cmds.addAttr(Func4, longName = 'Pupil', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.setAttr("{0}.overrideEnabled".format(Func4), True)
    cmds.setAttr("{0}.overrideColor".format(Func4), ColorCurve3) 

    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_L.ty";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_L.sz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_L.sx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_L.sy";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_L.ry";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_L.rx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_L.rz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Bow_Ctrl_L.v";')
    cmds.transformLimits(Func3, tx=(-1, 1), ty=(0, 0), tz=(-1, 1), rx=(0, 0), ry=(0, 0), rz=(0, 0), sx=(1, 1), sy=(1, 1), sz=(1, 1), etx=(True, True), ety=(True, True), etz=(True, True))
    cmds.listRelatives(Func3, shapes=True)
    cmds.addAttr(Func3, longName='______________________', attributeType='enum', en='____________', keyable=True)
    mel.eval('setAttr -lock true "Bow_Ctrl_L.______________________";')
    # cmds.addAttr(Func3, longName = 'Blink', attributeType = 'float', min = 0, max = 10, keyable=True) 
    # cmds.addAttr(Func3, longName = 'Iris', attributeType = 'float', min = 0, max = 10, keyable=True) 
    # cmds.addAttr(Func3, longName = 'Pupil', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.setAttr("{0}.overrideEnabled".format(Func3), True)
    cmds.setAttr("{0}.overrideColor".format(Func3), ColorCurve3) 

    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_R.ty";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_R.sz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_R.sx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_R.sy";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_R.ry";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_R.rx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_R.rz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_R.v";')
    cmds.transformLimits(Func1, tx=(-1, 1), ty=(0, 0), tz=(-1, 1), rx=(0, 0), ry=(0, 0), rz=(0, 0), sx=(1, 1), sy=(1, 1), sz=(1, 1), etx=(True, True), ety=(True, True), etz=(True, True))
    cmds.listRelatives(Func1, shapes=True)
    cmds.addAttr(Func1, longName='______________________', attributeType='enum', en='____________', keyable=True)
    mel.eval('setAttr -lock true "Eye_Ctrl_R.______________________";')
    cmds.addAttr(Func1, longName = 'Blink', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.addAttr(Func1, longName = 'Iris', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.addAttr(Func1, longName = 'Pupil', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.setAttr("{0}.overrideEnabled".format(Func1), True)
    cmds.setAttr("{0}.overrideColor".format(Func1), ColorCurve3) 

    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_L.ty";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_L.sz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_L.sx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_L.sy";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_L.ry";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_L.rx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_L.rz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Eye_Ctrl_L.v";')
    cmds.transformLimits(Func2, tx=(-1, 1), ty=(0, 0), tz=(-1, 1), rx=(0, 0), ry=(0, 0), rz=(0, 0), sx=(1, 1), sy=(1, 1), sz=(1, 1), etx=(True, True), ety=(True, True), etz=(True, True))
    cmds.listRelatives(Func2, shapes=True)
    cmds.addAttr(Func2, longName='______________________', attributeType='enum', en='____________', keyable=True)
    mel.eval('setAttr -lock true "Eye_Ctrl_L.______________________";')
    cmds.addAttr(Func2, longName = 'Blink', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.addAttr(Func2, longName = 'Iris', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.addAttr(Func2, longName = 'Pupil', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.setAttr("{0}.overrideEnabled".format(Func2), True)
    cmds.setAttr("{0}.overrideColor".format(Func2), ColorCurve3) 

    mel.eval('setAttr -lock true -keyable false -channelBox false "Mouth.ty";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Mouth.sz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Mouth.sx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Mouth.sy";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Mouth.ry";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Mouth.rx";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Mouth.rz";')
    mel.eval('setAttr -lock true -keyable false -channelBox false "Mouth.v";')
    cmds.transformLimits(Func5, tx=(-1, 1), ty=(0, 0), tz=(0, 2), rx=(0, 0), ry=(0, 0), rz=(0, 0), sx=(1, 1), sy=(1, 1), sz=(1, 1), etx=(True, True), ety=(True, True), etz=(True, True))
    cmds.listRelatives(Func5, shapes=True)
    cmds.addAttr(Func5, longName='______________________', attributeType='enum', en='____________', keyable=True)
    mel.eval('setAttr -lock true "Mouth.______________________";')
    cmds.addAttr(Func5, longName = 'Happy', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.addAttr(Func5, longName = 'Sad', attributeType = 'float', min = 0, max = 10, keyable=True) 
    # cmds.addAttr(Func5, longName = 'Wow', attributeType = 'float', min = 0, max = 10, keyable=True) 
    # cmds.addAttr(Func5, longName = 'Angry', attributeType = 'float', min = 0, max = 10, keyable=True) 
    cmds.setAttr("{0}.overrideEnabled".format(Func5), True)
    cmds.setAttr("{0}.overrideColor".format(Func5), ColorCurve3)     

    mel.eval("""
    rename "curve1" "Mouth_Function";
    """)
    cmds.parent("Mouth_Function", "LineFunction")
    groupMain_xf = cmds.xform(joint_Neck, query=True, translation=True, worldSpace=True)
    groupMain_xf_tuple = tuple(groupMain_xf)
    cmds.xform(groupMain, worldSpace=True, translation=groupMain_xf_tuple)

    mel.eval("""
    setAttr -lock true -keyable false -channelBox false "Line6.tx";
    setAttr -lock true -keyable false -channelBox false "Line2.tx";
    setAttr -lock true -keyable false -channelBox false "Line5.tx";
    setAttr -lock true -keyable false -channelBox false "Line4.tx";
    setAttr -lock true -keyable false -channelBox false "Line3.tx";
    setAttr -lock true -keyable false -channelBox false "LineFunction.tx";
    setAttr -lock true -keyable false -channelBox false "Line6.ty";
    setAttr -lock true -keyable false -channelBox false "Line2.ty";
    setAttr -lock true -keyable false -channelBox false "Line5.ty";
    setAttr -lock true -keyable false -channelBox false "Line4.ty";
    setAttr -lock true -keyable false -channelBox false "Line3.ty";
    setAttr -lock true -keyable false -channelBox false "LineFunction.ty";
    setAttr -lock true -keyable false -channelBox false "Line6.tz";
    setAttr -lock true -keyable false -channelBox false "Line2.tz";
    setAttr -lock true -keyable false -channelBox false "Line5.tz";
    setAttr -lock true -keyable false -channelBox false "Line4.tz";
    setAttr -lock true -keyable false -channelBox false "Line3.tz";
    setAttr -lock true -keyable false -channelBox false "LineFunction.tz";
    setAttr -lock true -keyable false -channelBox false "Line6.rx";
    setAttr -lock true -keyable false -channelBox false "Line2.rx";
    setAttr -lock true -keyable false -channelBox false "Line5.rx";
    setAttr -lock true -keyable false -channelBox false "Line4.rx";
    setAttr -lock true -keyable false -channelBox false "Line3.rx";
    setAttr -lock true -keyable false -channelBox false "LineFunction.rx";
    setAttr -lock true -keyable false -channelBox false "Line6.ry";
    setAttr -lock true -keyable false -channelBox false "Line2.ry";
    setAttr -lock true -keyable false -channelBox false "Line5.ry";
    setAttr -lock true -keyable false -channelBox false "Line4.ry";
    setAttr -lock true -keyable false -channelBox false "Line3.ry";
    setAttr -lock true -keyable false -channelBox false "LineFunction.ry";
    setAttr -lock true -keyable false -channelBox false "Line6.rz";
    setAttr -lock true -keyable false -channelBox false "Line2.rz";
    setAttr -lock true -keyable false -channelBox false "Line5.rz";
    setAttr -lock true -keyable false -channelBox false "Line4.rz";
    setAttr -lock true -keyable false -channelBox false "Line3.rz";
    setAttr -lock true -keyable false -channelBox false "LineFunction.rz";
    setAttr -lock true -keyable false -channelBox false "Line6.sx";
    setAttr -lock true -keyable false -channelBox false "Line2.sx";
    setAttr -lock true -keyable false -channelBox false "Line5.sx";
    setAttr -lock true -keyable false -channelBox false "Line4.sx";
    setAttr -lock true -keyable false -channelBox false "Line3.sx";
    setAttr -lock true -keyable false -channelBox false "LineFunction.sx";
    setAttr -lock true -keyable false -channelBox false "Line6.sy";
    setAttr -lock true -keyable false -channelBox false "Line2.sy";
    setAttr -lock true -keyable false -channelBox false "Line5.sy";
    setAttr -lock true -keyable false -channelBox false "Line4.sy";
    setAttr -lock true -keyable false -channelBox false "Line3.sy";
    setAttr -lock true -keyable false -channelBox false "LineFunction.sy";
    setAttr -lock true -keyable false -channelBox false "Line6.sz";
    setAttr -lock true -keyable false -channelBox false "Line2.sz";
    setAttr -lock true -keyable false -channelBox false "Line5.sz";
    setAttr -lock true -keyable false -channelBox false "Line4.sz";
    setAttr -lock true -keyable false -channelBox false "Line3.sz";
    setAttr -lock true -keyable false -channelBox false "LineFunction.sz";
    setAttr -lock true -keyable false -channelBox false "Line6.v";
    setAttr -lock true -keyable false -channelBox false "Line2.v";
    setAttr -lock true -keyable false -channelBox false "Line5.v";
    setAttr -lock true -keyable false -channelBox false "Line4.v";
    setAttr -lock true -keyable false -channelBox false "Line3.v";
    setAttr -lock true -keyable false -channelBox false "LineFunction.v";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.tx";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.ty";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.tz";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.rx";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.ry";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.rz";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.sx";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.sy";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.sz";
    setAttr -lock true -keyable false -channelBox false "Mouth_Function.v";
    """)
    cmds.listRelatives("Mouth_Function", shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format("Mouth_Function"), True)
    cmds.setAttr("{0}.overrideColor".format("Mouth_Function"), Color5)  
    mel.eval("""
    setAttr "Main_Face_Grp_dont_FreezeTransformations.rotateX" 90;
    select -r Main_Face_Grp_dont_FreezeTransformations ;
    //scale -r 0.3 0.3 0.3;
    setAttr "Main_Face_Grp_dont_FreezeTransformations.translateX" 3;
    setAttr "Main_Face_Grp_dont_FreezeTransformations.translateY" 16;

    """)
    cmds.parent(groupMain, "Controller")

    ############################# parent #########################
    mel.eval("""    
    select -r Main_Face_Grp_dont_FreezeTransformations ;
    select -tgl Neck_Ctrl ;
    parent;
    """)

    # ############################# add selected layer #########################
    # mel.eval("""
    # layerEditorCreateLayer 1;
    # layerEditorLayerButtonTypeChange layer1;
    # select -r LineFunction Line6 Line5 ;
    # select -tgl Line4 ;
    # select -tgl Line2 Line3 ;
    # editDisplayLayerMembers -noRecurse layer1 `ls -selection`;
    #                       """)
    # mel.eval('select -cl ;')  

    ############################################################## tuple
    Face_grp_pos = cmds.xform(joint_Neck, query=True, translation=True, worldSpace=True)
    Face_grp_tuple = tuple(Face_grp_pos)

    jnt_ER_pos = cmds.xform(joint_ER, query=True, translation=True, worldSpace=True)
    jnt_ER_tuple = tuple(jnt_ER_pos)

    jnt_EL_pos = cmds.xform(joint_EL, query=True, translation=True, worldSpace=True)
    jnt_EL_tuple = tuple(jnt_EL_pos)

    jnt_MUL_pos = cmds.xform(Jnt_MUL, query=True, translation=True, worldSpace=True)
    jnt_MUL_tuple = tuple(jnt_MUL_pos)

    jnt_BW1_pos = cmds.xform(Jnt_BW1, query=True, translation=True, worldSpace=True)
    jnt_BW1_tuple = tuple(jnt_BW1_pos)

    jnt_BW2_pos = cmds.xform(Jnt_BW2, query=True, translation=True, worldSpace=True)
    jnt_BW2_tuple = tuple(jnt_BW2_pos)

    jnt_RCL_pos = cmds.xform(Jnt_RCL, query=True, translation=True, worldSpace=True)
    jnt_RCL_tuple = tuple(jnt_RCL_pos)

    jnt_BW3_pos = cmds.xform(Jnt_BW3, query=True, translation=True, worldSpace=True)
    jnt_BW3_tuple = tuple(jnt_BW3_pos)

    jnt_BW4_pos = cmds.xform(Jnt_BW4, query=True, translation=True, worldSpace=True)
    jnt_BW4_tuple = tuple(jnt_BW4_pos)    

    jnt_MDL_pos = cmds.xform(Jnt_MDL, query=True, translation=True, worldSpace=True)
    jnt_MDL_tuple = tuple(jnt_MDL_pos)    

    jnt_LCL_pos = cmds.xform(Jnt_LCL, query=True, translation=True, worldSpace=True)
    jnt_LCL_tuple = tuple(jnt_LCL_pos)

    jnt_BW5_pos = cmds.xform(Jnt_BW5, query=True, translation=True, worldSpace=True)
    jnt_BW5_tuple = tuple(jnt_BW5_pos)

    jnt_BW6_pos = cmds.xform(Jnt_BW6, query=True, translation=True, worldSpace=True)
    jnt_BW6_tuple = tuple(jnt_BW6_pos) 

    jnt_BW7_pos = cmds.xform(Jnt_BW7, query=True, translation=True, worldSpace=True)
    jnt_BW7_tuple = tuple(jnt_BW7_pos)

    jnt_BW8_pos = cmds.xform(Jnt_BW8, query=True, translation=True, worldSpace=True)
    jnt_BW8_tuple = tuple(jnt_BW8_pos) 

    Jnt_RIB_pos = cmds.xform(Jnt_RIB, query=True, translation=True, worldSpace=True)
    Jnt_RIB_tuple = tuple(Jnt_RIB_pos) 
    
    Jnt_ROB_pos = cmds.xform(Jnt_ROB, query=True, translation=True, worldSpace=True)
    Jnt_ROB_tuple = tuple(Jnt_ROB_pos) 
    
    Jnt_LIB_pos = cmds.xform(Jnt_LIB, query=True, translation=True, worldSpace=True)
    Jnt_LIB_tuple = tuple(Jnt_LIB_pos) 
    
    Jnt_LOB_pos = cmds.xform(Jnt_LOB, query=True, translation=True, worldSpace=True)
    Jnt_LOB_tuple = tuple(Jnt_LOB_pos) 
    
    Jnt_Jaw_pos = cmds.xform(Jnt_Jaw, query=True, translation=True, worldSpace=True)
    Jnt_Jaw_tuple = tuple(Jnt_Jaw_pos) 
    
    Jnt_TG1_pos = cmds.xform(Jnt_TG1, query=True, translation=True, worldSpace=True)
    Jnt_TG1_tuple = tuple(Jnt_TG1_pos) 
    
    Jnt_TG2_pos = cmds.xform(Jnt_TG2, query=True, translation=True, worldSpace=True)
    Jnt_TG2_tuple = tuple(Jnt_TG2_pos) 

    Jnt_TG3_pos = cmds.xform(Jnt_TG3, query=True, translation=True, worldSpace=True)
    Jnt_TG3_tuple = tuple(Jnt_TG3_pos)  

    Jnt_TG4_pos = cmds.xform(Jnt_TG4, query=True, translation=True, worldSpace=True)
    Jnt_TG4_tuple = tuple(Jnt_TG4_pos) 
    ##############################################################
    ############################################################## Eye Build

    R_Eye_grp = cmds.group(n="R_Eye_Grp", empty=True)
    cmds.xform(R_Eye_grp, translation=jnt_ER_tuple)
    cmds.parent(R_Eye_grp, "Controller")
    R_Eye_Loc_grp = cmds.group(n="R_Eye_Loc_grp", empty=True)
    cmds.xform(R_Eye_Loc_grp, translation=jnt_ER_tuple)
    cmds.parent(R_Eye_Loc_grp, R_Eye_grp)
    R_Loc_ER = cmds.curve(name ="R_Loc_Ctrl", degree = 1,
                    knot = [0, 4.7999999999999998, 9.5999999999999996, 12.800000000000001, 17.600000000000001,
                            22.399999999999999, 25.600000000000001, 30.399999999999999, 35.200000000000003,
                            38.399999999999999, 43.200000000000003, 48, 51.200000000000003],
                    point = [(-0.64000000000000012, -2.5600000000000005, 0),
                            (-0.64000000000000012, -0.64000000000000012, 0),(-2.5600000000000005, -0.64000000000000012, 0),
                            (-2.5600000000000005, 0.64000000000000012, 0),(-0.64000000000000012, 0.64000000000000012, 0),
                            (-0.64000000000000012, 2.5600000000000005, 0),(0.64000000000000012, 2.5600000000000005, 0),
                            (0.64000000000000012, 0.64000000000000012, 0),(2.5600000000000005, 0.64000000000000012, 0),
                            (2.5600000000000005, -0.64000000000000012, 0),(0.64000000000000012, -0.64000000000000012, 0),
                            (0.64000000000000012, -2.5600000000000005, 0),(-0.64000000000000012, -2.5600000000000005, 0)])
    cmds.scale(0.2,0.2,0.2)
    cmds.listRelatives(R_Loc_ER, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(R_Loc_ER), True)
    cmds.setAttr("{0}.overrideColor".format(R_Loc_ER), Color4)
    cmds.xform(R_Loc_ER, translation=jnt_ER_tuple)
    cmds.parent(R_Loc_ER, R_Eye_Loc_grp)

    mel.eval("""
    setAttr "R_Eye_Loc_grp|R_Loc_Ctrl.translateZ" 4;
    FreezeTransformations;
    select -cl  ;
            """)

    L_Eye_grp = cmds.group(n="L_Eye_Grp", empty=True)
    cmds.xform(L_Eye_grp, translation=jnt_EL_tuple)
    cmds.parent(L_Eye_grp, "Controller")
    L_Eye_Loc_grp = cmds.group(n="L_Eye_Loc_grp", empty=True)
    cmds.xform(L_Eye_Loc_grp, translation=jnt_EL_tuple)
    cmds.parent(L_Eye_Loc_grp, L_Eye_grp)
    L_Loc_ER = cmds.curve(name ="L_Loc_Ctrl", degree = 1,
                    knot = [0, 4.7999999999999998, 9.5999999999999996, 12.800000000000001, 17.600000000000001,
                            22.399999999999999, 25.600000000000001, 30.399999999999999, 35.200000000000003,
                            38.399999999999999, 43.200000000000003, 48, 51.200000000000003],
                    point = [(-0.64000000000000012, -2.5600000000000005, 0),
                            (-0.64000000000000012, -0.64000000000000012, 0),(-2.5600000000000005, -0.64000000000000012, 0),
                            (-2.5600000000000005, 0.64000000000000012, 0),(-0.64000000000000012, 0.64000000000000012, 0),
                            (-0.64000000000000012, 2.5600000000000005, 0),(0.64000000000000012, 2.5600000000000005, 0),
                            (0.64000000000000012, 0.64000000000000012, 0),(2.5600000000000005, 0.64000000000000012, 0),
                            (2.5600000000000005, -0.64000000000000012, 0),(0.64000000000000012, -0.64000000000000012, 0),
                            (0.64000000000000012, -2.5600000000000005, 0),(-0.64000000000000012, -2.5600000000000005, 0)])
    cmds.scale(0.2,0.2,0.2)
    cmds.listRelatives(L_Loc_ER, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(L_Loc_ER), True)
    cmds.setAttr("{0}.overrideColor".format(L_Loc_ER), Color4)    
    cmds.xform(L_Loc_ER, translation=jnt_EL_tuple)
    cmds.parent(L_Loc_ER, L_Eye_Loc_grp)
    mel.eval("""
    setAttr "L_Eye_Loc_grp|L_Loc_Ctrl.translateZ" 4;
    FreezeTransformations;
    select -cl  ;
            """)    

    jnt_ER = cmds.joint(n="ERJ_R")
    cmds.xform(jnt_ER, worldSpace=True, translation = jnt_ER_tuple)
    cmds.parent(jnt_ER, R_Eye_Loc_grp)
    
    jnt_EL = cmds.joint(n="ERJ_L")
    cmds.xform(jnt_EL, worldSpace=True, translation = jnt_EL_tuple)
    cmds.parent(jnt_EL, L_Eye_Loc_grp)

    ############################################################ Parent Eye
    mel.eval("""
    select -r R_Eye_Loc_grp|R_Loc_Ctrl ;
    select -add ERJ_R ;
    aimConstraint -offset 0 0 0 -weight 1 -aimVector 1 0 0 -upVector 0 1 0 -worldUpType "vector" -worldUpVector 0 1 0;
    select -r L_Eye_Loc_grp|L_Loc_Ctrl ;
    select -add ERJ_L ;
    aimConstraint -offset 0 0 0 -weight 1 -aimVector 1 0 0 -upVector 0 1 0 -worldUpType "vector" -worldUpVector 0 1 0;
             
    select -r ERJ_R ;
    select -add EyeR ;
    parentConstraint -mo -weight 1;
    select -r ERJ_L ;
    select -add EyeL ;
    parentConstraint -mo -weight 1;

    select -r ERJ_R ;
    select -add ERJ_L ;
    toggleVisibilityAndKeepSelection `optionVar -query toggleVisibilityAndKeepSelectionBehaviour`;    
             """)
    
    ############################################################## set driven key eye
    mel.eval("""
    setAttr "Eye_Ctrl_L.translateX" 0;
    setAttr "L_Eye_Loc_grp.rotateY" 0;
    setDrivenKeyframe -currentDriver Eye_Ctrl_L.translateX L_Eye_Loc_grp.rotateY;
    setAttr "Eye_Ctrl_L.translateX" 1;
    setAttr "L_Eye_Loc_grp.rotateY" 40;
    setDrivenKeyframe -currentDriver Eye_Ctrl_L.translateX L_Eye_Loc_grp.rotateY;
    setAttr "Eye_Ctrl_L.translateX" -1;
    setAttr "L_Eye_Loc_grp.rotateY" -40;
    setDrivenKeyframe -currentDriver Eye_Ctrl_L.translateX L_Eye_Loc_grp.rotateY;

    setAttr "Eye_Ctrl_L.translateZ" 0;
    setAttr "L_Eye_Loc_grp.rotateX" 0;
    setDrivenKeyframe -currentDriver Eye_Ctrl_L.translateZ L_Eye_Loc_grp.rotateX;
    setAttr "Eye_Ctrl_L.translateZ" -1;
    setAttr "L_Eye_Loc_grp.rotateX" -40;
    setDrivenKeyframe -currentDriver Eye_Ctrl_L.translateZ L_Eye_Loc_grp.rotateX;
    setAttr "Eye_Ctrl_L.translateZ" 1;
    setAttr "L_Eye_Loc_grp.rotateX" 40;
    setDrivenKeyframe -currentDriver Eye_Ctrl_L.translateZ L_Eye_Loc_grp.rotateX;
             
    setAttr "Eye_Ctrl_R.translateX" 0;
    setAttr "R_Eye_Loc_grp.rotateY" 0;
    setDrivenKeyframe -currentDriver Eye_Ctrl_R.translateX R_Eye_Loc_grp.rotateY;
    setAttr "Eye_Ctrl_R.translateX" 1;
    setAttr "R_Eye_Loc_grp.rotateY" 40;
    setDrivenKeyframe -currentDriver Eye_Ctrl_R.translateX R_Eye_Loc_grp.rotateY;
    setAttr "Eye_Ctrl_R.translateX" -1;
    setAttr "R_Eye_Loc_grp.rotateY" -40;
    setDrivenKeyframe -currentDriver Eye_Ctrl_R.translateX R_Eye_Loc_grp.rotateY;

    setAttr "Eye_Ctrl_R.translateZ" 0;
    setAttr "R_Eye_Loc_grp.rotateX" 0;
    setDrivenKeyframe -currentDriver Eye_Ctrl_R.translateZ R_Eye_Loc_grp.rotateX;
    setAttr "Eye_Ctrl_R.translateZ" -1;
    setAttr "R_Eye_Loc_grp.rotateX" -40;
    setDrivenKeyframe -currentDriver Eye_Ctrl_R.translateZ R_Eye_Loc_grp.rotateX;
    setAttr "Eye_Ctrl_R.translateZ" 1;
    setAttr "R_Eye_Loc_grp.rotateX" 40;
    setDrivenKeyframe -currentDriver Eye_Ctrl_R.translateZ R_Eye_Loc_grp.rotateX;   

    setAttr "Eye_Ctrl_R.translateZ" 0;
    setAttr "Eye_Ctrl_L.translateZ" 0;
    setAttr "Eye_Ctrl_R.translateX" 0;
    setAttr "Eye_Ctrl_L.translateX" 0;                                                  
             """)
    
    ############################################################## P parentConstraint
    mel.eval("""
    select -r EyeR_parentConstraint1 ;
    select -add EyeL_parentConstraint1 ;
    select -add ERJ_R_aimConstraint1 ;
    select -add ERJ_L_aimConstraint1 ;
    select -add Constraint_Grp ;
    parent;
    select -r R_Eye_Grp L_Eye_Grp ;
    select -tgl Neck_Ctrl ;
    parent;
    select -cl  ;
             """)
    

    ############################################################## Mouth build
    ##############################################################
    Face_Grp = cmds.group(n="Face_Ctrl_Grp", empty=True)
    cmds.xform(Face_Grp, translation=Face_grp_tuple)
    cmds.parent(Face_Grp, "Neck_Ctrl")

    ############################ MUL
    MUL_grp = cmds.group(n="MUL_Grp", empty=True)
    cmds.xform(MUL_grp, translation=jnt_MUL_tuple)
    MUL_Jaw_grp = cmds.group(n="MUL_Jaw_grp", empty=True)
    cmds.xform(MUL_grp, translation=jnt_MUL_tuple)
    cmds.parent(MUL_Jaw_grp, MUL_grp)
    mel.eval("""
    select -r MUL_Jaw_grp ;
    FreezeTransformations;
    """)  
    cmds.CenterPivot(MUL_Jaw_grp)
    MUL_Ctrl_grp = cmds.group(n="MUL_Ctrl_grp", empty=True)
    cmds.xform(MUL_grp, translation=jnt_MUL_tuple)
    cmds.parent(MUL_Ctrl_grp, MUL_Jaw_grp)
    mel.eval("""
    select -r MUL_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(MUL_Ctrl_grp)
    MUL_Ctrl = cmds.curve(name ="Mid_Up_Lip_Ctrl", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.05, 0.05, 0.05)
    cmds.listRelatives(MUL_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(MUL_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(MUL_Ctrl), Color4)
    cmds.xform(MUL_Ctrl, translation=jnt_MUL_tuple)
    cmds.parent(MUL_Ctrl, MUL_Ctrl_grp)
    mel.eval("""
    select -r Mid_Up_Lip_Ctrl ;
    setAttr "Mid_Up_Lip_Ctrl.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(MUL_grp, Face_Grp)
    
    ############################ BW1
    BW1_grp = cmds.group(n="BW1_Grp", empty=True)
    cmds.xform(BW1_grp, translation=jnt_BW1_tuple)
    BW1_Jaw_grp = cmds.group(n="BW1_Jaw_grp", empty=True)
    cmds.xform(BW1_grp, translation=jnt_BW1_tuple)
    cmds.parent(BW1_Jaw_grp, BW1_grp)
    mel.eval("""
    select -r BW1_Jaw_grp ;
    FreezeTransformations;
    """) 
    cmds.CenterPivot()
    BW1_Ctrl_grp = cmds.group(n="BW1_Ctrl_grp", empty=True)
    cmds.xform(BW1_grp, translation=jnt_BW1_tuple)
    cmds.parent(BW1_Ctrl_grp, BW1_Jaw_grp)
    mel.eval("""
    select -r BW1_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(BW1_Ctrl_grp)
    BW1_Ctrl = cmds.curve(name ="BW1_Ctrl_R", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.05, 0.05, 0.05)
    cmds.listRelatives(BW1_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(BW1_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(BW1_Ctrl), Color4)
    cmds.xform(BW1_Ctrl, translation=jnt_BW1_tuple)
    cmds.parent(BW1_Ctrl, BW1_Ctrl_grp)
    mel.eval("""
    select -r BW1_Ctrl_R ;
    setAttr "BW1_Ctrl_R.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(BW1_grp, Face_Grp)

    ############################ BW2
    BW2_grp = cmds.group(n="BW2_Grp", empty=True)
    cmds.xform(BW2_grp, translation=jnt_BW2_tuple)
    BW2_Jaw_grp = cmds.group(n="BW2_Jaw_grp", empty=True)
    cmds.xform(BW2_grp, translation=jnt_BW2_tuple)
    cmds.parent(BW2_Jaw_grp, BW2_grp)
    mel.eval("""
    select -r BW2_Jaw_grp ;
    FreezeTransformations;
    """)     
    cmds.CenterPivot()
    BW2_Ctrl_grp = cmds.group(n="BW2_Ctrl_grp", empty=True)
    cmds.xform(BW2_grp, translation=jnt_BW2_tuple)
    cmds.parent(BW2_Ctrl_grp, BW2_Jaw_grp)
    mel.eval("""
    select -r BW2_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(BW2_Ctrl_grp)
    BW2_Ctrl = cmds.curve(name ="BW2_Ctrl_R", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.05, 0.05, 0.05)
    cmds.listRelatives(BW2_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(BW2_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(BW2_Ctrl), Color4)
    cmds.xform(BW2_Ctrl, translation=jnt_BW2_tuple)
    cmds.parent(BW2_Ctrl, BW2_Ctrl_grp)
    mel.eval("""
    select -r BW2_Ctrl_R ;
    setAttr "BW2_Ctrl_R.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(BW2_grp, Face_Grp)

    ############################ RCL
    RCL_grp = cmds.group(n="RCL_Grp", empty=True)
    cmds.xform(RCL_grp, translation=jnt_RCL_tuple)
    RCL_Jaw_grp = cmds.group(n="RCL_Jaw_grp", empty=True)
    cmds.xform(RCL_grp, translation=jnt_RCL_tuple)
    cmds.parent(RCL_Jaw_grp, RCL_grp)
    mel.eval("""
    select -r RCL_Jaw_grp ;
    FreezeTransformations;
    """)       
    cmds.CenterPivot()
    RCL_Ctrl_grp = cmds.group(n="RCL_Ctrl_grp", empty=True)
    cmds.xform(RCL_grp, translation=jnt_RCL_tuple)
    cmds.parent(RCL_Ctrl_grp, RCL_Jaw_grp)
    mel.eval("""
    select -r RCL_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(RCL_Ctrl_grp)
    RCL_Ctrl = cmds.curve(name ="RCL_Ctrl_R", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.05, 0.05, 0.05)
    cmds.listRelatives(RCL_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(RCL_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(RCL_Ctrl), Color4)
    cmds.xform(RCL_Ctrl, translation=jnt_RCL_tuple)
    cmds.parent(RCL_Ctrl, RCL_Ctrl_grp)
    mel.eval("""
    select -r RCL_Ctrl_R ;
    setAttr "RCL_Ctrl_R.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(RCL_grp, Face_Grp)

    ############################ BW3
    BW3_grp = cmds.group(n="BW3_Grp", empty=True)
    cmds.xform(BW3_grp, translation=jnt_BW3_tuple)
    BW3_Jaw_grp = cmds.group(n="BW3_Jaw_grp", empty=True)
    cmds.xform(BW3_grp, translation=jnt_BW3_tuple)
    cmds.parent(BW3_Jaw_grp, BW3_grp)
    mel.eval("""
    select -r BW3_Jaw_grp ;
    FreezeTransformations;
    """)      
    cmds.CenterPivot()
    BW3_Ctrl_grp = cmds.group(n="BW3_Ctrl_grp", empty=True)
    cmds.xform(BW3_grp, translation=jnt_BW3_tuple)
    cmds.parent(BW3_Ctrl_grp, BW3_Jaw_grp)
    mel.eval("""
    select -r BW3_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(BW3_Ctrl_grp)
    BW3_Ctrl = cmds.curve(name ="BW3_Ctrl_R", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.05, 0.05, 0.05)
    cmds.listRelatives(BW3_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(BW3_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(BW3_Ctrl), Color4)
    cmds.xform(BW3_Ctrl, translation=jnt_BW3_tuple)
    cmds.parent(BW3_Ctrl, BW3_Ctrl_grp)
    mel.eval("""
    select -r BW3_Ctrl_R ;
    setAttr "BW3_Ctrl_R.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(BW3_grp, Face_Grp)

    ############################ BW4
    BW4_grp = cmds.group(n="BW4_Grp", empty=True)
    cmds.xform(BW4_grp, translation=jnt_BW4_tuple)
    BW4_Jaw_grp = cmds.group(n="BW4_Jaw_grp", empty=True)
    cmds.xform(BW4_grp, translation=jnt_BW4_tuple)
    cmds.parent(BW4_Jaw_grp, BW4_grp)
    mel.eval("""
    select -r BW4_Jaw_grp ;
    FreezeTransformations;
    """)     
    cmds.CenterPivot()
    BW4_Ctrl_grp = cmds.group(n="BW4_Ctrl_grp", empty=True)
    cmds.xform(BW4_grp, translation=jnt_BW4_tuple)
    cmds.parent(BW4_Ctrl_grp, BW4_Jaw_grp)
    mel.eval("""
    select -r BW4_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(BW4_Ctrl_grp)
    BW4_Ctrl = cmds.curve(name ="BW4_Ctrl_R", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.05, 0.05, 0.05)
    cmds.listRelatives(BW4_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(BW4_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(BW4_Ctrl), Color4)
    cmds.xform(BW4_Ctrl, translation=jnt_BW4_tuple)
    cmds.parent(BW4_Ctrl, BW4_Ctrl_grp)
    mel.eval("""
    select -r BW4_Ctrl_R ;
    setAttr "BW4_Ctrl_R.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(BW4_grp, Face_Grp)

    ############################ MDL
    MDL_grp = cmds.group(n="MDL_Grp", empty=True)
    cmds.xform(MDL_grp, translation=jnt_MDL_tuple)
    MDL_Jaw_grp = cmds.group(n="MDL_Jaw_grp", empty=True)
    cmds.xform(MDL_grp, translation=jnt_MDL_tuple)
    cmds.parent(MDL_Jaw_grp, MDL_grp)
    mel.eval("""
    select -r MDL_Jaw_grp ;
    FreezeTransformations;
    """)       
    cmds.CenterPivot()
    MDL_Ctrl_grp = cmds.group(n="MDL_Ctrl_grp", empty=True)
    cmds.xform(MDL_grp, translation=jnt_MDL_tuple)
    cmds.parent(MDL_Ctrl_grp, MDL_Jaw_grp)
    cmds.CenterPivot(MDL_Ctrl_grp)
    mel.eval("""
    select -r MDL_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(MUL_Ctrl_grp)
    MDL_Ctrl = cmds.curve(name ="Mid_Down_Lip_Ctrl", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.05, 0.05, 0.05)
    cmds.listRelatives(MDL_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(MDL_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(MDL_Ctrl), Color4)
    cmds.xform(MDL_Ctrl, translation=jnt_MDL_tuple)
    cmds.parent(MDL_Ctrl, MDL_Ctrl_grp)
    mel.eval("""
    select -r Mid_Down_Lip_Ctrl ;
    setAttr "Mid_Down_Lip_Ctrl.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(MDL_grp, Face_Grp)

    ############################ BW5
    BW5_grp = cmds.group(n="BW5_Grp", empty=True)
    cmds.xform(BW5_grp, translation=jnt_BW5_tuple)
    BW5_Jaw_grp = cmds.group(n="BW5_Jaw_grp", empty=True)
    cmds.xform(BW5_grp, translation=jnt_BW5_tuple)
    cmds.parent(BW5_Jaw_grp, BW5_grp)
    mel.eval("""
    select -r BW5_Jaw_grp ;
    FreezeTransformations;
    """)       
    cmds.CenterPivot()
    BW5_Ctrl_grp = cmds.group(n="BW5_Ctrl_grp", empty=True)
    cmds.xform(BW5_grp, translation=jnt_BW5_tuple)
    cmds.parent(BW5_Ctrl_grp, BW5_Jaw_grp)
    mel.eval("""
    select -r BW5_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(BW5_Ctrl_grp)
    BW5_Ctrl = cmds.curve(name ="BW1_Ctrl_L", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.05, 0.05, 0.05)
    cmds.listRelatives(BW5_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(BW5_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(BW5_Ctrl), Color4)
    cmds.xform(BW5_Ctrl, translation=jnt_BW5_tuple)
    cmds.parent(BW5_Ctrl, BW5_Ctrl_grp)
    mel.eval("""
    select -r BW1_Ctrl_L ;
    setAttr "BW1_Ctrl_L.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(BW5_grp, Face_Grp)

    ############################ BW6
    BW6_grp = cmds.group(n="BW6_Grp", empty=True)
    cmds.xform(BW6_grp, translation=jnt_BW6_tuple)
    BW6_Jaw_grp = cmds.group(n="BW6_Jaw_grp", empty=True)
    cmds.xform(BW6_grp, translation=jnt_BW6_tuple)
    cmds.parent(BW6_Jaw_grp, BW6_grp)
    mel.eval("""
    select -r BW6_Jaw_grp ;
    FreezeTransformations;
    """)      
    cmds.CenterPivot()
    BW6_Ctrl_grp = cmds.group(n="BW6_Ctrl_grp", empty=True)
    cmds.xform(BW6_grp, translation=jnt_BW6_tuple)
    cmds.parent(BW6_Ctrl_grp, BW6_Jaw_grp)
    mel.eval("""
    select -r BW6_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(BW6_Ctrl_grp)
    BW6_Ctrl = cmds.curve(name ="BW2_Ctrl_L", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.05, 0.05, 0.05)
    cmds.listRelatives(BW6_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(BW6_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(BW6_Ctrl), Color4)
    cmds.xform(BW6_Ctrl, translation=jnt_BW6_tuple)
    cmds.parent(BW6_Ctrl, BW6_Ctrl_grp)
    mel.eval("""
    select -r BW2_Ctrl_L ;
    setAttr "BW2_Ctrl_L.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(BW6_grp, Face_Grp)

    ############################ BW7
    BW7_grp = cmds.group(n="BW7_Grp", empty=True)
    cmds.xform(BW7_grp, translation=jnt_BW7_tuple)
    BW7_Jaw_grp = cmds.group(n="BW7_Jaw_grp", empty=True)
    cmds.xform(BW7_grp, translation=jnt_BW7_tuple)
    cmds.parent(BW7_Jaw_grp, BW7_grp)
    mel.eval("""
    select -r BW7_Jaw_grp ;
    FreezeTransformations;
    """)      
    cmds.CenterPivot()
    BW7_Ctrl_grp = cmds.group(n="BW7_Ctrl_grp", empty=True)
    cmds.xform(BW7_grp, translation=jnt_BW7_tuple)
    cmds.parent(BW7_Ctrl_grp, BW7_Jaw_grp)
    mel.eval("""
    select -r BW7_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(BW7_Ctrl_grp)
    BW7_Ctrl = cmds.curve(name ="BW3_Ctrl_L", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.05, 0.05, 0.05)
    cmds.listRelatives(BW7_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(BW7_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(BW7_Ctrl), Color4)
    cmds.xform(BW7_Ctrl, translation=jnt_BW7_tuple)
    cmds.parent(BW7_Ctrl, BW7_Ctrl_grp)
    mel.eval("""
    select -r BW3_Ctrl_L ;
    setAttr "BW3_Ctrl_L.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(BW7_grp, Face_Grp)

    ############################ BW8
    BW8_grp = cmds.group(n="BW8_Grp", empty=True)
    cmds.xform(BW8_grp, translation=jnt_BW8_tuple)
    BW8_Jaw_grp = cmds.group(n="BW8_Jaw_grp", empty=True)
    cmds.xform(BW8_grp, translation=jnt_BW8_tuple)
    cmds.parent(BW8_Jaw_grp, BW8_grp)
    mel.eval("""
    select -r BW8_Jaw_grp ;
    FreezeTransformations;
    """)      
    cmds.CenterPivot()
    BW8_Ctrl_grp = cmds.group(n="BW8_Ctrl_grp", empty=True)
    cmds.xform(BW8_grp, translation=jnt_BW8_tuple)
    cmds.parent(BW8_Ctrl_grp, BW8_Jaw_grp)
    mel.eval("""
    select -r BW8_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(BW8_Ctrl_grp)
    BW8_Ctrl = cmds.curve(name ="BW4_Ctrl_L", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.05, 0.05, 0.05)
    cmds.listRelatives(BW8_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(BW8_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(BW8_Ctrl), Color4)
    cmds.xform(BW8_Ctrl, translation=jnt_BW8_tuple)
    cmds.parent(BW8_Ctrl, BW8_Ctrl_grp)
    mel.eval("""
    select -r BW4_Ctrl_L ;
    setAttr "BW4_Ctrl_L.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(BW8_grp, Face_Grp)

    ############################ LCL
    LCL_grp = cmds.group(n="LCL_Grp", empty=True)
    cmds.xform(LCL_grp, translation=jnt_LCL_tuple)
    LCL_Jaw_grp = cmds.group(n="LCL_Jaw_grp", empty=True)
    cmds.xform(LCL_grp, translation=jnt_LCL_tuple)
    cmds.parent(LCL_Jaw_grp, LCL_grp)
    mel.eval("""
    select -r LCL_Jaw_grp ;
    FreezeTransformations;
    """)     
    cmds.CenterPivot()
    LCL_Ctrl_grp = cmds.group(n="LCL_Ctrl_grp", empty=True)
    cmds.xform(LCL_grp, translation=jnt_LCL_tuple)
    cmds.parent(LCL_Ctrl_grp, LCL_Jaw_grp)
    mel.eval("""
    select -r LCL_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(LCL_Ctrl_grp)
    LCL_Ctrl = cmds.curve(name ="LCL_Ctrl_L", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.05, 0.05, 0.05)
    cmds.listRelatives(LCL_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(LCL_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(LCL_Ctrl), Color4)
    cmds.xform(LCL_Ctrl, translation=jnt_LCL_tuple)
    cmds.parent(LCL_Ctrl, LCL_Ctrl_grp)
    mel.eval("""
    select -r LCL_Ctrl_L ;
    setAttr "LCL_Ctrl_L.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(LCL_grp, Face_Grp)


    ######################################################################## Brow Build
    ########################################################################

    R_Brow_Grp = cmds.group(n="R_Brow_Grp", empty=True)
    cmds.xform(R_Brow_Grp, translation=Jnt_RIB_tuple)
    cmds.parent(R_Brow_Grp, Face_Grp)
    RIB_grp = cmds.group(n="RIB_Grp", empty=True)
    cmds.xform(RIB_grp, translation=Jnt_RIB_tuple)
    RIB_Ctrl_grp = cmds.group(n="RIB_Ctrl_grp", empty=True)
    cmds.xform(RIB_grp, translation=Jnt_RIB_tuple)
    cmds.parent(RIB_Ctrl_grp, RIB_grp)
    mel.eval("""
    select -r RIB_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(RIB_Ctrl_grp)
    RIB_Ctrl = cmds.curve(name ="RIB_Ctrl_R", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.05, 0.05, 0.05)
    cmds.listRelatives(RIB_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(RIB_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(RIB_Ctrl), Color2)
    cmds.xform(RIB_Ctrl, translation=Jnt_RIB_tuple)
    cmds.parent(RIB_Ctrl, RIB_Ctrl_grp)
    mel.eval("""
    select -r RIB_Ctrl_R ;
    setAttr "RIB_Ctrl_R.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(RIB_grp, R_Brow_Grp)

    
    ROB_grp = cmds.group(n="ROB_Grp", empty=True)
    cmds.xform(ROB_grp, translation=Jnt_ROB_tuple)
    ROB_Ctrl_grp = cmds.group(n="ROB_Ctrl_grp", empty=True)
    cmds.xform(ROB_grp, translation=Jnt_ROB_tuple)
    cmds.parent(ROB_Ctrl_grp, ROB_grp)
    mel.eval("""
    select -r ROB_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(ROB_Ctrl_grp)
    ROB_Ctrl = cmds.curve(name ="ROB_Ctrl_R", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.05, 0.05, 0.05)
    cmds.listRelatives(ROB_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(ROB_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(ROB_Ctrl), Color2)
    cmds.xform(ROB_Ctrl, translation=Jnt_ROB_tuple)
    cmds.parent(ROB_Ctrl, ROB_Ctrl_grp)
    mel.eval("""
    select -r ROB_Ctrl_R ;
    setAttr "ROB_Ctrl_R.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(ROB_grp, R_Brow_Grp)




    L_Brow_Grp = cmds.group(n="L_Brow_Grp", empty=True)
    cmds.xform(L_Brow_Grp, translation=Jnt_RIB_tuple)
    cmds.parent(L_Brow_Grp, Face_Grp)
    LIB_grp = cmds.group(n="LIB_Grp", empty=True)
    cmds.xform(LIB_grp, translation=Jnt_LIB_tuple)
    LIB_Ctrl_grp = cmds.group(n="LIB_Ctrl_grp", empty=True)
    cmds.xform(LIB_grp, translation=Jnt_LIB_tuple)
    cmds.parent(LIB_Ctrl_grp, LIB_grp)
    mel.eval("""
    select -r LIB_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(LIB_Ctrl_grp)
    LIB_Ctrl = cmds.curve(name ="LIB_Ctrl_L", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.05, 0.05, 0.05)
    cmds.listRelatives(LIB_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(LIB_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(LIB_Ctrl), Color2)
    cmds.xform(LIB_Ctrl, translation=Jnt_LIB_tuple)
    cmds.parent(LIB_Ctrl, LIB_Ctrl_grp)
    mel.eval("""
    select -r LIB_Ctrl_L ;
    setAttr "LIB_Ctrl_L.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(LIB_grp, L_Brow_Grp)

    

    LOB_grp = cmds.group(n="LOB_Grp", empty=True)
    cmds.xform(LOB_grp, translation=Jnt_LOB_tuple)
    LOB_Ctrl_grp = cmds.group(n="LOB_Ctrl_grp", empty=True)
    cmds.xform(LOB_grp, translation=Jnt_LOB_tuple)
    cmds.parent(LOB_Ctrl_grp, LOB_grp)
    mel.eval("""
    select -r LOB_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(LOB_Ctrl_grp)
    LOB_Ctrl = cmds.curve(name ="LOB_Ctrl_L", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.05, 0.05, 0.05)
    cmds.listRelatives(LOB_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(LOB_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(LOB_Ctrl), Color2)
    cmds.xform(LOB_Ctrl, translation=Jnt_LOB_tuple)
    cmds.parent(LOB_Ctrl, LOB_Ctrl_grp)
    mel.eval("""
    select -r LOB_Ctrl_L ;
    setAttr "LOB_Ctrl_L.translateZ" 0.1 ;
    FreezeTransformations;
            """) 
    cmds.parent(LOB_grp, L_Brow_Grp)


    Jaw_grp = cmds.group(n="Jaw_Grp", empty=True)
    cmds.xform(Jaw_grp, translation=Jnt_Jaw_tuple)
    Jaw_Ctrl_grp = cmds.group(n="Jaw_Ctrl_grp", empty=True)
    cmds.xform(Jaw_grp, translation=Jnt_Jaw_tuple)
    cmds.parent(Jaw_Ctrl_grp, Jaw_grp)
    mel.eval("""
    select -r Jaw_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(Jaw_Ctrl_grp)
    Jaw_Ctrl = cmds.curve(name ="Jaw_Ctrl", degree = 1,
                    knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                    point = [(0, 1, 0),(0, 0.92388000000000003, 0.382683),
                            (0, 0.70710700000000004, 0.70710700000000004),(0, 0.382683, 0.92388000000000003),(0, 0, 1),
                            (0, -0.382683, 0.92388000000000003),(0, -0.70710700000000004, 0.70710700000000004),
                            (0, -0.92388000000000003, 0.382683),(0, -1, 0),(0, -0.92388000000000003, -0.382683),
                            (0, -0.70710700000000004, -0.70710700000000004),(0, -0.382683, -0.92388000000000003),(0, 0, -1),
                            (0, 0.382683, -0.92388000000000003),(0, 0.70710700000000004, -0.70710700000000004),
                            (0, 0.92388000000000003, -0.382683),(0, 1, 0),(0.382683, 0.92388000000000003, 0),
                            (0.70710700000000004, 0.70710700000000004, 0),(0.92388000000000003, 0.382683, 0),(1, 0, 0),
                            (0.92388000000000003, -0.382683, 0),(0.70710700000000004, -0.70710700000000004, 0),
                            (0.382683, -0.92388000000000003, 0),(0, -1, 0),(-0.382683, -0.92388000000000003, 0),
                            (-0.70710700000000004, -0.70710700000000004, 0),(-0.92388000000000003, -0.382683, 0),(-1, 0, 0),
                            (-0.92388000000000003, 0.382683, 0),(-0.70710700000000004, 0.70710700000000004, 0),
                            (-0.382683, 0.92388000000000003, 0),(0, 1, 0),(0, 0.92388000000000003, -0.382683),
                            (0, 0.70710700000000004, -0.70710700000000004),(0, 0.382683, -0.92388000000000003),(0, 0, -1),
                            (-0.382683, 0, -0.92388000000000003),(-0.70710700000000004, 0, -0.70710700000000004),
                            (-0.92388000000000003, 0, -0.382683),(-1, 0, 0),(-0.92388000000000003, 0, 0.382683),
                            (-0.70710700000000004, 0, 0.70710700000000004),(-0.382683, 0, 0.92388000000000003),(0, 0, 1),
                            (0.382683, 0, 0.92388000000000003),(0.70710700000000004, 0, 0.70710700000000004),
                            (0.92388000000000003, 0, 0.382683),(1, 0, 0),(0.92388000000000003, 0, -0.382683),
                            (0.70710700000000004, 0, -0.70710700000000004),(0.382683, 0, -0.92388000000000003),(0, 0, -1)])
    cmds.scale(0.05, 0.05, 0.05)
    cmds.listRelatives(Jaw_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Jaw_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(Jaw_Ctrl), Color2)
    cmds.xform(Jaw_Ctrl, translation=Jnt_Jaw_tuple)
    cmds.parent(Jaw_Ctrl, Jaw_Ctrl_grp)
    mel.eval("""
    select -r Jaw_Ctrl ;
    setAttr "Jaw_Ctrl.translateZ" 1 ;
    FreezeTransformations;
            """) 
    cmds.parent(Jaw_grp, Face_Grp)
    cmds.matchTransform(Jaw_grp, Jnt_Jaw, rot=True)
    mel.eval("""
    select -r Jaw_Ctrl ;
    select -tgl Jaw_Jnt ;
    MatchPivots;
             """)

    TG1_Grp = cmds.group(n="TG1_Grp", empty=True)
    cmds.xform(TG1_Grp, translation=Jnt_TG1_tuple)
    Tongue1_Ctrl_grp = cmds.group(n="Tongue1_Ctrl_grp", empty=True)
    cmds.xform(TG1_Grp, translation=Jnt_TG1_tuple)
    cmds.parent(Tongue1_Ctrl_grp, TG1_Grp)
    mel.eval("""
    select -r Tongue1_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(Tongue1_Ctrl_grp)
    Tongue1_Ctrl = cmds.curve(name ="Tongue1_Ctrl", degree = 1, p=[
        (0, 0, 0),(0, 0.36, 0),(0.08, 0.37, 0),(0.15, 0.4, 0),(0.21, 0.44, 0),(0.26, 0.5, 0),
        (0.28, 0.57, 0),(0.3, 0.65, 0),(0, 0.65, 0),(0, 0.36, 0),(-0.08, 0.37, 0),
        (-0.15, 0.4, 0),(-0.21, 0.44, 0),(-0.26, 0.5, 0),(-0.28, 0.57, 0),(-0.3, 0.65, 0),
        (-0.28, 0.73, 0),(-0.26, 0.8, 0),(-0.21, 0.86, 0),(-0.15, 0.91, 0),(-0.08, 0.94, 0),
        (0, 0.95, 0),(0.08, 0.94, 0),(0.15, 0.91, 0),(0.21, 0.86, 0),(0.26, 0.8, 0),
        (0.28, 0.73, 0),(0.3, 0.65, 0),(-0.3, 0.65, 0),(0, 0.65, 0),(0, 0.95, 0)])
    cmds.scale(0.3,0.3,0.3)
    cmds.listRelatives(Tongue1_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Tongue1_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(Tongue1_Ctrl), Color2)
    cmds.xform(Tongue1_Ctrl, translation=Jnt_TG1_tuple)
    cmds.parent(Tongue1_Ctrl, Tongue1_Ctrl_grp)
    mel.eval("""
    select -r Tongue1_Ctrl ;
    FreezeTransformations;
            """) 
    cmds.parent(TG1_Grp, Face_Grp)
    cmds.matchTransform(TG1_Grp, Jnt_TG1, rot=True)


    TG2_Grp = cmds.group(n="TG2_Grp", empty=True)
    cmds.xform(TG2_Grp, translation=Jnt_TG2_tuple)
    Tongue2_Ctrl_grp = cmds.group(n="Tongue2_Ctrl_grp", empty=True)
    cmds.xform(TG2_Grp, translation=Jnt_TG2_tuple)
    cmds.parent(Tongue2_Ctrl_grp, TG2_Grp)
    mel.eval("""
    select -r Tongue2_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(Tongue2_Ctrl_grp)
    Tongue2_Ctrl = cmds.curve(name ="Tongue2_Ctrl", degree = 1, p=[
        (0, 0, 0),(0, 0.36, 0),(0.08, 0.37, 0),(0.15, 0.4, 0),(0.21, 0.44, 0),(0.26, 0.5, 0),
        (0.28, 0.57, 0),(0.3, 0.65, 0),(0, 0.65, 0),(0, 0.36, 0),(-0.08, 0.37, 0),
        (-0.15, 0.4, 0),(-0.21, 0.44, 0),(-0.26, 0.5, 0),(-0.28, 0.57, 0),(-0.3, 0.65, 0),
        (-0.28, 0.73, 0),(-0.26, 0.8, 0),(-0.21, 0.86, 0),(-0.15, 0.91, 0),(-0.08, 0.94, 0),
        (0, 0.95, 0),(0.08, 0.94, 0),(0.15, 0.91, 0),(0.21, 0.86, 0),(0.26, 0.8, 0),
        (0.28, 0.73, 0),(0.3, 0.65, 0),(-0.3, 0.65, 0),(0, 0.65, 0),(0, 0.95, 0)])
    cmds.scale(0.3,0.3,0.3)
    cmds.listRelatives(Tongue2_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Tongue2_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(Tongue2_Ctrl), Color2)
    cmds.xform(Tongue2_Ctrl, translation=Jnt_TG2_tuple)
    cmds.parent(Tongue2_Ctrl, Tongue2_Ctrl_grp)
    mel.eval("""
    select -r Tongue2_Ctrl ;
    FreezeTransformations;
            """) 
    cmds.parent(TG2_Grp, Tongue1_Ctrl)
    cmds.matchTransform(TG2_Grp, Jnt_TG2, rot=True)

    TG3_Grp = cmds.group(n="TG3_Grp", empty=True)
    cmds.xform(TG3_Grp, translation=Jnt_TG3_tuple)
    Tongue3_Ctrl_grp = cmds.group(n="Tongue3_Ctrl_grp", empty=True)
    cmds.xform(TG3_Grp, translation=Jnt_TG3_tuple)
    cmds.parent(Tongue3_Ctrl_grp, TG3_Grp)
    mel.eval("""
    select -r Tongue3_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(Tongue3_Ctrl_grp)
    Tongue3_Ctrl = cmds.curve(name ="Tongue3_Ctrl", degree = 1, p=[
        (0, 0, 0),(0, 0.36, 0),(0.08, 0.37, 0),(0.15, 0.4, 0),(0.21, 0.44, 0),(0.26, 0.5, 0),
        (0.28, 0.57, 0),(0.3, 0.65, 0),(0, 0.65, 0),(0, 0.36, 0),(-0.08, 0.37, 0),
        (-0.15, 0.4, 0),(-0.21, 0.44, 0),(-0.26, 0.5, 0),(-0.28, 0.57, 0),(-0.3, 0.65, 0),
        (-0.28, 0.73, 0),(-0.26, 0.8, 0),(-0.21, 0.86, 0),(-0.15, 0.91, 0),(-0.08, 0.94, 0),
        (0, 0.95, 0),(0.08, 0.94, 0),(0.15, 0.91, 0),(0.21, 0.86, 0),(0.26, 0.8, 0),
        (0.28, 0.73, 0),(0.3, 0.65, 0),(-0.3, 0.65, 0),(0, 0.65, 0),(0, 0.95, 0)])
    cmds.scale(0.3,0.3,0.3)
    cmds.listRelatives(Tongue3_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Tongue3_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(Tongue3_Ctrl), Color2)
    cmds.xform(Tongue3_Ctrl, translation=Jnt_TG3_tuple)
    cmds.parent(Tongue3_Ctrl, Tongue3_Ctrl_grp)
    mel.eval("""
    select -r Tongue3_Ctrl ;
    FreezeTransformations;
            """) 
    cmds.parent(TG3_Grp, Tongue2_Ctrl)
    cmds.matchTransform(TG3_Grp, Jnt_TG3, rot=True)


    TG4_Grp = cmds.group(n="TG4_Grp", empty=True)
    cmds.xform(TG4_Grp, translation=Jnt_TG4_tuple)
    Tongue4_Ctrl_grp = cmds.group(n="Tongue4_Ctrl_grp", empty=True)
    cmds.xform(TG4_Grp, translation=Jnt_Jaw_tuple)
    cmds.parent(Tongue4_Ctrl_grp, TG4_Grp)
    mel.eval("""
    select -r Tongue4_Ctrl_grp ;
    FreezeTransformations;
    """)
    cmds.CenterPivot(Tongue4_Ctrl_grp)
    Tongue4_Ctrl = cmds.curve(name ="Tongue4_Ctrl", degree = 1, p=[
        (0, 0, 0),(0, 0.36, 0),(0.08, 0.37, 0),(0.15, 0.4, 0),(0.21, 0.44, 0),(0.26, 0.5, 0),
        (0.28, 0.57, 0),(0.3, 0.65, 0),(0, 0.65, 0),(0, 0.36, 0),(-0.08, 0.37, 0),
        (-0.15, 0.4, 0),(-0.21, 0.44, 0),(-0.26, 0.5, 0),(-0.28, 0.57, 0),(-0.3, 0.65, 0),
        (-0.28, 0.73, 0),(-0.26, 0.8, 0),(-0.21, 0.86, 0),(-0.15, 0.91, 0),(-0.08, 0.94, 0),
        (0, 0.95, 0),(0.08, 0.94, 0),(0.15, 0.91, 0),(0.21, 0.86, 0),(0.26, 0.8, 0),
        (0.28, 0.73, 0),(0.3, 0.65, 0),(-0.3, 0.65, 0),(0, 0.65, 0),(0, 0.95, 0)])
    cmds.scale(0.3,0.3,0.3)
    cmds.listRelatives(Tongue4_Ctrl, shapes=True)
    cmds.setAttr("{0}.overrideEnabled".format(Tongue4_Ctrl), True)
    cmds.setAttr("{0}.overrideColor".format(Tongue4_Ctrl), Color2)
    cmds.xform(Tongue4_Ctrl, translation=Jnt_TG4_tuple)
    cmds.parent(Tongue4_Ctrl, Tongue4_Ctrl_grp)
    mel.eval("""
    select -r Tongue4_Ctrl ;
    FreezeTransformations;
            """) 
    cmds.parent(TG4_Grp, Tongue3_Ctrl)
    cmds.matchTransform(TG4_Grp, Jnt_TG4, rot=True)

    ############################################### set parent Mouth Ctrl
    mel.eval("""
    select -r Mid_Down_Lip_Ctrl ;
    select -tgl Neck|Mid_Up_Lip|Mid_Down_Lip ;
    parentConstraint -mo -weight 1;
             
    select -r Mid_Up_Lip_Ctrl ;
    select -tgl Neck|Mid_Up_Lip ;
    parentConstraint -mo -weight 1;
             
    select -r BW1_Ctrl_R ;
    select -tgl R_Between_1 ;
    parentConstraint -mo -weight 1;
             
    select -r BW2_Ctrl_R ;
    select -tgl R_Between_2 ;
    parentConstraint -mo -weight 1;
    
    select -r RCL_Ctrl_R ;
    select -tgl R_Corner_Lip ;
    parentConstraint -mo -weight 1;
             
    select -r BW3_Ctrl_R ;
    select -tgl R_Between_3 ;
    parentConstraint -mo -weight 1;
             
    select -r BW4_Ctrl_R ;
    select -tgl R_Between_4 ;
    parentConstraint -mo -weight 1;
             
    select -r BW1_Ctrl_L ;
    select -tgl L_Between_1 ;
    parentConstraint -mo -weight 1;
             
    select -r BW2_Ctrl_L ;
    select -tgl L_Between_2 ;
    parentConstraint -mo -weight 1;
             
    select -r LCL_Ctrl_L ;
    select -tgl L_Corner_Lip ;
    parentConstraint -mo -weight 1;
             
    select -r BW3_Ctrl_L ;
    select -tgl L_Between_3 ;
    parentConstraint -mo -weight 1;
        
    select -r BW4_Ctrl_L ;
    select -tgl L_Between_4 ;
    parentConstraint -mo -weight 1;
             """)
    
    ################################################################ set driven key mouth
    ###################### mouth translation #####################
    mel.eval("""
    setAttr "Mouth.translateZ" 0;
    setAttr "BW6_Ctrl_grp.translateY" 0;
    setAttr "MUL_Ctrl_grp.translateY" 0;
    setAttr "BW1_Ctrl_grp.translateY" 0;
    setAttr "BW2_Ctrl_grp.translateY" 0;
    setAttr "BW5_Ctrl_grp.translateY" 0;
    setAttr "LCL_Ctrl_grp.translateY" 0;
    setAttr "RCL_Ctrl_grp.translateY" 0;
    setAttr "BW7_Ctrl_grp.translateY" 0;
    setAttr "BW3_Ctrl_grp.translateY" 0;
    setAttr "BW8_Ctrl_grp.translateY" 0;
    setAttr "BW4_Ctrl_grp.translateY" 0;
    setAttr "MDL_Ctrl_grp.translateY" 0;
    setDrivenKeyframe -currentDriver Mouth.translateZ LCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW8_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW7_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW6_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW5_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ MDL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW4_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW3_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ RCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW2_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW1_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ MUL_Ctrl_grp.translateY;
                                
    setAttr "Mouth.translateZ" 2;
    setAttr "BW6_Ctrl_grp.translateY" -0.1;
    setAttr "MUL_Ctrl_grp.translateY" 0.1;
    setAttr "BW1_Ctrl_grp.translateY" 0.1;
    setAttr "BW2_Ctrl_grp.translateY" -0.1;
    setAttr "BW5_Ctrl_grp.translateY" 0.1;
    setAttr "LCL_Ctrl_grp.translateY" -0.5;
    setAttr "RCL_Ctrl_grp.translateY" -0.5;
    setAttr "BW3_Ctrl_grp.translateY" -1;
    setAttr "BW7_Ctrl_grp.translateY" -1;
    setAttr "BW4_Ctrl_grp.translateY" -1.25;
    setAttr "BW8_Ctrl_grp.translateY" -1.25;
    setAttr "MDL_Ctrl_grp.translateY" -1.3;
    setDrivenKeyframe -currentDriver Mouth.translateZ LCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW8_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW7_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW6_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW5_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ MDL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW4_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW3_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ RCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW2_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ BW1_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.translateZ MUL_Ctrl_grp.translateY;

    setAttr "Mouth.translateX" 0;
    setAttr "MUL_Ctrl_grp.translateX" 0;
    setAttr "LCL_Ctrl_grp.translateX" 0;
    setAttr "BW8_Ctrl_grp.translateX" 0;
    setAttr "BW7_Ctrl_grp.translateX" 0;
    setAttr "BW6_Ctrl_grp.translateX" 0;
    setAttr "BW5_Ctrl_grp.translateX" 0;
    setAttr "MDL_Ctrl_grp.translateX" 0;
    setAttr "BW4_Ctrl_grp.translateX" 0;
    setAttr "BW3_Ctrl_grp.translateX" 0;
    setAttr "RCL_Ctrl_grp.translateX" 0;
    setAttr "BW2_Ctrl_grp.translateX" 0;
    setAttr "BW1_Ctrl_grp.translateX" 0;
    setDrivenKeyframe -currentDriver Mouth.translateX LCL_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW8_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW7_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW6_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW5_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX MDL_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW4_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW3_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX RCL_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW2_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW1_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX MUL_Ctrl_grp.translateX;

    setAttr "Mouth.translateX" 1;
    setAttr "BW5_Ctrl_grp.translateX" 0.2;
    setAttr "BW8_Ctrl_grp.translateX" 0.2;
    setAttr "BW6_Ctrl_grp.translateX" 0.4;
    setAttr "BW7_Ctrl_grp.translateX" 0.4;
    setAttr "LCL_Ctrl_grp.translateX" 0.6;
    setAttr "BW1_Ctrl_grp.translateX" -0.2;
    setAttr "BW4_Ctrl_grp.translateX" -0.2;
    setAttr "RCL_Ctrl_grp.translateX" -0.2;
    setAttr "BW2_Ctrl_grp.translateX" -0.4;
    setAttr "BW3_Ctrl_grp.translateX" -0.4;
    setAttr "RCL_Ctrl_grp.translateX" -0.6;
    setDrivenKeyframe -currentDriver Mouth.translateX LCL_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW8_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW7_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW6_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW5_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX MDL_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW4_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW3_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX RCL_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW2_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW1_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX MUL_Ctrl_grp.translateX;
                
    setAttr "Mouth.translateX" -1;
    setAttr "BW5_Ctrl_grp.translateX" -0.3;
    setAttr "BW8_Ctrl_grp.translateX" -0.3;
    setAttr "BW6_Ctrl_grp.translateX" -0.6;
    setAttr "BW7_Ctrl_grp.translateX" -0.6;
    setAttr "LCL_Ctrl_grp.translateX" -0.9;
    setAttr "BW1_Ctrl_grp.translateX" 0.3;
    setAttr "BW4_Ctrl_grp.translateX" 0.3;
    setAttr "BW2_Ctrl_grp.translateX" 0.6;
    setAttr "BW3_Ctrl_grp.translateX" 0.6;
    setAttr "RCL_Ctrl_grp.translateX" 0.9;
    setDrivenKeyframe -currentDriver Mouth.translateX LCL_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW8_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW7_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW6_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW5_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX MDL_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW4_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW3_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX RCL_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW2_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX BW1_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Mouth.translateX MUL_Ctrl_grp.translateX;

    selectKey -clear ;
    selectKey -add -k -f 0 -f 2 LCL_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 BW8_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 BW7_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 BW6_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 BW5_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 MDL_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 BW4_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 BW3_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 RCL_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 BW2_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 BW1_Ctrl_grp_translateY ;
    selectKey -add -k -f 0 -f 2 MUL_Ctrl_grp_translateY ;
    selectKey -add -k LCL_Ctrl_grp_translateX BW8_Ctrl_grp_translateX BW7_Ctrl_grp_translateX BW6_Ctrl_grp_translateX BW5_Ctrl_grp_translateX MDL_Ctrl_grp_translateX BW4_Ctrl_grp_translateX BW3_Ctrl_grp_translateX RCL_Ctrl_grp_translateX BW2_Ctrl_grp_translateX BW1_Ctrl_grp_translateX MUL_Ctrl_grp_translateX ;
    keyTangent -itt linear -ott linear;             

    setAttr "Mouth.translateZ" 0;
    setAttr "Mouth.translateX" 0;
             
    """)

    ######################## mouth reaction #########################
    mel.eval("""
    //---------------------------------------------------------------- happy             
    setAttr "Mouth.Happy" 0;
    setAttr "BW5_Ctrl_grp.translateY" 0;
    setAttr "BW8_Ctrl_grp.translateY" 0;
    setAttr "BW6_Ctrl_grp.translateY" 0;
    setAttr "BW7_Ctrl_grp.translateY" 0;
    setAttr "LCL_Ctrl_grp.translateY" 0;
    setAttr "BW4_Ctrl_grp.translateY" 0;
    setAttr "BW1_Ctrl_grp.translateY" 0;
    setAttr "BW2_Ctrl_grp.translateY" 0;
    setAttr "BW3_Ctrl_grp.translateY" 0;
    setAttr "RCL_Ctrl_grp.translateY" 0;             
    setDrivenKeyframe -currentDriver Mouth.Happy LCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW8_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW7_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW6_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW5_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy MDL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW4_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW3_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy RCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW2_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW1_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy MUL_Ctrl_grp.translateY;
                
    setAttr "Mouth.Happy" 10;
    setAttr "BW5_Ctrl_grp.translateY" 0.2;
    setAttr "BW8_Ctrl_grp.translateY" 0.2;
    setAttr "BW6_Ctrl_grp.translateY" 0.4;
    setAttr "BW7_Ctrl_grp.translateY" 0.4;
    setAttr "LCL_Ctrl_grp.translateY" 0.5;
    setAttr "BW4_Ctrl_grp.translateY" 0.2;
    setAttr "BW1_Ctrl_grp.translateY" 0.2;
    setAttr "BW2_Ctrl_grp.translateY" 0.4;
    setAttr "BW3_Ctrl_grp.translateY" 0.4;
    setAttr "RCL_Ctrl_grp.translateY" 0.5;
    setDrivenKeyframe -currentDriver Mouth.Happy LCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW8_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW7_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW6_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW5_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy MDL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW4_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW3_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy RCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW2_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy BW1_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Happy MUL_Ctrl_grp.translateY;

    //---------------------------------------------------------------- sad
    setAttr "Mouth.Sad" 0;
    setAttr "MUL_Ctrl_grp.translateY" 0;
    setAttr "LCL_Ctrl_grp.translateY" 0;
    setAttr "BW8_Ctrl_grp.translateY" 0;
    setAttr "BW7_Ctrl_grp.translateY" 0;
    setAttr "BW6_Ctrl_grp.translateY" 0;
    setAttr "BW5_Ctrl_grp.translateY" 0;
    setAttr "MDL_Ctrl_grp.translateY" 0;
    setAttr "BW4_Ctrl_grp.translateY" 0;
    setAttr "BW3_Ctrl_grp.translateY" 0;
    setAttr "RCL_Ctrl_grp.translateY" 0;
    setAttr "BW2_Ctrl_grp.translateY" 0;
    setAttr "BW1_Ctrl_grp.translateY" 0;
    setDrivenKeyframe -currentDriver Mouth.Sad LCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW8_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW7_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW6_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW5_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad MDL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW4_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW3_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad RCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW2_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW1_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad MUL_Ctrl_grp.translateY;

    setAttr "Mouth.Sad" 10;
    setAttr "BW5_Ctrl_grp.translateY" -0.2;
    setAttr "BW8_Ctrl_grp.translateY" -0.2;
    setAttr "BW6_Ctrl_grp.translateY" -0.4;
    setAttr "BW7_Ctrl_grp.translateY" -0.4;
    setAttr "LCL_Ctrl_grp.translateY" -0.5;
    setAttr "BW4_Ctrl_grp.translateY" -0.2;
    setAttr "BW1_Ctrl_grp.translateY" -0.2;
    setAttr "BW2_Ctrl_grp.translateY" -0.4;
    setAttr "BW3_Ctrl_grp.translateY" -0.4;
    setAttr "RCL_Ctrl_grp.translateY" -0.5;
    setDrivenKeyframe -currentDriver Mouth.Sad LCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW8_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW7_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW6_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW5_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad MDL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW4_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW3_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad RCL_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW2_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad BW1_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Mouth.Sad MUL_Ctrl_grp.translateY;
    setAttr "Mouth.Happy" 0;
    setAttr "Mouth.Sad" 0;       
    """)


    ######################## parent brow #########################
    mel.eval("""
    select -r RIB_Ctrl_R ;
    select -tgl R_InnerBrow ;
    parentConstraint -mo -weight 1;
             
    select -r ROB_Ctrl_R ;
    select -tgl R_OuterBrow ;
    parentConstraint -mo -weight 1;
             
    select -r LIB_Ctrl_L ;
    select -tgl L_InnerBrow ;
    parentConstraint -mo -weight 1;
             
    select -r LOB_Ctrl_L ;
    select -tgl L_OuterBrow ;
    parentConstraint -mo -weight 1;
             
    """)

    ################### tongue parent #####################
    mel.eval("""
    select -r Tongue1_Ctrl ;
    select -tgl Tongue1_jnt ;
    parentConstraint -mo -weight 1;

    select -r Tongue2_Ctrl ;
    select -tgl Tongue2_jnt ;
    parentConstraint -mo -weight 1;

    select -r Tongue3_Ctrl ;
    select -tgl Tongue3_jnt ;
    parentConstraint -mo -weight 1;

    select -r Tongue4_Ctrl ;
    select -tgl Tongue4_jnt ;
    parentConstraint -mo -weight 1;
    """)

    ######################## brow set driven key ######################
    mel.eval("""
    setAttr "Bow_Ctrl_R.translateZ" 0;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateZ RIB_Grp.translateY;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateZ ROB_Grp.translateY;
    setAttr "Bow_Ctrl_R.translateZ" 1;
    setAttr "ROB_Grp.translateY" -0.3;
    setAttr "RIB_Grp.translateY" -0.3;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateZ RIB_Grp.translateY;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateZ ROB_Grp.translateY;
    setAttr "Bow_Ctrl_R.translateZ" -1;
    setAttr "ROB_Grp.translateY" 0.3;
    setAttr "RIB_Grp.translateY" 0.3;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateZ RIB_Grp.translateY;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateZ ROB_Grp.translateY;
    setAttr "Bow_Ctrl_R.translateZ" 0;

    setAttr "Bow_Ctrl_R.translateX" 0;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateX RIB_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateX RIB_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateX RIB_Ctrl_grp.translateZ;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateX RIB_Ctrl_grp.rotateX;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateX RIB_Ctrl_grp.rotateY;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateX RIB_Ctrl_grp.rotateZ;
    setAttr "Bow_Ctrl_R.translateX" 1;
    setAttr "RIB_Ctrl_grp.translateY" 0.3;
    setAttr "RIB_Ctrl_grp.rotateZ" 11;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateX RIB_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateX RIB_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateX RIB_Ctrl_grp.translateZ;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateX RIB_Ctrl_grp.rotateX;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateX RIB_Ctrl_grp.rotateY;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateX RIB_Ctrl_grp.rotateZ;
    setAttr "Bow_Ctrl_R.translateX" -1;
    setAttr "RIB_Ctrl_grp.translateY" -0.3;
    setAttr "RIB_Ctrl_grp.rotateZ" -11;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateX RIB_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateX RIB_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateX RIB_Ctrl_grp.translateZ;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateX RIB_Ctrl_grp.rotateX;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateX RIB_Ctrl_grp.rotateY;
    setDrivenKeyframe -currentDriver Bow_Ctrl_R.translateX RIB_Ctrl_grp.rotateZ;
    setAttr "Bow_Ctrl_R.translateX" 0;

                

    setAttr "Bow_Ctrl_L.translateZ" 0;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateZ LIB_Grp.translateY;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateZ LOB_Grp.translateY;
    setAttr "Bow_Ctrl_L.translateZ" 1;
    setAttr "LOB_Grp.translateY" -0.3;
    setAttr "LIB_Grp.translateY" -0.3;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateZ LIB_Grp.translateY;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateZ LOB_Grp.translateY;
    setAttr "Bow_Ctrl_L.translateZ" -1;
    setAttr "LOB_Grp.translateY" 0.3;
    setAttr "LIB_Grp.translateY" 0.3;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateZ LIB_Grp.translateY;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateZ LOB_Grp.translateY;
    setAttr "Bow_Ctrl_L.translateZ" 0;

    setAttr "Bow_Ctrl_L.translateX" 0;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateX LIB_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateX LIB_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateX LIB_Ctrl_grp.translateZ;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateX LIB_Ctrl_grp.rotateX;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateX LIB_Ctrl_grp.rotateY;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateX LIB_Ctrl_grp.rotateZ;
    setAttr "Bow_Ctrl_L.translateX" 1;
    setAttr "LIB_Ctrl_grp.translateY" 0.3;
    setAttr "LIB_Ctrl_grp.rotateZ" -11;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateX LIB_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateX LIB_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateX LIB_Ctrl_grp.translateZ;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateX LIB_Ctrl_grp.rotateX;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateX LIB_Ctrl_grp.rotateY;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateX LIB_Ctrl_grp.rotateZ;
    setAttr "Bow_Ctrl_L.translateX" -1;
    setAttr "LIB_Ctrl_grp.translateY" -0.3;
    setAttr "LIB_Ctrl_grp.rotateZ" 11;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateX LIB_Ctrl_grp.translateX;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateX LIB_Ctrl_grp.translateY;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateX LIB_Ctrl_grp.translateZ;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateX LIB_Ctrl_grp.rotateX;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateX LIB_Ctrl_grp.rotateY;
    setDrivenKeyframe -currentDriver Bow_Ctrl_L.translateX LIB_Ctrl_grp.rotateZ;
    setAttr "Bow_Ctrl_L.translateX" 0;
             
    selectKey -clear ;
    selectKey -add -k LOB_Grp_translateY LIB_Ctrl_grp_translateX LIB_Ctrl_grp_translateY LIB_Ctrl_grp_translateZ LIB_Ctrl_grp_rotateX LIB_Ctrl_grp_rotateY LIB_Ctrl_grp_rotateZ LIB_Grp_translateY ROB_Grp_translateY RIB_Ctrl_grp_translateX RIB_Ctrl_grp_translateY RIB_Ctrl_grp_translateZ RIB_Ctrl_grp_rotateX RIB_Ctrl_grp_rotateY RIB_Ctrl_grp_rotateZ RIB_Grp_translateY ;
    keyTangent -itt linear -ott linear;             

          
    select -r R_OuterBrow_parentConstraint1 ;
    select -add R_InnerBrow_parentConstraint1 ;
    select -add L_OuterBrow_parentConstraint1 ;
    select -add L_InnerBrow_parentConstraint1 ;
    select -add R_Between_4_parentConstraint1 ;
    select -add R_Between_3_parentConstraint1 ;
    select -add R_Corner_Lip_parentConstraint1 ;
    select -add R_Between_2_parentConstraint1 ;
    select -add R_Between_1_parentConstraint1 ;
    select -add Mid_Down_Lip_parentConstraint1 ;
    select -add L_Between_4_parentConstraint1 ;
    select -add L_Between_3_parentConstraint1 ;
    select -add L_Corner_Lip_parentConstraint1 ;
    select -add L_Between_2_parentConstraint1 ;
    select -add L_Between_1_parentConstraint1 ;
    select -add Mid_Up_Lip_parentConstraint1 ;
    select -add Constraint_Grp ;
    parent; 
    //setAttr "Skeleton.visibility" 0; 
    select -r pPlane1 ;    
    setAttr "pPlane1.visibility" 0;                                                    
    """)
    ########################################################
    ######################################################## jaw setup

    #################### jaw set driven key #################
    mel.eval("""
    select -r Jaw_Ctrl ;
    select -tgl Jaw_Jnt ;
    parentConstraint -mo -weight 1;
             
    setAttr "Mouth.translateZ" 0;
    setAttr "Jaw_Ctrl_grp.rotateX" 0;
    setDrivenKeyframe -currentDriver Mouth.translateZ Jaw_Ctrl_grp.rotateX;

    setAttr "Mouth.translateZ" 2;
    setAttr "Jaw_Ctrl_grp.rotateX" 70;
    setDrivenKeyframe -currentDriver Mouth.translateZ Jaw_Ctrl_grp.rotateX;
    setAttr "Mouth.translateZ" 0;

    selectKey -add -k -f 0 -f 2 Jaw_Ctrl_grp_rotateX ;
    keyTangent -itt linear -ott linear;

    """)

    mel.eval("""
    select -r Jaw_Jnt_parentConstraint1 ;
    select -add Tongue4_jnt_parentConstraint1 ;
    select -add Tongue3_jnt_parentConstraint1 ;
    select -add Tongue2_jnt_parentConstraint1 ;
    select -add Tongue1_jnt_parentConstraint1 ;
    select -add Constraint_Grp ;
    parent;
             """)

    mel.eval("""    
    select -cl ;
             """)  



def fixBuildBody(*arg):
    cmds.parent(joint_Root, world=True)
    cmds.parent(joint_RHand, world=True)
    cmds.delete("IK_L_Hip")
    cmds.delete("FK_L_Hip")
    cmds.delete("IK_R_Hip")
    cmds.delete("FK_R_Hip")
    cmds.delete("IK_R_Shoulder")
    cmds.delete("FK_R_Shoulder")
    cmds.delete(joint_LHip)
    cmds.delete(joint_LScapula)
    cmds.delete(joint_LHand)
    cmds.delete("Basic_Rig_Tri3D")



def fixBuildFace(*arg):
    mel.eval("""
             
    select -r Main_Face_Grp_dont_FreezeTransformations R_Eye_Grp L_Eye_Grp Face_Ctrl_Grp ;
    doDelete;         

    select -r R_OuterBrow ;
    select -tgl Neck ;
    parent;                 
    """)
    cmds.parent(Jnt_MUL, world=True)
    cmds.delete(Jnt_LIB)
    cmds.delete(Jnt_BW5)




   

    
    # //---------------------------------------------------------------- set driven key finger
    # setAttr "R_IKFK_Hand_Ctrl.Thump" 0;
    # setAttr "R_ThumbFinger3_Ctrl_Grp.rotateY" 0;
    # setAttr "R_ThumbFinger1_Ctrl_Grp.rotateY" 0;
    # setAttr "R_ThumbFinger2_Ctrl_Grp.rotateY" 0;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Thump R_ThumbFinger1_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Thump R_ThumbFinger2_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Thump R_ThumbFinger3_Ctrl_Grp.rotateY;

    # setAttr "R_IKFK_Hand_Ctrl.Thump" -2;
    # setAttr "R_ThumbFinger3_Ctrl_Grp.rotateY" -15;
    # setAttr "R_ThumbFinger1_Ctrl_Grp.rotateY" -15;
    # setAttr "R_ThumbFinger2_Ctrl_Grp.rotateY" -15;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Thump R_ThumbFinger1_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Thump R_ThumbFinger2_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Thump R_ThumbFinger3_Ctrl_Grp.rotateY;
                          
    # setAttr "R_IKFK_Hand_Ctrl.Thump" 10;
    # setAttr "R_ThumbFinger3_Ctrl_Grp.rotateY" 50;
    # setAttr "R_ThumbFinger1_Ctrl_Grp.rotateY" 50;
    # setAttr "R_ThumbFinger2_Ctrl_Grp.rotateY" 50;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Thump R_ThumbFinger1_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Thump R_ThumbFinger2_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Thump R_ThumbFinger3_Ctrl_Grp.rotateY;

    # setAttr "R_IKFK_Hand_Ctrl.Thump" 0;
             
    # setAttr "R_IKFK_Hand_Ctrl.Index" 0;
    # setAttr "R_IndexFinger3_Ctrl_Grp.rotateY" 0;
    # setAttr "R_IndexFinger1_Ctrl_Grp.rotateY" 0;
    # setAttr "R_IndexFinger2_Ctrl_Grp.rotateY" 0;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Index R_IndexFinger1_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Index R_IndexFinger2_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Index R_IndexFinger3_Ctrl_Grp.rotateY;

    # setAttr "R_IKFK_Hand_Ctrl.Index" -2;
    # setAttr "R_IndexFinger3_Ctrl_Grp.rotateY" -15;
    # setAttr "R_IndexFinger1_Ctrl_Grp.rotateY" -15;
    # setAttr "R_IndexFinger2_Ctrl_Grp.rotateY" -15;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Index R_IndexFinger1_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Index R_IndexFinger2_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Index R_IndexFinger3_Ctrl_Grp.rotateY;             

    # setAttr "R_IKFK_Hand_Ctrl.Index" 10;
    # setAttr "R_IndexFinger3_Ctrl_Grp.rotateY" 70;
    # setAttr "R_IndexFinger1_Ctrl_Grp.rotateY" 70;
    # setAttr "R_IndexFinger2_Ctrl_Grp.rotateY" 70;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Index R_IndexFinger1_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Index R_IndexFinger2_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Index R_IndexFinger3_Ctrl_Grp.rotateY;

    # setAttr "R_IKFK_Hand_Ctrl.Index" 0;

    # setAttr "R_IKFK_Hand_Ctrl.Middle" 0;
    # setAttr "R_MiddleFinger3_Ctrl_Grp.rotateY" 0;
    # setAttr "R_MiddleFinger1_Ctrl_Grp.rotateY" 0;
    # setAttr "R_MiddleFinger2_Ctrl_Grp.rotateY" 0;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Middle R_MiddleFinger1_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Middle R_MiddleFinger2_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Middle R_MiddleFinger3_Ctrl_Grp.rotateY;

    # setAttr "R_IKFK_Hand_Ctrl.Middle" -2;
    # setAttr "R_MiddleFinger3_Ctrl_Grp.rotateY" -15;
    # setAttr "R_MiddleFinger1_Ctrl_Grp.rotateY" -15;
    # setAttr "R_MiddleFinger2_Ctrl_Grp.rotateY" -15;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Middle R_MiddleFinger1_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Middle R_MiddleFinger2_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Middle R_MiddleFinger3_Ctrl_Grp.rotateY;              

    # setAttr "R_IKFK_Hand_Ctrl.Middle" 10;
    # setAttr "R_MiddleFinger3_Ctrl_Grp.rotateY" 70;
    # setAttr "R_MiddleFinger1_Ctrl_Grp.rotateY" 70;
    # setAttr "R_MiddleFinger2_Ctrl_Grp.rotateY" 70;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Middle R_MiddleFinger1_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Middle R_MiddleFinger2_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Middle R_MiddleFinger3_Ctrl_Grp.rotateY;

    # setAttr "R_IKFK_Hand_Ctrl.Middle" 0;

    # setAttr "R_IKFK_Hand_Ctrl.Ring" 0;
    # setAttr "R_RingFinger3_Ctrl_Grp.rotateY" 0;
    # setAttr "R_RingFinger1_Ctrl_Grp.rotateY" 0;
    # setAttr "R_RingFinger2_Ctrl_Grp.rotateY" 0;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Ring R_RingFinger1_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Ring R_RingFinger2_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Ring R_RingFinger3_Ctrl_Grp.rotateY;

    # setAttr "R_IKFK_Hand_Ctrl.Ring" -2;
    # setAttr "R_RingFinger3_Ctrl_Grp.rotateY" -15;
    # setAttr "R_RingFinger1_Ctrl_Grp.rotateY" -15;
    # setAttr "R_RingFinger2_Ctrl_Grp.rotateY" -15;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Ring R_RingFinger1_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Ring R_RingFinger2_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Ring R_RingFinger3_Ctrl_Grp.rotateY;               

    # setAttr "R_IKFK_Hand_Ctrl.Ring" 10;
    # setAttr "R_RingFinger3_Ctrl_Grp.rotateY" 70;
    # setAttr "R_RingFinger1_Ctrl_Grp.rotateY" 70;
    # setAttr "R_RingFinger2_Ctrl_Grp.rotateY" 70;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Ring R_RingFinger1_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Ring R_RingFinger2_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Ring R_RingFinger3_Ctrl_Grp.rotateY;

    # setAttr "R_IKFK_Hand_Ctrl.Ring" 0;

    # setAttr "R_IKFK_Hand_Ctrl.Pinky" 0;
    # setAttr "R_PinkyFinger3_Ctrl_Grp.rotateY" 0;
    # setAttr "R_PinkyFinger1_Ctrl_Grp.rotateY" 0;
    # setAttr "R_PinkyFinger2_Ctrl_Grp.rotateY" 0;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Pinky R_PinkyFinger1_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Pinky R_PinkyFinger2_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Pinky R_PinkyFinger3_Ctrl_Grp.rotateY;

    # setAttr "R_IKFK_Hand_Ctrl.Pinky" -2;
    # setAttr "R_PinkyFinger3_Ctrl_Grp.rotateY" -15;
    # setAttr "R_PinkyFinger1_Ctrl_Grp.rotateY" -15;
    # setAttr "R_PinkyFinger2_Ctrl_Grp.rotateY" -15;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Pinky R_PinkyFinger1_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Pinky R_PinkyFinger2_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Pinky R_PinkyFinger3_Ctrl_Grp.rotateY;               

    # setAttr "R_IKFK_Hand_Ctrl.Pinky" 10;
    # setAttr "R_PinkyFinger3_Ctrl_Grp.rotateY" 70;
    # setAttr "R_PinkyFinger1_Ctrl_Grp.rotateY" 70;
    # setAttr "R_PinkyFinger2_Ctrl_Grp.rotateY" 70;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Pinky R_PinkyFinger1_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Pinky R_PinkyFinger2_Ctrl_Grp.rotateY;
    # setDrivenKeyframe -currentDriver R_IKFK_Hand_Ctrl.Pinky R_PinkyFinger3_Ctrl_Grp.rotateY;

    # setAttr "R_IKFK_Hand_Ctrl.Pinky" 0;

    # //------ L_Finger
             
    # setAttr "L_IKFK_Hand_Ctrl.Thump" 0;
    # setAttr "L_ThumbFinger3_CtrL_Grp.rotateY" 0;
    # setAttr "L_ThumbFinger1_CtrL_Grp.rotateY" 0;
    # setAttr "L_ThumbFinger2_CtrL_Grp.rotateY" 0;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Thump L_ThumbFinger1_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Thump L_ThumbFinger2_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Thump L_ThumbFinger3_CtrL_Grp.rotateY;

    # setAttr "L_IKFK_Hand_Ctrl.Thump" -2;
    # setAttr "L_ThumbFinger3_CtrL_Grp.rotateY" -15;
    # setAttr "L_ThumbFinger1_CtrL_Grp.rotateY" -15;
    # setAttr "L_ThumbFinger2_CtrL_Grp.rotateY" -15;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Thump L_ThumbFinger1_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Thump L_ThumbFinger2_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Thump L_ThumbFinger3_CtrL_Grp.rotateY;
                          
    # setAttr "L_IKFK_Hand_Ctrl.Thump" 10;
    # setAttr "L_ThumbFinger3_CtrL_Grp.rotateY" 50;
    # setAttr "L_ThumbFinger1_CtrL_Grp.rotateY" 50;
    # setAttr "L_ThumbFinger2_CtrL_Grp.rotateY" 50;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Thump L_ThumbFinger1_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Thump L_ThumbFinger2_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Thump L_ThumbFinger3_CtrL_Grp.rotateY;

    # setAttr "L_IKFK_Hand_Ctrl.Thump" 0;
             
    # setAttr "L_IKFK_Hand_Ctrl.Index" 0;
    # setAttr "L_IndexFinger3_CtrL_Grp.rotateY" 0;
    # setAttr "L_IndexFinger1_CtrL_Grp.rotateY" 0;
    # setAttr "L_IndexFinger2_CtrL_Grp.rotateY" 0;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Index L_IndexFinger1_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Index L_IndexFinger2_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Index L_IndexFinger3_CtrL_Grp.rotateY;

    # setAttr "L_IKFK_Hand_Ctrl.Index" -2;
    # setAttr "L_IndexFinger3_CtrL_Grp.rotateY" -15;
    # setAttr "L_IndexFinger1_CtrL_Grp.rotateY" -15;
    # setAttr "L_IndexFinger2_CtrL_Grp.rotateY" -15;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Index L_IndexFinger1_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Index L_IndexFinger2_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Index L_IndexFinger3_CtrL_Grp.rotateY;             

    # setAttr "L_IKFK_Hand_Ctrl.Index" 10;
    # setAttr "L_IndexFinger3_CtrL_Grp.rotateY" 70;
    # setAttr "L_IndexFinger1_CtrL_Grp.rotateY" 70;
    # setAttr "L_IndexFinger2_CtrL_Grp.rotateY" 70;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Index L_IndexFinger1_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Index L_IndexFinger2_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Index L_IndexFinger3_CtrL_Grp.rotateY;

    # setAttr "L_IKFK_Hand_Ctrl.Index" 0;

    # setAttr "L_IKFK_Hand_Ctrl.Middle" 0;
    # setAttr "L_MiddleFinger3_CtrL_Grp.rotateY" 0;
    # setAttr "L_MiddleFinger1_CtrL_Grp.rotateY" 0;
    # setAttr "L_MiddleFinger2_CtrL_Grp.rotateY" 0;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Middle L_MiddleFinger1_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Middle L_MiddleFinger2_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Middle L_MiddleFinger3_CtrL_Grp.rotateY;

    # setAttr "L_IKFK_Hand_Ctrl.Middle" -2;
    # setAttr "L_MiddleFinger3_CtrL_Grp.rotateY" -15;
    # setAttr "L_MiddleFinger1_CtrL_Grp.rotateY" -15;
    # setAttr "L_MiddleFinger2_CtrL_Grp.rotateY" -15;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Middle L_MiddleFinger1_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Middle L_MiddleFinger2_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Middle L_MiddleFinger3_CtrL_Grp.rotateY;              

    # setAttr "L_IKFK_Hand_Ctrl.Middle" 10;
    # setAttr "L_MiddleFinger3_CtrL_Grp.rotateY" 70;
    # setAttr "L_MiddleFinger1_CtrL_Grp.rotateY" 70;
    # setAttr "L_MiddleFinger2_CtrL_Grp.rotateY" 70;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Middle L_MiddleFinger1_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Middle L_MiddleFinger2_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Middle L_MiddleFinger3_CtrL_Grp.rotateY;

    # setAttr "L_IKFK_Hand_Ctrl.Middle" 0;

    # setAttr "L_IKFK_Hand_Ctrl.Ring" 0;
    # setAttr "L_RingFinger3_CtrL_Grp.rotateY" 0;
    # setAttr "L_RingFinger1_CtrL_Grp.rotateY" 0;
    # setAttr "L_RingFinger2_CtrL_Grp.rotateY" 0;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Ring L_RingFinger1_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Ring L_RingFinger2_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Ring L_RingFinger3_CtrL_Grp.rotateY;

    # setAttr "L_IKFK_Hand_Ctrl.Ring" -2;
    # setAttr "L_RingFinger3_CtrL_Grp.rotateY" -15;
    # setAttr "L_RingFinger1_CtrL_Grp.rotateY" -15;
    # setAttr "L_RingFinger2_CtrL_Grp.rotateY" -15;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Ring L_RingFinger1_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Ring L_RingFinger2_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Ring L_RingFinger3_CtrL_Grp.rotateY;               

    # setAttr "L_IKFK_Hand_Ctrl.Ring" 10;
    # setAttr "L_RingFinger3_CtrL_Grp.rotateY" 70;
    # setAttr "L_RingFinger1_CtrL_Grp.rotateY" 70;
    # setAttr "L_RingFinger2_CtrL_Grp.rotateY" 70;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Ring L_RingFinger1_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Ring L_RingFinger2_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Ring L_RingFinger3_CtrL_Grp.rotateY;

    # setAttr "L_IKFK_Hand_Ctrl.Ring" 0;

    # setAttr "L_IKFK_Hand_Ctrl.Pinky" 0;
    # setAttr "L_PinkyFinger3_CtrL_Grp.rotateY" 0;
    # setAttr "L_PinkyFinger1_CtrL_Grp.rotateY" 0;
    # setAttr "L_PinkyFinger2_CtrL_Grp.rotateY" 0;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Pinky L_PinkyFinger1_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Pinky L_PinkyFinger2_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Pinky L_PinkyFinger3_CtrL_Grp.rotateY;

    # setAttr "L_IKFK_Hand_Ctrl.Pinky" -2;
    # setAttr "L_PinkyFinger3_CtrL_Grp.rotateY" -15;
    # setAttr "L_PinkyFinger1_CtrL_Grp.rotateY" -15;
    # setAttr "L_PinkyFinger2_CtrL_Grp.rotateY" -15;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Pinky L_PinkyFinger1_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Pinky L_PinkyFinger2_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Pinky L_PinkyFinger3_CtrL_Grp.rotateY;               

    # setAttr "L_IKFK_Hand_Ctrl.Pinky" 10;
    # setAttr "L_PinkyFinger3_CtrL_Grp.rotateY" 70;
    # setAttr "L_PinkyFinger1_CtrL_Grp.rotateY" 70;
    # setAttr "L_PinkyFinger2_CtrL_Grp.rotateY" 70;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Pinky L_PinkyFinger1_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Pinky L_PinkyFinger2_CtrL_Grp.rotateY;
    # setDrivenKeyframe -currentDriver L_IKFK_Hand_Ctrl.Pinky L_PinkyFinger3_CtrL_Grp.rotateY;

    # setAttr "L_IKFK_Hand_Ctrl.Pinky" 0;    