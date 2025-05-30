from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance
import pymel.core as pmc
import maya.cmds as cmds
import maya.OpenMayaUI as omui
import maya.OpenMaya as OpenMaya
from functools import partial
import sys


# noinspection PyArgumentList
def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    if sys.version_info.major >= 3:
        return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
    else:
        return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class EyeLidSetupUI(QtWidgets.QMainWindow):
    # noinspection PyArgumentList
    def __init__(self, parent=maya_main_window()):
        super(EyeLidSetupUI, self).__init__(parent)

        self.setWindowTitle('Eye Lid Setup Tool')
        self.setWindowFlags(QtCore.Qt.Window)

        self.setObjectName("eyeLidSetup")
        self.setProperty("saveWindowPref", True)

        self.setMinimumSize(QtCore.QSize(200, 180))
        self.setMaximumSize(QtCore.QSize(200, 180))

        # Create menubar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Edit Curve')
        self.actionCreateCrv = QtWidgets.QAction('Create From Selection', self)
        fileMenu.addAction(self.actionCreateCrv)
        self.actionReverseCrv = QtWidgets.QAction('Reverse Direction', self)
        fileMenu.addAction(self.actionReverseCrv)
        self.actionMirrorCrv = QtWidgets.QAction('Mirror Curves', self)
        fileMenu.addAction(self.actionMirrorCrv)
        self.actionSelectBindJoints = QtWidgets.QAction('Select Bind Joints', self)
        fileMenu.addAction(self.actionSelectBindJoints)

        # Building a layout
        container = QtWidgets.QWidget(self)
        self.gridLayout = QtWidgets.QGridLayout(container)
        self.gridLayout.setHorizontalSpacing(0)
        self.setLayout(self.gridLayout)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(3)

        # Menu Breakline setup
        self.menuLine = QtWidgets.QFrame()
        self.menuLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.menuLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout.addWidget(self.menuLine)


        #Setup left right Layout
        self.horizontalLayout01 = QtWidgets.QHBoxLayout()
        self.horizontalLayout01.setSpacing(2)
        self.setupLabel = QtWidgets.QLabel('Setup Side:')
        self.horizontalLayout01.addWidget(self.setupLabel)

        self.horizontalLayout01.addItem(QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))

        self.l_side_RB = QtWidgets.QRadioButton('Left')
        self.l_side_RB.setChecked(True)
        self.horizontalLayout01.addWidget(self.l_side_RB)

        self.r_side_RB = QtWidgets.QRadioButton('Right')
        self.horizontalLayout01.addWidget(self.r_side_RB)

        self.verticalLayout.addLayout(self.horizontalLayout01)

        #Top Breakline setup
        self.topLine = QtWidgets.QFrame()
        self.topLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.topLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout.addWidget(self.topLine)

        #Eye Center Layout
        self.horizontalLayout02 = QtWidgets.QHBoxLayout()
        self.horizontalLayout02.setSpacing(2)
        self.eyeCenterLabel = QtWidgets.QLabel('Eye Center:   ')
        self.horizontalLayout02.addWidget(self.eyeCenterLabel)

        self.eyeCenterLineEdit = QtWidgets.QLineEdit()
        self.eyeCenterLineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout02.addWidget(self.eyeCenterLineEdit)

        self.eyeCenterPB = QtWidgets.QPushButton('<<')
        self.eyeCenterPB.setMinimumSize(QtCore.QSize(30, 20))
        self.eyeCenterPB.setMaximumSize(QtCore.QSize(30, 20))
        self.horizontalLayout02.addWidget(self.eyeCenterPB)

        self.verticalLayout.addLayout(self.horizontalLayout02)

        #Upperlid Layout
        self.horizontalLayout03 = QtWidgets.QHBoxLayout()
        self.horizontalLayout03.setSpacing(2)
        self.upLidLabel = QtWidgets.QLabel('UpLid Curve:')
        self.horizontalLayout03.addWidget(self.upLidLabel)

        self.upLidLineEdit = QtWidgets.QLineEdit()
        self.upLidLineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout03.addWidget(self.upLidLineEdit)

        self.upLidPB = QtWidgets.QPushButton('<<')
        self.upLidPB.setMinimumSize(QtCore.QSize(30, 20))
        self.upLidPB.setMaximumSize(QtCore.QSize(30, 20))
        self.horizontalLayout03.addWidget(self.upLidPB)

        self.verticalLayout.addLayout(self.horizontalLayout03)

        #Lowerlid Layout
        self.horizontalLayout04 = QtWidgets.QHBoxLayout()
        self.horizontalLayout04.setSpacing(2)
        self.loLidLabel = QtWidgets.QLabel('LoLid Curve: ')
        self.horizontalLayout04.addWidget(self.loLidLabel)

        self.loLidLineEdit = QtWidgets.QLineEdit()
        self.loLidLineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout04.addWidget(self.loLidLineEdit)

        self.loLidPB = QtWidgets.QPushButton("<<")
        self.loLidPB.setMinimumSize(QtCore.QSize(30, 20))
        self.loLidPB.setMaximumSize(QtCore.QSize(30, 20))
        self.horizontalLayout04.addWidget(self.loLidPB)

        self.verticalLayout.addLayout(self.horizontalLayout04)

        #Bottom Breakline setup
        self.bottomLine = QtWidgets.QFrame()
        self.bottomLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.bottomLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout.addWidget(self.bottomLine)

        self.createSetupPB = QtWidgets.QPushButton('Build Eye Rig')
        self.verticalLayout.addWidget(self.createSetupPB)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.setCentralWidget(container)

        self.signalsAndSlots()


    def signalsAndSlots(self):
        self.eyeCenterPB.clicked.connect(partial(self.setTextField, self.eyeCenterPB))
        self.upLidPB.clicked.connect(partial(self.setTextField, self.upLidPB))
        self.loLidPB.clicked.connect(partial(self.setTextField, self.loLidPB))

        self.actionCreateCrv.triggered.connect(lambda: cmds.polyToCurve(n='highResolution_crv', form=2,degree=1))
        self.actionReverseCrv.triggered.connect(lambda: cmds.reverseCurve(cmds.ls(sl=True)[0], ch=1, rpo=1))
        self.actionMirrorCrv.triggered.connect(self.mirrorCrv)
        self.actionSelectBindJoints.triggered.connect(self.selectBindJoints)

        self.createSetupPB.clicked.connect(self.setupSide)


    def setTextField(self, btn):
        if btn == self.upLidPB:
            self.upLidLineEdit.setText(str(cmds.ls(sl=True)[0]))
            self.upLidLineEdit.setCursorPosition(0)
        elif btn == self.loLidPB:
            self.loLidLineEdit.setText(str(cmds.ls(sl=True)[0]))
            self.loLidLineEdit.setCursorPosition(0)
        elif btn == self.eyeCenterPB:
            self.eyeCenterLineEdit.setText(str(cmds.ls(sl=True)[0]))
            self.eyeCenterLineEdit.setCursorPosition(0)



    def getUParam(self, pnt=None, crv = None):
        if pnt is None:
            pnt = []
        point = OpenMaya.MPoint(pnt[0],pnt[1],pnt[2])
        curveFn = OpenMaya.MFnNurbsCurve(self.getDagPath(str(crv)))
        paramUtill=OpenMaya.MScriptUtil()
        paramPtr=paramUtill.asDoublePtr()
        isOnCurve = curveFn.isPointOnCurve(point)
        if isOnCurve == True:

            curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )
        else :
            point = curveFn.closestPoint(point,paramPtr,0.001,OpenMaya.MSpace.kObject)
            curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )

        param = paramUtill.getDouble(paramPtr)
        return param


    def getDagPath(self, objectName):
        if isinstance(objectName, list)==True:
            oNodeList=[]
            for o in objectName:
                selectionList = OpenMaya.MSelectionList()
                selectionList.add(o)
                oNode = OpenMaya.MDagPath()
                selectionList.getDagPath(0, oNode)
                oNodeList.append(oNode)
            return oNodeList
        else:
            selectionList = OpenMaya.MSelectionList()
            selectionList.add(objectName)
            oNode = OpenMaya.MDagPath()
            selectionList.getDagPath(0, oNode)
            return oNode

    # noinspection PyTypeChecker
    def mirrorCrv(self):
        crvs = cmds.ls(sl=True)
        if crvs is None:
            OpenMaya.MGlobal.displayWarning('Selected the eyelid curves you want to mirror')
        else:
            for crv in crvs:
                if not cmds.objectType(cmds.listRelatives(cmds.ls(sl=True)), isType='nurbsCurve'):
                    OpenMaya.MGlobal.displayWarning('The selected object is not a NurbsCurve')
                else:
                    rSideCrv = cmds.duplicate(crv)[0]
                    cmds.setAttr('{}.scalePivotX'.format(rSideCrv), 0)
                    cmds.setAttr('{}.sx'.format(rSideCrv), -1)
                    print("Curves mirrored to the right side",)
        cmds.select(cl=True)

    @staticmethod
    def selectBindJoints():
        cmds.select("*_*lid_*_s")

    def setupSide(self):
        if self.l_side_RB.isChecked():
            self.buildEyeRig('left')
        else:
            self.buildEyeRig('right')

    # noinspection PyUnboundLocalVariable,PyTypeChecker
    def buildEyeRig(self, setupSide):
        eyeCenter = self.eyeCenterLineEdit.text()
        lowerlidCrv = self.loLidLineEdit.text()
        upperlidCrv = self.upLidLineEdit.text()

        if setupSide == 'left':
            side = 'L_'
        else:
            side = 'R_'

        lidCntrlGrp = cmds.group(n='{}lidCntrlGrp'.format(side), em=True)
        lidControlJntGrp = cmds.group(n='{}lidControlJntGrp'.format(side), em=True)
        lidSkinJntGrp = cmds.group(n='{}lidSkinJntsGrp'.format(side), em=True)
        lidCrvGrp = cmds.group(n='{}lidCrvGrp'.format(side), em=True)
        lidLocGrp = cmds.group(n='{}lidLocGrp'.format(side), em=True)

        posC = cmds.xform(eyeCenter, t=True, ws=True, q=True)
        worldUplocator = cmds.spaceLocator(n='{}eyeUpVec_LOC'.format(side))[0]
        cmds.xform(worldUplocator, translation=posC, ws=True)
        cmds.setAttr('{}.visibility'.format(worldUplocator), 0)
        cmds.parent(worldUplocator, lidSkinJntGrp)

        for prefix in ['{}up'.format(side), '{}lo'.format(side)]:

            if prefix == '{}up'.format(side):
                crv = upperlidCrv
            else:
                crv = lowerlidCrv

            cmds.delete(crv, ch=True)
            cmds.makeIdentity(crv,apply=True, t=True, r=True, s=True)

            jntGrp = cmds.group(n='{}lidJntGrp'.format(prefix), em=True)
            locGrp = cmds.group(n='{}lidLocGrp'.format(prefix), em=True)
            cmds.parent(locGrp, lidLocGrp)
            cmds.parent(jntGrp, lidSkinJntGrp)

            numSpans = cmds.getAttr(crv + ".spans")
            degree = cmds.getAttr(crv + ".degree")
            numCVs = numSpans + degree

            baseJntList = []
            for v in range(numCVs):
                cmds.select(cl=True)
                skinJnt = cmds.joint(n='{}lid_%02d_s'.format(prefix) % (v+1,))
                cmds.setAttr('{}.radius'.format(skinJnt), 0.1)
                pos = cmds.pointPosition('{0}.cv[{1}]'.format(crv, v))
                cmds.xform(skinJnt, translation=pos, ws=True)
                loc = cmds.spaceLocator(n='{}lid_%02d_loc'.format(prefix) % (v+1,))[0]
                cmds.xform(loc, translation=pos, ws=True)
                cmds.select(cl=True)
                jntC = cmds.joint(n='{}lid_%02d_jnt'.format(prefix) % (v+1,))
                cmds.setAttr('{}.radius'.format(jntC), 0.1)
                cmds.xform(jntC, translation=posC, ws=True)
                baseJntList.append(jntC)
                cmds.joint(jntC, e=True, oj='xyz', secondaryAxisOrient='yup', ch=True, zso=True)
                aimconstraint = cmds.aimConstraint(loc, jntC, mo=False, weight=1, aimVector= (0,0,1), upVector = (0,1,0), worldUpType='objectrotation', worldUpObject=worldUplocator)
                cmds.parent(skinJnt, jntC)
                for each in [skinJnt, aimconstraint]:
                    cmds.reorder(each, b=True)
                u = self.getUParam(pos, crv)
                name = loc.replace('_loc', '_pci')
                pci = cmds.createNode('pointOnCurveInfo', n=name)
                cmds.connectAttr('{}.worldSpace'.format(crv), '{}.inputCurve'.format(pci))
                cmds.setAttr('{}.parameter'.format(pci), u)
                cmds.connectAttr('{}.position'.format(pci), '{}.translate'.format(loc))
                cmds.parent(loc, locGrp)
                cmds.parent(jntC, jntGrp)

            loCrv = cmds.rebuildCurve(crv, ch=False, rpo=False, kep=True, s=4, d=3,tol=0.01, n='{}lidLo_crv'.format(prefix))[0]
            for c in [crv, loCrv]:
                cmds.parent(c, lidCrvGrp)
            cmds.wire(crv, w=loCrv)

            numberOfJnts = len(baseJntList)
            midJntNum = int(abs(numberOfJnts / 2))
            midToCornerJntNum = int(midJntNum / 2)
            midToOutCornerNum = int(midJntNum + midToCornerJntNum)
            midToInCornerNum = int(midJntNum - midToCornerJntNum)

            bindToCurveJntList = []
            for c in range(7):
                if c == 0 and prefix == '{}up'.format(side):
                    cvPos = cmds.pointPosition('{0}.cv[{1}]'.format(loCrv, c))
                    grp = cmds.group(n='{}inlid_POS'.format(side),em=True)
                    sdk = cmds.group(n='{}inlid_SDK'.format(side), em=True)
                    cntrlCrv = cmds.circle(n='{}inlid'.format(side), ch=False, r=0.05)[0]
                    cmds.setAttr('{}.overrideEnabled'.format(cntrlCrv), 1)
                    cmds.setAttr('{}.overrideColor.'.format(cntrlCrv), 21)
                    cmds.select(cl=True)
                    jnt = cmds.joint(n='{}inlid_s'.format(side), p=[0,0,0])
                    baseJnt = baseJntList[0]
                    rot = cmds.xform(baseJnt, ro=True, q=True)[1]
                    cmds.parent(jnt, lidControlJntGrp)
                    cmds.parent(grp, lidCntrlGrp)
                    cmds.parent(sdk,grp)
                    cmds.parent(cntrlCrv,sdk)
                    cmds.pointConstraint(cntrlCrv, jnt)
                    bindToCurveJntList.append(jnt)
                    cmds.xform(grp, translation=cvPos)
                    cmds.xform(grp, rotation=[0,rot,0])

                elif c == 2:
                    cvPos = cmds.pointPosition('{0}.cv[{1}]'.format(loCrv, c))
                    grp = cmds.group(n='{}InLid_POS'.format(prefix), em=True)
                    sdk = cmds.group(n='{}InLid_SDK'.format(prefix), em=True)
                    cntrlCrv = cmds.circle(n='{}InLid'.format(prefix), ch=False, r=0.03)[0]
                    cmds.setAttr('{}.overrideEnabled'.format(cntrlCrv), 1)
                    cmds.setAttr('{}.overrideColor.'.format(cntrlCrv), 21)
                    cmds.select(cl=True)
                    jnt = cmds.joint(n='{}InLid_s'.format(prefix), p=[0,0,0])
                    baseJnt = baseJntList[midToInCornerNum-1]
                    rot = cmds.xform(baseJnt, ro=True, q=True)[1]
                    cmds.parent(jnt, lidControlJntGrp)
                    cmds.parent(grp, lidCntrlGrp)
                    cmds.parent(sdk,grp)
                    cmds.parent(cntrlCrv,sdk)
                    cmds.pointConstraint(cntrlCrv, jnt)
                    bindToCurveJntList.append(jnt)
                    cmds.xform(grp, translation=cvPos)
                    cmds.xform(grp, rotation=[0,rot,0])

                elif c == 3:
                    cvPos = cmds.pointPosition('{0}.cv[{1}]'.format(loCrv, c))
                    grp = cmds.group(em=True,n='{}lid_POS'.format(prefix))
                    sdk = cmds.group(em=True,n='{}lid_SDK'.format(prefix))
                    cntrlCrv = cmds.circle(n='{}lid'.format(prefix), ch=False, r=0.05)[0]
                    cmds.setAttr('{}.overrideEnabled'.format(cntrlCrv), 1)
                    cmds.setAttr('{}.overrideColor.'.format(cntrlCrv), 21)
                    cmds.select(cl=True)
                    jnt = cmds.joint(n='{}lid_s'.format(prefix), p=[0,0,0])
                    baseJnt = baseJntList[midJntNum-1]
                    rot = cmds.xform(baseJnt, ro=True, q=True)[1]
                    cmds.parent(jnt, lidControlJntGrp)
                    cmds.parent(grp, lidCntrlGrp)
                    cmds.parent(sdk,grp)
                    cmds.parent(cntrlCrv,sdk)
                    cmds.pointConstraint(cntrlCrv, jnt)
                    bindToCurveJntList.append(jnt)
                    cmds.xform(grp, translation=cvPos)
                    cmds.xform(grp, rotation=[0,rot,0])

                    if prefix == '{0}up'.format(side):
                        cmds.addAttr(cntrlCrv, ln='blinkHeight', at='double', min=0, max=1, dv=0.25)
                        cmds.setAttr('{}.blinkHeight'.format(cntrlCrv), keyable=True)
                        cmds.addAttr(cntrlCrv, ln='skinFollow', at='double', min=0, max=1, dv=0.3)
                        cmds.setAttr('{}.skinFollow'.format(cntrlCrv), keyable=True)

                    elif prefix == '{}lo'.format(side):
                        cmds.addAttr(cntrlCrv, ln='skinFollow', at='double', min=0, max=1, dv=0.3)
                        cmds.setAttr('{}.skinFollow'.format(cntrlCrv), keyable=True)

                    cmds.addAttr(cntrlCrv, ln='secondaryCtrl', at='bool')
                    cmds.setAttr('{}.secondaryCtrl'.format(cntrlCrv), keyable=True)

                    cmds.addAttr(cntrlCrv, ln='blink', at='double', min=0, max=1)
                    cmds.setAttr('{}.blink'.format(cntrlCrv), keyable=True)

                elif c == 4:
                    cvPos = cmds.pointPosition('{0}.cv[{1}]'.format(loCrv, c))
                    grp = cmds.group(em=True,n='{}OutLid_POS'.format(prefix))
                    sdk = cmds.group(em=True,n='{}OutLid_SDK'.format(prefix))
                    cntrlCrv = cmds.circle(n='{}OutLid'.format(prefix), ch=False, r=0.03)[0]
                    cmds.setAttr('{}.overrideEnabled'.format(cntrlCrv), 1)
                    cmds.setAttr('{}.overrideColor.'.format(cntrlCrv), 21)
                    cmds.select(cl=True)
                    jnt = cmds.joint(n='{}OutLid_s'.format(prefix), p=[0,0,0])
                    baseJnt = baseJntList[midToOutCornerNum-1]
                    rot = cmds.xform(baseJnt, ro=True, q=True)[1]
                    cmds.parent(jnt, lidControlJntGrp)
                    cmds.parent(grp, lidCntrlGrp)
                    cmds.parent(sdk,grp)
                    cmds.parent(cntrlCrv,sdk)
                    cmds.pointConstraint(cntrlCrv, jnt)
                    bindToCurveJntList.append(jnt)
                    cmds.xform(grp, translation=cvPos)
                    cmds.xform(grp, rotation=[0,rot,0])

                elif c == 6 and prefix == '{}up'.format(side):
                    cvPos = cmds.pointPosition('{0}.cv[{1}]'.format(loCrv, c))
                    grp = cmds.group(em=True,n='{}outlid_POS'.format(side))
                    sdk = cmds.group(em=True,n='{}outlid_SDK'.format(side))
                    cntrlCrv = cmds.circle(n='{}outlid'.format(side), ch=False, r=0.05)[0]
                    cmds.setAttr('{}.overrideEnabled'.format(cntrlCrv), 1)
                    cmds.setAttr('{}.overrideColor.'.format(cntrlCrv), 21)
                    cmds.select(cl=True)
                    jnt = cmds.joint(n='{}outlid_s'.format(side), p=[0,0,0])
                    baseJnt = baseJntList[-1]
                    rot = cmds.xform(baseJnt, ro=True, q=True)[1]
                    cmds.parent(jnt, lidControlJntGrp)
                    cmds.parent(grp, lidCntrlGrp)
                    cmds.parent(sdk,grp)
                    cmds.parent(cntrlCrv,sdk)
                    cmds.pointConstraint(cntrlCrv, jnt)
                    bindToCurveJntList.append(jnt)
                    cmds.xform(grp, translation=cvPos)
                    cmds.xform(grp, rotation=[0,rot,0])

                for a in ['sx', 'sy', 'sz', 'visibility']:
                    cmds.setAttr('{0}.{1}'.format(cntrlCrv, a), lock=True, keyable=False, channelBox=False)

            cmds.connectAttr('{}lid.secondaryCtrl'.format(prefix), '{}OutLid_POS.visibility'.format(prefix))
            cmds.connectAttr('{}lid.secondaryCtrl'.format(prefix), '{}InLid_POS.visibility'.format(prefix))

            if prefix == '{}up'.format(side):
                cmds.skinCluster(bindToCurveJntList, loCrv)
            else:
                bindToCurveJntList.append('{}outlid_s'.format(side))
                bindToCurveJntList.append('{}inlid_s'.format(side))
                cmds.skinCluster(bindToCurveJntList, loCrv)

        cmds.parentConstraint('{}outlid'.format(side), '{}uplid'.format(side), '{}upOutLid_SDK'.format(side), mo=True)
        cmds.parentConstraint('{}inlid'.format(side), '{}uplid'.format(side), '{}upInLid_SDK'.format(side), mo=True)
        cmds.parentConstraint('{}inlid'.format(side), '{}lolid'.format(side), '{}loInLid_SDK'.format(side), mo=True)
        cmds.parentConstraint('{}outlid'.format(side), '{}lolid'.format(side), '{}loOutLid_SDK'.format(side), mo=True)

        blinkCrv = cmds.duplicate('{}uplidLo_crv'.format(side), n='{}blink_crv'.format(side))[0]
        loLidBlinkCrv = cmds.duplicate(lowerlidCrv, n='{}lolidBlink_crv'.format(side))[0]
        upLidBlinkCrv = cmds.duplicate(upperlidCrv, n='{}uplidBlink_crv'.format(side))[0]

        blendShapeNode = cmds.blendShape('{}uplidLo_crv'.format(side), '{}lolidLo_crv'.format(side), blinkCrv, n='{}eyeRig_BS'.format(side))[0]
        revNode = cmds.shadingNode('reverse',asUtility=True, n='{}smartBlink_REV'.format(side))
        cmds.connectAttr('{}uplid.blinkHeight'.format(side), '{}.{}uplidLo_crv'.format(blendShapeNode, side))
        cmds.connectAttr('{}uplid.blinkHeight'.format(side),'{}.inputX'.format(revNode))
        cmds.connectAttr('{}.outputX'.format(revNode), '{}.{}lolidLo_crv'.format(blendShapeNode, side))

        cmds.setAttr('{}uplid.blinkHeight'.format(side), 1)
        wireNode = cmds.wire(upLidBlinkCrv, w=blinkCrv)[0]
        cmds.setAttr('{}.scale[0]'.format(wireNode), 0)

        cmds.setAttr('{}uplid.blinkHeight'.format(side), 0)
        wireNode = cmds.wire(loLidBlinkCrv, w=blinkCrv)[0]
        cmds.setAttr('{}.scale[0]'.format(wireNode), 0)
        cmds.setAttr('{}uplid.blinkHeight'.format(side), 0.25)

        upperBlinkBsNode = cmds.blendShape(upLidBlinkCrv, upperlidCrv)[0]
        cmds.connectAttr('{}uplid.blink'.format(side), '{0}.{1}'.format(upperBlinkBsNode, upLidBlinkCrv))

        lowerBlinkBsNode = cmds.blendShape(loLidBlinkCrv, lowerlidCrv)[0]
        cmds.connectAttr('{}lolid.blink'.format(side), '{0}.{1}'.format(lowerBlinkBsNode, loLidBlinkCrv))

        #clean up scene
        cmds.group(lidCntrlGrp, lidSkinJntGrp, n='{}lid_parentToHeadGrp'.format(side))
        parentToLocal = cmds.group(lidCrvGrp, lidControlJntGrp, lidLocGrp, n='{}lid_keepOutsideControlHierarchyGrp'.format(side))
        cmds.setAttr('{}.visibility'.format(parentToLocal), 0)
        self.eyeCenterLineEdit.clear()
        self.upLidLineEdit.clear()
        self.loLidLineEdit.clear()

        self.setupSoftEye(eyeCenter, side)

        self.r_side_RB.setChecked(True)


    def setupSoftEye(self, eyeCenter, side):

        upLidSDK = '{}uplid_SDK'.format(side)
        loLidSDK = '{}lolid_SDK'.format(side)

        upLid = '{}uplid'.format(side)
        loLid = '{}lolid'.format(side)

        eyeRotatePivot = cmds.xform(eyeCenter, rotatePivot=True, ws=True, q=True)
        cmds.xform(upLidSDK, rotatePivot=eyeRotatePivot, ws=True)
        cmds.xform(loLidSDK, rotatePivot=eyeRotatePivot, ws=True)

        upLidClmpNode = cmds.createNode('clamp', n='{}upLidSoftEye_CLMP'.format(side))
        cmds.connectAttr('{}.rotateX'.format(eyeCenter), '{}.inputR'.format(upLidClmpNode))
        cmds.connectAttr('{}.rotateY'.format(eyeCenter), '{}.inputG'.format(upLidClmpNode))

        cmds.connectAttr('{}.outputR'.format(upLidClmpNode), '{}.rotateX'.format(upLidSDK))
        cmds.connectAttr('{}.outputG'.format(upLidClmpNode), '{}.rotateY'.format(upLidSDK))

        upLidMdNode =  cmds.createNode("multiplyDivide", n="{}upLidSoftEye_MD".format(side))

        cmds.connectAttr('{}.rotateX'.format(eyeCenter), '{}.input1X'.format(upLidMdNode))
        cmds.connectAttr('{}.rotateY'.format(eyeCenter), '{}.input1Y'.format(upLidMdNode))

        cmds.connectAttr('{}.outputX'.format(upLidMdNode), '{}.inputR'.format(upLidClmpNode), f=True)
        cmds.connectAttr('{}.outputY'.format(upLidMdNode), '{}.inputG'.format(upLidClmpNode), f=True)

        cmds.setAttr('{}.minR'.format(upLidClmpNode), -15)
        cmds.setAttr('{}.maxR'.format(upLidClmpNode), 15)
        cmds.setAttr('{}.minG'.format(upLidClmpNode), -20)
        cmds.setAttr('{}.maxR'.format(upLidClmpNode), 20)

        cmds.connectAttr('{}.skinFollow'.format(upLid), '{}.input2X'.format(upLidMdNode))
        cmds.connectAttr('{}.skinFollow'.format(upLid), '{}.input2Y'.format(upLidMdNode))

        loLidClmpNode = cmds.createNode('clamp', n='{}loLidSoftEye_CLMP'.format(side))
        cmds.connectAttr('{}.rotateX'.format(eyeCenter), '{}.inputR'.format(loLidClmpNode))
        cmds.connectAttr('{}.rotateY'.format(eyeCenter), '{}.inputG'.format(loLidClmpNode))

        cmds.connectAttr('{}.outputR'.format(loLidClmpNode), '{}.rotateX'.format(loLidSDK))
        cmds.connectAttr('{}.outputG'.format(loLidClmpNode), '{}.rotateY'.format(loLidSDK))

        loLidMdNode =  cmds.createNode("multiplyDivide", n="{}loLidSoftEye_MD".format(side))
        cmds.connectAttr('{}.rotateX'.format(eyeCenter), '{}.input1X'.format(loLidMdNode))
        cmds.connectAttr('{}.rotateY'.format(eyeCenter), '{}.input1Y'.format(loLidMdNode))

        cmds.connectAttr('{}.outputX'.format(loLidMdNode), '{}.inputR'.format(loLidClmpNode), f=True)
        cmds.connectAttr('{}.outputY'.format(loLidMdNode), '{}.inputG'.format(loLidClmpNode), f=True)

        cmds.setAttr('{}.minR'.format(loLidClmpNode), -15)
        cmds.setAttr('{}.maxR'.format(loLidClmpNode), 15)
        cmds.setAttr('{}.minG'.format(loLidClmpNode), -20)
        cmds.setAttr('{}.maxR'.format(loLidClmpNode), 20)

        cmds.connectAttr('{}.skinFollow'.format(loLid), '{}.input2X'.format(loLidMdNode))
        cmds.connectAttr('{}.skinFollow'.format(loLid), '{}.input2Y'.format(loLidMdNode))

    wnd_instance = None

    @classmethod
    def mayaRun(cls):
        if not cls.wnd_instance:
            cls.wnd_instance = EyeLidSetupUI()

        if cls.wnd_instance.isHidden():
            cls.wnd_instance.show()
        else:
            cls.wnd_instance.raise_()
            cls.wnd_instance.activateWindow()

