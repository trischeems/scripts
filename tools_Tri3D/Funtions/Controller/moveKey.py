import maya.cmds as cmds



'''
main
'''
def useSEK(*arg):
    qUse= cmds.checkBox('UseSEK', q= 1, v= 1)
    if qUse:
        cmds.textField('startKey', e= 1, ed= 1, tx= int(cmds.currentTime(q= 1)))
        cmds.textField('endKey', e= 1, ed= 1, tx= int(cmds.playbackOptions(q= 1, aet= 1)))
    else:
        cmds.textField('startKey', e= 1, ed= 0, tx= '')
        cmds.textField('endKey', e= 1, ed= 0, tx= '')  

def selectCtrl(*arg):
    getSl= cmds.ls(sl= 1)
    qNameTx= ''
    qSelectAll= cmds.textField('selectAll', q= 1, tx= 1)
    
    if not getSl:
        cmds.textField('selectCtrl', e= 1, tx= '')
    else:
        cmds.textField('selectCtrl', e= 1, tx= '')
        cmds.textField('selectAll', e= 1, tx= '')
        for i in getSl:
            qNameTx= cmds.textField('selectCtrl', q= 1, tx= 1)
            cmds.textField('selectCtrl', e= 1, tx= qNameTx + ' ' + i)

def selectAll(*arg):
    if cmds.textField('selectAll', q= 1, tx= 1):
        cmds.textField('selectAll', e= 1, tx= '')
    else:
        cmds.textField('selectCtrl', e= 1, tx= '')
        getAnicmdsurve= cmds.ls(type= 'anicmdsurve')
        cmds.select(getAnicmdsurve, r= 1)
        cmds.textField('selectAll', e= 1, tx= 'Selected All Anim')
    
def butt_startKey(*arg):
    qUse= cmds.checkBox('UseSEK', q= 1, v= 1)
    if qUse:
        qCTime= cmds.currentTime(q= 1)
        cmds.textField('startKey', e= 1, tx= int(qCTime))

def butt_endKey(*arg):
    qUse= cmds.checkBox('UseSEK', q= 1, v= 1)
    if qUse:
        qCTime= cmds.currentTime(q= 1)
        cmds.textField('endKey', e= 1, tx= int(qCTime))

def butt_moveForward(*arg):
    getSK= cmds.textField('startKey', q= 1, tx= 1)
    getEK= cmds.textField('endKey', q= 1, tx= 1)
    getNK= cmds.intSliderGrp('numbersKey', q= 1, v= 1)
    qUse= cmds.checkBox('UseSEK', q= 1, v= 1)
    
    if not qUse:
        if (cmds.textField('selectAll', q= 1, tx= 1) == '') and (cmds.textField('selectCtrl', q= 1, tx= 1) == '' ):
            raise RuntimeError('You must select Ctrl !!!')
            
        elif cmds.textField('selectAll', q= 1, tx= 1):
            qCTime= cmds.currentTime(q= 1)
            getAnicmdsurve= cmds.ls(type= 'anicmdsurve')
            cmds.select(getAnicmdsurve)
            for i in getAnicmdsurve:
                cmds.keyframe(i, e=1, relative= 1, t= (qCTime,999999), tc= getNK)
        else:
            qCTime= cmds.currentTime(q= 1)
            getName= cmds.textField('selectCtrl', q= 1, tx= 1)
            splitName= getName.split()
        
            for i in splitName:
                cmds.keyframe(i, e=1, relative= 1, t= (qCTime,999999), tc= getNK)
    
    else:
        if (cmds.textField('selectAll', q= 1, tx= 1) == '') and (cmds.textField('selectCtrl', q= 1, tx= 1) == '' ):
            print 'Select Ctrl, please!!!'
        
        elif cmds.textField('selectAll', q= 1, tx= 1):
            print 'elif'
            getAnicmdsurve= cmds.ls(type= 'anicmdsurve')
            cmds.select(getAnicmdsurve)
            for i in getAnicmdsurve:
                cmds.keyframe(i, e=1, relative= 1, t= (getSK,getEK), tc= getNK)
            #cmds.textField('startKey', e= 1, tx= float(getSK) + float(getNK))
            cmds.textField('endKey', e= 1, tx= float(getEK) + float(getNK))
        else:
            qCTime= cmds.currentTime(q= 1)
            getName= cmds.textField('selectCtrl', q= 1, tx= 1)
            splitName= getName.split()
        
            for i in splitName:
                cmds.keyframe(i, e=1, relative= 1, t= (getSK,getEK), tc= getNK)
            #cmds.textField('startKey', e= 1, tx= float(getSK) + float(getNK))
            cmds.textField('endKey', e= 1, tx= float(getEK) + float(getNK))

