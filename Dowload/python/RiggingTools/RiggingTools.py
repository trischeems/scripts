###################################################################################################
######################################## Tools For Rigging ########################################
###################################################################################################
import maya.cmds as cmds
import maya.mel as mel
import sys
    
selectedList = cmds.ls(sl= 1)
controlersList = []
#################################### Start Windows functions ######################################
#### Start 'Controllers' Window ####
def ControllersWindow(*args):
    if cmds.window("Controllers" ,exists = True,rtf = True):
        cmds.deleteUI("Controllers")
    Controllers = cmds.window("Controllers",rtf = True,w=400)
    form_01 = cmds.formLayout(numberOfDivisions=100)
    B01 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/HalfSphereWithArrow_001.PBM', w= 72, h = 72, c = MakeController_001 )
    B02 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/HalfSphere_001.PBM'         , w= 72, h = 72, c = MakeController_002 )
    B03 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/Global_001.PBM'             , w= 72, h = 72, c = MakeController_003 )
    B04 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/Cylinder_001.PBM'           , w= 72, h = 72, c = MakeController_004 )
    B05 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/FourArrow_001.PBM'          , w= 72, h = 72, c = MakeController_005 )
    B06 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/Plus_001.PBM'               , w= 72, h = 72, c = MakeController_006 )
    B07 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/CircleOnLine_001.PBM'       , w= 72, h = 72, c = MakeController_007 )
    B08 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/BoomOnLine_001.PBM'         , w= 72, h = 72, c = MakeController_008 )
    B09 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/Refresh_001.PBM'            , w= 72, h = 72, c = MakeController_009 )
    B10 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/Square_001.PBM'             , w= 72, h = 72, c = MakeController_010 )
    B11 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/TwoCircleLine_001.PBM'      , w= 72, h = 72, c = MakeController_011 )
    B12 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/FlowerWithArrow_001.PBM'    , w= 72, h = 72, c = MakeController_012 )
    B13 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/Shoe_001.PBM'               , w= 72, h = 72, c = MakeController_013 )
    B14 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/Pyramid_001.PBM'            , w= 72, h = 72, c = MakeController_014 )
    B15 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/Diamond_001.PBM'            , w= 72, h = 72, c = MakeController_015 )
    B16 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/Eye_001.PBM'                , w= 72, h = 72, c = MakeController_016 )
    B17 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/ArrowCorner_001.PBM'        , w= 72, h = 72, c = MakeController_017 )
    B18 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/DoubleSideArrow_001.PBM'    , w= 72, h = 72, c = MakeController_018 )
    B19 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/SixArrow_001.PBM'           , w= 72, h = 72, c = MakeController_019 )
    B20 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/Sphere_001.PBM'             , w= 72, h = 72, c = MakeController_020 )
    B21 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/TwoTailArrow_001.PBM'       , w= 72, h = 72, c = MakeController_021 )
    B22 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/ThreeTailArrow_001.PBM'     , w= 72, h = 72, c = MakeController_022 )
    B23 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/CircleWithArrow_001.PBM'    , w= 72, h = 72, c = MakeController_023 )
    B24 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/Bow_001.PBM'                , w= 72, h = 72, c = MakeController_024 )
    B25 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/TwoBoldArrow_001.PBM'       , w= 72, h = 72, c = MakeController_025 )
    B26 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/Gizmo_001.PBM'              , w= 72, h = 72, c = MakeController_026 )
    B27 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/FourLeafFlower_001.PBM'     , w= 72, h = 72, c = MakeController_027 )
    B28 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/Wheel_001.PBM'              , w= 72, h = 72, c = MakeController_028 )
    B29 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/ArrowUp_001.PBM'            , w= 72, h = 72, c = MakeController_029 )
    B30 = cmds.symbolButton(hlc = [1,1,1], image ='RigTools/Hand_001.PBM'               , w= 72, h = 72, c = MakeController_030 )
    controllersColorSlider = cmds.colorIndexSliderGrp("colorIndexSlider",label='Select Color', min=0, max=32, value=0,dragCommand = overrideColor)
    
    cmds.formLayout( form_01, edit=True, attachForm=[
    (B01, 'top', 5 ),(B01, 'left', 4  ),
    (B02, 'top', 5 ),(B02, 'left', 70 ),
    (B03, 'top', 5 ),(B03, 'left', 136),
    (B04, 'top', 5 ),(B04, 'left', 202),
    (B05, 'top', 5 ),(B05, 'left', 268),
    (B06, 'top', 5 ),(B06, 'left', 334),
    (B07, 'top', 71 ),(B07, 'left', 4  ),
    (B08, 'top', 71 ),(B08, 'left', 70 ),
    (B09, 'top', 71 ),(B09, 'left', 136),
    (B10, 'top', 71 ),(B10, 'left', 202),
    (B11, 'top', 71 ),(B11, 'left', 268),
    (B12, 'top', 71 ),(B12, 'left', 334),
    (B13, 'top', 137 ),(B13, 'left', 4  ),
    (B14, 'top', 137 ),(B14, 'left', 70 ),
    (B15, 'top', 137 ),(B15, 'left', 136),
    (B16, 'top', 137 ),(B16, 'left', 202),
    (B17, 'top', 137 ),(B17, 'left', 268),
    (B18, 'top', 137 ),(B18, 'left', 334),
    (B19, 'top', 203 ),(B19, 'left', 4  ),
    (B20, 'top', 203 ),(B20, 'left', 70 ),
    (B21, 'top', 203 ),(B21, 'left', 136),
    (B22, 'top', 203 ),(B22, 'left', 202),
    (B23, 'top', 203 ),(B23, 'left', 268),
    (B24, 'top', 203 ),(B24, 'left', 334),
    (B25, 'top', 269 ),(B25, 'left', 4  ),
    (B26, 'top', 269 ),(B26, 'left', 70 ),
    (B27, 'top', 269 ),(B27, 'left', 136),
    (B28, 'top', 269 ),(B28, 'left', 202),
    (B29, 'top', 269 ),(B29, 'left', 268),
    (B30, 'top', 269 ),(B30, 'left', 334),
    (controllersColorSlider, 'top', 360 ),(controllersColorSlider, 'left', 0)
    ] )

    cmds.showWindow(Controllers)

def overrideColor(*args):
    sel = cmds.ls(sl=1)
    colorIndexSlider = cmds.colorIndexSliderGrp("colorIndexSlider", q=True, value=True)
    for i in sel:
        print(i)
        cmds.setAttr(i + ".overrideEnabled", 1)
        cmds.setAttr(i + ".overrideColor", colorIndexSlider)

    #### End 'Controllers' Window ####
def RiggingTools(*args):
    buttonHeigh = 25
    seperatorHeigh = 10
    objName = cmds.ls(sl = 1)
    if cmds.window("RiggingTools" ,exists = True,rtf = True):
        cmds.deleteUI("RiggingTools")
    RiggingTools = cmds.window("RiggingTools",rtf = True,w=400)
    form = cmds.formLayout()
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
    #### Start 'Create' Tab ####
    child1 = cmds.rowColumnLayout( numberOfColumns=3, columnWidth=[(1, 150), (2, 150), (3, 150)])
    
    cmds.separator(style = "none" , h = 10 )
    cmds.separator(style = "none" , h = 10 )
    cmds.separator(style = "none" , h = 10 )
    cmds.separator(style = "shelf", h = 10 )
    cmds.text("Object On Curve")
    cmds.separator(style = "shelf", h = 10 )
    cmds.separator(style = "none" , h = 10 )
    cmds.separator(style = "none" , h = 10 )
    cmds.separator(style = "none" , h = 10 )
    cmds.separator(style = "none" , h = 10 )
    cmds.separator(style = "none" , h = 10 )
    cmds.separator(style = "none" , h = 10 )
    cmds.optionMenu( "ObjectTypeOnCurve" ,label='Type' )
    cmds.menuItem("Joint"  , label = 'Joint'  )
    cmds.menuItem("Circle" , label = 'Circle' )
    cmds.menuItem("Locator", label = 'Locator')
    cmds.menuItem("Sphere" , label = 'Sphere' )
    cmds.text("Object Amount :        ")
    cmds.intField("ObjectAmount", min = 1, v = 1)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.checkBox("AtachOnCurve", label = "Atach On Curve", v = 0)
    cmds.checkBox("PathRotation", label = "PathRotation"  , v = 0)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.checkBox("Hirarchy", label = "Hirarchy")
    cmds.checkBox("ParametricLength", label = "Parametric Length", v = 0)
    cmds.button("MakeObject", w = 10, bgc = [0.4,0.69,0.67], c = Object0nCurve)
    cmds.separator(style = "none" , h = 10)
    cmds.separator(style = "none" , h = 10)
    cmds.separator(style = "none" , h = 10)
    cmds.separator(style = "shelf", h = 10)
    cmds.text("Joint On Selected")
    cmds.separator(style = "shelf", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.checkBox( "HirarchyJoints"          ,label = 'Hirarchy joints ?', v = False, h = 25)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.checkBox( "WorldRotation", label = "World Rotation ?", v = False, h = 25 )
    cmds.textField("NewJointName" , pht   = "Joint/s Name"    , h = 25   , w = 170)
    cmds.button("MakeJoint", w = 150, c = MakeJoint, h = 22, bgc = [0.4,0.69,0.67])
    cmds.separator(style = "none" , h = 10)
    cmds.separator(style = "none" , h = 10)
    cmds.separator(style = "none" , h = 10)
    cmds.separator(style = "none" , h = 10)
    cmds.separator(style = "none" , h = 10)
    cmds.separator(style = "none" , h = 10)
    cmds.separator(style = "shelf", h = 10)
    cmds.text("Make Controler")
    cmds.separator(style = "shelf", h = 10)
    cmds.separator(style = "none" , h = 10)
    cmds.separator(style = "none" , h = 10)
    cmds.separator(style = "none" , h = 10)
    cmds.textField("NewControllerNameField", pht = "controller/s Name", h = 25, w = 170)
    cmds.text("Controller Group/s")
    cmds.intField("controllerGroups",min = 0 , v = 1 , w = 50)
    cmds.separator(style = "none" ,h = 10)
    cmds.separator(style = "none" ,h = 10)
    cmds.separator(style = "none" ,h = 10)
    cmds.checkBox("HirarchyControllers",label='HirarchyControllers ?' , v = False,h = 25)
    cmds.text("Controller Scale")
    cmds.floatField("controllerScale",pre = 3 ,min = 0 , v = 1 , w = 50)
    cmds.separator(style = "none" ,h = 10)
    cmds.separator(style = "none" ,h = 10)
    cmds.separator(style = "none" ,h = 10)
    cmds.checkBox("parentConstraint", label = 'ParentConstraint ?' , v = False, h = 25)
    cmds.checkBox("scaleConstraint" , label = 'ScaleConstraint ?'  , v = False, h = 25)
    cmds.separator(style = "none" ,h = 10)
    cmds.separator(style = "none" ,h = 10)
    cmds.separator(style = "none" ,h = 10)
    cmds.separator(style = "none" ,h = 10)
    cmds.separator(style = "none" ,h = 10)
    cmds.text('Rotation Offset')
    cmds.separator(style = "none" ,h = 10)
    cmds.separator(style = "none" ,h = 10)
    cmds.separator(style = "none" ,h = 10)
    cmds.separator(style = "none" ,h = 10)
    cmds.floatField('rotationOffsetX', v=0, w = 10)
    cmds.floatField('rotationOffsetY', v=0, w = 10)
    cmds.floatField('rotationOffsetZ', v=0, w = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.button("Controllers" , c =ControllersWindow , bgc = [0.4,0.69,0.67] )
    cmds.separator(style="none",h=10)
    cmds.separator(style = "none" , h = 35)
    cmds.separator(style = "none" , h = 35)
    cmds.separator(style = "none" , h = 35)
    cmds.separator(style = "shelf", h = 10)
    cmds.separator(style = "shelf", h = 10)
    cmds.separator(style = "shelf", h = 10)
    cmds.setParent( '..' )
    #### End 'Create' Tab ####
    #### Start 'Rename' Tab ####
    child2 = cmds.rowColumnLayout(numberOfColumns = 3, columnWidth = [(1, 150), (2, 150), (3, 150)] )
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "shelf", h = seperatorHeigh)
    cmds.text("ReName", fn = "boldLabelFont")
    cmds.separator(style = "shelf",h = seperatorHeigh)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.intFieldGrp("Start"     , label = "Start"  , v1 = 1, h = buttonHeigh, adj = 1)
    cmds.intFieldGrp("StepNumber", label = "Step"   , v1 = 1, h = buttonHeigh, adj = 1)
    cmds.intFieldGrp("Padding"   , label = "Padding", v1 = 2, h = buttonHeigh, adj = 1)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.checkBox("hirarchyRename", label = "hirarchy Rename", v = False)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.textField("Rename", pht = "Rename",h = 20)
    cmds.textField("ObjectType", pht = "ObjectType : jnt , geo , etc ...",h=20)
    cmds.button("Rename", c = Rename, h = 20, bgc = [0.4,0.69,0.67])
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style = "none", h = 10)
    cmds.separator(style="shelf",h=seperatorHeigh)
    cmds.text("Search And Replace",fn="boldLabelFont")
    cmds.separator(style="shelf",h=seperatorHeigh)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=seperatorHeigh)
    cmds.separator(style="none",h=seperatorHeigh)
    cmds.checkBox("SearchAndReplace",label='Replace All',h=20)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.textField("Search", pht = "Search",h=20)
    cmds.textField("Replace", pht = "Replace",h=20)
    cmds.button("SearchAndReplace", c = SearchAndReplace,h=20, bgc = [0.4,0.69,0.67])
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="shelf",h=seperatorHeigh)
    cmds.text("Add Prefix / Suffix",fn="boldLabelFont")
    cmds.separator(style="shelf",h=seperatorHeigh)
    cmds.separator(style="none",h=20)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.text("Add Prefix")
    cmds.textField("Prefix", pht = "Prefix_####" ,h=20)
    cmds.button("Add To Start",c = Prefix, bgc = [0.4,0.69,0.67],h=20)
    cmds.separator(style="none",h=seperatorHeigh)
    cmds.separator(style="none",h=seperatorHeigh)
    cmds.separator(style="none",h=seperatorHeigh)
    cmds.text("Add Suffix")
    cmds.textField("Suffix", pht = "####_Suffix",h=20)
    cmds.button("Add To End",c = Suffix,h=20, bgc = [0.4,0.69,0.67])
    cmds.separator(style="none",h=seperatorHeigh)
    cmds.separator(style="none",h=seperatorHeigh)
    cmds.separator(style="none",h=seperatorHeigh)
    cmds.separator(style="shelf",h=seperatorHeigh )
    cmds.text("Remove One Start / End",fn="boldLabelFont")
    cmds.separator(style="shelf",h=seperatorHeigh )
    cmds.separator(style="none",h=20)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.text("IndexOfStart")
    cmds.intField("IndexOfStart" , v = 1,h=20 )
    cmds.button("RemoveOneStart",label = "- <---Remove One Start", c = RemoveOneStart,h=20, bgc = [0.4,0.69,0.67])    
    cmds.text("IndexOfEnd")
    cmds.intField("IndexOfEnd" , v = 1,h=20 )
    cmds.button("RemoveOneEnd" ,label = "Remove One End---> - ", c = RemoveOneEnd,h=20, bgc = [0.4,0.69,0.67])
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="shelf",h=seperatorHeigh)
    cmds.text("Add Letter On Index",fn="boldLabelFont" )
    cmds.separator(style="shelf",h=seperatorHeigh)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=20)
    cmds.intFieldGrp("LetterIndex",label = "Letter Index" , v1 = 1,h=20 ,adj = 1)
    cmds.textField("LetterOnIndex", pht = "Letter On Index ...",h=22)
    cmds.button("AddLetter",label = "Add Letter/s",h=20, c = LetterOnIndex, bgc = [0.4,0.69,0.67])
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="shelf",h=seperatorHeigh)
    cmds.text("Search Object With Letter",fn="boldLabelFont")
    cmds.separator(style="shelf",h=seperatorHeigh)
    cmds.separator(style="none",h=20)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.textField("SearchObjectWithLetter", pht = "Search Object With...",h=20)
    cmds.button("SearchObjectWithLetter",label = "Select Object/s",h=20, c = selectObjectWithLetters, bgc = [0.4,0.69,0.67])
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="shelf",h=seperatorHeigh)
    cmds.separator(style="shelf",h=seperatorHeigh)
    cmds.separator(style="shelf",h=seperatorHeigh)
    cmds.setParent( '..' )
    #### End 'Rename' Tab ####
    #### Start 'Tools_01' Tab ####
    child3 = cmds.rowColumnLayout( numberOfColumns=3,columnWidth=[(1, 150), (2, 150), (3, 150)])
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="shelf",h=10)
    cmds.text("Mirror")
    cmds.separator(style="shelf",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.checkBox("Duplicate",label="Duplicate",v=0)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.button("MirrorX",label = "MirrorX",h=buttonHeigh, c = MirrorX, bgc = [0.4,0.69,0.67])
    cmds.button("MirrorY",label = "MirrorY",h=buttonHeigh, c = MirrorY, bgc = [0.4,0.69,0.67])
    cmds.button("MirrorZ",label = "MirrorZ",h=buttonHeigh, c = MirrorZ, bgc = [0.4,0.69,0.67])
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="shelf",h=10)
    cmds.text(" Align , Lock , Hide")
    cmds.separator(style="shelf",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.checkBox("Translate",label="Translate",v=0, cc =TranslateCheckBox )
    cmds.checkBox("Rotate",label="Rotate",v=0, cc =RotateCheckBox)
    cmds.checkBox("Scale",label="Scale",v=0, cc =ScaleCheckBox)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.checkBox("TX",label="TX",v=0)
    cmds.checkBox("RX",label="RX",v=0)
    cmds.checkBox("SX",label="SX",v=0)
    cmds.checkBox("TY",label="TY",v=0)
    cmds.checkBox("RY",label="RY",v=0)
    cmds.checkBox("SY",label="SY",v=0)
    cmds.checkBox("TZ",label="TZ",v=0)
    cmds.checkBox("RZ",label="RZ",v=0)
    cmds.checkBox("SZ",label="SZ",v=0)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.button("Hide",label = "Hide Selected",h=buttonHeigh, c = HideSelected, bgc = [0.4,0.69,0.67])
    cmds.button("Lock",label = "Lock Selected",h=buttonHeigh, c = LockSelected, bgc = [0.4,0.69,0.67])
    cmds.button("Align" ,h=buttonHeigh,c=AlignSelected                        , bgc = [0.4,0.69,0.67])
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="shelf",h=10)
    cmds.text("Constraints")
    cmds.separator(style="shelf",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.checkBox("MaintainOffset",label="Maintain Offset",v=1)
    cmds.separator(style="none",h=10)
    cmds.button("ParentConstraint",label = "Parent Constraint" ,h=buttonHeigh, c = ParentConstraint , bgc = [0.4,0.69,0.67])
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.button("PointConstraint" ,label = "Point Constraint"  ,h=buttonHeigh,c = PointConstraint , bgc = [0.4,0.69,0.67])
    cmds.button("OrientConstraint",label = "Orient Constraint" ,h=buttonHeigh,c = OrientConstraint, bgc = [0.4,0.69,0.67])
    cmds.button("ScaleConstraint" ,label = "Scale Constraint"  ,h=buttonHeigh,c = ScaleConstraint , bgc = [0.4,0.69,0.67])
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="shelf",h=10)
    cmds.text("Parent")
    cmds.separator(style="shelf",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.button("Parent"      ,label = "Parent"      ,h=buttonHeigh , c = MakeHirarchyObjects, bgc = [0.4,0.69,0.67])
    cmds.button("UnParent"    ,label = "UnParent"    ,h=buttonHeigh , c = UnParentObjects    , bgc = [0.4,0.69,0.67])
    cmds.button("ReversParent",label = "ReversParent",h=buttonHeigh , c = ReversParent       , bgc = [0.4,0.69,0.67])
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="shelf",h=15)
    cmds.text("Extra Tools")
    cmds.separator(style="shelf",h=15)
    cmds.separator(style="none" ,h=10)
    cmds.separator(style="none" ,h=10)
    cmds.separator(style="none" ,h=10)
    cmds.button("FreezeTransform",label = "FreezeTransform",h=buttonHeigh , c = FreezeTransform, bgc = [0.4,0.69,0.67])
    cmds.button("CombineShapes",label = "Combine Shapes",h=buttonHeigh , c = CombineCurves, bgc = [0.4,0.69,0.67])
    cmds.button("CenterPivot"  ,label = "Center Pivot"  ,h=buttonHeigh , c = CenterPivot  , bgc = [0.4,0.69,0.67])
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="shelf",h=10)
    cmds.text("Skinning")
    cmds.separator(style="shelf",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.button("BindSkin",label = "Bind Skin",h=buttonHeigh, c = "mel.eval('SmoothBindSkinOptions;')", bgc = [0.4,0.69,0.67])
    cmds.button("UnBindSkin",label = "UnBind Skin",h=buttonHeigh, c = "mel.eval('DetachSkinOptions;')", bgc = [0.4,0.69,0.67])
    cmds.button("SelectSkinedJoint",label = "Select Skined Joint",h=buttonHeigh , c = SelectSkinedJoints, bgc = [0.4,0.69,0.67])
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="none",h=10)
    cmds.separator(style="shelf",h=10)
    cmds.separator(style="shelf",h=10)
    cmds.separator(style="shelf",h=10)
    cmds.setParent( '..'  )
    #### End 'Tools_01' Tab ####
    cmds.tabLayout( tabs, edit=True, tabLabel=((child1, 'Create'), (child2, 'Rename'), (child3, 'Tools_01')) )
    cmds.showWindow(RiggingTools)
    #####################################  End Windows functions ######################################
    ######################################### Start Functions #########################################
    #### Start Make Controller Functions ####

def MakeController_030(*args):
    AddControllers(30)
def MakeController_029(*args):
    AddControllers(29)
def MakeController_028(*args):
    AddControllers(28)
def MakeController_027(*args):
    AddControllers(27)
def MakeController_026(*args):
    AddControllers(26)
def MakeController_025(*args):
    AddControllers(25)
def MakeController_024(*args):
    AddControllers(24)
def MakeController_023(*args):
    AddControllers(23)
def MakeController_022(*args):
    AddControllers(22)
def MakeController_021(*args):
    AddControllers(21)
def MakeController_020(*args):
    AddControllers(20)
def MakeController_019(*args):
    AddControllers(19)
def MakeController_018(*args):
    AddControllers(18)
def MakeController_017(*args):
    AddControllers(17)
def MakeController_016(*args):
    AddControllers(16)
def MakeController_015(*args):
    AddControllers(15)
def MakeController_014(*args):
    AddControllers(14)
def MakeController_013(*args):
    AddControllers(13)
def MakeController_012(*args):
    AddControllers(12)
def MakeController_011(*args):
    AddControllers(11)
def MakeController_010(*args):
    AddControllers(10)
def MakeController_009(*args):
    AddControllers(9)
def MakeController_008(*args):
    AddControllers(8)
def MakeController_007(*args):
    AddControllers(7)
def MakeController_006(*args):
    AddControllers(6)
def MakeController_005(*args):
    AddControllers(5)
def MakeController_004(*args):
    AddControllers(4)
def MakeController_003(*args):
    AddControllers(3)
def MakeController_002(*args):
    AddControllers(2)
def MakeController_001(*args):
    AddControllers(1)
    #### End Make Controller Functions ####

