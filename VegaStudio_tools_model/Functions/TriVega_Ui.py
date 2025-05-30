######## Tri Vega #################################
######## Copyrights by Tri3D ######################
###################################################

                                 ############################
                        #######################################
                  ##############################################
           ####################################################
     ############################################################
  ################################################################
 ##################################################################
####################################################################
 ##################################################################
  ################################################################
     ############################################################
          #####################################################
                  ##############################################
                        #######################################
                                 ############################
                                                                
                                 ############################
                        #######################################
                  ##############################################
           ####################################################
     ############################################################
  ################################################################
 ##################################################################
####################################################################
 ##################################################################
  ################################################################
     ############################################################
          #####################################################
                  ##############################################
                        #######################################
                                 ############################


import maya.cmds as cmds
import os
########################################################################
IM_Path = os.path.join(os.path.dirname(__file__), 'Icons')
########################################################################
import VegaStudio_tools_model.Functions.TriVega_Tools as tools
reload(tools)########################################################################
import VegaStudio_tools_model.Functions.TriVega_Switch_Vraymtl as sdr
reload(sdr)########################################################################
import VegaStudio_tools_model.Functions.Vega_tools_ae as ae
reload(ae)########################################################################
###################### windows ######################
def triVegaUi():
    if cmds.window("triVegaUi", exists=True):
        cmds.deleteUI("triVegaUi")

    triVegaUiWD = cmds.window("triVegaUi", title=" Tri_Vega Model", w=290, sizeable=False, menuBar=True)
    cmds.windowPref("triVegaUi", remove=True)

    ###################### menu Bar #################
    cmds.menu(l="Modify")
    cmds.menuItem(l="Freeze Transformations", image= IM_Path + "/FreezeTransform.png", c=tools.freezeOptions)

    cmds.menu(l="Display")
    ###################### Layout #################
    cmds.columnLayout("triVegaUiLayout", w=290, adj=True)
    main_layout = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)


    ########################################################################
    ########################################################################
    #################   Model Tab Layout     ###############################
    ########################################################################
    ########################################################################
    cmds.setParent(main_layout)
    cmds.columnLayout("Model", w=290)

    ########## File #################
    cmds.setParent("Model")
    cmds.frameLayout("File", w=290, cll=False)
    cmds.rowColumnLayout("File", w=290, nc=10)
    cmds.symbolButton(image=IM_Path+"/otm.png", w=35, h=35, c=tools.OptimizeScene)
    cmds.symbolButton(image=IM_Path + "/Import.png", w=35, h=35, c=tools.Import)
    cmds.symbolButton(image=IM_Path + "/Reference.png", w=35, h=35, c=tools.ReferenceEditor)
    cmds.symbolButton(image=IM_Path + "/wd_FPE.png", w=35, h=35, c=tools.FilePathEditor)
    cmds.symbolButton(image=IM_Path + "/fpe.png", w=35, h=35, c=tools.filePathRepathWin)
    cmds.symbolButton(image=IM_Path + "/wd_NS.png", w=35, h=35, c=tools.NamespaceEditor)
    cmds.symbolButton(image=IM_Path + "/hypershadeIcon.png", w=35, h=35, c=tools.HypershadeWindow)
    cmds.symbolButton(image=IM_Path + "/textureEditor.png", w=35, h=35, c=tools.TextureViewWindow)
    cmds.symbolButton(image=IM_Path + "/blendShapeEditor.png", w=35, h=35, c=tools.CreateBlendShapeOptions)

    ########## rename #################
    cmds.setParent("Model")
    cmds.columnLayout("rename_layout", w=290)
    cmds.rowColumnLayout("Rename", w=290, nc=2)
    cmds.button(l="Front Name", w=90, c=tools.frontName, backgroundColor=[0.284,0.352,0.352])
    cmds.textField("frontName", w=200, h=30, placeholderText="Front_", text="")
    cmds.button(l="Back Name", w=90, c=tools.backName, backgroundColor=[0.284,0.352,0.352])
    cmds.textField("backName", w=200, h=30, placeholderText="_Back", text="")

    cmds.setParent("rename_layout")
    cmds.button(l=" Delete : Pasted__", w=290, c=tools.pasterdelete)

    ########## modify #################
    cmds.setParent("Model")
    cmds.frameLayout("Modify", w=290, cll=False)
    cmds.rowColumnLayout("Modify", w=290, nc=10)
    cmds.symbolButton(image=IM_Path + "/deleteHist.png", w=40, h=40, c=tools.deleteHistory)
    cmds.symbolButton(image=IM_Path + "/menuIconSelect.png", w=40, h=40, c=tools.SelectHierarchy)
    cmds.symbolButton(image=IM_Path + "/CenterPivot.png", w=40, h=40, c=tools.centerPivot)
    cmds.symbolButton(image=IM_Path + "/FreezeTransform.png", w=40, h=40, c=tools.freezeTrans)
    cmds.symbolButton(image=IM_Path + "/pivotReset.png", w=40, h=40, c=tools.resetPivot)
    cmds.symbolButton(image=IM_Path + "/match.png", w=40, h=40, c=tools.MatchTransform)
    cmds.symbolButton(image=IM_Path + "/unfreetransform.png", w=40, h=40, c=tools.unFreezeTrans)

    ########## polygon #################
    cmds.setParent("Model")
    cmds.frameLayout("Polygon", w=290, cll=False)
    cmds.rowColumnLayout("Polygon", w=290, nc=8)
    cmds.symbolButton(image=IM_Path + "/polyCube.png", w=35, h=35, c=tools.cubeAdd)
    cmds.symbolButton(image=IM_Path + "/polySphere.png", w=35, h=35, c=tools.sphereAdd)
    cmds.symbolButton(image=IM_Path + "/polyCylinder.png", w=35, h=35, c=tools.cylinderAdd)
    cmds.symbolButton(image=IM_Path + "/polyCone.png", w=35, h=35, c=tools.coneAdd)
    cmds.symbolButton(image=IM_Path + "/polyDisc.png", w=35, h=35, c=tools.discAdd)
    cmds.symbolButton(image=IM_Path + "/polyTorus.png", w=35, h=35, c=tools.torusAdd)
    cmds.symbolButton(image=IM_Path + "/polyPrism.png", w=35, h=35, c=tools.prismAdd)
    cmds.symbolButton(image=IM_Path + "/polyPyramid.png", w=35, h=35, c=tools.pyramidAdd)

    cmds.symbolButton(image=IM_Path + "/polyUnite.png", w=35, h=35, c=tools.CombinePolygons)
    cmds.symbolButton(image=IM_Path + "/polySeparate.png", w=35, h=35, c=tools.SeparatePolygon)
    cmds.symbolButton(image=IM_Path + "/polyBooleansUnion.png", w=35, h=35, c=tools.PolygonBooleanUnion)
    cmds.symbolButton(image=IM_Path + "/polyMergeToCenter.png", w=35, h=35, c=tools.MergeToCenter)
    cmds.symbolButton(image=IM_Path + "/polySmooth.png", w=35, h=35, c=tools.SmoothPolygon)
    cmds.symbolButton(image=IM_Path + "/polyReduce.png", w=35, h=35, c=tools.ReducePolygon)
    cmds.symbolButton(image=IM_Path + "/polyMirrorGeometry.png", w=35, h=35, c=tools.MirrorPolygonGeometryOptions)
    cmds.symbolButton(image=IM_Path + "/polyType.png", w=35, h=35, c=tools.CreatePolygonType)
    
    cmds.symbolButton(image=IM_Path + "/multiCut_NEX32.png", w=35, h=35, c=tools.dR_multiCutTool)
    cmds.symbolButton(image=IM_Path + "/weld_NEX32.png", w=35, h=35, c=tools.MergeVertexTool)
    cmds.symbolButton(image=IM_Path + "/polyDuplicateFacet.png", w=35, h=35, c=tools.DuplicateFace)
    cmds.symbolButton(image=IM_Path + "/polyBevel.png", w=35, h=35, c=tools.performBevelOrChamfer)
    cmds.symbolButton(image=IM_Path + "/polyBridge.png", w=35, h=35, c=tools.performBridgeOrFill)
    cmds.symbolButton(image=IM_Path + "/polyCleanup.png", w=35, h=35, c=tools.CleanupPolygon)
    cmds.symbolButton(image=IM_Path + "/polyFlip.png", w=35, h=35, c=tools.FlipMesh)
    cmds.symbolButton(image=IM_Path + "/polyAverageVertex.png", w=35, h=35, c=tools.AverageVertex)

    ########## sculp #################
    cmds.setParent("Model")
    cmds.frameLayout("Sculpting", w=290, cll=False)
    cmds.rowColumnLayout("Sculpting", w=290, nc=7)
    cmds.symbolButton(image=IM_Path + "/Sculpt.png", w=40, h=40, c=tools.SetMeshSculptTool)
    cmds.symbolButton(image=IM_Path + "/Smooth.png", w=40, h=40, c=tools.SetMeshSmoothTool)
    cmds.symbolButton(image=IM_Path + "/Relax.png", w=40, h=40, c=tools.SetMeshRelaxTool)
    cmds.symbolButton(image=IM_Path + "/Grab.png", w=40, h=40, c=tools.SetMeshGrabTool)
    cmds.symbolButton(image=IM_Path + "/Pinch.png", w=40, h=40, c=tools.SetMeshPinchTool)
    cmds.symbolButton(image=IM_Path + "/Flatten.png", w=40, h=40, c=tools.SetMeshFlattenTool)
    cmds.symbolButton(image=IM_Path + "/Foamy.png", w=40, h=40, c=tools.SetMeshFoamyTool)

    ########################################################################
    ########################################################################
    #################   Shader tab Layout     ##############################
    ########################################################################
    ########################################################################
    cmds.setParent(main_layout)
    cmds.columnLayout("Shader", w=290)

    cmds.setParent("Shader")
    cmds.frameLayout("Texture", w=290)
    cmds.rowColumnLayout("Texture", w=290, nc=7)
    cmds.symbolButton(image=IM_Path + "/out_file.png", w=40, h=40, c=sdr.addTexture)
    cmds.symbolButton(image=IM_Path + "/Raw_file.png", w=40, h=40, c=sdr.addTextureRaw)


    cmds.setParent("Shader")
    cmds.frameLayout("Shader", w=290)
    cmds.rowColumnLayout("Shader", w=290, nc=7)
    cmds.symbolButton(image=IM_Path + "/swmtl.png", w=55, h=55, c=sdr.swShadermtl)
    cmds.symbolButton(image=IM_Path + "/mtlBase.png", w=55, h=55, c=sdr.mtl_base)
    # cmds.symbolButton(image=IM_Path + "/swmtl.png", w=55, h=55)
    # cmds.symbolButton(image=IM_Path + "/swmtl.png", w=55, h=55)
    # cmds.symbolButton(image=IM_Path + "/swmtl.png", w=55, h=55)

    ########################################################################
    ########################################################################
    #################   Tools tab Layout     ###############################
    ########################################################################
    ########################################################################
    cmds.setParent(main_layout)
    cmds.columnLayout("Tools", w=290)

    cmds.setParent("Tools")
    cmds.frameLayout("Tools", w=290)
    cmds.rowColumnLayout("Check", w=290, nc=5)
    cmds.button(l="Name Space", w=70, h=25, c=ae.namespace)
    cmds.text(l="", w=10)
    cmds.button(l="On subs VRay", w=80, h=25, c=ae.makeVrayAttributes)
    cmds.text(l="", w=10)

    cmds.setParent("Tools")
    cmds.frameLayout("Ari tools", w=290)
    cmds.rowColumnLayout("Ari_tools", w=290, nc=5)
    cmds.symbolButton(image=IM_Path + "/AriCircleVertex.png", w=55, h=55, c=ae.AriCircleVertex)
    cmds.symbolButton(image=IM_Path + "/AriPolygonCounter.png", w=55, h=55, c=ae.AriPolygonCounter)
    cmds.symbolButton(image=IM_Path + "/AriSymmetryChecker.png", w=55, h=55, c=ae.AriSymmetryChecker)
    cmds.symbolButton(image=IM_Path + "/AriUVGridding.png", w=55, h=55, c=ae.AriUVFromVertexRatio)
    cmds.symbolButton(image=IM_Path + "/AriViewWindow.png", w=55, h=55, c=ae.AriViewWindow)
    cmds.symbolButton(image=IM_Path + "/Ari_tp.png", w=55, h=55, c=ae.AriTransferPosition)
    cmds.symbolButton(image=IM_Path + "/Ari_sv.png", w=55, h=55, c=ae.AriStraightVertex)
    cmds.symbolButton(image=IM_Path + "/Ari_dora.png", w=55, h=55, c=ae.DoraSkinWeightImpExp)
    # cmds.symbolButton(image=IM_Path + "/Ari_tp.png", w=55, h=55, c=ae.AriTransferPosition)
    # cmds.symbolButton(image=IM_Path + "/Ari_tp.png", w=55, h=55, c=ae.AriTransferPosition)

    ########################################################################
    ########################################################################
    #############################   About    ###############################
    ########################################################################
    ########################################################################
    cmds.setParent(main_layout)
    cmds.columnLayout("About", w=290)
    cmds.frameLayout("Click to button :", w=290)
    cmds.rowColumnLayout("Layer6", w=290, nc=5)
    # cmds.symbolButton(image=IM_Path +"/LogoGumroad.jpg", w=60, h=60, c=tools.openWebMessFB)
    cmds.text("                 ")
    cmds.symbolButton(image=IM_Path +"/gumroad.png", w=60, h=60, c=tools.openWebgumroad)
    cmds.text("                 ")

    cmds.symbolButton(image=IM_Path +"/Gmail_Icon.png", w=60, h=60, c=tools.openGmail)
    cmds.setParent("About")
    cmds.rowColumnLayout("Layer7", w=290, nc=3)
    cmds.button("Copy   ", w=100, c=tools.copyEmail)
    cmds.textField("Email", w=199, text="info.tri3d@gmail.com")
    cmds.setParent("About")
    cmds.columnLayout("duongdungrong", w=290)
    cmds.button(l="Update", w=290, h=30, backgroundColor=[1,0.774,0.108])
    cmds.button(l="Course Rigging", w=290, h=30, backgroundColor=[1,0.774,0.108], c=tools.openWebRiggingCause)
    cmds.image(image=IM_Path +"/LogoVega.jpg", w=290)

    cmds.showWindow(triVegaUiWD)

triVegaUi()    



