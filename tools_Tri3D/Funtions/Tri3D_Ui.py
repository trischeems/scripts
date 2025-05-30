############################################################################################################

###############################
###############################
                ###
                ###
                ###
                ###             #######################       ###          ##########        ##########
                ###             #######################       ###           #########        ###########
                ###             ###                 ###       ###                  ##        ##        ##
                ###             ###                 ###       ###                 ##         ##          ##
                ###             ###                 ###       ###            ########        ##          ##
                ###             ###                 ###       ###                   ##       ##         ##
                ###             ###                 ###       ###                  ##        ##        ##
                ###             ###                 ###       ###          ########          ##########

########### " Contacts with me : info.tri3d@gmail.com "
########### " Gumroad : https://phamtri.gumroad.com/"
########### " Copyright by Tri 3D "
########### " Thanks for you !!! "


import maya.cmds as cmds
import os
import pymel.core as pm


# link file funtions
import tools_Tri3D.Funtions.Tri3D_functions as func
reload(func)
import tools_Tri3D.Funtions.Animation.Tri3D_animation as anim
reload(anim)
import tools_Tri3D.Funtions.Animation.Tri3D_animationFuntions as Funcanim
reload(Funcanim)
import tools_Tri3D.Funtions.About.bank as bank
reload(bank)
import tools_Tri3D.Funtions.Rigging.Tri3D_rigFunctions as Rig
reload(Rig)
import tools_Tri3D.Funtions.Rigging.Tri3D_rigDetach as RigDetach
reload(RigDetach)
import tools_Tri3D.Funtions.Curve.CurveBasic as Cur
reload(Cur)
import tools_Tri3D.Funtions.Rigging.Tri3D_Test_AutoRig as autorig
reload(autorig)
import tools_Tri3D.Funtions.Rigging.Picker as picker
reload(picker)
import tools_Tri3D.Funtions.Curve.faceCtrl as faceCtrl
reload(faceCtrl)
import tools_Tri3D.Funtions.Rigging.Tri3D_rigHelp as helpRig
reload(helpRig)
import tools_Tri3D.Funtions.Rigging.Picker as pk
reload(pk)
import tools_Tri3D.Funtions.Rigging.Tri3D_rigFace as rf
reload(rf)
import tools_Tri3D.Funtions.Shader.Switch_Vraymtl as shd
reload(shd)
import tools_Tri3D.Funtions.Shader.TriVega_Switch_Vraymtl as sdr
reload(sdr)
import tools_Tri3D.Funtions.Shader.TriVega_tools_ae as ae
reload(ae)
import tools_Tri3D.Funtions.TriVega_Tools as tools
reload(tools)
import tools_Tri3D.Funtions.Rigging.Tri3D_IK_tools_Ui as rt
reload(rt)
import tools_Tri3D.Funtions.Model.Tri3D_moveObj as md
reload(md)
import tools_Tri3D.Funtions.Shader.Tri3D_Shader_Tools as Shader
reload(Shader)


IMAGE_PATH = os.path.join(os.path.dirname(__file__), "Icons")
IM_Path = os.path.join(os.path.dirname(__file__), "Icons")


################################################################ window functions
def createUI():
    if cmds.window("triWin", exists=True):
        cmds.deleteUI("triWin")


    triWin = cmds.window("triWin", title="tools_Tri3D Premium", sizeable=False, menuBar=True, resizeToFitChildren=True, w=310, h=500)
    # cmds.windowPref("triWin", remove=True, w=310)

    cmds.menu(l="Modify")
    cmds.menuItem(l="Freeze Transformations", image= IMAGE_PATH + "/FreezeTransform.png", c=func.freezeOptions )
    cmds.menuItem(l="Test", image= IMAGE_PATH + "/unfreetransform.png" )
    cmds.menuItem(l="Test", image= IMAGE_PATH + "/unfreetransform.png" )


    cmds.menu(l="Display")
    cmds.menuItem(l="Joint Size", image= IMAGE_PATH + "/jointSize.png", c=func.jointSizeOptions)
    cmds.menuItem(l="Test", image= IMAGE_PATH + "/jointSize.png", c=func.jointSizeOptions)
    cmds.menuItem(l="Test", image= IMAGE_PATH + "/jointSize.png", c=func.jointSizeOptions)

    cmds.menu(l="About")
    cmds.menuItem(l="Fanpage", image= IMAGE_PATH + "/LogoGumroad.jpg", c=func.openWebPageFB)
    cmds.menuItem(l="Gumroad", image= IMAGE_PATH + "/gumroad.png", c=func.openWebgumroad)
    cmds.menuItem(l="Contact by Email", image= IMAGE_PATH + "/Gmail_icon.png", c=func.openGmail)
    cmds.menuItem("info.tri3d@gmail.com", image=IMAGE_PATH + "/copyIcon.png", c=func.copyEmail)
    cmds.menuItem("Update Version to 2.0", image=IMAGE_PATH + "/updateicon.png", c=bank.createBank)

    cmds.menu(l="Course Rigging")
    cmds.menuItem(l="Khoa hoc Animation Basic", image= IMAGE_PATH + "/BasicAnimation.png")
    cmds.menuItem(l="Khoa hoc Rigging Basic", image= IMAGE_PATH + "/BasicRigging.png", c=func.openWebRiggingSlide)
    cmds.menuItem(l="Fanpage", image= IMAGE_PATH + "/LogoGumroad.jpg")
    cmds.menuItem(l="Fanpage", image= IMAGE_PATH + "/LogoGumroad.jpg")