def Rename(*args):
    selList = []
    ObjectsList = []
    Renaming = cmds.textField("Rename", q = True , text = True)
    SelectedType = cmds.textField("ObjectType", q = True , text = True)
    StepNumber = cmds.intFieldGrp("StepNumber" ,q = True,v1 = True)
    StartNum = cmds.intFieldGrp("Start" , q = True , v1 = True)
    PaddingNum = cmds.intFieldGrp("Padding" , q = True , v1 = True)
    hirarchyRename = cmds.checkBox("hirarchyRename",q = True , v = True)
    sel = cmds.ls(sl = True)
    if Renaming == "":
        cmds.warning("Enter Name ...")
        sys.exit()
    if hirarchyRename == 1:
        if cmds.objectType( sel, isType='joint' ) == 1 :
            cmds.select(hi = 1 ,add = 1)
            sel = cmds.ls(sl = True)
            index = 0
            for i in range(len(sel)):
                selList.append(sel[index])
                if len(sel) > index+1:
                    index +=1
            cmds.select(selList)
        else:
            cmds.select(hi = 1 ,add = 1)
            sel = cmds.ls(sl = True)
            index = 0
            for i in range(len(sel)/2):
                selList.append(sel[index])
                if len(sel) > index+1:
                    index +=2
            cmds.select(selList)
    sel = cmds.ls(sl = True)
    
    if hirarchyRename == 0:
        sel = cmds.ls(sl = 1)
    objIndx = 0
    for obj in sel:
        objIndx -= 1
        try:
            PrepareName = cmds.rename(sel[objIndx], "PrepareForRename"+str(abs(StartNum)).zfill(abs(PaddingNum)))
        except:
            continue
        if StepNumber>0:
            StartNum += StepNumber
        if StepNumber<1:
            cmds.warning("Step Number Must Be 1 or higher !")
            StartNum += 1
        ObjectsList.append(PrepareName)
    
    StartNum = cmds.intFieldGrp("Start" , q = True , v1 = True)
    objIndx = 0
    for obj in ObjectsList:
        objIndx -= 1
        if SelectedType == "":
            try:
                NewName = cmds.rename(ObjectsList[objIndx], Renaming + "_" +str(abs(StartNum)).zfill(abs(PaddingNum)))
            except:
                continue
        if SelectedType != "":
            try:
                NewName = cmds.rename(ObjectsList[objIndx], Renaming + "_" +SelectedType +"_"+str(abs(StartNum)).zfill(abs(PaddingNum)))
            except:
                continue
        if StepNumber>0:
            StartNum += StepNumber
        if StepNumber<1:
            cmds.warning("Step Number Must Be 1 or higher !")
            StartNum += 1
    ObjectsList = []
    
def LetterOnIndex(*args):
    LetterIndex = cmds.intFieldGrp("LetterIndex",q = True, v1 = True)
    LetterOnIndex = cmds.textField("LetterOnIndex", q = True, text = True)
    sel = cmds.ls(sl = 1)
    index = LetterIndex-1
    if LetterIndex >0:
        try:
            for obj in sel:
                if LetterIndex <= len(obj):
                    cmds.rename(obj,obj[:LetterIndex-1]+LetterOnIndex+obj[LetterIndex-1:])
                    print(obj)
                else:
                    cmds.warning("The Object Name Is Less Than Letter Index !")
        except:
            print("An exception occurred")
    else:
        cmds.warning("LetterIndex Must Be 0 or higher !")
    
def SearchAndReplace(*args):
    sel = cmds.ls(sl = 1)
    Search = cmds.textField("Search", q = True , text = True)
    Replace = cmds.textField("Replace", q = True , text = True)
    ReplaceCountCheck = cmds.checkBox("SearchAndReplace",q = True,value=True)
    try:
        for obj in sel:
            ReplaceCount = 1
            if ReplaceCountCheck == True:
                ReplaceCount = 1000
            newName = obj.replace(Search,Replace ,ReplaceCount)
            cmds.rename(obj,newName)
            print(obj)
    except:
        print("An exception occurred")
    
def selectObjectWithLetters(*args):
    objectsList=[]
    cmds.select(all=True ,hi=True )
    sel = cmds.ls(sl = 1)
    SearchForObject = cmds.textField("SearchObjectWithLetter", q = True , text = True)
    if SearchForObject == "":
        cmds.warning("Enter Some Letters In Search Field !")
        cmds.select(clear=True)
    if SearchForObject != "":
        try:
            for obj in sel:
                if SearchForObject in obj:
                    objectsList.append(obj)
        except:
            print("An exception occurred")
        cmds.select(clear=True)
        if len(objectsList)>0:
            for exist in objectsList:
                cmds.select(exist , add=True)
        if len(objectsList)== 0:
            cmds.warning( "Any Object/s Found With This Name !")
    
def Prefix(*args):
    sel = cmds.ls(sl = 1)
    Prefix = cmds.textField("Prefix", q = True , text = True)
    try:
        for obj in sel:
            cmds.rename(obj,Prefix + obj)
            print(obj)
    except:
        print("An exception occurred")
    
def Suffix(*args):
    sel = cmds.ls(sl = 1)
    Suffix = cmds.textField("Suffix", q = True , text = True)
    try:
        for obj in sel:
            cmds.rename(obj,obj+Suffix)
            print(obj)
    except:
        print("An exception occurred")
    
def RemoveOneStart(*args):
    IndexOfStart = cmds.intField("IndexOfStart",q = True, v = True)
    sel = cmds.ls(sl = 1)
    for obj in sel:
        objLen = len(obj)
        if IndexOfStart <= objLen and IndexOfStart > 0:
            First = obj[:IndexOfStart-1]
            Last = obj[IndexOfStart:]
            NewName = First+Last
            cmds.rename(obj,NewName)
        else:
            cmds.warning("Index Of End Must Be equal or Less Than Selected Name Length !")
    
def RemoveOneEnd(*args):
    IndexOfEnd = cmds.intField("IndexOfEnd",q = True, v = True)
    sel = cmds.ls(sl = 1)
    for obj in sel:
        objLen = len(obj)
        if IndexOfEnd <= objLen and IndexOfEnd > 0:
            First = obj[:objLen-IndexOfEnd]
            Last = obj[objLen-IndexOfEnd+1:]
            NewName = First+Last
            cmds.rename(obj,NewName)
        else:
            cmds.warning("Index Of End Must Be equal or Less Than Selected Name Length !")
    
