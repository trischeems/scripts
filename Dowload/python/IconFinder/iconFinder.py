try :#line:1
	from PySide2 .QtWidgets import *#line:2
	from PySide2 .QtCore import *#line:3
	from PySide2 .QtGui import *#line:4
	from PySide2 import QtUiTools #line:5
	from shiboken2 import wrapInstance #line:6
	from PySide2 import __version__ #line:7
except ImportError :#line:8
	from PySide .QtCore import *#line:9
	from PySide .QtGui import *#line:10
	from PySide import QtUiTools #line:11
	from shiboken import wrapInstance #line:12
	from PySide import __version__ #line:13
	from shiboken import wrapInstance #line:14
import os #line:15
from maya import OpenMayaUI as omui #line:16
import maya .mel as mel #line:17
import maya .cmds as cmds #line:18
from functools import partial #line:19
from os .path import isfile ,join #line:20
from os import listdir #line:21
from collections import OrderedDict #line:22
class IconFinder (QWidget ):#line:24
	def __init__ (O0OO0OO0O0O0O0OOO ,*OOO00O0000O0O000O ,**OO0OO0OO00O00OOO0 ):#line:25
		super (IconFinder ,O0OO0OO0O0O0O0OOO ).__init__ (*OOO00O0000O0O000O ,**OO0OO0OO00O00OOO0 )#line:26
		(lambda __g: [[[[[[(O0OO0OO0O0O0O0OOO.mainUI.setFixedSize(O0OO0OO0O0O0O0OOO.mainUI.size()), [(O0OO0OO0O0O0O0OOO.warning.setFixedSize(260, 150), (O0OO0OO0O0O0O0OOO.warning.move(90, 100), [[[(O0OO0OO0O0O0O0OOO.mainUI.show(), (O0OO0OO0O0O0O0OOO.initUI(), (O0OO0OO0O0O0O0OOO.hideWarning(), (O0OO0OO0O0O0O0OOO.setStylesheet(), None)[1])[1])[1])[1] for O0OO0OO0O0O0O0OOO.iconSortedList in [([])]][0] for O0OO0OO0O0O0O0OOO.preButton in [('')]][0] for O0OO0OO0O0O0O0OOO.iconDict in [(OrderedDict())]][0])[1])[1] for O0OO0OO0O0O0O0OOO.warning in [(O0OO0OO0O0O0O0OOO.loadUiWidget((OO000000OO000OOOO + '/ui/warningUI.ui'), O0OO0OO0O0O0O0OOO.mainUI))]][0])[1] for O0OO0OO0O0O0O0OOO.mainUI in [(O0OO0OO0O0O0O0OOO.loadUiWidget((OO000000OO000OOOO + '/ui/iconFinderUI.ui'), O0OO0O000OO00OOO0))]][0] for __g['O0OO0O000OO00OOO0'] in [(wrapInstance(long(O0OOOO00000O0OO00), QWidget))]][0] for __g['O0OOOO00000O0OO00'] in [(omui.MQtUtil.mainWindow())]][0] for O0OO0OO0O0O0O0OOO.imagePath in [(O0OO0OO0O0O0O0OOO.imagePath.replace('\\', '/'))]][0] for O0OO0OO0O0O0O0OOO.imagePath in [((os.path.dirname(os.path.abspath(__file__)) + '/ui/images/'))]][0] for __g['OO000000OO000OOOO'] in [(os.path.dirname(os.path.abspath(__file__)))]][0])(globals())
	def setStylesheet (O0O00OO00OO0OO0O0 ):#line:45
		(O0O00OO00OO0OO0O0.mainUI.groupBox.setStyleSheet('QFrame{background: #3C545F} QGroupBox { background: #3C545F; padding-top:5px; border: 1px solid #0F1317; border-radius: 6px; margin-top: 0.5em;} QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px;} QGroupBox::indicator {width: 0px; height: 0px;} .QPushButton{background-color: #2E414A; border-radius:2px; border: 1px solid #20333C;} .QPushButton:hover{background-color: #4A636F; } .QPushButton:pressed{background-color: #20333C; } QComboBox {background-color: #2E414A; border-radius:2px; border: 1px solid #20333C;} '), (O0O00OO00OO0OO0O0.mainUI.centralwidget.setStyleSheet((((('.QWidget#centralwidget {background-color: #384145; background-image: url(' + O0O00OO00OO0OO0O0.imagePath) + 'romboBack.png); border-image: url(') + O0O00OO00OO0OO0O0.imagePath) + 'vignetteFrame)} QToolTip {border-radius: 6px; border: 2px dashed #FFFFFF; padding: 2px; background: #674E4F; color: #FFFFFF}')), (O0O00OO00OO0OO0O0.mainUI.scrollAreaWidgetContents.setStyleSheet((('.QWidget {background:#393E43; background-image: url(' + O0O00OO00OO0OO0O0.imagePath) + 'squareBack.png);} .QPushButton {border: 0px; background:transparent}')), (O0O00OO00OO0OO0O0.mainUI.progressBar.setStyleSheet((('QProgressBar::chunk { background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #638289, stop: 0.49 #547881, stop: 0.55 #466E77, stop: 1 #39646E); border-radius: 8px; border: 0px solid black; background-image: url(' + O0O00OO00OO0OO0O0.imagePath) + 'progress.png);} QProgressBar { border: 1px solid #1F2124; text-align: center; padding: 0px; border-radius: 8px; background: QLinearGradient( x1: 0, y1: 0, x2: 0, y1: 1, stop: 0 #232F32, stop: 0.49 #314145, stop: 0.55 #3C4E52, stop: 1 #47585C); }')), (O0O00OO00OO0OO0O0.warning.setStyleSheet('QTextBrowser {background: #674E4F;} QGroupBox { background: #674E4F; padding-top:5px; border: 1px solid #3B2D2E; border-radius: 6px; margin-top: 0.5em;} QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px;} QGroupBox::indicator {width: 0px; height: 0px;} '), (O0O00OO00OO0OO0O0.warning.closeButton.setStyleSheet('.QPushButton { background-color: #3B2D2E; border-radius:2px; border: 1px solid #372122;} .QPushButton:hover{background-color: #876768; } .QPushButton:pressed{background-color: #3B2D2E;}'), (O0O00OO00OO0OO0O0.warning.showButton.setStyleSheet('.QPushButton { background-color: #3B2D2E; border-radius:2px; border: 1px solid #372122;} .QPushButton:hover{background-color: #876768; } .QPushButton:pressed{background-color: #3B2D2E;}'), (O0O00OO00OO0OO0O0.warning.setStyleSheet('QTextBrowser {background: #674E4F;} QGroupBox { background: #674E4F; font-size: 13px; font-weight: bold; padding-top:5px; border: 2px dashed #FFFFFF; border-top-left-radius: 40px; border-top-right-radius: 40px; border-bottom-left-radius: 40px; border-bottom-right-radius: 40px; margin-top: 0.5em;} QGroupBox::title { subcontrol-origin: margin; background: #372122; left: 40px; border: 1px solid #FFFFFF; border-radius:4px; padding: 3px 5px 3px 5px;} QGroupBox::indicator {width: 0px; height: 0px;} '), None)[1])[1])[1])[1])[1])[1])[1])[1]
	def showWarning (OOO000O0OOOO0O0OO ):#line:55
		try :#line:56
			OOO000O0OOOO0O0OO .warning .imageLabel .setText (str (len (OOO000O0OOOO0O0OO .iconSortedList ))+' icons found!\r\nDisplaying all of them can take a few seconds.\r\n\r\nProceed?')#line:57
			OOO000O0OOOO0O0OO .warning .show ()#line:58
		except :#line:59
			if cmds .confirmDialog (title ='Confirm',message =str (len (OOO000O0OOOO0O0OO .iconSortedList ))+' icons found!\r\nDisplaying all of them can take a few seconds.\r\n\r\nProceed?',button =['Sure','No!'],defaultButton ='No!',cancelButton ='No!',dismissString ='No!')=='Sure':#line:60
				OOO000O0OOOO0O0OO .populateIcons ()#line:61
	def hideWarning (OOOOO0OO00OOOO000 ):#line:63
		try :#line:64
			OOOOO0OO00OOOO000 .warning .hide ()#line:65
		except :#line:66
			pass ;#line:67
	def initUI (OO00OOO00000O0OOO ):#line:69
		(lambda __g: (OO00OOO00000O0OOO.mainUI.lineEdit.textChanged.connect(partial(OO00OOO00000O0OOO.searchIcons)), (OO00OOO00000O0OOO.mainUI.pushButton.clicked.connect(partial(OO00OOO00000O0OOO.searchIcons, 'All')), (OO00OOO00000O0OOO.mainUI.lineEdit.setToolTip('Enter more than 2 characters!'), (OO00OOO00000O0OOO.mainUI.keywordLabel.setToolTip('Enter more than 2 characters!'), (OO00OOO00000O0OOO.warning.closeButton.clicked.connect(partial(OO00OOO00000O0OOO.hideWarning)), (OO00OOO00000O0OOO.warning.showButton.clicked.connect(partial(OO00OOO00000O0OOO.populateIcons)), [[[[[[[[[None for __g['OOO0000O00O0O0O0O'] in [((OOO0000O00O0O0O0O + OO0OO00OOOOOOOO00))]][0] for __g['OO0O0O000OOOO00OO'] in [(0)]][0] for __g['O0OOOO00OO00OOO00'] in [(0)]][0] for __g['O0OO0OO0O0O0OOOO0'] in [(0)]][0] for __g['OOO00000OO0OOO0OO'] in [('')]][0] for __g['OOO0000O00O0O0O0O'] in [(OO0O0O0OO000OO00O.split('%B'))]][0] for __g['OO0OO00OOOOOOOO00'] in [(O0OO0O0O0OO0O00O0.split('%B'))]][0] for __g['O0OO0O0O0OO0O00O0'] in [(mel.eval('getenv "MAYA_FILE_ICON_PATH"'))]][0] for __g['OO0O0O0OO000OO00O'] in [(mel.eval('getenv "XBMLANGPATH"'))]][0])[1])[1])[1])[1])[1])[1])(globals())
		for OO00OO0OO0OO0O000 in OOO0000O00O0O0O0O :#line:85
			if OO00OO0OO0OO0O000 !='':#line:86
				if OO00OO0OO0OO0O000 [0 ]==':':#line:88
					OOO00000OO0OOO0OO =OO00OO0OO0OO0O000 .split (':')[1 ]#line:89
				else :#line:90
					OOO00000OO0OOO0OO =OO00OO0OO0OO0O000 #line:91
				if os .path .isdir (OOO00000OO0OOO0OO ):#line:93
					O0OOO000OO00OOO00 =[O0O0O0OO000OO0OO0 for O0O0O0OO000OO0OO0 in listdir (OOO00000OO0OOO0OO )if isfile (join (OOO00000OO0OOO0OO ,O0O0O0OO000OO0OO0 ))]#line:94
					for OO0O00OOOOO0000O0 in O0OOO000OO00OOO00 :#line:95
						OO00OOO00000O0OOO .iconDict [OO0O00OOOOO0000O0 ]=OOO00000OO0OOO0OO +OO0O00OOOOO0000O0 #line:96
		O00OO00O0000O0OO0 =cmds .resourceManager (nameFilter ='*')#line:97
		for O0O0O00O00O0OO0OO in O00OO00O0000O0OO0 :#line:98
			OO00OOO00000O0OOO .iconDict [O0O0O00O00O0OO0OO ]=''#line:99
		OO00OOO00000O0OOO .searchIcons ('')#line:100
	def searchIcons (OOOO000000000OOO0 ,OO00000O00OO0O0O0 ):#line:102
		OOOO000000000OOO0 .iconSortedList =[]#line:104
		if OO00000O00OO0O0O0 =='All':#line:105
			O0O0000OOO0O000OO =[]#line:106
			for OO00OO000O000O0OO in OOOO000000000OOO0 .iconDict .keys ():#line:107
				O0O0000OOO0O000OO .append (OO00OO000O000O0OO )#line:108
			OOOO000000000OOO0 .iconSortedList =sorted (O0O0000OOO0O000OO ,key =lambda OOO00000O00OO00OO :OOO00000O00OO00OO .lower ())#line:109
		else :#line:110
			OOOOO00O0O00OOOOO =str (OOOO000000000OOO0 .mainUI .lineEdit .text ())#line:111
			if len (OOOOO00O0O00OOOOO )>2 :#line:112
				O0O0000OOO0O000OO =[]#line:113
				for OO00OO000O000O0OO in OOOO000000000OOO0 .iconDict .keys ():#line:115
					if OOOOO00O0O00OOOOO .lower ()in OO00OO000O000O0OO .lower ():#line:116
						O0O0000OOO0O000OO .append (OO00OO000O000O0OO )#line:117
				OOOO000000000OOO0 .iconSortedList =sorted (O0O0000OOO0O000OO ,key =lambda O000O000OO00OO0O0 :O000O000OO00OO0O0 .lower ())#line:118
		if OOOO000000000OOO0 .iconSortedList :#line:119
			if len (OOOO000000000OOO0 .iconSortedList )>500 :#line:120
				OOOO000000000OOO0 .showWarning ()#line:121
			else :#line:122
				OOOO000000000OOO0 .populateIcons ()#line:123
	def populateIcons (O0O00OOOOOOO0O0O0 ):#line:125
		O0O00OOOOOOO0O0O0 .mainUI .progressBar .setValue (0 )#line:126
		for OOOO000000OOOO000 in reversed (range (O0O00OOOOOOO0O0O0 .mainUI .gridLayout .count ())):#line:127
			O0O00OOOOOOO0O0O0 .mainUI .gridLayout .itemAt (OOOO000000OOOO000 ).widget ().deleteLater ()#line:128
		O0O000O0O00O0OO00 =0 #line:129
		OO0OOOO0OO00O0O0O =0 #line:130
		OOOO0O0O000OO0000 =0 #line:131
		for OOO000O0OO00O0OOO in O0O00OOOOOOO0O0O0 .iconSortedList :#line:132
			(lambda __g: [(OOO000OO00OOOO000.setFixedSize(QSize(36, 36)), (OOO000OO00OOOO000.setToolTip(str(OOO000O0OO00O0OOO)), None)[1])[1] for __g['OOO000OO00OOOO000'] in [(QPushButton())]][0])(globals())
			if O0O00OOOOOOO0O0O0 .iconDict [OOO000O0OO00O0OOO ]!='':#line:136
				OOO000OO00OOOO000 .setIcon (QIcon (O0O00OOOOOOO0O0O0 .iconDict [OOO000O0OO00O0OOO ]))#line:137
				OOO000OO00OOOO000 .clicked .connect (partial (O0O00OOOOOOO0O0O0 .printPath ,O0O00OOOOOOO0O0O0 .iconDict [OOO000O0OO00O0OOO ],OOO000OO00OOOO000 ))#line:138
			else :#line:139
				(lambda __g: (OOO000OO00OOOO000.setIcon(QIcon((':/' + OOO000O0OO00O0OOO))), (OOO000OO00OOOO000.clicked.connect(partial(O0O00OOOOOOO0O0O0.printPath, OOO000O0OO00O0OOO, OOO000OO00OOOO000)), (OOO000OO00OOOO000.setContextMenuPolicy(Qt.CustomContextMenu), [(OOO0OOOOOOOOO0O0O.setStyleSheet('QMenu{background-color: #20333C; border-radius:2px; border: 1px solid #20333C;} QMenu::item:selected{background:#4A636F;}'), (OOO000OO00OOOO000.customContextMenuRequested.connect(partial(O0O00OOOOOOO0O0O0.on_context_menu, OOO000OO00OOOO000, OOO0OOOOOOOOO0O0O)), [[(OOO00O0O00OO0OOOO.triggered.connect(partial(O0O00OOOOOOO0O0O0.extractMaya, OOO000O0OO00O0OOO)), (OOO0OOOOOOOOO0O0O.addAction(OOO00O0O00OO0OOOO), None)[1])[1] for __g['OOO00O0O00OO0OOOO'] in [(O0O00O0O00O0O0OO0.addAction(QAction('Extract from Maya!', OOO000OO00OOOO000)))]][0] for __g['O0O00O0O00O0O0OO0'] in [(QActionGroup(OOO000OO00OOOO000, exclusive=True))]][0])[1])[1] for __g['OOO0OOOOOOOOO0O0O'] in [(QMenu(O0O00OOOOOOO0O0O0))]][0])[1])[1])[1])(globals())
			OOO000OO00OOOO000 .setIconSize (QSize (32 ,32 ))#line:150
			O0O00OOOOOOO0O0O0 .mainUI .gridLayout .addWidget (OOO000OO00OOOO000 ,O0O000O0O00O0OO00 ,OO0OOOO0OO00O0O0O )#line:151
			if OO0OOOO0OO00O0O0O <=10 :#line:152
				OO0OOOO0OO00O0O0O +=1 #line:153
			else :#line:154
				O0O000O0O00O0OO00 +=1 #line:155
				OO0OOOO0OO00O0O0O =0 #line:156
			OOOO0O0O000OO0000 +=1 #line:157
			O0O00OOOOOOO0O0O0 .mainUI .progressBar .setValue ((OOOO0O0O000OO0000 *100 )/len (O0O00OOOOOOO0O0O0 .iconSortedList ))#line:158
		O0O00OOOOOOO0O0O0 .hideWarning ()#line:159
	def extractMaya (OOO0000OO0OO00OOO ,O0O0OO0O000OO0OO0 ):#line:161
		OOO00O0OOO0OOO0O0 =str (QFileDialog .getExistingDirectory (OOO0000OO0OO00OOO ,"Select Directory"))#line:162
		if OOO00O0OOO0OOO0O0 :#line:163
			cmds .resourceManager (saveAs =(O0O0OO0O000OO0OO0 ,OOO00O0OOO0OOO0O0 +"/{0}".format (O0O0OO0O000OO0OO0 )))#line:164
	def on_context_menu (O0OO0OO0OOO00O0OO ,OO00O00OO0000OOOO ,O0O0O00OOOOOO0OOO ,O00O0OOOO0O0OO000 ):#line:166
		O0O0O00OOOOOO0OOO .exec_ (OO00O00OO0000OOOO .mapToGlobal (O00O0OOOO0O0OO000 ))#line:168
	def printPath (OO00O00OO0000OOO0 ,O0OO0000O0O0O00O0 ,O000O0000OOO0O000 ):#line:170
		OO00O00OO0000OOO0 .mainUI .pathLineEdit .setText (str (O0OO0000O0O0O00O0 ))#line:171
		if OO00O00OO0000OOO0 .preButton !='':#line:172
			try :#line:173
				OO00O00OO0000OOO0 .preButton .setStyleSheet ('QPushButton {border: 0px;}')#line:174
			except :#line:175
				pass ;#line:176
		try :#line:177
			O000O0000OOO0O000 .setStyleSheet ('QPushButton {border: 1px solid cyan;}')#line:178
			OO00O00OO0000OOO0 .preButton =O000O0000OOO0O000 #line:179
		except :#line:180
			pass ;#line:181
	def loadUiWidget (OOO0OO0000O000OOO ,OO0O0000OO00O00OO ,O0O00OO00OO0OOOO0 =None ):#line:183
		(lambda __g: [[(OO0000O0O0O0O00OO.open(QFile.ReadOnly), [(OO0000O0O0O0O00OO.close(), None)[1] for __g['OOOOOO00OO00O00OO'] in [(O00O0OO0O0OO00OO0.load(OO0000O0O0O0O00OO, O0O00OO00OO0OOOO0))]][0])[1] for __g['OO0000O0O0O0O00OO'] in [(QFile(OO0O0000OO00O00OO))]][0] for __g['O00O0OO0O0OO00OO0'] in [(QtUiTools.QUiLoader())]][0])(globals())
		return OOOOOO00OO00O00OO #line:189
	def moveButtonLeft (O00O00O0O000O0OO0 ):#line:191
		OO0OO000OOO0000OO =O00O00O0O000O0OO0 .button .pos ().x ()#line:192
		O00O00O0O000O0OO0 .button .move (OO0OO000OOO0000OO -1 ,20 )#line:193
	def moveButtonRight (OO0OOO0000OO0OOOO ):#line:195
		OOOO0OOO00O0OO0OO =OO0OOO0000OO0OOOO .button .pos ().x ()#line:196
		OO0OOO0000OO0OOOO .button .move (OOOO0OOO00O0OO0OO +1 ,20 )#line:197
def run ():#line:199
	IconFinder ()