################################################################ UI UX
################################################################
    main_layout = cmds.columnLayout(adjustableColumn=True)
    tab_layout_main = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)

    cmds.setParent(tab_layout_main)
    cmds.columnLayout("Modify", w=310)
    
    cmds.textField("frontName", w=310, h=40, placeholderText="Front_", text="")
    cmds.button(l="Front Name", w=310, c=func.frontName, backgroundColor=[0.284,0.352,0.352])
    #cmds.textField("newName", w=310, h=40, placeholderText="New_Name", text="")
    #cmds.button(l="Rename", w=310, c=func.reName, backgroundColor=[0.284,0.352,0.352])
    cmds.separator(w=310, h=3, style="in", backgroundColor=[0.284,0.352,0.352])
    cmds.textField("backName", w=310, h=40, placeholderText="_Back", text="")
    cmds.button(l="Back Name", w=310, c=func.backName, backgroundColor=[0.284,0.352,0.352])
    cmds.separator(w=310, h=3, style="in", backgroundColor=[0.284,0.352,0.352])
    cmds.button(l=" Delete : Pasted__", w=310, c=tools.pasterdelete)
    cmds.separator(w=310, h=3, style="in", backgroundColor=[0.284,0.352,0.352])
    # cmds.button(l="Picker", w=150, c=picker.animPickerTri3D)
    #cmds.button(l=" Delete : Import or Reference", w=310, c=func.deleteImportName)
    #cmds.symbolButton(image = IMAGE_PATH + "/ccFace.png", w=42, h=42, c=Cur.faceCurve)
    cmds.symbolButton(image=IMAGE_PATH + "/IK_tools.png", w=40, h=40, c=rt.IK_tools)



    cmds.setParent("Modify")
    #cmds.separator(w=310, h=10, style="in")
    # cmds.separator(w=310, h=3, style="in", backgroundColor=[0.284,0.352,0.352])
    cmds.frameLayout("Connect ", w=310, cll=True, cl=False)
    cmds.rowColumnLayout("Layout1", w=310, nc=5)
    cmds.button(l="Attribute", c=func.addattribute, w=61)
    cmds.button(label="Set", c=func.setdrivenkey, w=61)
    cmds.button(label="Connect", c=func.connectEditor, w=61)
    cmds.button(label="Node", c=func.Node, w=61)
    cmds.button(label="Influe", c=func.addinfluence, w=63)
    cmds.button(label="Group", c=func.groupobj, w=61)
    cmds.button(label="Lock", c=func.lockandhide, w=61)
    cmds.button(label="Color", c=func.add_color_attribute, w=61)
    cmds.button(label="Blend", c=func.add_blend_attribute, w=61)
    cmds.button(l="Channel", c=func.channelcontrol, w=61)

    ########## modify #################
    cmds.setParent("Modify")
    cmds.columnLayout("Modify_layout", w=310)
    cmds.frameLayout("Modify", w=310, cll=False)
    cmds.rowColumnLayout("Modify_row", w=310, nc=10)
    cmds.symbolButton(image=IM_Path + "/deleteHist.png", w=44, h=44, c=tools.deleteHistory)
    cmds.symbolButton(image=IM_Path + "/menuIconSelect.png", w=44, h=44, c=tools.SelectHierarchy)
    cmds.symbolButton(image=IM_Path + "/CenterPivot.png", w=44, h=44, c=tools.centerPivot)
    cmds.symbolButton(image=IM_Path + "/FreezeTransform.png", w=44, h=44, c=tools.freezeTrans)
    cmds.symbolButton(image=IM_Path + "/pivotReset.png", w=44, h=44, c=tools.resetPivot)
    cmds.symbolButton(image=IM_Path + "/match.png", w=44, h=44, c=tools.MatchTransform)
    cmds.symbolButton(image=IM_Path + "/unfreetransform.png", w=44, h=44, c=tools.unFreezeTrans)

    ########## polygon #################
    cmds.setParent("Modify")
    cmds.columnLayout("Polygon_layout", w=310)
    cmds.frameLayout("Polygon", w=310, cll=False)
    cmds.rowColumnLayout("Polygon", w=310, nc=8)
    cmds.symbolButton(image=IM_Path + "/polyCube.png", w=39, h=39, c=tools.cubeAdd)
    cmds.symbolButton(image=IM_Path + "/polySphere.png", w=39, h=39, c=tools.sphereAdd)
    cmds.symbolButton(image=IM_Path + "/polyCylinder.png", w=39, h=39, c=tools.cylinderAdd)
    cmds.symbolButton(image=IM_Path + "/polyCone.png", w=39, h=39, c=tools.coneAdd)
    cmds.symbolButton(image=IM_Path + "/polyDisc.png", w=39, h=39, c=tools.discAdd)
    cmds.symbolButton(image=IM_Path + "/polyTorus.png", w=39, h=39, c=tools.torusAdd)
    cmds.symbolButton(image=IM_Path + "/polyPrism.png", w=39, h=39, c=tools.prismAdd)
    cmds.symbolButton(image=IM_Path + "/polyPyramid.png", w=39, h=39, c=tools.pyramidAdd)

    cmds.symbolButton(image=IM_Path + "/polyUnite.png", w=39, h=39, c=tools.CombinePolygons)
    cmds.symbolButton(image=IM_Path + "/polySeparate.png", w=39, h=39, c=tools.SeparatePolygon)
    cmds.symbolButton(image=IM_Path + "/polyBooleansUnion.png", w=39, h=39, c=tools.PolygonBooleanUnion)
    cmds.symbolButton(image=IM_Path + "/polyMergeToCenter.png", w=39, h=39, c=tools.MergeToCenter)
    cmds.symbolButton(image=IM_Path + "/polySmooth.png", w=39, h=39, c=tools.SmoothPolygon)
    cmds.symbolButton(image=IM_Path + "/polyReduce.png", w=39, h=39, c=tools.ReducePolygon)
    cmds.symbolButton(image=IM_Path + "/polyMirrorGeometry.png", w=39, h=39, c=tools.MirrorPolygonGeometryOptions)
    cmds.symbolButton(image=IM_Path + "/polyType.png", w=39, h=39, c=tools.CreatePolygonType)
    
    cmds.symbolButton(image=IM_Path + "/multiCut_NEX32.png", w=39, h=39, c=tools.dR_multiCutTool)
    cmds.symbolButton(image=IM_Path + "/weld_NEX32.png", w=39, h=39, c=tools.MergeVertexTool)
    cmds.symbolButton(image=IM_Path + "/polyDuplicateFacet.png", w=39, h=39, c=tools.DuplicateFace)
    cmds.symbolButton(image=IM_Path + "/polyBevel.png", w=39, h=39, c=tools.performBevelOrChamfer)
    cmds.symbolButton(image=IM_Path + "/polyBridge.png", w=39, h=39, c=tools.performBridgeOrFill)
    cmds.symbolButton(image=IM_Path + "/polyCleanup.png", w=39, h=39, c=tools.CleanupPolygon)
    cmds.symbolButton(image=IM_Path + "/polyFlip.png", w=39, h=39, c=tools.FlipMesh)
    cmds.symbolButton(image=IM_Path + "/polyAverageVertex.png", w=39, h=39, c=tools.AverageVertex)

    ########## sculp #################
    cmds.setParent("Modify")
    cmds.frameLayout("Sculpting", w=310, cll=False)
    cmds.rowColumnLayout("Sculpting", w=310, nc=7, h=200)
    cmds.symbolButton(image=IM_Path + "/Sculpt.png", w=45, h=45, c=tools.SetMeshSculptTool)
    cmds.symbolButton(image=IM_Path + "/Smooth.png", w=45, h=45, c=tools.SetMeshSmoothTool)
    cmds.symbolButton(image=IM_Path + "/Relax.png", w=45, h=45, c=tools.SetMeshRelaxTool)
    cmds.symbolButton(image=IM_Path + "/Grab.png", w=45, h=45, c=tools.SetMeshGrabTool)
    cmds.symbolButton(image=IM_Path + "/Pinch.png", w=45, h=45, c=tools.SetMeshPinchTool)
    cmds.symbolButton(image=IM_Path + "/Flatten.png", w=45, h=45, c=tools.SetMeshFlattenTool)
    cmds.symbolButton(image=IM_Path + "/Foamy.png", w=45, h=45, c=tools.SetMeshFoamyTool)