def AddControllers(ControllerType):
    global controlersList
    HirarchyList = []
    controllerNameNum = 1
    controllerGrpNameNum = 1
    HirarchyControllers = cmds.checkBox("HirarchyControllers",q= True, v = False)
    rotationOffsetX = cmds.floatField('rotationOffsetX',  q=True,  v=True)
    rotationOffsetY = cmds.floatField('rotationOffsetY',  q=True,  v=True)
    rotationOffsetZ = cmds.floatField('rotationOffsetZ',  q=True,  v=True)
    controllerScale = cmds.floatField("controllerScale",q= True ,v = True)
    scaleConstraintStatue = cmds.checkBox( "scaleConstraint", q=True , v = True)
    parentConstraintStatue = cmds.checkBox( "parentConstraint",q = True, v = True)
    controllerGroupNum = cmds.intField("controllerGroups" , q = True , v=True )
    ControllerName = cmds.textField("NewControllerNameField", q = True , text = True)
    controllerList = []
    sel = cmds.ls(sl = True)
    if len(sel) > 0:
        for obj in sel:
            controllerList.append(obj)
            if ControllerType == 1:
                newController = mel.eval("curve -d 1 -p 1 0 0 -p 0.951057 0 0.309017 -p 0.809017 0 0.587785 -p 0.587785 0 0.809017 -p 0.309017 0 0.951057 -p -2.98023e-08 0 1 -p -0.309017 0 0.951057 -p -0.587785 0 0.809017 -p -0.809017 0 0.587785 -p -0.951057 0 0.309017 -p -1 0 0 -p -0.951057 0 -0.309017 -p -0.809017 0 -0.587785 -p -0.587785 0 -0.809017 -p -0.309017 0 -0.951057 -p 0 0 -1 -p 0.309017 0 -0.951057 -p 0.587786 0 -0.809017 -p 0.809018 0 -0.587786 -p 0.951057 0 -0.309017 -p 1 0 0 -p 0.987688 0.156434 0 -p 0.951057 0.309017 0 -p 0.891007 0.453991 0 -p 0.809017 0.587785 0 -p 0.707107 0.707107 0 -p 0.587785 0.809017 0 -p 0.453991 0.891007 0 -p 0.309017 0.951057 0 -p 0.156434 0.987688 0 -p 0 1 0 -p -0.156435 0.987688 0 -p -0.309017 0.951057 0 -p -0.453991 0.891007 0 -p -0.587785 0.809017 0 -p -0.707107 0.707107 0 -p -0.809017 0.587785 0 -p -0.891007 0.453991 0 -p -0.951057 0.309017 0 -p -0.987689 0.156434 0 -p -1 0 0 -p -0.951057 0 -0.309017 -p -0.809017 0 -0.587785 -p -0.587785 0 -0.809017 -p -0.309017 0 -0.951057 -p 0 0 -1 -p 0 0.156434 -0.987689 -p 0 0.309017 -0.951057 -p 0 0.453991 -0.891007 -p 0 0.587785 -0.809017 -p 0 0.707107 -0.707107 -p 0 0.809017 -0.587786 -p 0 0.891007 -0.453991 -p 0 0.951057 -0.309017 -p 0 0.987688 -0.156435 -p 0 1 0 -p -4.66211e-09 0.987688 0.156434 -p -9.20942e-09 0.951057 0.309017 -p -1.353e-08 0.891007 0.453991 -p -1.75174e-08 0.809017 0.587785 -p -2.10734e-08 0.707107 0.707107 -p -2.41106e-08 0.587785 0.809017 -p -2.65541e-08 0.453991 0.891007 -p -2.83437e-08 0.309017 0.951057 -p -2.94354e-08 0.156434 0.987688 -p -2.98023e-08 0 1 -p 0 0 0 -p 0 0 -1 -p -0.309017 0 -0.951057 -p -0.587785 0 -0.809017 -p -0.809017 0 -0.587785 -p -0.951057 0 -0.309017 -p -1 0 0 -p 0 0 0 -p 1 0 0 -p 0 0 0 -p 0 1 0 -p 0 1.784043 0 -p 0 2.873933 0 -p 0.544945 1.784043 0 -p 0.518274 1.784043 -0.168397 -p 0.44087 1.784043 -0.320311 -p 0.320311 1.784043 -0.44087 -p 0.168397 1.784043 -0.518274 -p 0 1.784043 -0.544945 -p -0.168397 1.784043 -0.518274 -p -0.320311 1.784043 -0.44087 -p -0.44087 1.784043 -0.320311 -p -0.518274 1.784043 -0.168397 -p -0.544945 1.784043 0 -p -0.518274 1.784043 0.168397 -p -0.44087 1.784043 0.320311 -p -0.320311 1.784043 0.44087 -p -0.168397 1.784043 0.518274 -p -1.62406e-08 1.784043 0.544945 -p 0.168397 1.784043 0.518274 -p 0.320311 1.784043 0.44087 -p 0.44087 1.784043 0.320311 -p 0.518274 1.784043 0.168397 -p 0.544945 1.784043 0 -p 0 2.873933 0 -p -1.62406e-08 1.784043 0.544945 -p 0 2.873933 0 -p -0.544945 1.784043 0 -p 0 2.873933 0 -p 0 1.784043 -0.544945 -p 0 2.873933 0 -p 0.518274 1.784043 -0.168397 -p 0 2.873933 0 -p 0.44087 1.784043 -0.320311 -p 0 2.873933 0 -p 0.320311 1.784043 -0.44087 -p 0 2.873933 0 -p 0.168397 1.784043 -0.518274 -p 0 2.873933 0 -p -0.168397 1.784043 -0.518274 -p 0 2.873933 0 -p -0.320311 1.784043 -0.44087 -p 0 2.873933 0 -p -0.44087 1.784043 -0.320311 -p 0 2.873933 0 -p -0.518274 1.784043 -0.168397 -p 0 2.873933 0 -p -0.518274 1.784043 0.168397 -p 0 2.873933 0 -p -0.44087 1.784043 0.320311 -p 0 2.873933 0 -p -0.320311 1.784043 0.44087 -p 0 2.873933 0 -p -0.168397 1.784043 0.518274 -p 0 2.873933 0 -p 0.168397 1.784043 0.518274 -p 0 2.873933 0 -p 0.320311 1.784043 0.44087 -p 0 2.873933 0 -p 0.44087 1.784043 0.320311 -p 0 2.873933 0 -p 0.518274 1.784043 0.168397 -p 0 2.873933 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 -k 70 -k 71 -k 72 -k 73 -k 74 -k 75 -k 76 -k 77 -k 78 -k 79 -k 80 -k 81 -k 82 -k 83 -k 84 -k 85 -k 86 -k 87 -k 88 -k 89 -k 90 -k 91 -k 92 -k 93 -k 94 -k 95 -k 96 -k 97 -k 98 -k 99 -k 100 -k 101 -k 102 -k 103 -k 104 -k 105 -k 106 -k 107 -k 108 -k 109 -k 110 -k 111 -k 112 -k 113 -k 114 -k 115 -k 116 -k 117 -k 118 -k 119 -k 120 -k 121 -k 122 -k 123 -k 124 -k 125 -k 126 -k 127 -k 128 -k 129 -k 130 -k 131 -k 132 -k 133 -k 134 -k 135 -k 136 -k 137 -k 138 ;")
            if ControllerType == 2:
                newController = mel.eval("curve -d 1 -p -1 0 -5.96046e-08 -p -0.965926 0 0.258819 -p -0.866025 0 0.5 -p -0.707107 0 0.707107 -p -0.5 0 0.866025 -p -0.258819 0 0.965926 -p -2.98023e-08 0 1 -p 0.258819 0 0.965926 -p 0.5 0 0.866025 -p 0.707107 0 0.707107 -p 0.866025 0 0.5 -p 0.965926 0 0.258819 -p 1 0 0 -p 0.965925 0 -0.258819 -p 0.866025 0 -0.5 -p 0.707106 0 -0.707106 -p 0.5 0 -0.866025 -p 0.258819 0 -0.965925 -p 1.19209e-07 0 -0.999999 -p -0.258819 0 -0.965925 -p -0.5 0 -0.866025 -p -0.707106 0 -0.707107 -p -0.866025 0 -0.5 -p -0.965926 0 -0.258819 -p -1 0 -5.96046e-08 -p -0.987688 0.156434 -5.88708e-08 -p -0.951056 0.309017 -5.66874e-08 -p -0.891006 0.453991 -5.31081e-08 -p -0.809017 0.587785 -4.82212e-08 -p -0.707107 0.707107 -4.21468e-08 -p -0.587785 0.809017 -3.50347e-08 -p -0.45399 0.891007 -2.70599e-08 -p -0.309017 0.951057 -1.84188e-08 -p -0.156434 0.987688 -9.32422e-09 -p 0 1 0 -p 0.156434 0.987688 0 -p 0.309017 0.951057 0 -p 0.453991 0.891007 0 -p 0.587785 0.809017 0 -p 0.707107 0.707107 0 -p 0.809017 0.587785 0 -p 0.891007 0.453991 0 -p 0.951057 0.309017 0 -p 0.987688 0.156434 0 -p 1 0 0 -p 0.965925 0 -0.258819 -p 0.866025 0 -0.5 -p 0.707106 0 -0.707106 -p 0.5 0 -0.866025 -p 0.258819 0 -0.965925 -p 1.19209e-07 0 -0.999999 -p 1.17742e-07 0.156434 -0.987688 -p 1.13375e-07 0.309017 -0.951056 -p 1.06216e-07 0.453991 -0.891006 -p 9.64423e-08 0.587785 -0.809017 -p 8.42937e-08 0.707107 -0.707106 -p 7.00695e-08 0.809017 -0.587785 -p 5.41199e-08 0.891007 -0.45399 -p 3.68377e-08 0.951057 -0.309017 -p 1.86484e-08 0.987688 -0.156434 -p 0 1 0 -p -4.66211e-09 0.987688 0.156434 -p -9.20942e-09 0.951057 0.309017 -p -1.353e-08 0.891007 0.45399 -p -1.75174e-08 0.809017 0.587785 -p -2.10734e-08 0.707107 0.707107 -p -2.41106e-08 0.587785 0.809017 -p -2.65541e-08 0.453991 0.891006 -p -2.83437e-08 0.309017 0.951056 -p -2.94354e-08 0.156434 0.987688 -p -2.98023e-08 0 1 -p 0.258819 0 0.965926 -p 0.5 0 0.866025 -p 0.707107 0 0.707107 -p 0.698401 0.156434 0.698401 -p 0.672498 0.309017 0.672499 -p 0.630037 0.453991 0.630037 -p 0.572061 0.587785 0.572061 -p 0.5 0.707107 0.5 -p 0.415627 0.809017 0.415627 -p 0.32102 0.891007 0.32102 -p 0.218508 0.951057 0.218508 -p 0.110616 0.987688 0.110616 -p 0 1 0 -p -0.110616 0.987688 -0.110616 -p -0.218508 0.951057 -0.218508 -p -0.32102 0.891007 -0.32102 -p -0.415627 0.809017 -0.415627 -p -0.5 0.707107 -0.5 -p -0.572061 0.587785 -0.572061 -p -0.630036 0.453991 -0.630037 -p -0.672498 0.309017 -0.672498 -p -0.698401 0.156434 -0.698401 -p -0.707106 0 -0.707107 -p -0.5 0 -0.866025 -p -0.258819 0 -0.965925 -p 1.19209e-07 0 -0.999999 -p 0.258819 0 -0.965925 -p 0.5 0 -0.866025 -p 0.707106 0 -0.707106 -p 0.698401 0.156434 -0.698401 -p 0.672498 0.309017 -0.672498 -p 0.630036 0.453991 -0.630036 -p 0.572061 0.587785 -0.572061 -p 0.5 0.707107 -0.5 -p 0.415627 0.809017 -0.415627 -p 0.32102 0.891007 -0.32102 -p 0.218508 0.951057 -0.218508 -p 0.110616 0.987688 -0.110616 -p 0 1 0 -p -0.110616 0.987688 0.110616 -p -0.218508 0.951057 0.218508 -p -0.32102 0.891007 0.32102 -p -0.415627 0.809017 0.415627 -p -0.5 0.707107 0.5 -p -0.572061 0.587785 0.572061 -p -0.630037 0.453991 0.630037 -p -0.672498 0.309017 0.672498 -p -0.698401 0.156434 0.698401 -p -0.707107 0 0.707107 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 -k 70 -k 71 -k 72 -k 73 -k 74 -k 75 -k 76 -k 77 -k 78 -k 79 -k 80 -k 81 -k 82 -k 83 -k 84 -k 85 -k 86 -k 87 -k 88 -k 89 -k 90 -k 91 -k 92 -k 93 -k 94 -k 95 -k 96 -k 97 -k 98 -k 99 -k 100 -k 101 -k 102 -k 103 -k 104 -k 105 -k 106 -k 107 -k 108 -k 109 -k 110 -k 111 -k 112 -k 113 -k 114 -k 115 -k 116 -k 117 -k 118 -k 119 ;")
            if ControllerType == 3:
                newController = mel.eval("curve -d 1 -p -1.296206 0 0 -p -1.050693 0 -0.245513 -p -1.050693 0 -0.122757 -p -1.024305 -4.37114e-09 -0.12197 -p -0.99861 -4.37114e-09 -0.324468 -p -0.849468 -4.37114e-09 -0.617175 -p -0.617175 -4.37114e-09 -0.849468 -p -0.324468 -4.37114e-09 -0.99861 -p 0 -4.37114e-09 -1.05 -p 0.324468 -4.37114e-09 -0.99861 -p 0.617175 -4.37114e-09 -0.849468 -p 0.849468 -4.37114e-09 -0.617175 -p 0.99861 -4.37114e-09 -0.324468 -p 1.05 -4.37114e-09 0 -p 0.998609 -4.37114e-09 0.324468 -p 0.849468 -4.37114e-09 0.617175 -p 0.617175 -4.37114e-09 0.849468 -p 0.324468 -4.37114e-09 0.998609 -p -3.12924e-08 -4.37114e-09 1.05 -p -0.324468 -4.37114e-09 0.998609 -p -0.617175 -4.37114e-09 0.849468 -p -0.849468 -4.37114e-09 0.617175 -p -0.99861 -4.37114e-09 0.324468 -p -1.024305 -4.37114e-09 0.12197 -p -1.050693 0 0.122757 -p -1.050693 0 0.245513 -p -1.296206 0 0 -p -1.050693 0 0 -p -0.95 0 0 -p -0.926752 0 -0.110354 -p -0.903504 0 -0.293566 -p -0.768566 0 -0.558396 -p -0.558396 0 -0.768566 -p -0.293566 0 -0.903504 -p 0 0 -0.95 -p 0.293566 0 -0.903504 -p 0.558396 0 -0.768567 -p 0.768567 0 -0.558396 -p 0.903504 0 -0.293566 -p 0.95 0 0 -p 0.903504 0 0.293566 -p 0.768566 0 0.558396 -p 0.558396 0 0.768566 -p 0.293566 0 0.903504 -p -2.83122e-08 0 0.95 -p -0.293566 0 0.903504 -p -0.558396 0 0.768566 -p -0.768566 0 0.558396 -p -0.903504 0 0.293566 -p -0.926752 0 0.110354 -p -0.95 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 ;")
            if ControllerType == 4:
                newController = mel.eval("curve -d 1 -p -1 -0.285425 -5.96046e-08 -p -0.965926 -0.285425 0.258819 -p -0.866025 -0.285425 0.5 -p -0.707107 -0.285425 0.707107 -p -0.5 -0.285425 0.866025 -p -0.258819 -0.285425 0.965926 -p -2.98023e-08 -0.285425 1 -p 0.258819 -0.285425 0.965926 -p 0.5 -0.285425 0.866025 -p 0.707107 -0.285425 0.707107 -p 0.866025 -0.285425 0.5 -p 0.965926 -0.285425 0.258819 -p 1 -0.285425 0 -p 0.965925 -0.285425 -0.258819 -p 0.866025 -0.285425 -0.5 -p 0.707106 -0.285425 -0.707106 -p 0.5 -0.285425 -0.866025 -p 0.258819 -0.285425 -0.965925 -p 1.19209e-07 -0.285425 -0.999999 -p -0.258819 -0.285425 -0.965925 -p -0.5 -0.285425 -0.866025 -p -0.707106 -0.285425 -0.707107 -p -0.866025 -0.285425 -0.5 -p -0.965926 -0.285425 -0.258819 -p -1 -0.285425 -5.96046e-08 -p -1 0.285425 -5.96046e-08 -p -0.965926 0.285425 -0.258819 -p -0.866025 0.285425 -0.5 -p -0.707106 0.285425 -0.707107 -p -0.707106 -0.285425 -0.707107 -p -0.707106 0.285425 -0.707107 -p -0.5 0.285425 -0.866025 -p -0.258819 0.285425 -0.965925 -p 1.19209e-07 0.285425 -0.999999 -p 1.19209e-07 -0.285425 -0.999999 -p 1.19209e-07 0.285425 -0.999999 -p 0.258819 0.285425 -0.965925 -p 0.5 0.285425 -0.866025 -p 0.707106 0.285425 -0.707106 -p 0.707106 -0.285425 -0.707106 -p 0.707106 0.285425 -0.707106 -p 0.866025 0.285425 -0.5 -p 0.965925 0.285425 -0.258819 -p 1 0.285425 0 -p 1 -0.285425 0 -p 1 0.285425 0 -p 0.965926 0.285425 0.258819 -p 0.866025 0.285425 0.5 -p 0.707107 0.285425 0.707107 -p 0.707107 -0.285425 0.707107 -p 0.707107 0.285425 0.707107 -p 0.5 0.285425 0.866025 -p 0.258819 0.285425 0.965926 -p -2.98023e-08 0.285425 1 -p -0.258819 0.285425 0.965926 -p -0.5 0.285425 0.866025 -p -0.707107 0.285425 0.707107 -p -0.707107 -0.285425 0.707107 -p -0.707107 0.285425 0.707107 -p -0.866025 0.285425 0.5 -p -0.965926 0.285425 0.258819 -p -1 0.285425 -5.96046e-08 -p -0.965926 0.285425 0.258819 -p -0.866025 0.285425 0.5 -p -0.707107 0.285425 0.707107 -p -0.5 0.285425 0.866025 -p -0.258819 0.285425 0.965926 -p -2.98023e-08 0.285425 1 -p -2.98023e-08 -0.285425 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 ;")
            if ControllerType == 5:
                newController = mel.eval("curve -d 1 -p 0 0 1 -p 0 0 1 -p -0.399952 0 0.599928 -p -0.199976 0 0.599928 -p -0.199976 0 0.199976 -p -0.599928 0 0.199976 -p -0.599928 0 0.399952 -p -1 0 0 -p -0.599928 0 -0.399952 -p -0.599928 0 -0.199976 -p -0.199976 0 -0.199976 -p -0.199976 0 -0.599928 -p -0.399952 0 -0.599928 -p 0 0 -1 -p 0.399952 0 -0.599928 -p 0.199976 0 -0.599928 -p 0.199976 0 -0.199976 -p 0.599928 0 -0.199976 -p 0.599928 0 -0.399952 -p 1 0 0 -p 0.599928 0 0.399952 -p 0.599928 0 0.199976 -p 0.199976 0 0.199976 -p 0.199976 0 0.599928 -p 0.399952 0 0.599928 -p 0 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 ;")
            if ControllerType == 6:
                newController = mel.eval("curve -d 1 -p -0.25 0 1 -p -0.25 0 0.25 -p -1 0 0.25 -p -1 0 -0.25 -p -0.25 0 -0.25 -p -0.25 0 -1 -p 0.25 0 -1 -p 0.25 0 -0.25 -p 1 0 -0.25 -p 1 0 0.25 -p 0.25 0 0.25 -p 0.25 0 1 -p -0.25 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 ;")
            if ControllerType == 7:
                newController = mel.eval("curve -d 1 -p 0 0 0 -p 0 4.032974 0 -p -0.156435 4.045285 0 -p -0.309017 4.081917 0 -p -0.453991 4.141967 0 -p -0.587785 4.223957 0 -p -0.707107 4.325867 0 -p -0.809017 4.445189 0 -p -0.891007 4.578983 0 -p -0.951057 4.723957 0 -p -0.987689 4.876539 0 -p -1 5.032974 0 -p -0.987689 5.189408 0 -p -0.951057 5.341991 0 -p -0.891007 5.486964 0 -p -0.809017 5.620759 0 -p -0.707107 5.74008 0 -p -0.587785 5.841991 0 -p -0.453991 5.92398 0 -p -0.309017 5.98403 0 -p -0.156435 6.020662 0 -p 0 6.032974 0 -p 0.156434 6.020662 0 -p 0.309017 5.98403 0 -p 0.453991 5.92398 0 -p 0.587785 5.841991 0 -p 0.707107 5.74008 0 -p 0.809017 5.620759 0 -p 0.891007 5.486964 0 -p 0.951057 5.341991 0 -p 0.987688 5.189408 0 -p 1 5.032974 0 -p 0.987688 4.876539 0 -p 0.951057 4.723957 0 -p 0.891007 4.578983 0 -p 0.809017 4.445189 0 -p 0.707107 4.325867 0 -p 0.587785 4.223957 0 -p 0.453991 4.141967 0 -p 0.309017 4.081917 0 -p 0.156434 4.045285 0 -p 0 4.032974 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 ;")
            if ControllerType == 8:
                newController = mel.eval("curve -d 1 -p 0 0 0 -p -2.98023e-08 4.048372 0 -p -1.33187e-08 4.601471 0 -p -0.309017 4.097315 0 -p -0.262682 4.686821 0 -p -0.809017 4.460587 0 -p -0.425028 4.910272 0 -p -1 5.048372 0 -p -0.425028 5.186472 0 -p -0.809017 5.636157 0 -p -0.262682 5.409923 0 -p -0.309017 5.999429 0 -p 0 5.495273 0 -p 0.309017 5.999429 0 -p 0.262682 5.409923 0 -p 0.809018 5.636158 0 -p 0.425028 5.186472 0 -p 1 5.048372 0 -p 0.425028 4.910272 0 -p 0.809017 4.460587 0 -p 0.262682 4.686821 0 -p 0.309017 4.097315 0 -p -1.33187e-08 4.601471 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 ;")
            if ControllerType == 9:
                newController = mel.eval("curve -d 1 -p 0.802112 0 0 -p 1 0 0 -p 0.951057 -0.309017 0 -p 0.809017 -0.587785 0 -p 0.587785 -0.809017 0 -p 0.309017 -0.951057 0 -p -2.98023e-08 -1 0 -p -0.309017 -0.951057 0 -p -0.587785 -0.809017 0 -p -0.809017 -0.587785 0 -p -0.951057 -0.309017 0 -p -1 0 0 -p -0.951057 0.309017 0 -p -0.809017 0.587785 0 -p -0.587785 0.809017 0 -p -0.309017 0.951057 0 -p 0 1 0 -p 0.0221199 1.302628 0 -p 0.828684 0.899346 0 -p 0.0221199 0.496064 0 -p 0 0.802112 0 -p -0.247866 0.762854 0 -p -0.47147 0.648922 0 -p -0.648922 0.47147 0 -p -0.762854 0.247866 0 -p -0.802112 0 0 -p -0.762854 -0.247866 0 -p -0.648922 -0.471469 0 -p -0.471469 -0.648922 0 -p -0.247866 -0.762854 0 -p -2.39048e-08 -0.802112 0 -p 0.247866 -0.762854 0 -p 0.471469 -0.648922 0 -p 0.648922 -0.471469 0 -p 0.762854 -0.247866 0 -p 0.802112 0 0 -p 1 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 ;")
            if ControllerType == 10:
                newController = mel.eval("curve -d 1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 -1 -p -1 0 1 -p 1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;")
            if ControllerType == 11:
                newController = mel.eval("curve -d 1 -p 0 -1.29603e-09 0.688679 -p 0.0962036 -1.29603e-09 0.703916 -p 0.18299 -1.29603e-09 0.748136 -p 0.251864 -1.29603e-09 0.81701 -p 0.296084 -1.29603e-09 0.903796 -p 0.311321 -1.29603e-09 1 -p 0.296084 -1.29603e-09 1.096204 -p 0.251864 -1.29603e-09 1.18299 -p 0.18299 -1.29603e-09 1.251864 -p 0.0962036 -1.29603e-09 1.296084 -p -9.2781e-09 -1.29603e-09 1.311321 -p -0.0962036 -1.29603e-09 1.296084 -p -0.18299 -1.29603e-09 1.251864 -p -0.251864 -1.29603e-09 1.18299 -p -0.296084 -1.29603e-09 1.096204 -p -0.311321 -1.29603e-09 1 -p -0.296084 -1.29603e-09 0.903796 -p -0.251864 -1.29603e-09 0.81701 -p -0.18299 -1.29603e-09 0.748136 -p -0.0962036 -1.29603e-09 0.703916 -p 0 -1.29603e-09 0.688679 -p 0 0 0 -p -9.2781e-09 -1.29603e-09 -0.688679 -p -0.0962036 -1.29603e-09 -0.703916 -p -0.18299 -1.29603e-09 -0.748136 -p -0.251864 -1.29603e-09 -0.81701 -p -0.296084 -1.29603e-09 -0.903796 -p -0.311321 -1.29603e-09 -1 -p -0.296084 -1.29603e-09 -1.096204 -p -0.251864 -1.29603e-09 -1.18299 -p -0.18299 -1.29603e-09 -1.251864 -p -0.0962036 -1.29603e-09 -1.296084 -p 0 -1.29603e-09 -1.311321 -p 0.0962036 -1.29603e-09 -1.296084 -p 0.18299 -1.29603e-09 -1.251864 -p 0.251864 -1.29603e-09 -1.18299 -p 0.296084 -1.29603e-09 -1.096204 -p 0.311321 -1.29603e-09 -1 -p 0.296084 -1.29603e-09 -0.903796 -p 0.251864 -1.29603e-09 -0.81701 -p 0.18299 -1.29603e-09 -0.748136 -p 0.0962036 -1.29603e-09 -0.703916 -p -9.2781e-09 -1.29603e-09 -0.688679 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 ;")
            if ControllerType == 12:
                newController = mel.eval("curve -d 1 -p 0.624948 0.273104 0.636666 -p 0.706724 0.706724 1.00216 -p 0.273104 0.624948 0.636666 -p -1.68791e-09 0.999458 1.00216 -p -0.248791 0.635019 0.636666 -p -0.706724 0.706724 1.00216 -p -0.624948 0.273104 0.636666 -p -0.999458 -1.68791e-09 1.00216 -p -0.624948 -0.273104 0.636666 -p -0.706724 -0.706724 1.00216 -p -0.248791 -0.635019 0.636666 -p 1.68791e-09 -0.999458 1.00216 -p 0.264025 -0.633976 0.6367 -p 0.706724 -0.706724 1.00216 -p 0.634983 -0.261595 0.6367 -p 0.999458 1.68791e-09 1.00216 -p 0.624948 0.273104 0.636666 -p 0 0 0 -p 0.273104 0.624948 0.636666 -p 0 0 0 -p -0.248791 0.635019 0.636666 -p 0 0 0 -p -0.624948 0.273104 0.636666 -p 0 0 0 -p -0.624948 -0.273104 0.636666 -p 0 0 0 -p -0.248791 -0.635019 0.636666 -p 0 0 0 -p 0.264025 -0.633976 0.6367 -p 0 0 0 -p 0.634983 -0.261595 0.6367 -p 0 0 0 -p 0 0 1.841218 -p 3.41745e-08 0.260607 1.841218 -p -0.260607 2.2783e-08 1.841218 -p -1.13915e-08 -0.260607 1.841218 -p 0.260607 0 1.841218 -p 3.41745e-08 0.260607 1.841218 -p -1.13915e-08 -0.260607 1.841218 -p 0.260607 0 1.841218 -p -0.260607 2.2783e-08 1.841218 -p 0 0 2.348702 -p 3.41745e-08 0.260607 1.841218 -p 0 0 2.348702 -p 0.260607 0 1.841218 -p 0 0 2.348702 -p -1.13915e-08 -0.260607 1.841218 -p 0 0 2.348702 -p -0.260607 2.2783e-08 1.841218 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 ;")
            if ControllerType == 13:
                newController = mel.eval("curve -d 1 -p -0.500011 0 -0.342423 -p -0.475538 0 -0.546073 -p -0.404517 0 -0.729788 -p -0.293899 0 -0.875585 -p -0.154512 0 -0.969192 -p 0 0 -1.001447 -p 0.154512 0 -0.969193 -p 0.293899 0 -0.875585 -p 0.404517 0 -0.729788 -p 0.475538 0 -0.546073 -p 0.50001 0 -0.342423 -p 0.50001 0 -7.45074e-09 -p 0.50001 0 0.250005 -p 0.50001 0 0.50001 -p 0.487474 0 0.611273 -p 0.450494 0 0.716957 -p 0.390924 0 0.811762 -p 0.311751 0 0.890934 -p 0.216946 0 0.950504 -p 0.111263 0 0.987485 -p 0 0 1.000021 -p -0.111263 0 0.987485 -p -0.216946 0 0.950504 -p -0.311751 0 0.890934 -p -0.390924 0 0.811762 -p -0.450494 0 0.716957 -p -0.487474 0 0.611273 -p -0.500011 0 0.50001 -p -0.500011 0 0.250005 -p -0.500011 0 -7.45074e-09 -p -0.500011 0 -0.342423 -p -0.493855 0.0782188 -0.342423 -p -0.475538 0.154512 -0.342423 -p -0.445513 0.227 -0.342423 -p -0.404517 0.293899 -0.342423 -p -0.353561 0.353561 -0.342423 -p -0.293899 0.404517 -0.342423 -p -0.227 0.445513 -0.342423 -p -0.154512 0.475538 -0.342423 -p -0.0782189 0.493854 -0.342423 -p 0 0.50001 -0.342423 -p 0.0782189 0.493854 -0.342423 -p 0.154512 0.475538 -0.342423 -p 0.227 0.445513 -0.342423 -p 0.293899 0.404517 -0.342423 -p 0.353561 0.353561 -0.342423 -p 0.404517 0.293899 -0.342423 -p 0.445513 0.227 -0.342423 -p 0.475538 0.154512 -0.342423 -p 0.493854 0.0782188 -0.342423 -p 0.50001 0 -0.342423 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 ;")
            if ControllerType == 14:
                newController = mel.eval("curve -d 1 -p 0 2 0 -p -1 0 -8.74228e-08 -p 1.31134e-07 0 -1 -p 0 2 0 -p 1.31134e-07 0 -1 -p 1 0 0 -p 0 2 0 -p 1 0 0 -p -4.37114e-08 0 1 -p 0 2 0 -p -4.37114e-08 0 1 -p -1 0 -8.74228e-08 -p 0 2 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 ;")
            if ControllerType == 15:
                newController = mel.eval("curve -d 1 -p 1.31134e-07 0 -1 -p 0 -1 0 -p -4.37114e-08 0 1 -p 0 1 0 -p 1.31134e-07 0 -1 -p 1 0 0 -p -4.37114e-08 0 1 -p -1 0 -8.74228e-08 -p 1.31134e-07 0 -1 -p 1 0 0 -p 0 -1 0 -p -1 0 -8.74228e-08 -p 0 1 0 -p 1 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 ;")
            if ControllerType == 16:
                newController = mel.eval("curve -d 1 -p -1 0 0 -p -0.976649 0.0403494 0 -p -0.900118 0.0982616 0 -p -0.797187 0.209749 0 -p -0.70454 0.321503 0 -p -0.570132 0.458003 0 -p -0.431729 0.546423 0 -p -0.242886 0.615884 0 -p -0.0762568 0.640181 0 -p 0 0.649903 0 -p 0.0780068 0.629549 0 -p 0.184417 0.491045 0 -p 0.226461 0.36648 0 -p 0.249787 0.261573 0 -p 0.257746 0.152078 0 -p 0.25393 0.0458305 0 -p 0.237242 -0.066641 0 -p 0.209472 -0.170002 0 -p 0.159341 -0.275547 0 -p 0.0936243 -0.353376 0 -p 0.00278143 -0.395603 0 -p -0.0939869 -0.353027 0 -p -0.156973 -0.278751 0 -p -0.203105 -0.187712 0 -p -0.23646 -0.0701566 0 -p -0.254189 0.0494566 0 -p -0.258595 0.140181 0 -p -0.251477 0.239877 0 -p -0.229974 0.350679 0 -p -0.189943 0.475675 0 -p -0.117905 0.582293 0 -p -0.064095 0.63318 0 -p 0 0.649903 0 -p 0.0652413 0.641022 0 -p 0.216261 0.620465 0 -p 0.386892 0.559551 0 -p 0.522426 0.485287 0 -p 0.662175 0.374169 0 -p 0.771204 0.255743 0 -p 0.855995 0.163618 0 -p 0.957245 0.0625218 0 -p 0.992191 0.00580352 0 -p 0.975819 -0.0416966 0 -p 0.895059 -0.121241 0 -p 0.804982 -0.222674 0 -p 0.670153 -0.368554 0 -p 0.568298 -0.457874 0 -p 0.419555 -0.547289 0 -p 0.22243 -0.620251 0 -p 0.00288299 -0.649515 0 -p -0.227529 -0.619587 0 -p -0.400218 -0.554941 0 -p -0.555939 -0.463581 0 -p -0.673564 -0.356247 0 -p -0.765684 -0.252221 0 -p -0.878425 -0.124209 0 -p -0.924528 -0.0847122 0 -p -0.971997 -0.045168 0 -p -1 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 ;")
            if ControllerType == 17:
                newController = mel.eval("curve -d 1 -p 0 0 0 -p 1 0 1 -p 0.333333 0 1 -p 1 0 1 -p 1 0 0.333333 -p 1 0 1 -p 0 0 0 -p -1 0 -1 -p -0.333333 0 -1 -p -1 0 -1 -p -1 0 -0.333333 -p -1 0 -1 -p 0 0 0 -p 1 0 -1 -p 1 0 -0.333333 -p 1 0 -1 -p 0.333333 0 -1 -p 1 0 -1 -p 0 0 0 -p -1 0 1 -p -0.333333 0 1 -p -1 0 1 -p -1 0 0.333333 -p -1 0 1 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 ;")
            if ControllerType == 18:
                newController = mel.eval("curve -d 1 -p -1 0 0 -p -0.602634 0 -0.400331 -p -0.602634 0 -0.201158 -p 0.602634 0 -0.201158 -p 0.602634 0 -0.400331 -p 1 0 0 -p 0.602634 0 0.400331 -p 0.602634 0 0.201158 -p -0.602634 0 0.201158 -p -0.602634 0 0.400331 -p -1 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 ;")
            if ControllerType == 19:
                newController = mel.eval("curve -d 1 -p 0 0 0 -p 0 0 1 -p 0.0321135 0.0988352 0.71074 -p -0.0840743 0.0610835 0.71074 -p -0.0840743 -0.0610835 0.71074 -p 0.0321135 -0.0988352 0.71074 -p 0.103922 0 0.71074 -p 0.0321135 0.0988352 0.71074 -p 0 0 1 -p 0.0321135 0.0988352 0.71074 -p 0 0 1 -p 0.103922 0 0.71074 -p 0 0 1 -p 0.0321135 -0.0988352 0.71074 -p 0 0 1 -p -0.0840743 -0.0610835 0.71074 -p 0 0 1 -p -0.0840743 0.0610835 0.71074 -p 0 0 1 -p 0.0321135 0.0988352 0.71074 -p 0 0 1 -p 0 0 0 -p 0 0 -1 -p 0.0321135 0.0988352 -0.71074 -p -0.0840743 0.0610835 -0.71074 -p -0.0840743 -0.0610835 -0.71074 -p 0.0321135 -0.0988352 -0.71074 -p 0.103922 0 -0.71074 -p 0.0321135 0.0988352 -0.71074 -p 0 0 -1 -p 0.0321135 0.0988352 -0.71074 -p 0 0 -1 -p 0.103922 0 -0.71074 -p 0 0 -1 -p 0.0321135 -0.0988352 -0.71074 -p 0 0 -1 -p -0.0840743 -0.0610835 -0.71074 -p 0 0 -1 -p -0.0840743 0.0610835 -0.71074 -p 0 0 -1 -p 0.0321135 0.0988352 -0.71074 -p 0 0 -1 -p 0 0 0 -p 0 0.999563 0 -p 0.103922 0.71074 0 -p 0.0321135 0.71074 -0.0988352 -p -0.0840743 0.71074 -0.0610835 -p -0.0840743 0.71074 0.0610835 -p 0.0321135 0.71074 0.0988352 -p 0.103922 0.71074 0 -p 0 0.999563 0 -p 0.0321135 0.71074 0.0988352 -p 0 0.999563 0 -p -0.0840743 0.71074 0.0610835 -p 0 0.999563 0 -p -0.0840743 0.71074 -0.0610835 -p 0 0.999563 0 -p 0.0321135 0.71074 -0.0988352 -p 0 0.999563 0 -p 0.103922 0.71074 0 -p 0 0.999563 0 -p 0 0 0 -p 0 -0.999563 0 -p 0.0321135 -0.71074 -0.0988352 -p 0.103922 -0.71074 0 -p 0.0321135 -0.71074 0.0988352 -p -0.0840743 -0.71074 0.0610835 -p -0.0840743 -0.71074 -0.0610835 -p 0.0321135 -0.71074 -0.0988352 -p 0 -0.999563 0 -p 0.103922 -0.71074 0 -p 0 -0.999563 0 -p 0.0321135 -0.71074 0.0988352 -p 0 -0.999563 0 -p -0.0840743 -0.71074 0.0610835 -p 0 -0.999563 0 -p -0.0840743 -0.71074 -0.0610835 -p 0 -0.999563 0 -p 0.0321135 -0.71074 -0.0988352 -p 0 -0.999563 0 -p 0 0 0 -p 0.999563 0 0 -p 0.71074 0.0321135 0.0988352 -p 0.71074 0.103922 0 -p 0.71074 0.0321135 -0.0988352 -p 0.71074 -0.0840743 -0.0610835 -p 0.71074 -0.0840743 0.0610835 -p 0.71074 0.0321135 0.0988352 -p 0.999563 0 0 -p 0.71074 0.103922 0 -p 0.999563 0 0 -p 0.71074 0.0321135 -0.0988352 -p 0.999563 0 0 -p 0.71074 -0.0840743 -0.0610835 -p 0.999563 0 0 -p 0.71074 -0.0840743 0.0610835 -p 0.999563 0 0 -p 0 0 0 -p -0.999563 0 0 -p -0.71074 -0.0840743 0.0610835 -p -0.71074 0.0321135 0.0988352 -p -0.71074 0.103922 0 -p -0.71074 0.0321135 -0.0988352 -p -0.71074 -0.0840743 -0.0610835 -p -0.71074 -0.0840743 0.0610835 -p -0.999563 0 0 -p -0.71074 0.0321135 0.0988352 -p -0.999563 0 0 -p -0.71074 0.103922 0 -p -0.999563 0 0 -p -0.71074 0.0321135 -0.0988352 -p -0.999563 0 0 -p -0.71074 -0.0840743 -0.0610835 -p -0.999563 0 0 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 -k 70 -k 71 -k 72 -k 73 -k 74 -k 75 -k 76 -k 77 -k 78 -k 79 -k 80 -k 81 -k 82 -k 83 -k 84 -k 85 -k 86 -k 87 -k 88 -k 89 -k 90 -k 91 -k 92 -k 93 -k 94 -k 95 -k 96 -k 97 -k 98 -k 99 -k 100 -k 101 -k 102 -k 103 -k 104 -k 105 -k 106 -k 107 -k 108 -k 109 -k 110 -k 111 -k 112 -k 113 -k 114 ;")
            if ControllerType == 20:
                newController = mel.eval("curve -d 1 -p 0 1 0 -p -0.222521 0.974928 -7.95797e-08 -p -0.433884 0.900969 -1.55169e-07 -p -0.62349 0.781831 -2.22977e-07 -p -0.781832 0.62349 -2.79605e-07 -p -0.900969 0.433884 -3.22212e-07 -p -0.974928 0.222521 -3.48661e-07 -p -1 0 -3.57628e-07 -p -0.974928 -0.222521 -3.48661e-07 -p -0.900969 -0.433884 -3.22212e-07 -p -0.781832 -0.62349 -2.79605e-07 -p -0.62349 -0.781831 -2.22977e-07 -p -0.433884 -0.900969 -1.55169e-07 -p -0.222521 -0.974928 -7.95797e-08 -p 0 -1 0 -p 0.222521 -0.974928 0 -p 0.433884 -0.900969 0 -p 0.62349 -0.781831 0 -p 0.781832 -0.62349 0 -p 0.900969 -0.433884 0 -p 0.974928 -0.222521 0 -p 1 0 0 -p 0.974928 0.222521 0 -p 0.900969 0.433884 0 -p 0.781832 0.62349 0 -p 0.62349 0.781831 0 -p 0.433884 0.900969 0 -p 0.222521 0.974928 0 -p 0 1 0 -p 1.12738e-07 0.974928 -0.222521 -p 2.19823e-07 0.900969 -0.433884 -p 3.15885e-07 0.781831 -0.62349 -p 3.96107e-07 0.62349 -0.781831 -p 4.56466e-07 0.433884 -0.900969 -p 4.93937e-07 0.222521 -0.974928 -p 5.06639e-07 0 -1 -p 4.93937e-07 -0.222521 -0.974928 -p 4.56466e-07 -0.433884 -0.900969 -p 3.96107e-07 -0.62349 -0.781831 -p 3.15885e-07 -0.781831 -0.62349 -p 2.19823e-07 -0.900969 -0.433884 -p 1.12738e-07 -0.974928 -0.222521 -p 0 -1 0 -p -3.31582e-08 -0.974928 0.222521 -p -6.46537e-08 -0.900969 0.433884 -p -9.29072e-08 -0.781831 0.62349 -p -1.16502e-07 -0.62349 0.781832 -p -1.34255e-07 -0.433884 0.900969 -p -1.45276e-07 -0.222521 0.974928 -p -1.49012e-07 0 1 -p -1.45276e-07 0.222521 0.974928 -p -1.34255e-07 0.433884 0.900969 -p -1.16502e-07 0.62349 0.781832 -p -9.29072e-08 0.781831 0.62349 -p -6.46537e-08 0.900969 0.433884 -p -3.31582e-08 0.974928 0.222521 -p 0 1 0 -p 0.222521 0.974928 0 -p 0.433884 0.900969 0 -p 0.62349 0.781831 0 -p 0.781832 0.62349 0 -p 0.900969 0.433884 0 -p 0.974928 0.222521 0 -p 1 0 0 -p 0.92388 0 -0.382683 -p 0.707107 0 -0.707106 -p 0.382684 0 -0.923879 -p 5.06639e-07 0 -1 -p -0.382683 0 -0.92388 -p -0.707106 0 -0.707107 -p -0.923879 0 -0.382684 -p -1 0 -3.57628e-07 -p -0.92388 0 0.382683 -p -0.707107 0 0.707107 -p -0.382684 0 0.923879 -p -1.49012e-07 0 1 -p 0.382683 0 0.92388 -p 0.707107 0 0.707107 -p 0.92388 0 0.382683 -p 1 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 -k 70 -k 71 -k 72 -k 73 -k 74 -k 75 -k 76 -k 77 -k 78 -k 79 ;")
            if ControllerType == 21:
                newController = mel.eval("curve -d 1 -p -0.930754 0 0 -p -0.999823 0 -0.225742 -p -0.929112 0 -0.225742 -p -0.871025 0 -0.0343219 -p -0.795975 0 -0.0343219 -p -0.855002 0 -0.225742 -p -0.784291 0 -0.225742 -p -0.725416 0 -0.0343219 -p 0.571271 0 -0.0343219 -p 0.53502 5.86654e-09 -0.232606 -p 1 0 0 -p 0.53502 -1.95551e-09 0.232606 -p 0.571271 0 0.0343219 -p -0.725416 0 0.0343219 -p -0.784291 0 0.225742 -p -0.855002 0 0.225742 -p -0.795975 0 0.0343219 -p -0.871025 0 0.0343219 -p -0.929112 0 0.225742 -p -0.999823 0 0.225742 -p -0.930754 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 ;")
            if ControllerType == 22:
                newController = mel.eval("curve -d 1 -p -0.930754 0 0 -p -0.999823 0 0.225742 -p -0.929112 0 0.225742 -p -0.871025 0 0.0343219 -p -0.795975 0 0.0343219 -p -0.855002 0 0.225742 -p -0.784291 0 0.225742 -p -0.725416 0 0.0343219 -p -0.65215 0 0.0339838 -p -0.70891 0 0.225742 -p -0.638199 0 0.225742 -p -0.579488 0 0.0357706 -p 0.571271 0 0.0343219 -p 0.53502 -1.95551e-09 0.232606 -p 1 0 0 -p 0.53502 5.86654e-09 -0.232606 -p 0.571271 0 -0.0343219 -p -0.578353 0 -0.0354073 -p -0.638199 0 -0.225742 -p -0.70891 0 -0.225742 -p -0.650934 0 -0.03416 -p -0.725416 0 -0.0343219 -p -0.784291 0 -0.225742 -p -0.855002 0 -0.225742 -p -0.795975 0 -0.0343219 -p -0.871025 0 -0.0343219 -p -0.929112 0 -0.225742 -p -0.999823 0 -0.225742 -p -0.930754 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 ;")
            if ControllerType == 23:
                newController = mel.eval("curve -d 1 -p 0.987688 -0.156434 0 -p 1.011839 -0.15624 0 -p 1.036134 -0.152464 0 -p 1.05954 -0.144934 0 -p 1.08148 -0.133836 0 -p 1.101413 -0.119442 0 -p 1.118849 -0.102107 0 -p 1.133359 -0.0822576 0 -p 1.144585 -0.0603829 0 -p 1.152251 -0.0370213 0 -p 1.156168 -0.0127483 0 -p 1.15624 0.0118387 0 -p 1.152464 0.0361342 0 -p 1.144934 0.05954 0 -p 1.133836 0.0814797 0 -p 1.119442 0.101413 0 -p 1.102107 0.118849 0 -p 1.082258 0.133359 0 -p 1.060383 0.144585 0 -p 1.037021 0.152251 0 -p 1.012748 0.156168 0 -p 0.988161 0.15624 0 -p 0.963866 0.152464 0 -p 0.94046 0.144934 0 -p 0.91852 0.133836 0 -p 0.898587 0.119442 0 -p 0.881151 0.102107 0 -p 0.866641 0.0822576 0 -p 0.855415 0.0603829 0 -p 0.847749 0.0370213 0 -p 0.843832 0.0127483 0 -p 0.84376 -0.0118387 0 -p 0.847536 -0.0361342 0 -p 0.855066 -0.05954 0 -p 0.866164 -0.0814797 0 -p 0.880558 -0.101413 0 -p 0.897893 -0.118849 0 -p 0.917742 -0.133359 0 -p 0.939617 -0.144585 0 -p 0.962979 -0.152251 0 -p 0.987252 -0.156168 0 -p 0.951057 -0.309017 0 -p 0.891007 -0.453991 0 -p 0.809017 -0.587785 0 -p 0.707107 -0.707107 0 -p 0.587785 -0.809017 0 -p 0.453991 -0.891007 0 -p 0.309017 -0.951057 0 -p 0.156434 -0.987688 0 -p 0 -1 0 -p -0.156435 -0.987688 0 -p -0.309017 -0.951057 0 -p -0.453991 -0.891007 0 -p -0.587785 -0.809017 0 -p -0.707107 -0.707107 0 -p -0.809017 -0.587785 0 -p -0.891007 -0.453991 0 -p -0.951057 -0.309017 0 -p -0.987689 -0.156434 0 -p -1 0 0 -p -0.987689 0.156434 0 -p -0.951057 0.309017 0 -p -0.891007 0.453991 0 -p -0.809017 0.587785 0 -p -0.707107 0.707107 0 -p -0.587785 0.809017 0 -p -0.453991 0.891007 0 -p -0.309017 0.951057 0 -p -0.156435 0.987688 0 -p 0.033317 1.003527 0 -p 0 0.772254 0 -p 0 1 -0.227746 -p 0 1.227746 -1.99102e-08 -p 0 1 0.227746 -p 0 0.772254 0 -p 0.455491 1 0 -p 0 1.227746 -1.99102e-08 -p 0.033317 1.003527 0 -p 0 1 0.227746 -p 0.455491 1 0 -p 0 1 -0.227746 -p 0.033317 1.003527 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 -k 70 -k 71 -k 72 -k 73 -k 74 -k 75 -k 76 -k 77 -k 78 -k 79 -k 80 -k 81 ;")
            if ControllerType == 24:
                newController = mel.eval("curve -d 1 -p 1.044843 0.451543 -1.71274e-08 -p 0.943201 0.349574 0 -p 0.856409 0.452596 0 -p 0.748529 0.544474 0 -p 0.622217 0.622945 0 -p 0.480585 0.686077 0 -p 0.327119 0.732316 0 -p 0.165598 0.760522 0 -p 0 0.770002 0 -p -0.165598 0.760522 0 -p -0.327119 0.732316 0 -p -0.480585 0.686077 0 -p -0.622217 0.622945 0 -p -0.748529 0.544474 0 -p -0.856409 0.452596 0 -p -0.943201 0.349574 0 -p -1.044843 0.451543 -1.71274e-08 -p -1.133634 0.0225564 0 -p -0.73717 0.208915 0 -p -0.862344 0.287681 0 -p -0.847811 0.31422 0 -p -0.769797 0.406823 0 -p -0.672827 0.489409 0 -p -0.55929 0.559944 0 -p -0.431981 0.616691 0 -p -0.294036 0.658254 0 -p -0.148851 0.683608 0 -p 0 0.692129 0 -p 0.148851 0.683608 0 -p 0.294036 0.658254 0 -p 0.431981 0.616691 0 -p 0.55929 0.559944 0 -p 0.672827 0.489409 0 -p 0.769796 0.406823 0 -p 0.847811 0.31422 0 -p 0.864885 0.287155 0 -p 0.73717 0.208915 0 -p 1.133634 0.0225564 0 -p 1.044843 0.451543 -1.71274e-08 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 ;")
            if ControllerType == 25:
                newController = mel.eval("curve -d 1 -p 1 0 0 -p 0.608742 0 0.202943 -p 0.608742 0.202943 -1.77419e-08 -p 0.608742 0 -0.202943 -p 0.608742 -0.202943 0 -p 0.608742 0 0.202943 -p 0.608742 0.202943 -1.77419e-08 -p 1 0 0 -p 0.608742 0 -0.202943 -p 1 0 0 -p 0.608742 -0.202943 0 -p 1 0 0 -p 0.608742 0 0.202943 -p 0.608742 0 0.0848705 -p 0.608742 0.0848706 -1.49012e-08 -p 0.608742 0.202943 -1.77419e-08 -p 0.608742 0.0848706 -1.49012e-08 -p 0.608742 0 -0.0848705 -p 0.608742 0 -0.202943 -p 0.608742 0 -0.0848705 -p 0.608742 -0.0848705 0 -p 0.608742 -0.202943 0 -p 0.608742 -0.0848705 0 -p 0.608742 0 0.0848705 -p 0.608742 0 0.202943 -p 0.608742 0 0.0848705 -p -0.608742 0 0.0848705 -p -0.608742 0.0848706 -1.49012e-08 -p 0.608742 0.0848706 -1.49012e-08 -p 0.608742 0 -0.0848705 -p -0.608742 0 -0.0848705 -p -0.608742 0.0848706 -1.49012e-08 -p -0.608742 0 -0.0848705 -p -0.608742 -0.0848705 0 -p 0.608742 -0.0848705 0 -p -0.608742 -0.0848705 0 -p -0.608742 0 0.0848705 -p -0.608742 0 0.202943 -p -0.608742 0.202943 -1.77419e-08 -p -0.608742 0.0848706 -1.49012e-08 -p -0.608742 0.202943 -1.77419e-08 -p -0.608742 0 -0.202943 -p -0.608742 0 -0.0848705 -p -0.608742 -0.0848705 0 -p -0.608742 -0.202943 0 -p -0.608742 0 -0.202943 -p -0.608742 -0.202943 0 -p -0.608742 0 0.202943 -p -1 0 0 -p -0.608742 0.202943 -1.77419e-08 -p -1 0 0 -p -0.608742 0 0.202943 -p -1 0 0 -p -0.608742 -0.202943 0 -p -1 0 0 -p -0.608742 0 -0.202943 -p -1 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 ;")
            if ControllerType == 26:
                newController = mel.eval("curve -d 1 -p 0 0 0 -p 0 1.998578 0 -p -0.111667 1.545617 0 -p -0.0558338 1.545617 0.0967067 -p 0.0558338 1.545617 0.0967067 -p 0.111667 1.545617 0 -p 0.0558338 1.545617 -0.0967067 -p -0.0558338 1.545617 -0.0967067 -p -0.111667 1.545617 0 -p 0 1.998578 0 -p -0.111667 1.545617 0 -p 0 1.998578 0 -p -0.0558338 1.545617 -0.0967067 -p 0 1.998578 0 -p 0.0558338 1.545617 -0.0967067 -p 0 1.998578 0 -p 0.111667 1.545617 0 -p 0 1.998578 0 -p 0.0558338 1.545617 0.0967067 -p 0 1.998578 0 -p -0.0558338 1.545617 0.0967067 -p 0 1.998578 0 -p 0 0.397564 0 -p 0 0.397001 0.397001 -p 0 0 0.396933 -p 0.397001 0 0.397001 -p 0.397001 0.000154271 0 -p 0.397001 0.397001 0 -p 0 0.397564 0 -p 0 0 0 -p 0.397001 0.000154271 0 -p 2 0 0 -p 1.545617 0.111667 0 -p 1.545617 0.0558338 0.0967067 -p 1.545617 -0.0558338 0.0967067 -p 1.545617 -0.111667 0 -p 1.545617 -0.0558338 -0.0967067 -p 1.545617 0.0558338 -0.0967067 -p 1.545617 0.111667 0 -p 2 0 0 -p 1.545617 0.0558338 -0.0967067 -p 2 0 0 -p 1.545617 -0.0558338 -0.0967067 -p 2 0 0 -p 1.545617 -0.111667 0 -p 2 0 0 -p 1.545617 -0.0558338 0.0967067 -p 2 0 0 -p 1.545617 0.0558338 0.0967067 -p 2 0 0 -p 1.545617 0.111667 0 -p 2 0 0 -p 0.397001 0.000154271 0 -p 0 0 0 -p 0 0 0.396933 -p 0 0 2 -p 0 0.111667 1.545617 -p 0.0967067 0.0558338 1.545617 -p 0.0967067 -0.0558338 1.545617 -p 0 -0.111667 1.545617 -p -0.0967067 -0.0558338 1.545617 -p -0.0967067 0.0558338 1.545617 -p 0 0.111667 1.545617 -p 0 0 2 -p 0.0967067 0.0558338 1.545617 -p 0 0 2 -p 0.0967067 -0.0558338 1.545617 -p 0 0 2 -p 0 -0.111667 1.545617 -p 0 0 2 -p -0.0967067 -0.0558338 1.545617 -p 0 0 2 -p -0.0967067 0.0558338 1.545617 -p 0 0 2 -p 0 0 0.396933 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 -k 70 -k 71 -k 72 -k 73 -k 74 -k 75 ;")
            if ControllerType == 27:
                newController = mel.eval("curve -d 1 -p 0 0 0 -p -0.632534 0.260586 0.633477 -p -0.995603 0 0.997087 -p -0.632569 -0.247831 0.633443 -p 0 0 0 -p -0.247831 -0.632569 0.633443 -p 0 -0.995603 0.997087 -p 0.260586 -0.632534 0.633477 -p 0 0 0 -p 0.632649 0.260503 0.633593 -p 0.995603 0 0.997087 -p 0.632534 -0.260586 0.633477 -p 0 0 0 -p 0.260586 0.632534 0.633477 -p 0 0.995603 0.997087 -p -0.260586 0.632534 0.633477 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;")
            if ControllerType == 28:
                newController = mel.eval("curve -d 1 -p -1.42936e-08 0.26231 0.479614 -p -0.148209 0.26231 0.45614 -p -0.28191 0.26231 0.388016 -p -0.388016 0.26231 0.28191 -p -0.45614 0.26231 0.148209 -p -0.479614 0.26231 0 -p -0.45614 0.26231 -0.148209 -p -0.388016 0.26231 -0.28191 -p -0.28191 0.26231 -0.388016 -p -0.148209 0.26231 -0.45614 -p 0 0.26231 -0.479614 -p 0.148209 0.26231 -0.45614 -p 0.28191 0.26231 -0.388016 -p 0.388016 0.26231 -0.28191 -p 0.45614 0.26231 -0.148209 -p 0.479614 0.26231 0 -p 0.45614 0.26231 0.148209 -p 0.388016 0.26231 0.28191 -p 0.28191 0.26231 0.388016 -p 0.148209 0.26231 0.45614 -p -1.42936e-08 0.26231 0.479614 -p -1.42936e-08 -0.26231 0.479614 -p -0.148209 -0.26231 0.45614 -p -0.28191 -0.26231 0.388016 -p -0.388016 -0.26231 0.28191 -p -0.45614 -0.26231 0.148209 -p -0.479614 -0.26231 0 -p -0.45614 -0.26231 -0.148209 -p -0.388016 -0.26231 -0.28191 -p -0.28191 -0.26231 -0.388016 -p -0.148209 -0.26231 -0.45614 -p 0 -0.26231 -0.479614 -p 0.148209 -0.26231 -0.45614 -p 0.28191 -0.26231 -0.388016 -p 0.388016 -0.26231 -0.28191 -p 0.45614 -0.26231 -0.148209 -p 0.479614 -0.26231 0 -p 0.45614 -0.26231 0.148209 -p 0.388016 -0.26231 0.28191 -p 0.28191 -0.26231 0.388016 -p 0.148209 -0.26231 0.45614 -p -1.42936e-08 -0.26231 0.479614 -p -1.42936e-08 0.26231 0.479614 -p -2.99285e-08 0.26231 1.004233 -p -0.310325 0.26231 0.955083 -p -0.590274 0.26231 0.812442 -p -0.812442 0.26231 0.590274 -p -0.955083 0.26231 0.310325 -p -1.004234 0.26231 0 -p -0.955083 0.26231 -0.310325 -p -0.812442 0.26231 -0.590274 -p -0.590274 0.26231 -0.812442 -p -0.310325 0.26231 -0.955083 -p 0 0.26231 -1.004234 -p 0.310325 0.26231 -0.955083 -p 0.590274 0.26231 -0.812442 -p 0.812442 0.26231 -0.590274 -p 0.955083 0.26231 -0.310325 -p 1.004233 0.26231 0 -p 0.955083 0.26231 0.310325 -p 0.812442 0.26231 0.590274 -p 0.590274 0.26231 0.812442 -p 0.310325 0.26231 0.955083 -p -2.99285e-08 0.26231 1.004233 -p -2.99285e-08 -0.26231 1.004233 -p 0.310325 -0.26231 0.955083 -p 0.590273 -0.26231 0.812442 -p 0.812442 -0.26231 0.590274 -p 0.955083 -0.26231 0.310325 -p 1.004233 -0.26231 0 -p 0.955083 -0.26231 -0.310325 -p 0.812442 -0.26231 -0.590274 -p 0.590274 -0.26231 -0.812442 -p 0.310325 -0.26231 -0.955083 -p 0 -0.26231 -1.004234 -p -0.310325 -0.26231 -0.955083 -p -0.590274 -0.26231 -0.812442 -p -0.812442 -0.26231 -0.590274 -p -0.955083 -0.26231 -0.310325 -p -1.004234 -0.26231 0 -p -0.955083 -0.26231 0.310325 -p -0.812442 -0.26231 0.590274 -p -0.590274 -0.26231 0.812442 -p -0.310325 -0.26231 0.955083 -p -2.99285e-08 -0.26231 1.004233 -p 0.310325 -0.26231 0.955083 -p 0.590273 -0.26231 0.812442 -p 0.812442 -0.26231 0.590274 -p 0.955083 -0.26231 0.310325 -p 1.004233 -0.26231 0 -p 1.004233 0.26231 0 -p 0.479614 0.26231 0 -p 0.479614 -0.26231 0 -p 1.004233 -0.26231 0 -p 1.004233 0.26231 0 -p 0.955083 0.26231 -0.310325 -p 0.812442 0.26231 -0.590274 -p 0.590274 0.26231 -0.812442 -p 0.310325 0.26231 -0.955083 -p 0 0.26231 -1.004234 -p 0 -0.26231 -1.004234 -p 0 -0.26231 -0.479614 -p 0 0.26231 -0.479614 -p 0 0.26231 -1.004234 -p -0.310325 0.26231 -0.955083 -p -0.590274 0.26231 -0.812442 -p -0.812442 0.26231 -0.590274 -p -0.955083 0.26231 -0.310325 -p -1.004234 0.26231 0 -p -1.004234 -0.26231 0 -p -0.479614 -0.26231 0 -p -0.479614 0.26231 0 -p -1.004234 0.26231 0 -p -0.955083 0.26231 0.310325 -p -0.812442 0.26231 0.590274 -p -0.590274 0.26231 0.812442 -p -0.310325 0.26231 0.955083 -p -2.99285e-08 0.26231 1.004233 -p -2.99285e-08 -0.26231 1.004233 -p -1.42936e-08 -0.26231 0.479614 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 -k 70 -k 71 -k 72 -k 73 -k 74 -k 75 -k 76 -k 77 -k 78 -k 79 -k 80 -k 81 -k 82 -k 83 -k 84 -k 85 -k 86 -k 87 -k 88 -k 89 -k 90 -k 91 -k 92 -k 93 -k 94 -k 95 -k 96 -k 97 -k 98 -k 99 -k 100 -k 101 -k 102 -k 103 -k 104 -k 105 -k 106 -k 107 -k 108 -k 109 -k 110 -k 111 -k 112 -k 113 -k 114 -k 115 -k 116 -k 117 -k 118 -k 119 ;")
            if ControllerType == 29:
                newController = mel.eval("curve -d 1 -p -2.98863e-08 -1.12841e-08 1.002818 -p -0.309888 -1.12841e-08 0.953737 -p -0.589442 -1.12841e-08 0.811297 -p -0.811297 -1.12841e-08 0.589442 -p -0.953737 -1.12841e-08 0.309888 -p -1.002819 -1.12841e-08 0 -p -0.953737 -1.12841e-08 -0.309888 -p -0.811297 -1.12841e-08 -0.589442 -p -0.589442 -1.12841e-08 -0.811297 -p -0.309888 -1.12841e-08 -0.953737 -p 0 -1.12841e-08 -1.002819 -p 0.309888 -1.12841e-08 -0.953737 -p 0.589442 -1.12841e-08 -0.811297 -p 0.811298 -1.12841e-08 -0.589442 -p 0.953737 -1.12841e-08 -0.309888 -p 1.002818 -1.12841e-08 0 -p 0.953737 -1.12841e-08 0.309888 -p 0.811297 -1.12841e-08 0.589442 -p 0.589442 -1.12841e-08 0.811297 -p 0.309888 -1.12841e-08 0.953737 -p -2.98863e-08 -1.12841e-08 1.002818 -p 0 0 0 -p 0 -1.12841e-08 -1.002819 -p 0.309888 -1.12841e-08 -0.953737 -p 0.589442 -1.12841e-08 -0.811297 -p 0.811298 -1.12841e-08 -0.589442 -p 0.953737 -1.12841e-08 -0.309888 -p 1.002818 -1.12841e-08 0 -p 0 0 0 -p -1.002819 -1.12841e-08 0 -p 0 0 0 -p 0 1.170479 0 -p 0 2.13812 0 -p 0.483821 1.170479 0 -p 0.342113 1.170479 -0.342113 -p 0 1.170479 -0.483821 -p -0.342113 1.170479 -0.342113 -p -0.483821 1.170479 0 -p -0.342113 1.170479 0.342113 -p 0 1.170479 0.483821 -p 0.342113 1.170479 0.342113 -p 0.483821 1.170479 0 -p 0.342113 1.170479 -0.342113 -p 0 2.13812 0 -p 0 1.170479 -0.483821 -p 0 2.13812 0 -p -0.342113 1.170479 -0.342113 -p 0 2.13812 0 -p -0.483821 1.170479 0 -p 0 2.13812 0 -p -0.342113 1.170479 0.342113 -p 0 2.13812 0 -p 0 1.170479 0.483821 -p 0 2.13812 0 -p 0.342113 1.170479 0.342113 -p 0 2.13812 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 ;")
            if ControllerType == 30:
                newController = mel.eval("curve -d 3 -p 0.244733 0.11108 0 -p 0.2124 0.0739642 0 -p 0.147736 -0.000267686 0 -p -0.0752292 -0.0629865 0 -p -0.165999 -0.00164294 0 -p -0.341003 -0.042708 0 -p -0.505952 0.0602088 0 -p -0.626887 0.255968 0 -p -0.633052 0.591231 0 -p -0.611347 0.647309 0 -p -0.674305 0.724892 0 -p -0.886647 0.924843 0 -p -0.983152 1.020888 0 -p -0.990416 1.150432 0 -p -0.91098 1.246545 0 -p -0.797106 1.239931 0 -p -0.769309 1.2164 0 -p -0.57924 1.012709 0 -p -0.537053 0.956169 0 -p -0.508415 0.943213 0 -p -0.508328 0.950102 0 -p -0.504414 0.95985 0 -p -0.512971 0.992988 0 -p -0.5078 0.987173 0 -p -0.588169 1.174841 0 -p -0.679893 1.294614 0 -p -0.745245 1.486832 0 -p -0.689984 1.664983 0 -p -0.540877 1.688412 0 -p -0.430568 1.575873 0 -p -0.362822 1.379146 0 -p -0.34926 1.246432 0 -p -0.305002 1.1566 0 -p -0.273924 1.115243 0 -p -0.269772 1.127311 0 -p -0.259976 1.13764 0 -p -0.297565 1.386036 0 -p -0.354392 1.55342 0 -p -0.368255 1.795484 0 -p -0.291944 1.909761 0 -p -0.115731 1.911981 0 -p -0.0426305 1.779833 0 -p -0.0256664 1.55985 0 -p -0.00851656 1.387778 0 -p 0.0128518 1.253462 0 -p 0.0438934 1.134074 0 -p 0.0668622 1.126045 0 -p 0.0823771 1.150848 0 -p 0.0820804 1.237602 0 -p 0.104469 1.337456 0 -p 0.13101 1.591276 0 -p 0.186932 1.79924 0 -p 0.360336 1.868929 0 -p 0.481175 1.782737 0 -p 0.502229 1.587967 0 -p 0.44352 1.344087 0 -p 0.384292 1.155026 0 -p 0.340648 0.873485 0 -p 0.385972 0.690293 0 -p 0.559313 0.762202 0 -p 0.668786 0.865086 0 -p 0.905714 0.890538 0 -p 1.045379 0.629301 0 -p 0.890624 0.508491 0 -p 0.747996 0.451928 0 -p 0.533551 0.389219 0 -p 0.453023 0.34236 0 -p 0.314163 0.188174 0 -p 0.244733 0.11108 0 -k 0 -k 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 66 -k 66 ;")
    
            CcName = cmds.rename(newController ,ControllerName+"_cc_"   +str(controllerNameNum).zfill(3))
            cmds.setAttr(CcName+'.scale' ,controllerScale,controllerScale,controllerScale )
            getRotationOffsetX = cmds.getAttr(CcName+'.rx')
            getRotationOffsetY = cmds.getAttr(CcName+'.ry')
            getRotationOffsetZ = cmds.getAttr(CcName+'.rz')
            cmds.setAttr(CcName+'.rotate' ,getRotationOffsetX + rotationOffsetX,getRotationOffsetY + rotationOffsetY,getRotationOffsetZ + rotationOffsetZ)
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
            controllerNameNum += 1
            child = CcName
            if controllerGroupNum > 0:
                for grp in range (controllerGroupNum):
                    GrpName = (ControllerName+"_cc_grp_"   +str(controllerGrpNameNum).zfill(3))
                    controllerGrp = cmds.group( n = GrpName , em = True)
                    cmds.parent(child , controllerGrp)
                    controllerGrpNameNum +=1
                    child = controllerGrp
                HirarchyList.append(CcName)
                HirarchyList.append(child)
                cmds.delete(cmds.parentConstraint( obj , controllerGrp , mo = 0))
                if parentConstraintStatue == 1:
                    cmds.parentConstraint( CcName , obj , mo = 0)
                if scaleConstraintStatue == 1:
                    cmds.scaleConstraint( CcName , obj)
            else:
                cmds.delete(cmds.parentConstraint( obj , CcName , mo = 0))
                if parentConstraintStatue == 1:
                    cmds.parentConstraint( CcName , obj , mo = 0)
                if scaleConstraintStatue == 1:
                    cmds.scaleConstraint( CcName , obj)
        if HirarchyControllers == True:
            Range = len(HirarchyList)/2
            parentNum = 3
            childNum = 0
            HirarchyList.reverse()
            print(HirarchyList)
            for Hir in range(Range-1):
                cmds.parent(HirarchyList[childNum] , HirarchyList[parentNum])
                parentNum += 2
                childNum += 2
    
    if len(sel) == 0:
        if ControllerType == 1:
            newController = mel.eval("curve -d 1 -p 1 0 0 -p 0.951057 0 0.309017 -p 0.809017 0 0.587785 -p 0.587785 0 0.809017 -p 0.309017 0 0.951057 -p -2.98023e-08 0 1 -p -0.309017 0 0.951057 -p -0.587785 0 0.809017 -p -0.809017 0 0.587785 -p -0.951057 0 0.309017 -p -1 0 0 -p -0.951057 0 -0.309017 -p -0.809017 0 -0.587785 -p -0.587785 0 -0.809017 -p -0.309017 0 -0.951057 -p 0 0 -1 -p 0.309017 0 -0.951057 -p 0.587786 0 -0.809017 -p 0.809018 0 -0.587786 -p 0.951057 0 -0.309017 -p 1 0 0 -p 0.987688 0.156434 0 -p 0.951057 0.309017 0 -p 0.891007 0.453991 0 -p 0.809017 0.587785 0 -p 0.707107 0.707107 0 -p 0.587785 0.809017 0 -p 0.453991 0.891007 0 -p 0.309017 0.951057 0 -p 0.156434 0.987688 0 -p 0 1 0 -p -0.156435 0.987688 0 -p -0.309017 0.951057 0 -p -0.453991 0.891007 0 -p -0.587785 0.809017 0 -p -0.707107 0.707107 0 -p -0.809017 0.587785 0 -p -0.891007 0.453991 0 -p -0.951057 0.309017 0 -p -0.987689 0.156434 0 -p -1 0 0 -p -0.951057 0 -0.309017 -p -0.809017 0 -0.587785 -p -0.587785 0 -0.809017 -p -0.309017 0 -0.951057 -p 0 0 -1 -p 0 0.156434 -0.987689 -p 0 0.309017 -0.951057 -p 0 0.453991 -0.891007 -p 0 0.587785 -0.809017 -p 0 0.707107 -0.707107 -p 0 0.809017 -0.587786 -p 0 0.891007 -0.453991 -p 0 0.951057 -0.309017 -p 0 0.987688 -0.156435 -p 0 1 0 -p -4.66211e-09 0.987688 0.156434 -p -9.20942e-09 0.951057 0.309017 -p -1.353e-08 0.891007 0.453991 -p -1.75174e-08 0.809017 0.587785 -p -2.10734e-08 0.707107 0.707107 -p -2.41106e-08 0.587785 0.809017 -p -2.65541e-08 0.453991 0.891007 -p -2.83437e-08 0.309017 0.951057 -p -2.94354e-08 0.156434 0.987688 -p -2.98023e-08 0 1 -p 0 0 0 -p 0 0 -1 -p -0.309017 0 -0.951057 -p -0.587785 0 -0.809017 -p -0.809017 0 -0.587785 -p -0.951057 0 -0.309017 -p -1 0 0 -p 0 0 0 -p 1 0 0 -p 0 0 0 -p 0 1 0 -p 0 1.784043 0 -p 0 2.873933 0 -p 0.544945 1.784043 0 -p 0.518274 1.784043 -0.168397 -p 0.44087 1.784043 -0.320311 -p 0.320311 1.784043 -0.44087 -p 0.168397 1.784043 -0.518274 -p 0 1.784043 -0.544945 -p -0.168397 1.784043 -0.518274 -p -0.320311 1.784043 -0.44087 -p -0.44087 1.784043 -0.320311 -p -0.518274 1.784043 -0.168397 -p -0.544945 1.784043 0 -p -0.518274 1.784043 0.168397 -p -0.44087 1.784043 0.320311 -p -0.320311 1.784043 0.44087 -p -0.168397 1.784043 0.518274 -p -1.62406e-08 1.784043 0.544945 -p 0.168397 1.784043 0.518274 -p 0.320311 1.784043 0.44087 -p 0.44087 1.784043 0.320311 -p 0.518274 1.784043 0.168397 -p 0.544945 1.784043 0 -p 0 2.873933 0 -p -1.62406e-08 1.784043 0.544945 -p 0 2.873933 0 -p -0.544945 1.784043 0 -p 0 2.873933 0 -p 0 1.784043 -0.544945 -p 0 2.873933 0 -p 0.518274 1.784043 -0.168397 -p 0 2.873933 0 -p 0.44087 1.784043 -0.320311 -p 0 2.873933 0 -p 0.320311 1.784043 -0.44087 -p 0 2.873933 0 -p 0.168397 1.784043 -0.518274 -p 0 2.873933 0 -p -0.168397 1.784043 -0.518274 -p 0 2.873933 0 -p -0.320311 1.784043 -0.44087 -p 0 2.873933 0 -p -0.44087 1.784043 -0.320311 -p 0 2.873933 0 -p -0.518274 1.784043 -0.168397 -p 0 2.873933 0 -p -0.518274 1.784043 0.168397 -p 0 2.873933 0 -p -0.44087 1.784043 0.320311 -p 0 2.873933 0 -p -0.320311 1.784043 0.44087 -p 0 2.873933 0 -p -0.168397 1.784043 0.518274 -p 0 2.873933 0 -p 0.168397 1.784043 0.518274 -p 0 2.873933 0 -p 0.320311 1.784043 0.44087 -p 0 2.873933 0 -p 0.44087 1.784043 0.320311 -p 0 2.873933 0 -p 0.518274 1.784043 0.168397 -p 0 2.873933 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 -k 70 -k 71 -k 72 -k 73 -k 74 -k 75 -k 76 -k 77 -k 78 -k 79 -k 80 -k 81 -k 82 -k 83 -k 84 -k 85 -k 86 -k 87 -k 88 -k 89 -k 90 -k 91 -k 92 -k 93 -k 94 -k 95 -k 96 -k 97 -k 98 -k 99 -k 100 -k 101 -k 102 -k 103 -k 104 -k 105 -k 106 -k 107 -k 108 -k 109 -k 110 -k 111 -k 112 -k 113 -k 114 -k 115 -k 116 -k 117 -k 118 -k 119 -k 120 -k 121 -k 122 -k 123 -k 124 -k 125 -k 126 -k 127 -k 128 -k 129 -k 130 -k 131 -k 132 -k 133 -k 134 -k 135 -k 136 -k 137 -k 138 ;")
        if ControllerType == 2:
            newController = mel.eval("curve -d 1 -p -1 0 -5.96046e-08 -p -0.965926 0 0.258819 -p -0.866025 0 0.5 -p -0.707107 0 0.707107 -p -0.5 0 0.866025 -p -0.258819 0 0.965926 -p -2.98023e-08 0 1 -p 0.258819 0 0.965926 -p 0.5 0 0.866025 -p 0.707107 0 0.707107 -p 0.866025 0 0.5 -p 0.965926 0 0.258819 -p 1 0 0 -p 0.965925 0 -0.258819 -p 0.866025 0 -0.5 -p 0.707106 0 -0.707106 -p 0.5 0 -0.866025 -p 0.258819 0 -0.965925 -p 1.19209e-07 0 -0.999999 -p -0.258819 0 -0.965925 -p -0.5 0 -0.866025 -p -0.707106 0 -0.707107 -p -0.866025 0 -0.5 -p -0.965926 0 -0.258819 -p -1 0 -5.96046e-08 -p -0.987688 0.156434 -5.88708e-08 -p -0.951056 0.309017 -5.66874e-08 -p -0.891006 0.453991 -5.31081e-08 -p -0.809017 0.587785 -4.82212e-08 -p -0.707107 0.707107 -4.21468e-08 -p -0.587785 0.809017 -3.50347e-08 -p -0.45399 0.891007 -2.70599e-08 -p -0.309017 0.951057 -1.84188e-08 -p -0.156434 0.987688 -9.32422e-09 -p 0 1 0 -p 0.156434 0.987688 0 -p 0.309017 0.951057 0 -p 0.453991 0.891007 0 -p 0.587785 0.809017 0 -p 0.707107 0.707107 0 -p 0.809017 0.587785 0 -p 0.891007 0.453991 0 -p 0.951057 0.309017 0 -p 0.987688 0.156434 0 -p 1 0 0 -p 0.965925 0 -0.258819 -p 0.866025 0 -0.5 -p 0.707106 0 -0.707106 -p 0.5 0 -0.866025 -p 0.258819 0 -0.965925 -p 1.19209e-07 0 -0.999999 -p 1.17742e-07 0.156434 -0.987688 -p 1.13375e-07 0.309017 -0.951056 -p 1.06216e-07 0.453991 -0.891006 -p 9.64423e-08 0.587785 -0.809017 -p 8.42937e-08 0.707107 -0.707106 -p 7.00695e-08 0.809017 -0.587785 -p 5.41199e-08 0.891007 -0.45399 -p 3.68377e-08 0.951057 -0.309017 -p 1.86484e-08 0.987688 -0.156434 -p 0 1 0 -p -4.66211e-09 0.987688 0.156434 -p -9.20942e-09 0.951057 0.309017 -p -1.353e-08 0.891007 0.45399 -p -1.75174e-08 0.809017 0.587785 -p -2.10734e-08 0.707107 0.707107 -p -2.41106e-08 0.587785 0.809017 -p -2.65541e-08 0.453991 0.891006 -p -2.83437e-08 0.309017 0.951056 -p -2.94354e-08 0.156434 0.987688 -p -2.98023e-08 0 1 -p 0.258819 0 0.965926 -p 0.5 0 0.866025 -p 0.707107 0 0.707107 -p 0.698401 0.156434 0.698401 -p 0.672498 0.309017 0.672499 -p 0.630037 0.453991 0.630037 -p 0.572061 0.587785 0.572061 -p 0.5 0.707107 0.5 -p 0.415627 0.809017 0.415627 -p 0.32102 0.891007 0.32102 -p 0.218508 0.951057 0.218508 -p 0.110616 0.987688 0.110616 -p 0 1 0 -p -0.110616 0.987688 -0.110616 -p -0.218508 0.951057 -0.218508 -p -0.32102 0.891007 -0.32102 -p -0.415627 0.809017 -0.415627 -p -0.5 0.707107 -0.5 -p -0.572061 0.587785 -0.572061 -p -0.630036 0.453991 -0.630037 -p -0.672498 0.309017 -0.672498 -p -0.698401 0.156434 -0.698401 -p -0.707106 0 -0.707107 -p -0.5 0 -0.866025 -p -0.258819 0 -0.965925 -p 1.19209e-07 0 -0.999999 -p 0.258819 0 -0.965925 -p 0.5 0 -0.866025 -p 0.707106 0 -0.707106 -p 0.698401 0.156434 -0.698401 -p 0.672498 0.309017 -0.672498 -p 0.630036 0.453991 -0.630036 -p 0.572061 0.587785 -0.572061 -p 0.5 0.707107 -0.5 -p 0.415627 0.809017 -0.415627 -p 0.32102 0.891007 -0.32102 -p 0.218508 0.951057 -0.218508 -p 0.110616 0.987688 -0.110616 -p 0 1 0 -p -0.110616 0.987688 0.110616 -p -0.218508 0.951057 0.218508 -p -0.32102 0.891007 0.32102 -p -0.415627 0.809017 0.415627 -p -0.5 0.707107 0.5 -p -0.572061 0.587785 0.572061 -p -0.630037 0.453991 0.630037 -p -0.672498 0.309017 0.672498 -p -0.698401 0.156434 0.698401 -p -0.707107 0 0.707107 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 -k 70 -k 71 -k 72 -k 73 -k 74 -k 75 -k 76 -k 77 -k 78 -k 79 -k 80 -k 81 -k 82 -k 83 -k 84 -k 85 -k 86 -k 87 -k 88 -k 89 -k 90 -k 91 -k 92 -k 93 -k 94 -k 95 -k 96 -k 97 -k 98 -k 99 -k 100 -k 101 -k 102 -k 103 -k 104 -k 105 -k 106 -k 107 -k 108 -k 109 -k 110 -k 111 -k 112 -k 113 -k 114 -k 115 -k 116 -k 117 -k 118 -k 119 ;")
        if ControllerType == 3:
            newController = mel.eval("curve -d 1 -p -1.296206 0 0 -p -1.050693 0 -0.245513 -p -1.050693 0 -0.122757 -p -1.024305 -4.37114e-09 -0.12197 -p -0.99861 -4.37114e-09 -0.324468 -p -0.849468 -4.37114e-09 -0.617175 -p -0.617175 -4.37114e-09 -0.849468 -p -0.324468 -4.37114e-09 -0.99861 -p 0 -4.37114e-09 -1.05 -p 0.324468 -4.37114e-09 -0.99861 -p 0.617175 -4.37114e-09 -0.849468 -p 0.849468 -4.37114e-09 -0.617175 -p 0.99861 -4.37114e-09 -0.324468 -p 1.05 -4.37114e-09 0 -p 0.998609 -4.37114e-09 0.324468 -p 0.849468 -4.37114e-09 0.617175 -p 0.617175 -4.37114e-09 0.849468 -p 0.324468 -4.37114e-09 0.998609 -p -3.12924e-08 -4.37114e-09 1.05 -p -0.324468 -4.37114e-09 0.998609 -p -0.617175 -4.37114e-09 0.849468 -p -0.849468 -4.37114e-09 0.617175 -p -0.99861 -4.37114e-09 0.324468 -p -1.024305 -4.37114e-09 0.12197 -p -1.050693 0 0.122757 -p -1.050693 0 0.245513 -p -1.296206 0 0 -p -1.050693 0 0 -p -0.95 0 0 -p -0.926752 0 -0.110354 -p -0.903504 0 -0.293566 -p -0.768566 0 -0.558396 -p -0.558396 0 -0.768566 -p -0.293566 0 -0.903504 -p 0 0 -0.95 -p 0.293566 0 -0.903504 -p 0.558396 0 -0.768567 -p 0.768567 0 -0.558396 -p 0.903504 0 -0.293566 -p 0.95 0 0 -p 0.903504 0 0.293566 -p 0.768566 0 0.558396 -p 0.558396 0 0.768566 -p 0.293566 0 0.903504 -p -2.83122e-08 0 0.95 -p -0.293566 0 0.903504 -p -0.558396 0 0.768566 -p -0.768566 0 0.558396 -p -0.903504 0 0.293566 -p -0.926752 0 0.110354 -p -0.95 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 ;")
        if ControllerType == 4:
            newController = mel.eval("curve -d 1 -p -1 -0.285425 -5.96046e-08 -p -0.965926 -0.285425 0.258819 -p -0.866025 -0.285425 0.5 -p -0.707107 -0.285425 0.707107 -p -0.5 -0.285425 0.866025 -p -0.258819 -0.285425 0.965926 -p -2.98023e-08 -0.285425 1 -p 0.258819 -0.285425 0.965926 -p 0.5 -0.285425 0.866025 -p 0.707107 -0.285425 0.707107 -p 0.866025 -0.285425 0.5 -p 0.965926 -0.285425 0.258819 -p 1 -0.285425 0 -p 0.965925 -0.285425 -0.258819 -p 0.866025 -0.285425 -0.5 -p 0.707106 -0.285425 -0.707106 -p 0.5 -0.285425 -0.866025 -p 0.258819 -0.285425 -0.965925 -p 1.19209e-07 -0.285425 -0.999999 -p -0.258819 -0.285425 -0.965925 -p -0.5 -0.285425 -0.866025 -p -0.707106 -0.285425 -0.707107 -p -0.866025 -0.285425 -0.5 -p -0.965926 -0.285425 -0.258819 -p -1 -0.285425 -5.96046e-08 -p -1 0.285425 -5.96046e-08 -p -0.965926 0.285425 -0.258819 -p -0.866025 0.285425 -0.5 -p -0.707106 0.285425 -0.707107 -p -0.707106 -0.285425 -0.707107 -p -0.707106 0.285425 -0.707107 -p -0.5 0.285425 -0.866025 -p -0.258819 0.285425 -0.965925 -p 1.19209e-07 0.285425 -0.999999 -p 1.19209e-07 -0.285425 -0.999999 -p 1.19209e-07 0.285425 -0.999999 -p 0.258819 0.285425 -0.965925 -p 0.5 0.285425 -0.866025 -p 0.707106 0.285425 -0.707106 -p 0.707106 -0.285425 -0.707106 -p 0.707106 0.285425 -0.707106 -p 0.866025 0.285425 -0.5 -p 0.965925 0.285425 -0.258819 -p 1 0.285425 0 -p 1 -0.285425 0 -p 1 0.285425 0 -p 0.965926 0.285425 0.258819 -p 0.866025 0.285425 0.5 -p 0.707107 0.285425 0.707107 -p 0.707107 -0.285425 0.707107 -p 0.707107 0.285425 0.707107 -p 0.5 0.285425 0.866025 -p 0.258819 0.285425 0.965926 -p -2.98023e-08 0.285425 1 -p -0.258819 0.285425 0.965926 -p -0.5 0.285425 0.866025 -p -0.707107 0.285425 0.707107 -p -0.707107 -0.285425 0.707107 -p -0.707107 0.285425 0.707107 -p -0.866025 0.285425 0.5 -p -0.965926 0.285425 0.258819 -p -1 0.285425 -5.96046e-08 -p -0.965926 0.285425 0.258819 -p -0.866025 0.285425 0.5 -p -0.707107 0.285425 0.707107 -p -0.5 0.285425 0.866025 -p -0.258819 0.285425 0.965926 -p -2.98023e-08 0.285425 1 -p -2.98023e-08 -0.285425 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 ;")
        if ControllerType == 5:
            newController = mel.eval("curve -d 1 -p 0 0 1 -p 0 0 1 -p -0.399952 0 0.599928 -p -0.199976 0 0.599928 -p -0.199976 0 0.199976 -p -0.599928 0 0.199976 -p -0.599928 0 0.399952 -p -1 0 0 -p -0.599928 0 -0.399952 -p -0.599928 0 -0.199976 -p -0.199976 0 -0.199976 -p -0.199976 0 -0.599928 -p -0.399952 0 -0.599928 -p 0 0 -1 -p 0.399952 0 -0.599928 -p 0.199976 0 -0.599928 -p 0.199976 0 -0.199976 -p 0.599928 0 -0.199976 -p 0.599928 0 -0.399952 -p 1 0 0 -p 0.599928 0 0.399952 -p 0.599928 0 0.199976 -p 0.199976 0 0.199976 -p 0.199976 0 0.599928 -p 0.399952 0 0.599928 -p 0 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 ;")
        if ControllerType == 6:
            newController = mel.eval("curve -d 1 -p -0.25 0 1 -p -0.25 0 0.25 -p -1 0 0.25 -p -1 0 -0.25 -p -0.25 0 -0.25 -p -0.25 0 -1 -p 0.25 0 -1 -p 0.25 0 -0.25 -p 1 0 -0.25 -p 1 0 0.25 -p 0.25 0 0.25 -p 0.25 0 1 -p -0.25 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 ;")
        if ControllerType == 7:
            newController = mel.eval("curve -d 1 -p 0 0 0 -p 0 4.032974 0 -p -0.156435 4.045285 0 -p -0.309017 4.081917 0 -p -0.453991 4.141967 0 -p -0.587785 4.223957 0 -p -0.707107 4.325867 0 -p -0.809017 4.445189 0 -p -0.891007 4.578983 0 -p -0.951057 4.723957 0 -p -0.987689 4.876539 0 -p -1 5.032974 0 -p -0.987689 5.189408 0 -p -0.951057 5.341991 0 -p -0.891007 5.486964 0 -p -0.809017 5.620759 0 -p -0.707107 5.74008 0 -p -0.587785 5.841991 0 -p -0.453991 5.92398 0 -p -0.309017 5.98403 0 -p -0.156435 6.020662 0 -p 0 6.032974 0 -p 0.156434 6.020662 0 -p 0.309017 5.98403 0 -p 0.453991 5.92398 0 -p 0.587785 5.841991 0 -p 0.707107 5.74008 0 -p 0.809017 5.620759 0 -p 0.891007 5.486964 0 -p 0.951057 5.341991 0 -p 0.987688 5.189408 0 -p 1 5.032974 0 -p 0.987688 4.876539 0 -p 0.951057 4.723957 0 -p 0.891007 4.578983 0 -p 0.809017 4.445189 0 -p 0.707107 4.325867 0 -p 0.587785 4.223957 0 -p 0.453991 4.141967 0 -p 0.309017 4.081917 0 -p 0.156434 4.045285 0 -p 0 4.032974 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 ;")
        if ControllerType == 8:
            newController = mel.eval("curve -d 1 -p 0 0 0 -p -2.98023e-08 4.048372 0 -p -1.33187e-08 4.601471 0 -p -0.309017 4.097315 0 -p -0.262682 4.686821 0 -p -0.809017 4.460587 0 -p -0.425028 4.910272 0 -p -1 5.048372 0 -p -0.425028 5.186472 0 -p -0.809017 5.636157 0 -p -0.262682 5.409923 0 -p -0.309017 5.999429 0 -p 0 5.495273 0 -p 0.309017 5.999429 0 -p 0.262682 5.409923 0 -p 0.809018 5.636158 0 -p 0.425028 5.186472 0 -p 1 5.048372 0 -p 0.425028 4.910272 0 -p 0.809017 4.460587 0 -p 0.262682 4.686821 0 -p 0.309017 4.097315 0 -p -1.33187e-08 4.601471 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 ;")
        if ControllerType == 9:
            newController = mel.eval("curve -d 1 -p 0.802112 0 0 -p 1 0 0 -p 0.951057 -0.309017 0 -p 0.809017 -0.587785 0 -p 0.587785 -0.809017 0 -p 0.309017 -0.951057 0 -p -2.98023e-08 -1 0 -p -0.309017 -0.951057 0 -p -0.587785 -0.809017 0 -p -0.809017 -0.587785 0 -p -0.951057 -0.309017 0 -p -1 0 0 -p -0.951057 0.309017 0 -p -0.809017 0.587785 0 -p -0.587785 0.809017 0 -p -0.309017 0.951057 0 -p 0 1 0 -p 0.0221199 1.302628 0 -p 0.828684 0.899346 0 -p 0.0221199 0.496064 0 -p 0 0.802112 0 -p -0.247866 0.762854 0 -p -0.47147 0.648922 0 -p -0.648922 0.47147 0 -p -0.762854 0.247866 0 -p -0.802112 0 0 -p -0.762854 -0.247866 0 -p -0.648922 -0.471469 0 -p -0.471469 -0.648922 0 -p -0.247866 -0.762854 0 -p -2.39048e-08 -0.802112 0 -p 0.247866 -0.762854 0 -p 0.471469 -0.648922 0 -p 0.648922 -0.471469 0 -p 0.762854 -0.247866 0 -p 0.802112 0 0 -p 1 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 ;")
        if ControllerType == 10:
            newController = mel.eval("curve -d 1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 -1 -p -1 0 1 -p 1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;")
        if ControllerType == 11:
            newController = mel.eval("curve -d 1 -p 0 -1.29603e-09 0.688679 -p 0.0962036 -1.29603e-09 0.703916 -p 0.18299 -1.29603e-09 0.748136 -p 0.251864 -1.29603e-09 0.81701 -p 0.296084 -1.29603e-09 0.903796 -p 0.311321 -1.29603e-09 1 -p 0.296084 -1.29603e-09 1.096204 -p 0.251864 -1.29603e-09 1.18299 -p 0.18299 -1.29603e-09 1.251864 -p 0.0962036 -1.29603e-09 1.296084 -p -9.2781e-09 -1.29603e-09 1.311321 -p -0.0962036 -1.29603e-09 1.296084 -p -0.18299 -1.29603e-09 1.251864 -p -0.251864 -1.29603e-09 1.18299 -p -0.296084 -1.29603e-09 1.096204 -p -0.311321 -1.29603e-09 1 -p -0.296084 -1.29603e-09 0.903796 -p -0.251864 -1.29603e-09 0.81701 -p -0.18299 -1.29603e-09 0.748136 -p -0.0962036 -1.29603e-09 0.703916 -p 0 -1.29603e-09 0.688679 -p 0 0 0 -p -9.2781e-09 -1.29603e-09 -0.688679 -p -0.0962036 -1.29603e-09 -0.703916 -p -0.18299 -1.29603e-09 -0.748136 -p -0.251864 -1.29603e-09 -0.81701 -p -0.296084 -1.29603e-09 -0.903796 -p -0.311321 -1.29603e-09 -1 -p -0.296084 -1.29603e-09 -1.096204 -p -0.251864 -1.29603e-09 -1.18299 -p -0.18299 -1.29603e-09 -1.251864 -p -0.0962036 -1.29603e-09 -1.296084 -p 0 -1.29603e-09 -1.311321 -p 0.0962036 -1.29603e-09 -1.296084 -p 0.18299 -1.29603e-09 -1.251864 -p 0.251864 -1.29603e-09 -1.18299 -p 0.296084 -1.29603e-09 -1.096204 -p 0.311321 -1.29603e-09 -1 -p 0.296084 -1.29603e-09 -0.903796 -p 0.251864 -1.29603e-09 -0.81701 -p 0.18299 -1.29603e-09 -0.748136 -p 0.0962036 -1.29603e-09 -0.703916 -p -9.2781e-09 -1.29603e-09 -0.688679 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 ;")
        if ControllerType == 12:
            newController = mel.eval("curve -d 1 -p 0.624948 0.273104 0.636666 -p 0.706724 0.706724 1.00216 -p 0.273104 0.624948 0.636666 -p -1.68791e-09 0.999458 1.00216 -p -0.248791 0.635019 0.636666 -p -0.706724 0.706724 1.00216 -p -0.624948 0.273104 0.636666 -p -0.999458 -1.68791e-09 1.00216 -p -0.624948 -0.273104 0.636666 -p -0.706724 -0.706724 1.00216 -p -0.248791 -0.635019 0.636666 -p 1.68791e-09 -0.999458 1.00216 -p 0.264025 -0.633976 0.6367 -p 0.706724 -0.706724 1.00216 -p 0.634983 -0.261595 0.6367 -p 0.999458 1.68791e-09 1.00216 -p 0.624948 0.273104 0.636666 -p 0 0 0 -p 0.273104 0.624948 0.636666 -p 0 0 0 -p -0.248791 0.635019 0.636666 -p 0 0 0 -p -0.624948 0.273104 0.636666 -p 0 0 0 -p -0.624948 -0.273104 0.636666 -p 0 0 0 -p -0.248791 -0.635019 0.636666 -p 0 0 0 -p 0.264025 -0.633976 0.6367 -p 0 0 0 -p 0.634983 -0.261595 0.6367 -p 0 0 0 -p 0 0 1.841218 -p 3.41745e-08 0.260607 1.841218 -p -0.260607 2.2783e-08 1.841218 -p -1.13915e-08 -0.260607 1.841218 -p 0.260607 0 1.841218 -p 3.41745e-08 0.260607 1.841218 -p -1.13915e-08 -0.260607 1.841218 -p 0.260607 0 1.841218 -p -0.260607 2.2783e-08 1.841218 -p 0 0 2.348702 -p 3.41745e-08 0.260607 1.841218 -p 0 0 2.348702 -p 0.260607 0 1.841218 -p 0 0 2.348702 -p -1.13915e-08 -0.260607 1.841218 -p 0 0 2.348702 -p -0.260607 2.2783e-08 1.841218 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 ;")
        if ControllerType == 13:
            newController = mel.eval("curve -d 1 -p -0.500011 0 -0.342423 -p -0.475538 0 -0.546073 -p -0.404517 0 -0.729788 -p -0.293899 0 -0.875585 -p -0.154512 0 -0.969192 -p 0 0 -1.001447 -p 0.154512 0 -0.969193 -p 0.293899 0 -0.875585 -p 0.404517 0 -0.729788 -p 0.475538 0 -0.546073 -p 0.50001 0 -0.342423 -p 0.50001 0 -7.45074e-09 -p 0.50001 0 0.250005 -p 0.50001 0 0.50001 -p 0.487474 0 0.611273 -p 0.450494 0 0.716957 -p 0.390924 0 0.811762 -p 0.311751 0 0.890934 -p 0.216946 0 0.950504 -p 0.111263 0 0.987485 -p 0 0 1.000021 -p -0.111263 0 0.987485 -p -0.216946 0 0.950504 -p -0.311751 0 0.890934 -p -0.390924 0 0.811762 -p -0.450494 0 0.716957 -p -0.487474 0 0.611273 -p -0.500011 0 0.50001 -p -0.500011 0 0.250005 -p -0.500011 0 -7.45074e-09 -p -0.500011 0 -0.342423 -p -0.493855 0.0782188 -0.342423 -p -0.475538 0.154512 -0.342423 -p -0.445513 0.227 -0.342423 -p -0.404517 0.293899 -0.342423 -p -0.353561 0.353561 -0.342423 -p -0.293899 0.404517 -0.342423 -p -0.227 0.445513 -0.342423 -p -0.154512 0.475538 -0.342423 -p -0.0782189 0.493854 -0.342423 -p 0 0.50001 -0.342423 -p 0.0782189 0.493854 -0.342423 -p 0.154512 0.475538 -0.342423 -p 0.227 0.445513 -0.342423 -p 0.293899 0.404517 -0.342423 -p 0.353561 0.353561 -0.342423 -p 0.404517 0.293899 -0.342423 -p 0.445513 0.227 -0.342423 -p 0.475538 0.154512 -0.342423 -p 0.493854 0.0782188 -0.342423 -p 0.50001 0 -0.342423 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 ;")
        if ControllerType == 14:
            newController = mel.eval("curve -d 1 -p 0 2 0 -p -1 0 -8.74228e-08 -p 1.31134e-07 0 -1 -p 0 2 0 -p 1.31134e-07 0 -1 -p 1 0 0 -p 0 2 0 -p 1 0 0 -p -4.37114e-08 0 1 -p 0 2 0 -p -4.37114e-08 0 1 -p -1 0 -8.74228e-08 -p 0 2 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 ;")
        if ControllerType == 15:
            newController = mel.eval("curve -d 1 -p 1.31134e-07 0 -1 -p 0 -1 0 -p -4.37114e-08 0 1 -p 0 1 0 -p 1.31134e-07 0 -1 -p 1 0 0 -p -4.37114e-08 0 1 -p -1 0 -8.74228e-08 -p 1.31134e-07 0 -1 -p 1 0 0 -p 0 -1 0 -p -1 0 -8.74228e-08 -p 0 1 0 -p 1 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 ;")
        if ControllerType == 16:
            newController = mel.eval("curve -d 1 -p -1 0 0 -p -0.976649 0.0403494 0 -p -0.900118 0.0982616 0 -p -0.797187 0.209749 0 -p -0.70454 0.321503 0 -p -0.570132 0.458003 0 -p -0.431729 0.546423 0 -p -0.242886 0.615884 0 -p -0.0762568 0.640181 0 -p 0 0.649903 0 -p 0.0780068 0.629549 0 -p 0.184417 0.491045 0 -p 0.226461 0.36648 0 -p 0.249787 0.261573 0 -p 0.257746 0.152078 0 -p 0.25393 0.0458305 0 -p 0.237242 -0.066641 0 -p 0.209472 -0.170002 0 -p 0.159341 -0.275547 0 -p 0.0936243 -0.353376 0 -p 0.00278143 -0.395603 0 -p -0.0939869 -0.353027 0 -p -0.156973 -0.278751 0 -p -0.203105 -0.187712 0 -p -0.23646 -0.0701566 0 -p -0.254189 0.0494566 0 -p -0.258595 0.140181 0 -p -0.251477 0.239877 0 -p -0.229974 0.350679 0 -p -0.189943 0.475675 0 -p -0.117905 0.582293 0 -p -0.064095 0.63318 0 -p 0 0.649903 0 -p 0.0652413 0.641022 0 -p 0.216261 0.620465 0 -p 0.386892 0.559551 0 -p 0.522426 0.485287 0 -p 0.662175 0.374169 0 -p 0.771204 0.255743 0 -p 0.855995 0.163618 0 -p 0.957245 0.0625218 0 -p 0.992191 0.00580352 0 -p 0.975819 -0.0416966 0 -p 0.895059 -0.121241 0 -p 0.804982 -0.222674 0 -p 0.670153 -0.368554 0 -p 0.568298 -0.457874 0 -p 0.419555 -0.547289 0 -p 0.22243 -0.620251 0 -p 0.00288299 -0.649515 0 -p -0.227529 -0.619587 0 -p -0.400218 -0.554941 0 -p -0.555939 -0.463581 0 -p -0.673564 -0.356247 0 -p -0.765684 -0.252221 0 -p -0.878425 -0.124209 0 -p -0.924528 -0.0847122 0 -p -0.971997 -0.045168 0 -p -1 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 ;")
        if ControllerType == 17:
            newController = mel.eval("curve -d 1 -p 0 0 0 -p 1 0 1 -p 0.333333 0 1 -p 1 0 1 -p 1 0 0.333333 -p 1 0 1 -p 0 0 0 -p -1 0 -1 -p -0.333333 0 -1 -p -1 0 -1 -p -1 0 -0.333333 -p -1 0 -1 -p 0 0 0 -p 1 0 -1 -p 1 0 -0.333333 -p 1 0 -1 -p 0.333333 0 -1 -p 1 0 -1 -p 0 0 0 -p -1 0 1 -p -0.333333 0 1 -p -1 0 1 -p -1 0 0.333333 -p -1 0 1 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 ;")
        if ControllerType == 18:
            newController = mel.eval("curve -d 1 -p -1 0 0 -p -0.602634 0 -0.400331 -p -0.602634 0 -0.201158 -p 0.602634 0 -0.201158 -p 0.602634 0 -0.400331 -p 1 0 0 -p 0.602634 0 0.400331 -p 0.602634 0 0.201158 -p -0.602634 0 0.201158 -p -0.602634 0 0.400331 -p -1 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 ;")
        if ControllerType == 19:
            newController = mel.eval("curve -d 1 -p 0 0 0 -p 0 0 1 -p 0.0321135 0.0988352 0.71074 -p -0.0840743 0.0610835 0.71074 -p -0.0840743 -0.0610835 0.71074 -p 0.0321135 -0.0988352 0.71074 -p 0.103922 0 0.71074 -p 0.0321135 0.0988352 0.71074 -p 0 0 1 -p 0.0321135 0.0988352 0.71074 -p 0 0 1 -p 0.103922 0 0.71074 -p 0 0 1 -p 0.0321135 -0.0988352 0.71074 -p 0 0 1 -p -0.0840743 -0.0610835 0.71074 -p 0 0 1 -p -0.0840743 0.0610835 0.71074 -p 0 0 1 -p 0.0321135 0.0988352 0.71074 -p 0 0 1 -p 0 0 0 -p 0 0 -1 -p 0.0321135 0.0988352 -0.71074 -p -0.0840743 0.0610835 -0.71074 -p -0.0840743 -0.0610835 -0.71074 -p 0.0321135 -0.0988352 -0.71074 -p 0.103922 0 -0.71074 -p 0.0321135 0.0988352 -0.71074 -p 0 0 -1 -p 0.0321135 0.0988352 -0.71074 -p 0 0 -1 -p 0.103922 0 -0.71074 -p 0 0 -1 -p 0.0321135 -0.0988352 -0.71074 -p 0 0 -1 -p -0.0840743 -0.0610835 -0.71074 -p 0 0 -1 -p -0.0840743 0.0610835 -0.71074 -p 0 0 -1 -p 0.0321135 0.0988352 -0.71074 -p 0 0 -1 -p 0 0 0 -p 0 0.999563 0 -p 0.103922 0.71074 0 -p 0.0321135 0.71074 -0.0988352 -p -0.0840743 0.71074 -0.0610835 -p -0.0840743 0.71074 0.0610835 -p 0.0321135 0.71074 0.0988352 -p 0.103922 0.71074 0 -p 0 0.999563 0 -p 0.0321135 0.71074 0.0988352 -p 0 0.999563 0 -p -0.0840743 0.71074 0.0610835 -p 0 0.999563 0 -p -0.0840743 0.71074 -0.0610835 -p 0 0.999563 0 -p 0.0321135 0.71074 -0.0988352 -p 0 0.999563 0 -p 0.103922 0.71074 0 -p 0 0.999563 0 -p 0 0 0 -p 0 -0.999563 0 -p 0.0321135 -0.71074 -0.0988352 -p 0.103922 -0.71074 0 -p 0.0321135 -0.71074 0.0988352 -p -0.0840743 -0.71074 0.0610835 -p -0.0840743 -0.71074 -0.0610835 -p 0.0321135 -0.71074 -0.0988352 -p 0 -0.999563 0 -p 0.103922 -0.71074 0 -p 0 -0.999563 0 -p 0.0321135 -0.71074 0.0988352 -p 0 -0.999563 0 -p -0.0840743 -0.71074 0.0610835 -p 0 -0.999563 0 -p -0.0840743 -0.71074 -0.0610835 -p 0 -0.999563 0 -p 0.0321135 -0.71074 -0.0988352 -p 0 -0.999563 0 -p 0 0 0 -p 0.999563 0 0 -p 0.71074 0.0321135 0.0988352 -p 0.71074 0.103922 0 -p 0.71074 0.0321135 -0.0988352 -p 0.71074 -0.0840743 -0.0610835 -p 0.71074 -0.0840743 0.0610835 -p 0.71074 0.0321135 0.0988352 -p 0.999563 0 0 -p 0.71074 0.103922 0 -p 0.999563 0 0 -p 0.71074 0.0321135 -0.0988352 -p 0.999563 0 0 -p 0.71074 -0.0840743 -0.0610835 -p 0.999563 0 0 -p 0.71074 -0.0840743 0.0610835 -p 0.999563 0 0 -p 0 0 0 -p -0.999563 0 0 -p -0.71074 -0.0840743 0.0610835 -p -0.71074 0.0321135 0.0988352 -p -0.71074 0.103922 0 -p -0.71074 0.0321135 -0.0988352 -p -0.71074 -0.0840743 -0.0610835 -p -0.71074 -0.0840743 0.0610835 -p -0.999563 0 0 -p -0.71074 0.0321135 0.0988352 -p -0.999563 0 0 -p -0.71074 0.103922 0 -p -0.999563 0 0 -p -0.71074 0.0321135 -0.0988352 -p -0.999563 0 0 -p -0.71074 -0.0840743 -0.0610835 -p -0.999563 0 0 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 -k 70 -k 71 -k 72 -k 73 -k 74 -k 75 -k 76 -k 77 -k 78 -k 79 -k 80 -k 81 -k 82 -k 83 -k 84 -k 85 -k 86 -k 87 -k 88 -k 89 -k 90 -k 91 -k 92 -k 93 -k 94 -k 95 -k 96 -k 97 -k 98 -k 99 -k 100 -k 101 -k 102 -k 103 -k 104 -k 105 -k 106 -k 107 -k 108 -k 109 -k 110 -k 111 -k 112 -k 113 -k 114 ;")
        if ControllerType == 20:
            newController = mel.eval("curve -d 1 -p 0 1 0 -p -0.222521 0.974928 -7.95797e-08 -p -0.433884 0.900969 -1.55169e-07 -p -0.62349 0.781831 -2.22977e-07 -p -0.781832 0.62349 -2.79605e-07 -p -0.900969 0.433884 -3.22212e-07 -p -0.974928 0.222521 -3.48661e-07 -p -1 0 -3.57628e-07 -p -0.974928 -0.222521 -3.48661e-07 -p -0.900969 -0.433884 -3.22212e-07 -p -0.781832 -0.62349 -2.79605e-07 -p -0.62349 -0.781831 -2.22977e-07 -p -0.433884 -0.900969 -1.55169e-07 -p -0.222521 -0.974928 -7.95797e-08 -p 0 -1 0 -p 0.222521 -0.974928 0 -p 0.433884 -0.900969 0 -p 0.62349 -0.781831 0 -p 0.781832 -0.62349 0 -p 0.900969 -0.433884 0 -p 0.974928 -0.222521 0 -p 1 0 0 -p 0.974928 0.222521 0 -p 0.900969 0.433884 0 -p 0.781832 0.62349 0 -p 0.62349 0.781831 0 -p 0.433884 0.900969 0 -p 0.222521 0.974928 0 -p 0 1 0 -p 1.12738e-07 0.974928 -0.222521 -p 2.19823e-07 0.900969 -0.433884 -p 3.15885e-07 0.781831 -0.62349 -p 3.96107e-07 0.62349 -0.781831 -p 4.56466e-07 0.433884 -0.900969 -p 4.93937e-07 0.222521 -0.974928 -p 5.06639e-07 0 -1 -p 4.93937e-07 -0.222521 -0.974928 -p 4.56466e-07 -0.433884 -0.900969 -p 3.96107e-07 -0.62349 -0.781831 -p 3.15885e-07 -0.781831 -0.62349 -p 2.19823e-07 -0.900969 -0.433884 -p 1.12738e-07 -0.974928 -0.222521 -p 0 -1 0 -p -3.31582e-08 -0.974928 0.222521 -p -6.46537e-08 -0.900969 0.433884 -p -9.29072e-08 -0.781831 0.62349 -p -1.16502e-07 -0.62349 0.781832 -p -1.34255e-07 -0.433884 0.900969 -p -1.45276e-07 -0.222521 0.974928 -p -1.49012e-07 0 1 -p -1.45276e-07 0.222521 0.974928 -p -1.34255e-07 0.433884 0.900969 -p -1.16502e-07 0.62349 0.781832 -p -9.29072e-08 0.781831 0.62349 -p -6.46537e-08 0.900969 0.433884 -p -3.31582e-08 0.974928 0.222521 -p 0 1 0 -p 0.222521 0.974928 0 -p 0.433884 0.900969 0 -p 0.62349 0.781831 0 -p 0.781832 0.62349 0 -p 0.900969 0.433884 0 -p 0.974928 0.222521 0 -p 1 0 0 -p 0.92388 0 -0.382683 -p 0.707107 0 -0.707106 -p 0.382684 0 -0.923879 -p 5.06639e-07 0 -1 -p -0.382683 0 -0.92388 -p -0.707106 0 -0.707107 -p -0.923879 0 -0.382684 -p -1 0 -3.57628e-07 -p -0.92388 0 0.382683 -p -0.707107 0 0.707107 -p -0.382684 0 0.923879 -p -1.49012e-07 0 1 -p 0.382683 0 0.92388 -p 0.707107 0 0.707107 -p 0.92388 0 0.382683 -p 1 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 -k 70 -k 71 -k 72 -k 73 -k 74 -k 75 -k 76 -k 77 -k 78 -k 79 ;")
        if ControllerType == 21:
            newController = mel.eval("curve -d 1 -p -0.930754 0 0 -p -0.999823 0 -0.225742 -p -0.929112 0 -0.225742 -p -0.871025 0 -0.0343219 -p -0.795975 0 -0.0343219 -p -0.855002 0 -0.225742 -p -0.784291 0 -0.225742 -p -0.725416 0 -0.0343219 -p 0.571271 0 -0.0343219 -p 0.53502 5.86654e-09 -0.232606 -p 1 0 0 -p 0.53502 -1.95551e-09 0.232606 -p 0.571271 0 0.0343219 -p -0.725416 0 0.0343219 -p -0.784291 0 0.225742 -p -0.855002 0 0.225742 -p -0.795975 0 0.0343219 -p -0.871025 0 0.0343219 -p -0.929112 0 0.225742 -p -0.999823 0 0.225742 -p -0.930754 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 ;")
        if ControllerType == 22:
            newController = mel.eval("curve -d 1 -p -0.930754 0 0 -p -0.999823 0 0.225742 -p -0.929112 0 0.225742 -p -0.871025 0 0.0343219 -p -0.795975 0 0.0343219 -p -0.855002 0 0.225742 -p -0.784291 0 0.225742 -p -0.725416 0 0.0343219 -p -0.65215 0 0.0339838 -p -0.70891 0 0.225742 -p -0.638199 0 0.225742 -p -0.579488 0 0.0357706 -p 0.571271 0 0.0343219 -p 0.53502 -1.95551e-09 0.232606 -p 1 0 0 -p 0.53502 5.86654e-09 -0.232606 -p 0.571271 0 -0.0343219 -p -0.578353 0 -0.0354073 -p -0.638199 0 -0.225742 -p -0.70891 0 -0.225742 -p -0.650934 0 -0.03416 -p -0.725416 0 -0.0343219 -p -0.784291 0 -0.225742 -p -0.855002 0 -0.225742 -p -0.795975 0 -0.0343219 -p -0.871025 0 -0.0343219 -p -0.929112 0 -0.225742 -p -0.999823 0 -0.225742 -p -0.930754 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 ;")
        if ControllerType == 23:
            newController = mel.eval("curve -d 1 -p 0.987688 -0.156434 0 -p 1.011839 -0.15624 0 -p 1.036134 -0.152464 0 -p 1.05954 -0.144934 0 -p 1.08148 -0.133836 0 -p 1.101413 -0.119442 0 -p 1.118849 -0.102107 0 -p 1.133359 -0.0822576 0 -p 1.144585 -0.0603829 0 -p 1.152251 -0.0370213 0 -p 1.156168 -0.0127483 0 -p 1.15624 0.0118387 0 -p 1.152464 0.0361342 0 -p 1.144934 0.05954 0 -p 1.133836 0.0814797 0 -p 1.119442 0.101413 0 -p 1.102107 0.118849 0 -p 1.082258 0.133359 0 -p 1.060383 0.144585 0 -p 1.037021 0.152251 0 -p 1.012748 0.156168 0 -p 0.988161 0.15624 0 -p 0.963866 0.152464 0 -p 0.94046 0.144934 0 -p 0.91852 0.133836 0 -p 0.898587 0.119442 0 -p 0.881151 0.102107 0 -p 0.866641 0.0822576 0 -p 0.855415 0.0603829 0 -p 0.847749 0.0370213 0 -p 0.843832 0.0127483 0 -p 0.84376 -0.0118387 0 -p 0.847536 -0.0361342 0 -p 0.855066 -0.05954 0 -p 0.866164 -0.0814797 0 -p 0.880558 -0.101413 0 -p 0.897893 -0.118849 0 -p 0.917742 -0.133359 0 -p 0.939617 -0.144585 0 -p 0.962979 -0.152251 0 -p 0.987252 -0.156168 0 -p 0.951057 -0.309017 0 -p 0.891007 -0.453991 0 -p 0.809017 -0.587785 0 -p 0.707107 -0.707107 0 -p 0.587785 -0.809017 0 -p 0.453991 -0.891007 0 -p 0.309017 -0.951057 0 -p 0.156434 -0.987688 0 -p 0 -1 0 -p -0.156435 -0.987688 0 -p -0.309017 -0.951057 0 -p -0.453991 -0.891007 0 -p -0.587785 -0.809017 0 -p -0.707107 -0.707107 0 -p -0.809017 -0.587785 0 -p -0.891007 -0.453991 0 -p -0.951057 -0.309017 0 -p -0.987689 -0.156434 0 -p -1 0 0 -p -0.987689 0.156434 0 -p -0.951057 0.309017 0 -p -0.891007 0.453991 0 -p -0.809017 0.587785 0 -p -0.707107 0.707107 0 -p -0.587785 0.809017 0 -p -0.453991 0.891007 0 -p -0.309017 0.951057 0 -p -0.156435 0.987688 0 -p 0.033317 1.003527 0 -p 0 0.772254 0 -p 0 1 -0.227746 -p 0 1.227746 -1.99102e-08 -p 0 1 0.227746 -p 0 0.772254 0 -p 0.455491 1 0 -p 0 1.227746 -1.99102e-08 -p 0.033317 1.003527 0 -p 0 1 0.227746 -p 0.455491 1 0 -p 0 1 -0.227746 -p 0.033317 1.003527 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 -k 70 -k 71 -k 72 -k 73 -k 74 -k 75 -k 76 -k 77 -k 78 -k 79 -k 80 -k 81 ;")
        if ControllerType == 24:
            newController = mel.eval("curve -d 1 -p 1.044843 0.451543 -1.71274e-08 -p 0.943201 0.349574 0 -p 0.856409 0.452596 0 -p 0.748529 0.544474 0 -p 0.622217 0.622945 0 -p 0.480585 0.686077 0 -p 0.327119 0.732316 0 -p 0.165598 0.760522 0 -p 0 0.770002 0 -p -0.165598 0.760522 0 -p -0.327119 0.732316 0 -p -0.480585 0.686077 0 -p -0.622217 0.622945 0 -p -0.748529 0.544474 0 -p -0.856409 0.452596 0 -p -0.943201 0.349574 0 -p -1.044843 0.451543 -1.71274e-08 -p -1.133634 0.0225564 0 -p -0.73717 0.208915 0 -p -0.862344 0.287681 0 -p -0.847811 0.31422 0 -p -0.769797 0.406823 0 -p -0.672827 0.489409 0 -p -0.55929 0.559944 0 -p -0.431981 0.616691 0 -p -0.294036 0.658254 0 -p -0.148851 0.683608 0 -p 0 0.692129 0 -p 0.148851 0.683608 0 -p 0.294036 0.658254 0 -p 0.431981 0.616691 0 -p 0.55929 0.559944 0 -p 0.672827 0.489409 0 -p 0.769796 0.406823 0 -p 0.847811 0.31422 0 -p 0.864885 0.287155 0 -p 0.73717 0.208915 0 -p 1.133634 0.0225564 0 -p 1.044843 0.451543 -1.71274e-08 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 ;")
        if ControllerType == 25:
            newController = mel.eval("curve -d 1 -p 1 0 0 -p 0.608742 0 0.202943 -p 0.608742 0.202943 -1.77419e-08 -p 0.608742 0 -0.202943 -p 0.608742 -0.202943 0 -p 0.608742 0 0.202943 -p 0.608742 0.202943 -1.77419e-08 -p 1 0 0 -p 0.608742 0 -0.202943 -p 1 0 0 -p 0.608742 -0.202943 0 -p 1 0 0 -p 0.608742 0 0.202943 -p 0.608742 0 0.0848705 -p 0.608742 0.0848706 -1.49012e-08 -p 0.608742 0.202943 -1.77419e-08 -p 0.608742 0.0848706 -1.49012e-08 -p 0.608742 0 -0.0848705 -p 0.608742 0 -0.202943 -p 0.608742 0 -0.0848705 -p 0.608742 -0.0848705 0 -p 0.608742 -0.202943 0 -p 0.608742 -0.0848705 0 -p 0.608742 0 0.0848705 -p 0.608742 0 0.202943 -p 0.608742 0 0.0848705 -p -0.608742 0 0.0848705 -p -0.608742 0.0848706 -1.49012e-08 -p 0.608742 0.0848706 -1.49012e-08 -p 0.608742 0 -0.0848705 -p -0.608742 0 -0.0848705 -p -0.608742 0.0848706 -1.49012e-08 -p -0.608742 0 -0.0848705 -p -0.608742 -0.0848705 0 -p 0.608742 -0.0848705 0 -p -0.608742 -0.0848705 0 -p -0.608742 0 0.0848705 -p -0.608742 0 0.202943 -p -0.608742 0.202943 -1.77419e-08 -p -0.608742 0.0848706 -1.49012e-08 -p -0.608742 0.202943 -1.77419e-08 -p -0.608742 0 -0.202943 -p -0.608742 0 -0.0848705 -p -0.608742 -0.0848705 0 -p -0.608742 -0.202943 0 -p -0.608742 0 -0.202943 -p -0.608742 -0.202943 0 -p -0.608742 0 0.202943 -p -1 0 0 -p -0.608742 0.202943 -1.77419e-08 -p -1 0 0 -p -0.608742 0 0.202943 -p -1 0 0 -p -0.608742 -0.202943 0 -p -1 0 0 -p -0.608742 0 -0.202943 -p -1 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 ;")
        if ControllerType == 26:
            newController = mel.eval("curve -d 1 -p 0 0 0 -p 0 1.998578 0 -p -0.111667 1.545617 0 -p -0.0558338 1.545617 0.0967067 -p 0.0558338 1.545617 0.0967067 -p 0.111667 1.545617 0 -p 0.0558338 1.545617 -0.0967067 -p -0.0558338 1.545617 -0.0967067 -p -0.111667 1.545617 0 -p 0 1.998578 0 -p -0.111667 1.545617 0 -p 0 1.998578 0 -p -0.0558338 1.545617 -0.0967067 -p 0 1.998578 0 -p 0.0558338 1.545617 -0.0967067 -p 0 1.998578 0 -p 0.111667 1.545617 0 -p 0 1.998578 0 -p 0.0558338 1.545617 0.0967067 -p 0 1.998578 0 -p -0.0558338 1.545617 0.0967067 -p 0 1.998578 0 -p 0 0.397564 0 -p 0 0.397001 0.397001 -p 0 0 0.396933 -p 0.397001 0 0.397001 -p 0.397001 0.000154271 0 -p 0.397001 0.397001 0 -p 0 0.397564 0 -p 0 0 0 -p 0.397001 0.000154271 0 -p 2 0 0 -p 1.545617 0.111667 0 -p 1.545617 0.0558338 0.0967067 -p 1.545617 -0.0558338 0.0967067 -p 1.545617 -0.111667 0 -p 1.545617 -0.0558338 -0.0967067 -p 1.545617 0.0558338 -0.0967067 -p 1.545617 0.111667 0 -p 2 0 0 -p 1.545617 0.0558338 -0.0967067 -p 2 0 0 -p 1.545617 -0.0558338 -0.0967067 -p 2 0 0 -p 1.545617 -0.111667 0 -p 2 0 0 -p 1.545617 -0.0558338 0.0967067 -p 2 0 0 -p 1.545617 0.0558338 0.0967067 -p 2 0 0 -p 1.545617 0.111667 0 -p 2 0 0 -p 0.397001 0.000154271 0 -p 0 0 0 -p 0 0 0.396933 -p 0 0 2 -p 0 0.111667 1.545617 -p 0.0967067 0.0558338 1.545617 -p 0.0967067 -0.0558338 1.545617 -p 0 -0.111667 1.545617 -p -0.0967067 -0.0558338 1.545617 -p -0.0967067 0.0558338 1.545617 -p 0 0.111667 1.545617 -p 0 0 2 -p 0.0967067 0.0558338 1.545617 -p 0 0 2 -p 0.0967067 -0.0558338 1.545617 -p 0 0 2 -p 0 -0.111667 1.545617 -p 0 0 2 -p -0.0967067 -0.0558338 1.545617 -p 0 0 2 -p -0.0967067 0.0558338 1.545617 -p 0 0 2 -p 0 0 0.396933 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 -k 70 -k 71 -k 72 -k 73 -k 74 -k 75 ;")
        if ControllerType == 27:
            newController = mel.eval("curve -d 1 -p 0 0 0 -p -0.632534 0.260586 0.633477 -p -0.995603 0 0.997087 -p -0.632569 -0.247831 0.633443 -p 0 0 0 -p -0.247831 -0.632569 0.633443 -p 0 -0.995603 0.997087 -p 0.260586 -0.632534 0.633477 -p 0 0 0 -p 0.632649 0.260503 0.633593 -p 0.995603 0 0.997087 -p 0.632534 -0.260586 0.633477 -p 0 0 0 -p 0.260586 0.632534 0.633477 -p 0 0.995603 0.997087 -p -0.260586 0.632534 0.633477 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;")
        if ControllerType == 28:
            newController = mel.eval("curve -d 1 -p -1.42936e-08 0.26231 0.479614 -p -0.148209 0.26231 0.45614 -p -0.28191 0.26231 0.388016 -p -0.388016 0.26231 0.28191 -p -0.45614 0.26231 0.148209 -p -0.479614 0.26231 0 -p -0.45614 0.26231 -0.148209 -p -0.388016 0.26231 -0.28191 -p -0.28191 0.26231 -0.388016 -p -0.148209 0.26231 -0.45614 -p 0 0.26231 -0.479614 -p 0.148209 0.26231 -0.45614 -p 0.28191 0.26231 -0.388016 -p 0.388016 0.26231 -0.28191 -p 0.45614 0.26231 -0.148209 -p 0.479614 0.26231 0 -p 0.45614 0.26231 0.148209 -p 0.388016 0.26231 0.28191 -p 0.28191 0.26231 0.388016 -p 0.148209 0.26231 0.45614 -p -1.42936e-08 0.26231 0.479614 -p -1.42936e-08 -0.26231 0.479614 -p -0.148209 -0.26231 0.45614 -p -0.28191 -0.26231 0.388016 -p -0.388016 -0.26231 0.28191 -p -0.45614 -0.26231 0.148209 -p -0.479614 -0.26231 0 -p -0.45614 -0.26231 -0.148209 -p -0.388016 -0.26231 -0.28191 -p -0.28191 -0.26231 -0.388016 -p -0.148209 -0.26231 -0.45614 -p 0 -0.26231 -0.479614 -p 0.148209 -0.26231 -0.45614 -p 0.28191 -0.26231 -0.388016 -p 0.388016 -0.26231 -0.28191 -p 0.45614 -0.26231 -0.148209 -p 0.479614 -0.26231 0 -p 0.45614 -0.26231 0.148209 -p 0.388016 -0.26231 0.28191 -p 0.28191 -0.26231 0.388016 -p 0.148209 -0.26231 0.45614 -p -1.42936e-08 -0.26231 0.479614 -p -1.42936e-08 0.26231 0.479614 -p -2.99285e-08 0.26231 1.004233 -p -0.310325 0.26231 0.955083 -p -0.590274 0.26231 0.812442 -p -0.812442 0.26231 0.590274 -p -0.955083 0.26231 0.310325 -p -1.004234 0.26231 0 -p -0.955083 0.26231 -0.310325 -p -0.812442 0.26231 -0.590274 -p -0.590274 0.26231 -0.812442 -p -0.310325 0.26231 -0.955083 -p 0 0.26231 -1.004234 -p 0.310325 0.26231 -0.955083 -p 0.590274 0.26231 -0.812442 -p 0.812442 0.26231 -0.590274 -p 0.955083 0.26231 -0.310325 -p 1.004233 0.26231 0 -p 0.955083 0.26231 0.310325 -p 0.812442 0.26231 0.590274 -p 0.590274 0.26231 0.812442 -p 0.310325 0.26231 0.955083 -p -2.99285e-08 0.26231 1.004233 -p -2.99285e-08 -0.26231 1.004233 -p 0.310325 -0.26231 0.955083 -p 0.590273 -0.26231 0.812442 -p 0.812442 -0.26231 0.590274 -p 0.955083 -0.26231 0.310325 -p 1.004233 -0.26231 0 -p 0.955083 -0.26231 -0.310325 -p 0.812442 -0.26231 -0.590274 -p 0.590274 -0.26231 -0.812442 -p 0.310325 -0.26231 -0.955083 -p 0 -0.26231 -1.004234 -p -0.310325 -0.26231 -0.955083 -p -0.590274 -0.26231 -0.812442 -p -0.812442 -0.26231 -0.590274 -p -0.955083 -0.26231 -0.310325 -p -1.004234 -0.26231 0 -p -0.955083 -0.26231 0.310325 -p -0.812442 -0.26231 0.590274 -p -0.590274 -0.26231 0.812442 -p -0.310325 -0.26231 0.955083 -p -2.99285e-08 -0.26231 1.004233 -p 0.310325 -0.26231 0.955083 -p 0.590273 -0.26231 0.812442 -p 0.812442 -0.26231 0.590274 -p 0.955083 -0.26231 0.310325 -p 1.004233 -0.26231 0 -p 1.004233 0.26231 0 -p 0.479614 0.26231 0 -p 0.479614 -0.26231 0 -p 1.004233 -0.26231 0 -p 1.004233 0.26231 0 -p 0.955083 0.26231 -0.310325 -p 0.812442 0.26231 -0.590274 -p 0.590274 0.26231 -0.812442 -p 0.310325 0.26231 -0.955083 -p 0 0.26231 -1.004234 -p 0 -0.26231 -1.004234 -p 0 -0.26231 -0.479614 -p 0 0.26231 -0.479614 -p 0 0.26231 -1.004234 -p -0.310325 0.26231 -0.955083 -p -0.590274 0.26231 -0.812442 -p -0.812442 0.26231 -0.590274 -p -0.955083 0.26231 -0.310325 -p -1.004234 0.26231 0 -p -1.004234 -0.26231 0 -p -0.479614 -0.26231 0 -p -0.479614 0.26231 0 -p -1.004234 0.26231 0 -p -0.955083 0.26231 0.310325 -p -0.812442 0.26231 0.590274 -p -0.590274 0.26231 0.812442 -p -0.310325 0.26231 0.955083 -p -2.99285e-08 0.26231 1.004233 -p -2.99285e-08 -0.26231 1.004233 -p -1.42936e-08 -0.26231 0.479614 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 -k 70 -k 71 -k 72 -k 73 -k 74 -k 75 -k 76 -k 77 -k 78 -k 79 -k 80 -k 81 -k 82 -k 83 -k 84 -k 85 -k 86 -k 87 -k 88 -k 89 -k 90 -k 91 -k 92 -k 93 -k 94 -k 95 -k 96 -k 97 -k 98 -k 99 -k 100 -k 101 -k 102 -k 103 -k 104 -k 105 -k 106 -k 107 -k 108 -k 109 -k 110 -k 111 -k 112 -k 113 -k 114 -k 115 -k 116 -k 117 -k 118 -k 119 ;")
        if ControllerType == 29:
            newController = mel.eval("curve -d 1 -p -2.98863e-08 -1.12841e-08 1.002818 -p -0.309888 -1.12841e-08 0.953737 -p -0.589442 -1.12841e-08 0.811297 -p -0.811297 -1.12841e-08 0.589442 -p -0.953737 -1.12841e-08 0.309888 -p -1.002819 -1.12841e-08 0 -p -0.953737 -1.12841e-08 -0.309888 -p -0.811297 -1.12841e-08 -0.589442 -p -0.589442 -1.12841e-08 -0.811297 -p -0.309888 -1.12841e-08 -0.953737 -p 0 -1.12841e-08 -1.002819 -p 0.309888 -1.12841e-08 -0.953737 -p 0.589442 -1.12841e-08 -0.811297 -p 0.811298 -1.12841e-08 -0.589442 -p 0.953737 -1.12841e-08 -0.309888 -p 1.002818 -1.12841e-08 0 -p 0.953737 -1.12841e-08 0.309888 -p 0.811297 -1.12841e-08 0.589442 -p 0.589442 -1.12841e-08 0.811297 -p 0.309888 -1.12841e-08 0.953737 -p -2.98863e-08 -1.12841e-08 1.002818 -p 0 0 0 -p 0 -1.12841e-08 -1.002819 -p 0.309888 -1.12841e-08 -0.953737 -p 0.589442 -1.12841e-08 -0.811297 -p 0.811298 -1.12841e-08 -0.589442 -p 0.953737 -1.12841e-08 -0.309888 -p 1.002818 -1.12841e-08 0 -p 0 0 0 -p -1.002819 -1.12841e-08 0 -p 0 0 0 -p 0 1.170479 0 -p 0 2.13812 0 -p 0.483821 1.170479 0 -p 0.342113 1.170479 -0.342113 -p 0 1.170479 -0.483821 -p -0.342113 1.170479 -0.342113 -p -0.483821 1.170479 0 -p -0.342113 1.170479 0.342113 -p 0 1.170479 0.483821 -p 0.342113 1.170479 0.342113 -p 0.483821 1.170479 0 -p 0.342113 1.170479 -0.342113 -p 0 2.13812 0 -p 0 1.170479 -0.483821 -p 0 2.13812 0 -p -0.342113 1.170479 -0.342113 -p 0 2.13812 0 -p -0.483821 1.170479 0 -p 0 2.13812 0 -p -0.342113 1.170479 0.342113 -p 0 2.13812 0 -p 0 1.170479 0.483821 -p 0 2.13812 0 -p 0.342113 1.170479 0.342113 -p 0 2.13812 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 ;")
        if ControllerType == 30:
            newController = mel.eval("curve -d 3 -p 0.244733 0.11108 0 -p 0.2124 0.0739642 0 -p 0.147736 -0.000267686 0 -p -0.0752292 -0.0629865 0 -p -0.165999 -0.00164294 0 -p -0.341003 -0.042708 0 -p -0.505952 0.0602088 0 -p -0.626887 0.255968 0 -p -0.633052 0.591231 0 -p -0.611347 0.647309 0 -p -0.674305 0.724892 0 -p -0.886647 0.924843 0 -p -0.983152 1.020888 0 -p -0.990416 1.150432 0 -p -0.91098 1.246545 0 -p -0.797106 1.239931 0 -p -0.769309 1.2164 0 -p -0.57924 1.012709 0 -p -0.537053 0.956169 0 -p -0.508415 0.943213 0 -p -0.508328 0.950102 0 -p -0.504414 0.95985 0 -p -0.512971 0.992988 0 -p -0.5078 0.987173 0 -p -0.588169 1.174841 0 -p -0.679893 1.294614 0 -p -0.745245 1.486832 0 -p -0.689984 1.664983 0 -p -0.540877 1.688412 0 -p -0.430568 1.575873 0 -p -0.362822 1.379146 0 -p -0.34926 1.246432 0 -p -0.305002 1.1566 0 -p -0.273924 1.115243 0 -p -0.269772 1.127311 0 -p -0.259976 1.13764 0 -p -0.297565 1.386036 0 -p -0.354392 1.55342 0 -p -0.368255 1.795484 0 -p -0.291944 1.909761 0 -p -0.115731 1.911981 0 -p -0.0426305 1.779833 0 -p -0.0256664 1.55985 0 -p -0.00851656 1.387778 0 -p 0.0128518 1.253462 0 -p 0.0438934 1.134074 0 -p 0.0668622 1.126045 0 -p 0.0823771 1.150848 0 -p 0.0820804 1.237602 0 -p 0.104469 1.337456 0 -p 0.13101 1.591276 0 -p 0.186932 1.79924 0 -p 0.360336 1.868929 0 -p 0.481175 1.782737 0 -p 0.502229 1.587967 0 -p 0.44352 1.344087 0 -p 0.384292 1.155026 0 -p 0.340648 0.873485 0 -p 0.385972 0.690293 0 -p 0.559313 0.762202 0 -p 0.668786 0.865086 0 -p 0.905714 0.890538 0 -p 1.045379 0.629301 0 -p 0.890624 0.508491 0 -p 0.747996 0.451928 0 -p 0.533551 0.389219 0 -p 0.453023 0.34236 0 -p 0.314163 0.188174 0 -p 0.244733 0.11108 0 -k 0 -k 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 66 -k 66 ;")
        CcName = cmds.rename(newController ,ControllerName+"_cc_"   +str(controllerNameNum).zfill(3))
        cmds.setAttr(CcName+'.scale' ,controllerScale,controllerScale,controllerScale )
        getRotationOffsetX = cmds.getAttr(CcName+'.rx')
        getRotationOffsetY = cmds.getAttr(CcName+'.ry')
        getRotationOffsetZ = cmds.getAttr(CcName+'.rz')
        cmds.setAttr(CcName+'.rotate' ,getRotationOffsetX + rotationOffsetX,getRotationOffsetY + rotationOffsetY,getRotationOffsetZ + rotationOffsetZ)
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        controllerNameNum += 1
        child = CcName
        if controllerGroupNum > 0:
            for grp in range (controllerGroupNum):
                GrpName = (ControllerName+"_cc_grp_"   +str(controllerGrpNameNum).zfill(3))
                controllerGrp = cmds.group( n = GrpName , em = True)
                cmds.parent(child , controllerGrp)
                controllerGrpNameNum +=1
                child = controllerGrp
            if parentConstraintStatue == 1 or scaleConstraintStatue == 1:
                cmds.warning("Any object is selected for constraint !")
        else:
            cmds.delete(cmds.parentConstraint( obj , CcName , mo = 0))
            if parentConstraintStatue == 1 or scaleConstraintStatue == 1:
                cmds.warning("Any object is selected for constraint !")
    
