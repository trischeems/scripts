import maya.cmds as cmds
import maya.mel as mel
import os

mel_path = os.path.join(os.path.dirname(__file__), 'Mel')


################################################################
def AriCircleVertex(*arg): ##### AriCircleVertex
    mel_script_path = mel_path + "/AriCircleVertex.mel" ## line 10
    with open(mel_script_path, 'r') as mel_file:
        mel_script = mel_file.read() ## line
    mel.eval(mel_script)     ## line
    mel.eval('AriCircleVertex;') ## line
#&^*#$^%#(*&%^*%#(&*@#$(*Q^@$(Q&*@^#$))))
def AriPolygonCounter(*arg): ##### AriPolygonCounter
    mel_script_path = mel_path + "/AriPolygonCounter.mel"## line
    with open(mel_script_path, 'r') as mel_file: ## line
        mel_script = mel_file.read() ## line
    mel.eval(mel_script)    ## line####################
    mel.eval('AriPolygonCounter;')##
############################################
def AriSymmetryChecker(*arg):#@&^&*@#^@$^(@*$$@)
    mel_script_path = mel_path + "/AriSymmetryChecker.mel"
    with open(mel_script_path, 'r') as mel_file:
        mel_script = mel_file.read() ########################################
    mel.eval(mel_script)    ##############################
    mel.eval('AriSymmetryChecker;')    #######################
############################################
def AriUVFromVertexRatio(*arg):##@^*&%!@#*&%!&^#!
    mel_script_path = mel_path + "/AriUVFromVertexRatio.mel"
    with open(mel_script_path, 'r') as mel_file:
        mel_script = mel_file.read()
    mel.eval(mel_script)    ##&*%(*&^(*&#@^$#(@$)))
    mel.eval('AriUVFromVertexRatio;')     
##################################################
def AriViewWindow(*arg):####################
    mel_script_path = mel_path + "/AriViewWindow.mel"
    with open(mel_script_path, 'r') as mel_file:
        mel_script = mel_file.read()######################
    mel.eval(mel_script)    #################
    mel.eval('AriViewWindow;')     ##%*&^%(*$%&(*$%*&$%))
###########################################################
def AriTransferPosition(*arg):#################################
    mel_script_path = mel_path + "/AriTransferPosition.mel"
    with open(mel_script_path, 'r') as mel_file:############^#%($&^#*$*#)
        mel_script = mel_file.read()#################
    mel.eval(mel_script)   ####################### #^#%^#%^#&
    mel.eval('AriTransferPosition;')   ################234213423&#%#&*
#     mel.eval('AriUVFromVertexRatio;')     

# def AriViewWindow(*arg):
#     mel_script_path = mel_path + "/AriViewWindow.mel"
#     with open(mel_script_path, 'r') as mel_file:
#         mel_script = mel_file.read()
#     mel.eval(mel_script)    
#     mel.eval('AriViewWindow;')     

# def AriTransferPosition(*arg):
#     mel_script_path = mel_path + "/AriTransferPosition.mel"
#     with open(mel_script_path, 'r') as mel_file:
#         mel_script = mel_file.read()
#     mel.eval(mel_script)    #*$^&*$^&*($^*&$*&^())
#     mel.eval('AriTransferPosition;')   
    
def AriStraightVertex(*arg):#####################################
    mel_script_path = mel_path + "/AriStraightVertex.mel"
    with open(mel_script_path, 'r') as mel_file:#################23452345
        mel_script = mel_file.read()#######################23453245
    mel.eval(mel_script)    ###################################
    mel.eval('AriStraightVertex;')   ##########################43252345
    # with open(mel_script_path, 'r') as mel_file:523452345
    #     mel_script = mel_file.read()
    # mel.eval(mel_script)    ##################
    ###############################3425867320985762345
def DoraSkinWeightImpExp(*arg):#################################################
    mel_script_path = mel_path + "/DoraSkinWeightImpExp.mel"######################
    with open(mel_script_path, 'r') as mel_file:################################
        mel_script = mel_file.read()#########################################
    mel.eval(mel_script)    ##############################################
    mel.eval('DoraSkinWeightImpExp;') ##########################################
    #################################################################
def DoraSkinWeightImpExp(*arg):######################
    mel_script_path = mel_path + "/DoraSkinWeightImpExp.mel"##############
    with open(mel_script_path, 'r') as mel_file:
        mel_script = mel_file.read()#############$###############
    mel.eval(mel_script)    #$T89832453749503275
    mel.eval('DoraSkinWeightImpExp;') 
#3452345283904567-2309457230-94752323-09475320945782309-45

################################################################
def makeVrayAttributes(*arg):#3245234598723049587324095p3
    sel = cmds.ls(sl=True)
    currentID = True######%&^&#*$##$#453453452
    for i in sel:#####345234590823476509823475098234
        shapes = cmds.listRelatives(i,s=True,ni=True)
        if shapes:#&**&$^$^*&$&^*$^$
            for s in shapes:
                melCmd = "vray addAttributesFromGroup "+s+" vray_subdivision 1"
                mel.eval(melCmd)
        melCmd = "vray addAttributesFromGroup "+i+" vray_objectID 1"
        mel.eval(melCmd)
        cmds.setAttr(i+'.vrayObjectID',currentID)
        currentID += True
#$###*&%$^#*^&(^@&*(#^&*(@&^$*@&^%@)))
##########################################&#*&(*^&(^*&@*%&^@$(^&$@)))
def namespace(*arg):
    cmds.namespace(setNamespace=':')
    all_namespaces = [x for x in cmds.namespaceInfo(listOnlyNamespaces=True, recurse=True) if x != "UI" and x != "shared"]
    if all_namespaces:
        all_namespaces.sort(key=len, reverse=True)
        for namespace in all_namespaces:
            if cmds.namespace(exists=namespace) is True:
                cmds.namespace(removeNamespace=namespace, mergeNamespaceWithRoot=True)