################################################################ Rigs
################################################################

    cmds.setParent(tab_layout_main)
    cmds.scrollLayout("Rig", horizontalScrollBarThickness=16)
    # cmds.button(l="Detach Window", w=310, c=RigDetach.detachwdRig)
    cmds.separator(w=310, style="in")
    cmds.setParent("Rig")
    cmds.rowColumnLayout("Connect_Layout", w=310, nc=5)
    # cmds.button(l="Attribute", c=func.addattribute, w=60)
    # cmds.button(label="Set", c=func.setdrivenkey, w=60)
    # cmds.button(label="Connect", c=func.connectEditor, w=60)
    # cmds.button(label="Node", c=func.Node, w=60)
    cmds.button(label="Influe", c=func.addinfluence, w=60)
    cmds.button(label="Group", c=func.groupobj, w=60)
    cmds.button(label="Lock", c=func.lockandhide, w=60)
    cmds.button(label="Color", c=func.add_color_attribute, w=60)
    cmds.button(label="Blend", c=func.add_blend_attribute, w=60)
    # cmds.button(l="Channel", c=func.channelcontrol, w=60)


    ########################## control functions #########################
    cmds.setParent("Rig")
    cmds.frameLayout("Controller", w=310, cll=True, cl=False)
    cmds.columnLayout("Controller_Main", w=310)

    cmds.setParent("Controller_Main")
    cmds.rowColumnLayout("Controller_Layout_Rig", w=310, nc=8)
    ButtonLocParent1 = cmds.textField("scaleTextField", w=37, h=37, ec=func.ctrlIn, text="1")
    cmds.symbolButton(image=IMAGE_PATH + "/objtoctrl.png",  c=func.ctrlIn, w=37, h=37)
    cmds.symbolButton(image=IMAGE_PATH + "/add1ctrl.png",  c=func.create1Ctrl, w=37, h=37)
    cmds.symbolButton(image=IMAGE_PATH + "/add2ctrl.png",  c=func.create2Ctrl, w=37, h=37)
    ButtonLocParent = cmds.symbolButton(image=IMAGE_PATH + "/Locator.png", w=37, h=37, c=func.ctrlInB)
    cmds.symbolButton(image=IMAGE_PATH + "/jointadd.png", c=func.createJoint, w=37, h=37)
    cmds.symbolButton(image=IMAGE_PATH + "/jointaddpivot.png", c=func.create1Ctrlparentobj, w=37, h=37)
    cmds.symbolButton(image=IMAGE_PATH + "/jointbind.png", c=func.createjntbind, w=37, h=37)



    cmds.setParent("Controller_Main")
    cmds.rowColumnLayout("curve_out_jnt", w=310, nc=3)
    # cmds.button(l="Select", w=50, c=Cur.get_selected_joint_names)
    # cmds.textField("select_jnt_viewport", w=250, editable=False)
    # cmds.setParent("Controller_Main")
    cmds.rowColumnLayout("select_options_curve", w=310, nc=11)
    cmds.textField("scale_value_Ctrl", w=30, text="1")
    cmds.text(l="", w=10)
    cmds.button(l="Create", w=50, c=Cur.create_circles_for_joints)
    cmds.text(l="", w=10)
    cmds.text(l="-", w=10)
    cmds.text(l="", w=10)
    cmds.textField("scale_curve_value", w=50, text="1.1")
    cmds.text(l="", w=10)
    cmds.button(l="Scale +", w=50, c=Rig.scalePoCurve)
    cmds.text(l="", w=10)
    cmds.button(l="Scale -", w=50, c=Rig.scaleNeCurve)



    ######################### set driven keys #################
    cmds.setParent("Controller_Main")
    # cmds.separator(w=310, h=5, style="in", backgroundColor=[0.284,0.352,0.352])
    cmds.frameLayout("Set Driven Key Color", cll=True, cl=False, w=310)
    cmds.columnLayout("Set_driven_Key_Color_layout", w=310)
    cmds.rowColumnLayout("Color_Set", w=310, nc=8)
    cmds.text(l=" Type ", w=50, backgroundColor=[0.284,0.352,0.352])
    cmds.textField("Type_Attr_field", w=80, placeholderText="long or float", text="long")
    cmds.text(l="Min :", w=50)
    cmds.textField("min_value_attribute", w=30, text="1")
    cmds.text(l="Max :", w=50)
    cmds.textField("max_value_attribute", w=30, text = "20")

    cmds.setParent("Set_driven_Key_Color_layout")
    cmds.rowColumnLayout("typing_value_driven_key", w=310, nc=2)
    cmds.button(l=" Name Attr ", w=80, c=func.add_attribute_ctrl)
    cmds.textField("Name_Attr_field", text = "Color", w=220)
    cmds.text(l=" Driver ", w=80, backgroundColor=[0.284,0.352,0.352])
    cmds.textField("driver_field", text ="ctrlBox", w=220)
    cmds.text(l="   Driven ", w=80, backgroundColor=[0.284,0.352,0.352])
    cmds.textField("driven_field", w=220)
    cmds.button(l="Set", w=80, c=func.Color_Set_Attr)
    cmds.textField("exp_color_attr", w=220, text="expression1")
    cmds.text(l="   Driver Name ", w=80, backgroundColor=[0.284,0.352,0.352])
    cmds.textField("driver_name_attr", w=220)
    cmds.text(l="   Driven Name ", w=80, backgroundColor=[0.284,0.352,0.352])
    cmds.textField("driven_name_attr", w=220)
    cmds.button(l="Key", w=80, c=func.set_key_attr)
    cmds.textField("key_warning", w=220, editable=False, text="hehe")