def Grouping(*args):
    sel = cmds.ls(sl = 1)
    selected = []
    for i in sel:
        selected.append(i)
    for i in range(len(selected)-1):
        child = selected[i]
        childForParent = selected[i+1]
        parent = child.replace("_cc_","_cc_grp_")
        cmds.select(parent)
        cmds.parent(parent, childForParent)
    
def DeletHistory(*args):
    sel = cmds.ls(sl=1)
    for i in sel:
        cmds.delete(i, ch = True)
    
def FreezeTransform(*args):
    sel = cmds.ls(sl=1)
    for i in sel:
        cmds.makeIdentity( apply=True, t=1, r=1, s=1)
    
def SelectSkinJoint(*args):
    cmds.select(controlersList)
    
def BindSkin(*args):
    cmds.skinCluster(toSelectedBones = 1,dr = 4 ,bm = 0 , sm = 0 ,mi =5)
    
def CreateRootConroleler(*args):
    TypeOfObject = cmds.textField("SelectedType", q = True , text = True)
    Renaming = cmds.textField("Renaming", q = True , text = True)
    ChildList = []
    sel = cmds.ls(sl=1)
    for i in sel:
        child = i.replace("_" + TypeOfObject + "_", "_cc_grp_")
        ChildList.append(child)
    RootName = Renaming + "_" + TypeOfObject + "_", "_cc_root_"
    RootCc = cmds.circle(n=RootName)
    RootCcGrp = cmds.group( n = RootName.replace("_cc_Root_" , "_cc_root_grp_") )
    for i in ChildList:
        cmds.parent(RootCc, i)
    