def butt_moveBackward(*arg):
    getSK= cmds.textField('startKey', q= 1, tx= 1)
    getEK= cmds.textField('endKey', q= 1, tx= 1)
    getNK= cmds.intSliderGrp('numbersKey', q= 1, v= 1)
    qUse= cmds.checkBox('UseSEK', q= 1, v= 1)
    
    if not qUse:
        if (cmds.textField('selectAll', q= 1, tx= 1) == '') and (cmds.textField('selectCtrl', q= 1, tx= 1) == '' ):
            raise RuntimeError('You must select Ctrl !!!')
            
        elif cmds.textField('selectAll', q= 1, tx= 1):
            qCTime= cmds.currentTime(q= 1)
            getAnicmdsurve= cmds.ls(type= 'anicmdsurve')
            cmds.select(getAnicmdsurve)
            for i in getAnicmdsurve:
                cmds.keyframe(i, e=1, relative= 1, t= (qCTime,999999), tc= - getNK)
        else:
            qCTime= cmds.currentTime(q= 1)
            getName= cmds.textField('selectCtrl', q= 1, tx= 1)
            splitName= getName.split()
        
            for i in splitName:
                cmds.keyframe(i, e=1, relative= 1, t= (qCTime,999999), tc= - getNK)
    
    else:
        if (cmds.textField('selectAll', q= 1, tx= 1) == '') and (cmds.textField('selectCtrl', q= 1, tx= 1) == '' ):
            print 'Select Ctrl, please!!!'
            
        elif cmds.textField('selectAll', q= 1, tx= 1):
            getAnicmdsurve= cmds.ls(type= 'anicmdsurve')
            cmds.select(getAnicmdsurve)
            for i in getAnicmdsurve:
                cmds.keyframe(i, e=1, relative= 1, t= (getSK,getEK), tc= - getNK)
            #cmds.textField('startKey', e= 1, tx= float(getSK) - float(getNK))
            cmds.textField('endKey', e= 1, tx= float(getEK) - float(getNK))
        
        else:
            getName= cmds.textField('selectCtrl', q= 1, tx= 1)
            splitName= getName.split()
            for i in splitName:
                print i
                cmds.keyframe(i, e=1, relative= 1, t= (getSK,getEK), tc= - getNK)
        
            #cmds.textField('startKey', e= 1, tx= float(getSK) - float(getNK))
            cmds.textField('endKey', e= 1, tx= float(getEK) - float(getNK))
            
if cmds.window('moveKey', exists= 1):
    cmds.deleteUI('moveKey')
cmds.window('moveKey', sizeable= 1, resizeToFitChildren= 1)
moveKeyWd= cmds.window('moveKey', e= 1, t= 'Move Key Pro')
cmds.windowPref('moveKey', remove=True)

cmds.columnLayout("Main_Layout", w=300, adj= 1)
cmds.rowColumnLayout("Move_Pro", w=300, nc=4)
cmds.button(l= 'Select', c= selectCtrl, w=50)
cmds.textField('selectCtrl', w= 250, ed= 0, placeholderText="Select_Ctrl")
#cmds.button(l= 'Select', c= selectAll, w=50)
#cmds.textField('selectAll', w= 100, ed= 0, placeholderText="Select_Ctrl")

cmds.setParent("Main_Layout")
cmds.rowColumnLayout("Button2", w=300, nc=4)
cmds.button(l= 'Start Key', c= butt_startKey, w=50)
cmds.textField('startKey', w= 100, ed= 0, tx= '')
cmds.button(l= 'End Key', c= butt_endKey, w=50)
cmds.textField('endKey', w= 100, ed= 0, tx= '')
cmds.setParent("Main_Layout")
cmds.checkBox('UseSEK', l= 'Use Start-End Key', v= 0, cc= useSEK)
cmds.intSliderGrp('numbersKey', f= 1, min= 1, v= 1, max= 999999)
cmds.setParent("Main_Layout")
cmds.rowColumnLayout("button select", w=300, nc=2)
cmds.button('moveForward', l= '<<< Move Back', c=butt_moveForward, w=150)
cmds.button('moveBackward', l= 'Move Go >>>', c= butt_moveBackward, w=150)



#cmds.showWindow(moveKeyWd)