################################################################ color #################################################################
    cmds.setParent("Controller_Main")
    cmds.frameLayout("Change Color", w=310, cll=True, cl=False)
    cmds.scrollLayout("ChangeColor_scLayout", w=300, h=65)
    cmds.rowColumnLayout("ChangeColor_Layout", w=310, nc=5)
    cmds.button(l="Refill",c=func.refillcolorctrl, w=49, backgroundColor=[1,1,1])
    cmds.canvas(w=59, rgb=[1,0,0], pressCommand=func.redColorCtrl)
    cmds.canvas(w=59, rgb=[1,0.250,0.078], pressCommand=func.cl_lightOrangeColorCtrl)
    cmds.canvas(w=59, rgb=[1,1,0], pressCommand=func.yellowColorCtrl)
    cmds.canvas(w=59, rgb=[1,0.506,0.766], pressCommand=func.pinkColorCtrl)
    cmds.canvas(w=59, rgb=[0,1,0], pressCommand=func.greenColorCtrl)
    cmds.canvas(w=59, rgb=[1,1,1], pressCommand=func.whileColorCtrl)
    cmds.canvas(w=59, rgb=[1,0,1], pressCommand=func.purpleColorCtrl)
    cmds.canvas(w=59, rgb=[0,1,1], pressCommand=func.blueLColorCtrl)
    cmds.canvas(w=59, rgb=[0,0,1], pressCommand=func.cl_darkBlueColorCtrl)
    cmds.canvas(w=59, rgb=[0,0,0], pressCommand=func.blackColorCtrl)
    cmds.canvas(w=59, rgb=[0.19,0.19,0.19], pressCommand=func.greyColorCtrl)
    cmds.canvas(w=59, rgb=[0.352,0.116,0.037], pressCommand=func.cl_brownColorCtrl)
    cmds.canvas(w=59, rgb=[0.53,0.014,0.014], pressCommand=func.cl_darkRedColorCtrl)
    cmds.canvas(w=59, rgb=[0.085,0.386,0.206], pressCommand=func.cl_midnightGreenColorCtrl)

    cmds.setParent("Controller_Main")
    cmds.frameLayout("Curve", w=310, cll=True, cl=False)
    cmds.columnLayout("Curve_Layout_Main", w=310)
    cmds.rowColumnLayout("Curve_Layout", w=310, nc=7)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton02.png", w=42, h=42, c=Cur.cubeCurve)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton08.png", w=42, h=42, c=Cur.pringleCurve)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton48.png", w=42, h=42, c=Cur.handCircleCurve)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton11.png", w=42, h=42, c=Cur.handCurve)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton12.png", w=42, h=42, c=Cur.footCurve)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton46.png", w=42, h=42, c=Cur.VerticalSlider)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton47.png", w=42, h=42, c=Cur.handPet)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton03.png", w=42, h=42, c=Cur.arrowTriangle)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton09.png", w=42, h=42, c=Cur.LocatorCurve)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton10.png", w=42, h=42, c=Cur.circleD)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton19.png", w=42, h=42, c=Cur.ccButton19)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton17.png", w=42, h=42, c=Cur.plusCurve)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton23.png", w=42, h=42, c=Cur.circleP)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton27.png", w=42, h=42, c=Cur.rotateCurve)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton28.png", w=42, h=42, c=Cur.axisC)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton29.png", w=42, h=42, c=Cur.arrowCurve)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton32.png", w=42, h=42, c=Cur.circleAround)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton35.png", w=42, h=42, c=Cur.wardCtrl)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton36.png", w=42, h=42, c=Cur.EyeCtrl)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton38.png", w=42, h=42, c=Cur.fourAround)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton40.png", w=42, h=42, c=Cur.ccButton40)
    cmds.symbolButton(image = IMAGE_PATH + "/ccButton43.png", w=42, h=42, c=Cur.ccButton43)
    cmds.symbolButton(image = IMAGE_PATH + "/ccSquare.png", w=42, h=42, c=Cur.squareCurve)
    cmds.symbolButton(image = IMAGE_PATH + "/ccSlider.png", w=42, h=42, c=Cur.functionsCurve)
    cmds.symbolButton(image = IMAGE_PATH + "/ccFace.png", w=42, h=42, c=Cur.faceCurve)
    cmds.setParent("Curve_Layout_Main")
    cmds.columnLayout("Curve_Layout_cl", w=310, columnAttach = ('left', 5))
    #cmds.button(l="Combine Shape", w=310)
    cmds.colorIndexSliderGrp(Rig.ctrlColor, minValue = 1, maxValue = 31, value = 16, columnWidth = (1,60), columnWidth2 = (1, 220),\
                              dragCommand = Rig.hideManipulator, changeCommand = Rig.showManipulator) 
    #cmds.symbolButton(image=IMAGE_PATH + "/blendShapeEditor.png", w=42, h=42, c=func.ShapeEditor)

    cmds.setParent("Curve_Layout_Main")
    cmds.frameLayout("Curve Code", w=310, cll=True, cl=True)
    cmds.columnLayout("Curve_code", w=310)
    cmds.textField("tx_roundNum_ctt", w=310,text="2")
    cmds.scrollField("tx_codeCTL_ctt", w=310, h=50, wordWrap=True)
    cmds.button(l="Create Code", w=310, c=Cur.createCodeCurve_ctt)

    cmds.setParent("Curve_code")
    cmds.rowColumnLayout("Edge_to_curve", w=310, nc=7)
    degree_Curve = cmds.textField("degree_text", w=43, h=30, ec=Cur.edgeToCurve, placeholderText="1 or 3")
    cmds.symbolButton(image=IMAGE_PATH + "/Ari_etc.png", c=Cur.edgeToCurve, w=100, h=20)
    cmds.separator(w=5, h=30, style="in")
    cmds.setParent("Controller_Main")
    cmds.frameLayout("Modify", w=310, cll=True, cl=False)
    cmds.columnLayout("Modify_Layout", w=310)

    cmds.setParent("Modify_Layout")
    cmds.rowColumnLayout("Modify_Layout", w=310, nc=7, backgroundColor=[0.284,0.352,0.352])
    cmds.symbolButton(image=IMAGE_PATH + "/menuIconSelect.png", w=42, h=42, c=func.SelectHierarchy)
    cmds.symbolButton(image=IMAGE_PATH + "/deleteHist.png", w=42, h=42, c=func.deleteHistory)
    cmds.symbolButton(image=IMAGE_PATH + "/FreezeTransform.png", w=42, h=42, c=func.freezeTrans)
    cmds.symbolButton(image=IMAGE_PATH + "/CenterPivot.png", w=42, h=42, c=func.centerPivot)
    cmds.symbolButton(image=IMAGE_PATH + "/pivotReset.png", w=42, h=42, c=func.resetPivot)
    cmds.symbolButton(image=IMAGE_PATH + "/match.png", w=42, h=42, c=func.MatchTransform)
    cmds.symbolButton(image=IMAGE_PATH + "/unfreetransform.png", w=42, h=42, c=func.unFreezeTrans)
    cmds.symbolButton(image=IMAGE_PATH + "/circle.png", w=42, h=42, c=func.createCircle)
    cmds.symbolButton(image=IMAGE_PATH + "/pencil.png", w=42, h=42, c=func.PencilCurveTool)
    cmds.symbolButton(image=IMAGE_PATH + "/curveEP.png", w=42, h=42, c=func.EPCurveTool)
    cmds.symbolButton(image=IMAGE_PATH + "/ngSkinTools2ShelfIcon.png", w=42, h=42)
    cmds.symbolButton(image=IMAGE_PATH + "/textureEditor.png", w=42, h=42, c=func.TextureViewWindow)
    cmds.symbolButton(image=IMAGE_PATH + "/getGraphEditor.png", w=42, h=42, c=func.graphEditor)
    cmds.symbolButton(h=30, w=30, image= IMAGE_PATH + "/jointSize.png", c=func.jointSizeOptions) 
    cmds.symbolButton(h=42, w=42, image= IMAGE_PATH +"/kinJoint.png" , c=func.jointTools)
    cmds.symbolButton(h=42, w=42, image= IMAGE_PATH +"/kinMirrorJoint_S.png" , c=func.jointMirror)
    cmds.symbolButton(h=42, w=42, image= IMAGE_PATH +"/orientJoint.png", c=func.orientJoint)
    cmds.symbolButton(h=42, w=42, image= IMAGE_PATH +"/smoothSkin.png" , c=func.SmoothBindSkin)
    cmds.symbolButton(h=42, w=42, image= IMAGE_PATH +"/detachSkin.png" , c=func.DetachSkin)
    cmds.symbolButton(h=42, w=42, image= IMAGE_PATH +"/copySkinWeight.png" , c=func.CopySkinWeights)
    cmds.symbolButton(h=42, w=42, image= IMAGE_PATH +"/lattice.png", c=func.CreateLattice)
    cmds.symbolButton(h=42, w=42, image= IMAGE_PATH +"/parentConstraint.png" , c=func.ParentConstraintOptions)
    cmds.symbolButton(h=42, w=42, image= IMAGE_PATH +"/orientConstraint.png" , c=func.OrientConstraint)
    cmds.symbolButton(h=42, w=42, image= IMAGE_PATH +"/aimConstraint.png" , c=func.AimConstraint)
    cmds.symbolButton(h=42, w=42, image= IMAGE_PATH +"/posConstraint.png" , c=func.PointConstraint)
    cmds.symbolButton(h=42, w=42, image= IMAGE_PATH +"/scaleConstraint.png" , c=func.ScaleConstraintOptions)
    cmds.symbolButton(h=42, w=42, image= IMAGE_PATH +"/poleVectorConstraint.png" , c=func.PoleVectorConstraint)
    cmds.symbolButton(h=42, w=42, image= IMAGE_PATH +"/blendShape.png", c=func.CreateBlendShape)

    cmds.setParent("Rig")
    cmds.frameLayout("Rig tools", w=310, cll=True, cl=False)
    cmds.columnLayout("rigTools_Layout", w=310)
    cmds.rowColumnLayout("Rig_Char", w=310, nc=6)
    cmds.symbolButton(image=IMAGE_PATH + "/eyeRig.png", w=40, h=40, c=Rig.run_eye_lid_setup)
    cmds.symbolButton(image=IMAGE_PATH + "/IK_tools.png", w=40, h=40, c=rt.IK_tools)


    ############################################################## wheel tools
    cmds.setParent("rigTools_Layout")
    cmds.frameLayout("Wheel tools", w=310, cll=True, cl=False)
    cmds.columnLayout("Engine_rig")
    cmds.rowColumnLayout("Rig_Engine", w=310, nc=6)
    cmds.symbolButton(image=IMAGE_PATH + "/VibratingAdd.png", w=40, h=40, c=func.loopVibrating, backgroundColor=[0.284,0.352,0.352])
    cmds.symbolButton(image=IMAGE_PATH + "/VibratingOn.png", w=40, h=40, c=func.addExpressionToObject, backgroundColor=[0.284,0.352,0.352])
    #cmds.symbolButton(image=IMAGE_PATH + "/Wheel.png", w=40, h=40, c=Rig.Ui, backgroundColor=[0.284,0.352,0.352])

    ############################################################## auto wheel
    cmds.setParent("Engine_rig")
    pm.columnLayout('mainWindowColumnLayout', adjustableColumn=1, w=310)
    pm.rowLayout(numberOfColumns=2, w=310, adj=2, columnAlign=(1, 'center'), columnAttach=[(1, 'both', 0), (2, 'both', 0)] )
    pm.text('textName', label='Name: ', w=40)
    pm.textField('textFieldName', text='', w=220)

    pm.setParent('mainWindowColumnLayout')
    #pm.rowLayout(numberOfColumns=2, w=310, columnAlign=(1, 'center'), columnAttach=[(1, 'both', 0), (2, 'both', 0)] )
    pm.rowColumnLayout("Checkbox_autoWheel", w=310, nc=4)
    pm.checkBox(Rig.checkBox1, label='Selected ', w=75, cc= Rig.changestate)
    pm.checkBox(Rig.checkBox2, label='Position', w=75)
    #pm.setParent('mainWindowColumnLayout')
    #pm.rowLayout(numberOfColumns=2, w=310, columnAlign=(1, 'center'), columnAttach=[(1, 'both', 0), (2, 'both', 0)] )
    pm.checkBox(Rig.checkBox3, label='Bind Skin', w=75, cc=Rig.changestatebind,enable=0)
    pm.checkBox(Rig.checkBox4, label='Constrain', w=75, cc=Rig.changestatecons,enable=0)
    pm.setParent('mainWindowColumnLayout')
    pm.optionMenu(Rig.optionMenu1, label='Move Direction :',ni=6)
    pm.menuItem('x', label='x' )
    pm.menuItem('y', label='y' )
    pm.menuItem('z', label='z' )
    pm.menuItem('xx', label='-x' )
    pm.menuItem('yy', label='-y' )
    pm.menuItem('zz', label='-z' )
    pm.optionMenu(Rig.optionMenu1, e=1, v='z')
    pm.rowLayout(numberOfColumns=2, w=310, columnAlign=(1, 'right'), columnAttach=[(1, 'both', 0), (2, 'both', 0)] )
    pm.button(Rig.buttonMenu1, label=Rig.labelButtonMenu1, command=Rig.buttonMenu1Function, w=150)
    pm.button(Rig.buttonMenu2, label=Rig.labelButtonMenu2, command=Rig.buttonMenu2Function, w=150)



    # cmds.setParent("Rig")
    # cmds.frameLayout("Add joint to curve", w=310, cll=True, cl=False)
    # cmds.rowColumnLayout("Layout7", w=310, nc=1)
    # cmds.textField("loadcurve",ed=0, w=310)
    # cmds.button( label='Add Curve' ,c =func.addcurve, w=310)
    # cmds.textField("numberofjointfeild",pht="Number of Joints", w=310)
    # cmds.button( label='Run',c=func.inbetweenjoints, w=310)