def MakeJoint(*args):
    jntList = []
    nameNumber = 1
    locList = []
    sel = cmds.ls(sl=1)
    locPosX = 0
    locPosY = 0
    locPosZ = 0
    NewJointName = cmds.textField("NewJointName" , q = True , text = True)
    WorldRotation = cmds.checkBox( "WorldRotation" , q = True , v = True)
    HirarchyCheckBox = cmds.checkBox( "HirarchyJoints"     ,q = 1,v = 1)
    if NewJointName == "":
        NewJointName = "joint"
    for i in sel:
        locator = cmds.spaceLocator(n ="locator_For_Rig_"+ str(nameNumber).zfill(4))
        locList.append(locator[0])
        nameNumber += 1
        cmds.delete(cmds.parentConstraint( i , locator , mo = 0 ))
        cmds.select( clear=True )
    nameNumber = 0
    for Loc in locList:
        locPosX = cmds.getAttr(Loc+".translateX")
        locPosY = cmds.getAttr(Loc+".translateY")
        locPosZ = cmds.getAttr(Loc+".translateZ")
        newJoint = cmds.joint(p=(locPosX, locPosY, locPosZ),n = NewJointName + "_jnt_" +str(nameNumber).zfill(4))
        nameNumber += 1
        jntList.append(newJoint)
    if WorldRotation == 0:
        cmds.joint(jntList[0] ,e= True,oj = "xyz" , sao = "yup" , ch = True , zso = True )
    if HirarchyCheckBox == 0:
        for jnt in jntList:
            try:
                cmds.parent(jnt , world = True)
            except:
                print("")
    cmds.select( locList )
    cmds.delete()
    
