import maya.cmds as cmds

if cmds.window('moveKey', exists= 1):
    cmds.deleteUI('moveKey')
cmds.window('moveKey', sizeable= 1, resizeToFitChildren= 1)
moveKeyWd= cmds.window('moveKey', e= 1, t= 'Move Key')

cmds.columnLayout("Main_Layout", w=350)
cmds.rowColumnLayout("Button", w=350)
cmds.textField('selectCtrl', w= 100, ed= 0)
cmds.button(l= 'Select', c= 'selectCtrl()', w=50)