########################################################################
    ########################################################################
    #################   Tools tab Layout     ###############################
    ########################################################################
    ########################################################################

    cmds.setParent(tab_layout_main)
    cmds.columnLayout("Model", w=310)
    cmds.frameLayout("Modeling", w=310)

    cmds.setParent("Model")
    cmds.text(l="Move model to vertex : " , w=310, h=15, backgroundColor=[0.284,0.352,0.352])
    cmds.rowColumnLayout("Tools_model", w=310, nc=2)
    cmds.button(l="Select", w=40, h=20, c=md.button1_select_obj)
    cmds.textField("move_obj_to_vertex", placeholderText = "Select Model", editable=False, w=310, h=20)
    cmds.button(l="Move", w=80, h=20, c=md.button2_move_obj)
    cmds.textField("move_obj_to_vertex_comp", placeholderText = "!!!", editable=False, w=310, h=20)


    ################### Toolbar Layout #########################
    cmds.setParent(tab_layout_main)
    cmds.columnLayout("Tools", w=310)

    cmds.setParent("Tools")
    cmds.frameLayout("Tools", w=310)
    cmds.rowColumnLayout("Check", w=310, nc=5)
    cmds.button(l="Name Space", w=70, h=25, c=ae.namespace)
    cmds.text(l="", w=10)
    cmds.button(l="On subs VRay", w=80, h=25, c=ae.makeVrayAttributes)
    cmds.text(l="", w=10)

    cmds.setParent("Tools")
    cmds.frameLayout("Ari tools", w=310)
    cmds.rowColumnLayout("Ari_tools", w=310, nc=5)
    cmds.symbolButton(image=IM_Path + "/AriCircleVertex.png", w=55, h=55, c=ae.AriCircleVertex)
    cmds.symbolButton(image=IM_Path + "/AriPolygonCounter.png", w=55, h=55, c=ae.AriPolygonCounter)
    cmds.symbolButton(image=IM_Path + "/AriSymmetryChecker.png", w=55, h=55, c=ae.AriSymmetryChecker)
    cmds.symbolButton(image=IM_Path + "/AriUVGridding.png", w=55, h=55, c=ae.AriUVFromVertexRatio)
    cmds.symbolButton(image=IM_Path + "/AriViewWindow.png", w=55, h=55, c=ae.AriViewWindow)
    cmds.symbolButton(image=IM_Path + "/Ari_tp.png", w=55, h=55, c=ae.AriTransferPosition)
    cmds.symbolButton(image=IM_Path + "/Ari_sv.png", w=55, h=55, c=ae.AriStraightVertex)
    cmds.symbolButton(image=IM_Path + "/Ari_dora.png", w=55, h=55, c=ae.DoraSkinWeightImpExp)