def Object0nCurve(*args):
    ObjectType = cmds.optionMenu( "ObjectTypeOnCurve" ,q = True ,value=True )
    PathRotation = cmds.checkBox("PathRotation", q = 1 , v = 0 )
    PathEnable = cmds.checkBox("PathRotation", q = 1 , en = 1 )
    AtachOnCurve = cmds.checkBox("AtachOnCurve",q = 1 , v = 1 )
    JointAmount = cmds.intField("ObjectAmount", q = 1 , v = 1 )
    HirarchyOnCurve = cmds.checkBox("Hirarchy" , q = 1 , v = 1 )
    ParametricLength = cmds.checkBox("ParametricLength" , q = 1 , v = 1 )
    sel = cmds.ls(sl = 1)
    jointName = "Object_On_Curve_"
    for i in sel:
        path = i
        padding = 0
        for jnt in range(0,JointAmount):
            cmds.select(clear = 1)
            if ObjectType == "Joint":
                newJnt = cmds.joint(n = jointName+str(padding).zfill(3))
            if ObjectType == "Circle":
                newJnt = cmds.circle(n = jointName+str(padding).zfill(3))
            if ObjectType == "Locator":
                newJnt = cmds.spaceLocator(n = jointName+str(padding).zfill(3))
            if ObjectType == "Sphere":
                newJnt = cmds.polySphere(n = jointName+str(padding).zfill(3))
            padding +=1
            if PathRotation == 1 :
                follow = 1
            if PathRotation == 0 :
                follow = 0
            if ParametricLength == 1:
                pathAnim = cmds.pathAnimation(newJnt ,stu = 1, etu = 100 ,f = follow ,fractionMode = 0 , c=path )
                cmds.keyTangent( pathAnim + ".u", edit=True , ott="linear", itt="linear" )
                if JointAmount > 1 :
                    cmds.currentTime( jnt * (100.0 / (JointAmount-1)) , edit=True )
                cmds.cutKey(pathAnim + ".u", time = ())
            if ParametricLength == 0:
                pathAnim = cmds.pathAnimation(newJnt ,fractionMode = 1 ,f = follow, c=path )
                cmds.cutKey(pathAnim + ".u", time = ())
                if JointAmount > 1 :
                    cmds.setAttr(pathAnim + ".u" ,jnt * (1.0 / (JointAmount-1)) )
            cmds.select(clear = 1)
            if AtachOnCurve == 0:
                if ObjectType == "Joint":
                    cmds.delete(newJnt + ".tx" , icn = 1)
                    cmds.delete(newJnt + ".ty" , icn = 1)
                    cmds.delete(newJnt + ".tz" , icn = 1)
                    cmds.delete(newJnt + ".rx" , icn = 1)
                    cmds.delete(newJnt + ".ry" , icn = 1)
                    cmds.delete(newJnt + ".rz" , icn = 1)
                else:
                    cmds.delete(newJnt[0] + ".tx" , icn = 1)
                    cmds.delete(newJnt[0] + ".ty" , icn = 1)
                    cmds.delete(newJnt[0] + ".tz" , icn = 1)
                    cmds.delete(newJnt[0] + ".rx" , icn = 1)
                    cmds.delete(newJnt[0] + ".ry" , icn = 1)
                    cmds.delete(newJnt[0] + ".rz" , icn = 1)
                cmds.delete(pathAnim)
            if jnt == 0 :
                oldJnt = newJnt
                rootJnt = newJnt
                continue
            if jnt > 0 and HirarchyOnCurve == 1 :
                cmds.parent(newJnt , oldJnt)
                oldJnt = newJnt
        if ObjectType == "Joint" and PathRotation == 1:
            cmds.joint(rootJnt ,e = 1 , sao = "yup" , oj = "xyz" , ch = 1 , zso = 1)
        if jnt > 0 and HirarchyOnCurve == 0  and follow == 1:
            try:
                sel = cmds.select(rootJnt , hi = 1)
                cmds.select(sel[-1],d = 1)
                cmds.parent(w = 1)
            except:
                continue
    
def MirrorX(*args):
    sel = cmds.ls(sl=1)
    Duplicate = cmds.checkBox("Duplicate",q=1,v=1)
    if Duplicate == 1:
        for obj in sel:
            if cmds.objectType( obj, isType='joint' ):
                cmds.mirrorJoint( obj , mirrorBehavior=1 , mirrorYZ=1)
            if cmds.objectType( obj, isType='joint' ) == 0:
                DupedObj = cmds.duplicate(obj , n = "Dulicated_"+obj)
                Grp = cmds.group(em = 1 , n = "Referenced_"+obj+"_Grp")
                print(DupedObj[0])
                cmds.parent(DupedObj[0],"Referenced_"+obj+"_Grp")
                SX = cmds.getAttr(Grp + ".sx")
                cmds.setAttr(Grp + ".sx" , -SX)
                cmds.parent(DupedObj[0], w = 1)
                cmds.delete("Referenced_"+obj+"_Grp")
    if Duplicate == 0:
        for obj in sel:
            if cmds.objectType( obj, isType='joint' ):
                cmds.spaceLocator(n = "ReferenceLocator" )
                cmds.delete(cmds.parentConstraint(obj , "ReferenceLocator" , mo = 0))
                TX = cmds.getAttr("ReferenceLocator.tx")
                RY = cmds.getAttr("ReferenceLocator.ry")
                RZ = cmds.getAttr("ReferenceLocator.rz")
                cmds.setAttr("ReferenceLocator.tx",-TX)
                cmds.setAttr("ReferenceLocator.ry",-RY)
                cmds.setAttr("ReferenceLocator.rz",-RZ)
                cmds.delete(cmds.parentConstraint("ReferenceLocator", obj , mo = 0))
                SZ = cmds.getAttr(obj+".sx")
                cmds.setAttr(obj+".sx",-SX )
                cmds.delete("ReferenceLocator")
            if cmds.objectType( obj, isType='joint' ) == 0:
                Grp = cmds.group(em = 1 , n = "Referenced_"+obj+"_Grp")
                cmds.parent(obj,"Referenced_"+obj+"_Grp")
                SX = cmds.getAttr(Grp + ".sx")
                cmds.setAttr(Grp + ".sx" , -SX)
                cmds.parent(obj , w = 1)
                cmds.delete("Referenced_"+obj+"_Grp")
    