################################################################ Shader
################################################################
    cmds.setParent(tab_layout_main)
    cmds.columnLayout("Shader", w=310)

    cmds.setParent("Shader")
    cmds.frameLayout("Texture", w=310)
    cmds.rowColumnLayout("Texture", w=310, nc=7)
    cmds.symbolButton(image=IMAGE_PATH + "/out_file.png", w=40, h=40, c=sdr.addTexture)
    cmds.symbolButton(image=IMAGE_PATH + "/Raw_file.png", w=40, h=40, c=sdr.addTextureRaw)

    cmds.setParent("Shader")
    cmds.frameLayout("Shader Tools", w=310)
    cmds.rowColumnLayout("Shader_Tools", w=310, nc=7)
    # cmds.symbolButton(image=IMAGE_PATH + "/duplicate_shader.png", w=40, h=40, c=Shader.duplicateShaderWithConnect)
    # cmds.symbolButton(image=IMAGE_PATH + "/duplicate_shaderS.png", w=40, h=40, c=Shader.duplicateShaderWithConnect)
    cmds.button(l="Dup C Shader", w=90, c=Shader.duplicateShaderWithConnect)
    cmds.text(l="", w=15)
    cmds.button(l="Dup S Shader", w=90, c=Shader.duplicateShaderSingle)


    cmds.setParent("Shader")
    cmds.frameLayout("Shader", w=310)
    cmds.rowColumnLayout("Shader", w=310, nc=7)
    cmds.symbolButton(image=IMAGE_PATH + "/swmtl.png", w=55, h=55, c=sdr.swShadermtl)
    cmds.symbolButton(image=IMAGE_PATH + "/mtlBase.png", w=55, h=55, c=sdr.mtl_base)
    # cmds.symbolButton(image=IMAGE_PATH + "/swmtl.png", w=55, h=55)
    # cmds.symbolButton(image=IMAGE_PATH + "/swmtl.png", w=55, h=55)
    # cmds.symbolButton(image=IMAGE_PATH + "/swmtl.png", w=55, h=55)


################################################################ Animation
################################################################
    cmds.setParent(tab_layout_main)
    cmds.columnLayout("Animation", w=310)
    cmds.setParent("Animation")
    cmds.frameLayout("Graph", w=310)
    cmds.rowColumnLayout("FunctionsKey_Layout", nc=5, w=310, backgroundColor=[0.284,0.352,0.352])
    cmds.symbolButton(image = IMAGE_PATH +"/ResetKey.png", w=60, h=22, c=Funcanim.resetKey)
    cmds.symbolButton(image = IMAGE_PATH +"/copyKey.png", w=60, h=22, c=Funcanim.copyKey)
    cmds.symbolButton(image = IMAGE_PATH +"/pasteKey.png", w=60, h=22, c=Funcanim.pasteKey)
    cmds.symbolButton(image = IMAGE_PATH +"/deleteKey.png", w=60, h=22, c=Funcanim.cutKey)
    cmds.symbolButton(image = IMAGE_PATH +"/Picker.png", w=60, h=22, c=pk.animPickerTri3D)

    cmds.setParent("Animation")
    cmds.rowColumnLayout("FunctionsGraph_Layout", nc=10, w=310, backgroundColor=[0.284,0.352,0.352])
    cmds.textField("timeChangeField", w=50, placeholderText="Enter_")
    cmds.symbolButton(image = IMAGE_PATH + "/moveKeyLe.png", w=30, h=30, c=Funcanim.moveKeyBUi)
    cmds.symbolButton(image = IMAGE_PATH + "/moveKeyRi.png", w=30, h=30, c=Funcanim.moveKeyFUi)
    cmds.symbolButton(image = IMAGE_PATH +"/autoTangent.png", w=30, h=30, c=Funcanim.TangentsAuto)
    cmds.symbolButton(image = IMAGE_PATH +"/splineTangent.png", w=30, h=30, c=Funcanim.TangentsSpline)
    cmds.symbolButton(image = IMAGE_PATH +"/clampedTangent.png", w=30, h=30, c=Funcanim.TangentsClamped)
    cmds.symbolButton(image = IMAGE_PATH +"/linearTangent.png", w=30, h=30, c=Funcanim.TangentsLinear)
    cmds.symbolButton(image = IMAGE_PATH +"/flatTangent.png", w=30, h=30, c=Funcanim.TangentsFlat)
    cmds.symbolButton(image = IMAGE_PATH + "/getGraphEditor.png", w=30, h=30, c=func.graphEditor)

    cmds.setParent("Animation")
    cmds.rowColumnLayout("Layer8", w=310, nc=2, backgroundColor=[0.284,0.352,0.352])
    cmds.button(l="Detach Window", w=310, c=anim.animWindow)
    # cmds.button(l="Picker", w=150, c=picker.animPickerTri3D)
    #cmds.text(l="", w=80)
    #cmds.iconTextButton(style="iconAndTextHorizontal", image = IMAGE_PATH + "/windowDetach.png", label="Detach Window", w=130, h=30, c=Funcanim.animWindow)
    #cmds.text(l="", w=50)

    ################################################################ move key pro
    cmds.setParent("Animation")
    cmds.frameLayout("Move Key Pro", w=310, cll=True, cl=False)
    cmds.columnLayout("Main_Layout", w=310, adj= 1)
    cmds.rowColumnLayout("Move_Pro", w=310, nc=4)
    cmds.button(l= 'Select', c= Funcanim.selectCtrl, w=57)
    cmds.textField('selectCtrl', w= 250, ed= 0, placeholderText="Select_Controller")
    cmds.button(l= 'Select', c= Funcanim.selectAll, w=50)
    cmds.textField('selectAll', w= 100, ed= 0, placeholderText="Select_Ctrl")

    cmds.setParent("Main_Layout")
    cmds.checkBox('UseSEK', l= 'On_Start_End', v= 0, cc= Funcanim.useSEK)
    cmds.rowColumnLayout("Button2", w=310, nc=4)
    cmds.button(l= 'Start Key', c= Funcanim.butt_startKey, w=57)
    cmds.textField('startKey', w= 100, ed= 0, tx= '')
    cmds.button(l= 'End Key', c= Funcanim.butt_endKey, w=50)
    cmds.textField('endKey', w= 100, ed= 0, tx= '')
    cmds.setParent("Main_Layout")
    cmds.intSliderGrp('numbersKey', f= 1, min= 1, v= 1, max= 999999)
    cmds.setParent("Main_Layout")
    cmds.rowColumnLayout("button select", w=310, nc=2)
    cmds.button('moveBackward', l= '<<< Move Back', c= Funcanim.butt_moveBackward, w=155)
    cmds.button('moveForward', l= 'Move Go >>>', c= Funcanim.butt_moveForward, w=155)    