def MirrorY(*args):
    sel = cmds.ls(sl=1)
    Duplicate = cmds.checkBox("Duplicate",q=1,v=1)
    if Duplicate == 1:
        for obj in sel:
            if cmds.objectType( obj, isType='joint' ):
                cmds.mirrorJoint( obj , mirrorBehavior=1 , mirrorXZ=1)
            if cmds.objectType( obj, isType='joint' ) == 0:
                DupedObj = cmds.duplicate(obj , n = "Dulicated_"+obj)
                Grp = cmds.group(em = 1 , n = "Referenced_"+obj+"_Grp")
                cmds.parent(DupedObj[0],"Referenced_"+obj+"_Grp")
                SY = cmds.getAttr(Grp + ".sy")
                cmds.setAttr(Grp + ".sy" , -SY)
                cmds.parent(DupedObj[0] , w = 1)
                cmds.delete("Referenced_"+obj+"_Grp")
    if Duplicate == 0:
        for obj in sel:
            if cmds.objectType( obj, isType='joint' ):
                cmds.spaceLocator(n = "ReferenceLocator" )
                cmds.delete(cmds.parentConstraint(obj , "ReferenceLocator" , mo = 0))
                TY = cmds.getAttr("ReferenceLocator.ty")
                RX = cmds.getAttr("ReferenceLocator.rx")
                RZ = cmds.getAttr("ReferenceLocator.rz")
                cmds.setAttr("ReferenceLocator.ty",-TY)
                cmds.setAttr("ReferenceLocator.rx",-RX)
                cmds.setAttr("ReferenceLocator.rz",-RZ)
                cmds.delete(cmds.parentConstraint("ReferenceLocator", obj , mo = 0))
                SY = cmds.getAttr(obj+".sy")
                cmds.setAttr(obj+".sy",-SY )
                cmds.delete("ReferenceLocator")
            if cmds.objectType( obj, isType='joint' ) == 0:
                Grp = cmds.group(em = 1 , n = "Referenced_"+obj+"_Grp")
                cmds.parent(obj,"Referenced_"+obj+"_Grp")
                SY = cmds.getAttr(Grp + ".sy")
                cmds.setAttr(Grp + ".sy" , -SY)
                cmds.parent(obj , w = 1)
                cmds.delete("Referenced_"+obj+"_Grp")
    
def MirrorZ(*args):
    sel = cmds.ls(sl=1)
    Duplicate = cmds.checkBox("Duplicate",q=1,v=1)
    if Duplicate == 1:
        for obj in sel:
            if cmds.objectType( obj, isType='joint' ):
                cmds.mirrorJoint( obj , mirrorBehavior=1 , mirrorXY=1)
            if cmds.objectType( obj, isType='joint' ) == 0:
                DupedObj = cmds.duplicate(obj , n = "Dulicated_"+obj)
                Grp = cmds.group(em = 1 , n = "Referenced_"+obj+"_Grp")
                cmds.parent(DupedObj[0],"Referenced_"+obj+"_Grp")
                SZ = cmds.getAttr(Grp + ".sz")
                cmds.setAttr(Grp + ".sz" , -SZ)
                cmds.parent(DupedObj[0] , w = 1)
                cmds.delete("Referenced_"+obj+"_Grp")
    if Duplicate == 0:
        for obj in sel:
            if cmds.objectType( obj, isType='joint' ):
                cmds.spaceLocator(n = "ReferenceLocator" )
                cmds.delete(cmds.parentConstraint(obj , "ReferenceLocator" , mo = 0))
                TZ = cmds.getAttr("ReferenceLocator.tz")
                RX = cmds.getAttr("ReferenceLocator.rx")
                RY = cmds.getAttr("ReferenceLocator.ry")
                cmds.setAttr("ReferenceLocator.tz",-TZ)
                cmds.setAttr("ReferenceLocator.rx",-RX)
                cmds.setAttr("ReferenceLocator.rz",-RY)
                cmds.delete(cmds.parentConstraint("ReferenceLocator", obj , mo = 0))
                SZ = cmds.getAttr(obj+".sz")
                cmds.setAttr(obj+".sz",-SZ )
                cmds.delete("ReferenceLocator")
            if cmds.objectType( obj, isType='joint' ) == 0:
                Grp = cmds.group(em = 1 , n = "Referenced_"+obj+"_Grp")
                cmds.parent(obj,"Referenced_"+obj+"_Grp")
                SZ = cmds.getAttr(Grp + ".sz")
                cmds.setAttr(Grp + ".sz" , -SZ)
                cmds.parent(obj , w = 1)
                cmds.delete("Referenced_"+obj+"_Grp")
    
def TranslateCheckBox(*args):
    Translate = cmds.checkBox("Translate",q=1,v=1)
    if Translate == 1:
        cmds.checkBox("TX",edit=1,v=1)
        cmds.checkBox("TY",edit=1,v=1)
        cmds.checkBox("TZ",edit=1,v=1)
    else:
        cmds.checkBox("TX",edit=1,v=0)
        cmds.checkBox("TY",edit=1,v=0)
        cmds.checkBox("TZ",edit=1,v=0)
    
def RotateCheckBox(*args):
    Translate = cmds.checkBox("Rotate",q=1,v=1)
    if Translate == 1:
        cmds.checkBox("RX",edit=1,v=1)
        cmds.checkBox("RY",edit=1,v=1)
        cmds.checkBox("RZ",edit=1,v=1)
    else:
        cmds.checkBox("RX",edit=1,v=0)
        cmds.checkBox("RY",edit=1,v=0)
        cmds.checkBox("RZ",edit=1,v=0)
    
def ScaleCheckBox(*args):
    Translate = cmds.checkBox("Scale",q=1,v=1)
    if Translate == 1:
        cmds.checkBox("SX",edit=1,v=1)
        cmds.checkBox("SY",edit=1,v=1)
        cmds.checkBox("SZ",edit=1,v=1)
    else:
        cmds.checkBox("SX",edit=1,v=0)
        cmds.checkBox("SY",edit=1,v=0)
        cmds.checkBox("SZ",edit=1,v=0)
    
def CenterPivot(*args):
    cmds.xform( cp=True )
    
def DeleteHistory(*args):
    cmds.delete( ch=True )
    
def CombineCurves(*args):
    sel = cmds.ls(sl = True)
    if len(sel) < 2:
        sys.exit('Select at least 2 object to combine.\n')
    shape = cmds.listRelatives(shapes = True)
    for x in range(len(sel)):
        try:
            cmds.makeIdentity(sel[x], apply = True, rotate = True, scale = True, translate = True)
        except:
            continue
    group = cmds.group(empty = True, name = '_NewObjectCreated_')
    cmds.select(shape[0])
    for x in range(1, (len(shape))):
        cmds.select(shape[x], add  = True)
    cmds.select(group, add = True) 
    cmds.parent(relative = True, shape = True)
    cmds.xform(group ,cp=1)
    cmds.delete(sel)
    
def LockSelected(*args):
    transform = [".tx" ,".ty",".tz",".rx",".ry",".rz",".sx",".sy",".sz"]
    capTransform = ["TX" ,"TY","TZ","RX","RY","RZ","SX","SY","SZ"]
    sel = cmds.ls(sl = 1)
    for obj in sel:
        for i in range(9):
            checkBoxTr = cmds.checkBox(capTransform[i],q=1,v=1)
            if checkBoxTr == 1:
                if cmds.getAttr(obj+transform[i] , l = 1) == 1 :
                    cmds.setAttr(obj+transform[i], l =0 )
                else:
                    cmds.setAttr(obj+transform[i] ,l=1)
    
def HideSelected(*args):
    transform = [".tx" ,".ty",".tz",".rx",".ry",".rz",".sx",".sy",".sz"]
    capTransform = ["TX" ,"TY","TZ","RX","RY","RZ","SX","SY","SZ"]
    sel = cmds.ls(sl = 1)
    for obj in sel:
        for i in range(9):
            checkBoxTr = cmds.checkBox(capTransform[i],q=1,v=1)
            if checkBoxTr == 1:
                if cmds.getAttr(obj+transform[i] , k = 1) == 1 :
                    cmds.setAttr(obj+transform[i], k =0 )
                else:
                    cmds.setAttr(obj+transform[i] ,k=1)
    
def MakeHirarchyObjects(*args):
    sel = cmds.ls(sl = 1)
    for i in sel:
        if sel.index(i) == 0:
            oldObj = i
        if sel.index(i) > 0:
            newObj = i
            cmds.parent(newObj , oldObj)
            oldObj = newObj
    
def UnParentObjects(*args):
    sel = cmds.ls(sl = 1)
    for i in sel:
        try:
            cmds.parent(w = 1)
        except:
            continue
    
def ReversParent(*args):
    selList = []
    sel = cmds.ls(sl = 1)
    selList.append(sel[0])
    cmds.select(hi= 1)
    cmds.parent(w = 1)
    childSel = cmds.ls(sl = 1)
    for i in childSel:
        selList.append(i)
    selList.reverse()
    for i in selList:
        print(selList)
        if selList.index(i) == 0:
            oldObj = i
        if selList.index(i) > 0:
            newObj = i
            cmds.parent(newObj , oldObj)
            oldObj = newObj
    
def BindSkin(*args):
    mel.eval("SmoothBindSkinOptions;")
    
def SelectSkinedJoint(*args):
    print("SelectSkinedJoint")
    
def ParentConstraint(*args):
    MaintainOffset = cmds.checkBox("MaintainOffset",q=1,v=1)
    MO = MaintainOffset
    sel = cmds.ls(sl=1)
    parent = sel[-1]
    for obj in sel:
        if sel.index(obj)+1 != len(sel):
            cmds.parentConstraint(parent,obj,mo=MaintainOffset)
    
def PointConstraint(*args):
    MaintainOffset = cmds.checkBox("MaintainOffset",q=1,v=1)
    MO = MaintainOffset
    sel = cmds.ls(sl=1)
    parent = sel[-1]
    for obj in sel:
        if sel.index(obj)+1 != len(sel):
            cmds.pointConstraint(parent,obj,mo=MaintainOffset)
    
def OrientConstraint(*args):
    MaintainOffset = cmds.checkBox("MaintainOffset",q=1,v=1)
    MO = MaintainOffset
    sel = cmds.ls(sl=1)
    parent = sel[-1]
    for obj in sel:
        if sel.index(obj)+1 != len(sel):
            cmds.orientConstraint(parent,obj,mo=MaintainOffset)
    
def ScaleConstraint(*args):
    MaintainOffset = cmds.checkBox("MaintainOffset",q=1,v=1)
    MO = MaintainOffset
    sel = cmds.ls(sl=1)
    parent = sel[-1]
    for obj in sel:
        if sel.index(obj)+1 != len(sel):
            cmds.scaleConstraint(parent,obj,mo=MaintainOffset)
    
def AlignSelected(*args):
    checkTX = cmds.checkBox("TX",q=1,v=1)
    checkTY = cmds.checkBox("TY",q=1,v=1)
    checkTZ = cmds.checkBox("TZ",q=1,v=1)
    checkRX = cmds.checkBox("RX",q=1,v=1)
    checkRY = cmds.checkBox("RY",q=1,v=1)
    checkRZ = cmds.checkBox("RZ",q=1,v=1)
    checkSX = cmds.checkBox("SX",q=1,v=1)
    checkSY = cmds.checkBox("SY",q=1,v=1)
    checkSZ = cmds.checkBox("SZ",q=1,v=1)
    selList=[]
    print("AlignSelected")
    sel = cmds.ls(sl=1)
    for obj in sel:
        selList.append(obj)
    parent = selList[-1]
    print(parent)
    for i in selList:
        if selList.index(i)+1 != len(selList):
            cmds.spaceLocator(n="RefferenceLocator",p=(0,0,0))
            cmds.delete(cmds.parentConstraint(i,"RefferenceLocator"))
            parentRX = cmds.getAttr(parent+".rx")
            parentRY = cmds.getAttr(parent+".ry")
            parentRZ = cmds.getAttr(parent+".rz")
            parentSX = cmds.getAttr(parent+".sx")
            parentSY = cmds.getAttr(parent+".sy")
            parentSZ = cmds.getAttr(parent+".sz")
            ITX = cmds.getAttr(i+".tx")
            ITY = cmds.getAttr(i+".ty")
            ITZ = cmds.getAttr(i+".tz")
            cmds.makeIdentity( "RefferenceLocator" ,apply=True, t=1, r=1, s=1 )
            cmds.setAttr("RefferenceLocator.tx",-ITX)
            cmds.setAttr("RefferenceLocator.ty",-ITY)
            cmds.setAttr("RefferenceLocator.tz",-ITZ)
            cmds.makeIdentity( "RefferenceLocator" ,apply=True, t=1, r=1, s=1 )
            cmds.delete(cmds.parentConstraint(parent,"RefferenceLocator"))
            locTX = cmds.getAttr("RefferenceLocator.tx")
            locTY = cmds.getAttr("RefferenceLocator.ty")
            locTZ = cmds.getAttr("RefferenceLocator.tz")
            if checkTX == 1:
                cmds.setAttr(i+".tx",locTX)
            if checkTY == 1:
                cmds.setAttr(i+".ty",locTY)
            if checkTZ == 1:
                cmds.setAttr(i+".tz",locTZ)
            if checkRX == 1:
                cmds.setAttr(i+".rx",parentRX)
            if checkRY == 1:
                cmds.setAttr(i+".ry",parentRY)
            if checkRZ == 1:
                cmds.setAttr(i+".rz",parentRZ)
            if checkSX == 1:
                cmds.setAttr(i+".sx",parentSX)
            if checkSY == 1:
                cmds.setAttr(i+".sy",parentSY)
            if checkSZ == 1:
                cmds.setAttr(i+".sz",parentSZ)
            cmds.delete("RefferenceLocator")
    
def SelectSkinedJoints(*args):
    sel = cmds.ls(sl=True)
    cmds.select(cl=True)
    for obj in sel:
        cmds.select(cmds.skinCluster(obj, query=True, inf=True),add=1)
    
RiggingTools()