################################################################ autorig
################################################################
    cmds.setParent(tab_layout_main)
    cmds.scrollLayout("Auto_Rig")

    cmds.setParent("Auto_Rig")
    cmds.frameLayout("Setup", w=310)
    cmds.rowColumnLayout("Setup_Layout", w=310, nc=3)

    cmds.button(l="Import biped", w=80, c=autorig.createBone)
    cmds.textField("Import_biped_Text", w=100, editable=False, placeholderText="Import not yet !")
    cmds.checkBox("Import_CheckBox",l="", w=30, enable=False, cc=autorig.deleteImportBone)

    cmds.button(l="Done Setup", w=80, c=autorig.DoneSetupBone)
    cmds.textField("Done_Setup_Bone", w=100, editable=False, placeholderText="Setup not yet !")
    cmds.checkBox("Done_Setup_CheckBox",l="", w=30, enable=False)  

    cmds.button(l="Mirror", w=80, c=autorig.mirrorBone)
    cmds.textField("Mirror_Text", w=100, editable=False, placeholderText="Mirror not yet !")
    cmds.checkBox("Mirror_Checkbox",l="", w=30, enable=False)

    cmds.setParent("Auto_Rig")
    cmds.rowColumnLayout("Build_Auto_Rig", w=310, nc=3)
    cmds.button(l="Build", w=140, c=autorig.buildAutoRig)
    cmds.text(l="", w=20)
    cmds.button(l="Fix", w=140, c=autorig.fixBuildBody)
    cmds.text(l="", w=20)
    cmds.text(l="", w=20)
    cmds.text(l="", w=20)
    cmds.button(l="Demo Rig", w=140, c=func.DemoRig)

    cmds.setParent("Auto_Rig")
    cmds.frameLayout("Face Setup", w=310, cll=True, cl=False)
    cmds.columnLayout("Face_Ctrl_Layout", w=310)
    cmds.rowColumnLayout("Face_Layout", w=310, nc=5) 

    cmds.button(l="Right Eye", w=100, c=autorig.rightEye)
    cmds.textField("RE_Text", w=130, editable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("RE_CheckBox",l="", w=25, enable=False, cc=autorig.dltRE)
    cmds.button(l="Help", w=30, c=helpRig.RightEye)

    cmds.button(l="Left Eye", w=100, c=autorig.leftEye)
    cmds.textField("LE_Text", w=130, editable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("LE_CheckBox",l="", w=25, enable=False, cc=autorig.dltLE)
    cmds.button(l="Help", w=30, c=helpRig.LeftEye)

    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)

    cmds.button(l="Mid Up Lip ", w=100, c=autorig.MidUpLip)
    cmds.textField("MUL_Text", w=130, editable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("MUL_CheckBox",l="", w=25, enable=False, cc=autorig.dltMUL)
    cmds.button(l="Help", w=30, c=helpRig.MUL)

    cmds.button(l="R_Between_1", w=100, c=autorig.MidBW1)
    cmds.textField("RB1_Text", w=130, editable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("RB1_CheckBox",l="", w=25, enable=False, cc=autorig.dltBW1)
    cmds.button(l="Help", w=30, c=helpRig.BW1)

    cmds.button(l="R_Between_2", w=100, c=autorig.MidBW2)
    cmds.textField("RB2_Text", w=130, editable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("RB2_CheckBox",l="", w=25, enable=False, cc=autorig.dltBW2)
    cmds.button(l="Help", w=30, c=helpRig.BW2)

    cmds.button(l="Right Corner Lip", w=100, c=autorig.R_Corner_Lip)
    cmds.textField("RCL_Text", w=130, editable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("RCL_CheckBox",l="", w=25, enable=False, cc=autorig.dltRCL)
    cmds.button(l="Help", w=30, c=helpRig.Corner)
        
    cmds.button(l="R_Between_3", w=100, c=autorig.MidBW3)
    cmds.textField("RB3_Text", w=130, editable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("RB3_CheckBox",l="", w=25, enable=False, cc=autorig.dltBW3)
    cmds.button(l="Help", w=30, c=helpRig.BW3)
        
    cmds.button(l="R_Between_4", w=100, c=autorig.MidBW4)
    cmds.textField("RB4_Text", w=130, editable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("RB4_CheckBox",l="", w=25, enable=False, cc=autorig.dltBW4)
    cmds.button(l="Help", w=30, c=helpRig.BW4)
    
    cmds.button(l="Mid Down Lip", w=100, c=autorig.MidDownLip)
    cmds.textField("MDL_Text", w=130, editable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("MDL_CheckBox",l="", w=25, enable=False, cc=autorig.dltMDL)
    cmds.button(l="Help", w=30, c=helpRig.MLL)

    cmds.setParent("Face_Ctrl_Layout")
    cmds.rowColumnLayout("Tongue_Ctrl_Layout", w=310, nc=10)
    cmds.button(l="Tong1", w=50, c=autorig.Jnt_TOG1)
    cmds.text(l="", w=10)
    cmds.button(l="Tong2", w=50, c=autorig.Jnt_TOG2)
    cmds.text(l="", w=10)
    cmds.button(l="Tong3", w=50, c=autorig.Jnt_TOG3)
    cmds.text(l="", w=10)
    cmds.button(l="Tong4", w=50, c=autorig.Jnt_TOG4)
    cmds.text(l="", w=10)
    cmds.checkBox("Tongue_checkbox",l="", w=25, enable=False, cc=autorig.dltTG1)
    cmds.button(l="Help", w=30, c=helpRig.TG)

    cmds.setParent("Face_Ctrl_Layout")
    cmds.rowColumnLayout("Brow_Layout", w=310, nc=5)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    
    cmds.button(l="Right Inner Brow", w=100, c=autorig.InnerBrow)
    cmds.textField("RIB_Text", w=130, editable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("RIB_CheckBox",l="", w=25, enable=False, cc=autorig.dltRIB)
    cmds.button(l="Help", w=30, c=helpRig.INB)
        
    cmds.button(l="Right Outer Brow", w=100, c=autorig.OuterBrow)
    cmds.textField("LIB_Text", w=130, editable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("LIB_CheckBox",l="", w=25, enable=False, cc=autorig.dltROB)
    cmds.button(l="Help", w=30, c=helpRig.OTB)

    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)

    cmds.button(l="Jaw", w=100, c=autorig.jawJnt)
    cmds.textField("Jaw_Text", w=130, editable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("Jaw_CheckBox",l="", w=25, enable=False, cc=autorig.dltJaw)
    cmds.button(l="Help", w=30, c=helpRig.JAW)

    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    
    cmds.setParent("Face_Ctrl_Layout")    
    cmds.rowColumnLayout("Mirror_Face_Ctrl", w=310, nc=6)    
    cmds.button(l="Mirror", w=100, c=autorig.MirrorMouth)
    cmds.textField("MR_Text", w=130, editable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("MR_CheckBox",l="", w=25, enable=False)
    cmds.button(l="Help", w=30)

    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)

    cmds.setParent("Face_Ctrl_Layout")
    cmds.rowColumnLayout("FIx_Build", w=310, nc=3)
    cmds.button(l="Build", w=140, c=autorig.buildFace)
    cmds.text(l="", w=20)
    cmds.button(l="Fix", w=140, c=autorig.fixBuildFace)
    cmds.text(l="", w=10)

    cmds.setParent("Auto_Rig")
    cmds.frameLayout("Custom Curve", w=310, cll=True, cl=False)
    cmds.columnLayout("Curve_Layout", w=310, adj=True)  
    cmds.setParent("Curve_Layout")
    cmds.rowColumnLayout("Curve_autorig", w=310, nc=6)    
    cmds.textField("enter_number_curve", placeholderText="Enter", w=100)
    cmds.button(l="Set", w=55, c=Rig.scalePoCurve)
    cmds.text(l="", w=10)
    cmds.button(l="Scale +", w=60, c=Rig.scalePoCurve)
    cmds.text(l="", w=10)
    cmds.button(l="Scale -", w=60, c=Rig.scaleNeCurve)

##################### Auto face Car #########################
    cmds.setParent("Auto_Rig")
    cmds.frameLayout("Face Car Setup", w=310, cll=True, cl=False)
    cmds.columnLayout("Face_Car_Ctrl_Layout", w=310)
    cmds.rowColumnLayout("Face_Layout", w=310, nc=5) 

    cmds.button(l="Right Eye", w=100, c=rf.rightEye)
    cmds.textField("RE_Car_Text", w=130, enable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("RE_Car_CheckBox",l="", w=25, enable=False, cc=rf.dltRE)
    cmds.button(l="Help", w=30, c=helpRig.RightEye)

    cmds.button(l="Left Eye", w=100, c=rf.leftEye)
    cmds.textField("LE_Car_Text", w=130, enable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("LE_Car_CheckBox",l="", w=25, enable=False, cc=rf.dltLE)
    cmds.button(l="Help", w=30, c=helpRig.LeftEye)

    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)

    cmds.button(l="Mid Up Lip ", w=100, c=rf.MidUpLip)
    cmds.textField("MUL_Car_Text", w=130, enable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("MUL_Car_CheckBox",l="", w=25, enable=False, cc=rf.dltMUL)
    cmds.button(l="Help", w=30, c=helpRig.MUL)

    cmds.button(l="R_Between_1", w=100, c=rf.MidBW1)
    cmds.textField("RB1_Car_Text", w=130, enable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("RB1_Car_CheckBox",l="", w=25, enable=False, cc=rf.dltBW1)
    cmds.button(l="Help", w=30, c=helpRig.BW1)

    cmds.button(l="R_Between_2", w=100, c=rf.MidBW2)
    cmds.textField("RB2_Car_Text", w=130, enable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("RB2_Car_CheckBox",l="", w=25, enable=False, cc=rf.dltBW2)
    cmds.button(l="Help", w=30, c=helpRig.BW2)

    cmds.button(l="Right Corner Lip", w=100, c=rf.R_Corner_Lip)
    cmds.textField("RCL_Car_Text", w=130, enable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("RCL_Car_CheckBox",l="", w=25, enable=False, cc=rf.dltRCL)
    cmds.button(l="Help", w=30, c=helpRig.Corner)
        
    cmds.button(l="R_Between_3", w=100, c=rf.MidBW3)
    cmds.textField("RB3_Car_Text", w=130, enable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("RB3_Car_CheckBox",l="", w=25, enable=False, cc=rf.dltBW3)
    cmds.button(l="Help", w=30, c=helpRig.BW3)
        
    cmds.button(l="R_Between_4", w=100, c=rf.MidBW4)
    cmds.textField("RB4_Car_Text", w=130, enable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("RB4_Car_CheckBox",l="", w=25, enable=False, cc=rf.dltBW4)
    cmds.button(l="Help", w=30, c=helpRig.BW4)
    
    cmds.button(l="Mid Down Lip", w=100, c=rf.MidDownLip)
    cmds.textField("MDL_Car_Text", w=130, enable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("MDL_Car_CheckBox",l="", w=25, enable=False, cc=rf.dltMDL)
    cmds.button(l="Help", w=30, c=helpRig.MLL)

    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    
    cmds.setParent("Face_Car_Ctrl_Layout")    
    cmds.rowColumnLayout("Mirror_Face_Ctrl", w=310, nc=6)    
    cmds.button(l="Mirror", w=100, c=rf.MirrorMouth)
    cmds.textField("MR_Car_Text", w=130, enable=False)
    cmds.text(l="", w=10)
    cmds.checkBox("MR_CAr_CheckBox",l="", w=25, enable=False)
    cmds.button(l="Help", w=30)

    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)
    cmds.text(l="", w=10)

    cmds.setParent("Face_Car_Ctrl_Layout")
    cmds.rowColumnLayout("Fix_Build", w=310, nc=3)
    cmds.button(l="Build", w=140, c=rf.buildFace)
    cmds.text(l="", w=20)
    cmds.button(l="Fix", w=140, c=rf.fixBuildFace)
    cmds.text(l="", w=10)    



################################################################ copy right by Tri 3D
################################################################
    cmds.setParent(tab_layout_main)
    cmds.columnLayout("About", w=310)
    cmds.frameLayout("Click to button :", w=310)
    cmds.rowColumnLayout("Layer6", w=310, nc=5)
    cmds.symbolButton(image=IMAGE_PATH +"/LogoGumroad.jpg", w=60, h=60, c=func.openWebMessFB)
    cmds.text("                   ")
    cmds.symbolButton(image=IMAGE_PATH +"/gumroad.png", w=60, h=60, c=func.openWebgumroad)
    cmds.text("                   ")

    cmds.symbolButton(image=IMAGE_PATH +"/Gmail_Icon.png", w=60, h=60, c=func.openGmail)
    cmds.setParent("About")
    cmds.rowColumnLayout("Layer7", w=310, nc=3)
    cmds.button("Copy   ", w=100, c=func.copyEmail)
    cmds.textField("Email", w=199, text="info.tri3d@gmail.com")
    cmds.setParent("About")
    cmds.columnLayout("duongdungrong", w=310)
    cmds.button(l="I love VN", w=310, h=30, backgroundColor=[1,1,1])
    cmds.button(l="Update Version to 2.0", w=310, h=30, backgroundColor=[1,0.774,0.108])
    cmds.button(l="Course Rigging", w=310, h=30, backgroundColor=[1,0.774,0.108], c=func.openWebRiggingCause)
   # cmds.button(l="Khoa hoc Auto Rigging", w=310, h=30, backgroundColor=[1,0.774,0.108], c=func.openWebRiggingCause)
    cmds.image(image=IMAGE_PATH +"/vn.png", w=310)
    cmds.setParent(tab_layout_main)

    cmds.showWindow(triWin)
    # dock = cmds.dockControl(allowedArea=['right', 'left'], area='right', content=triWin, label="Tri 3D Tools", epo=True)



createUI()






