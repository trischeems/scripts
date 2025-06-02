import os
import maya.cmds as cmds
def read_bin_and_save():
    key = 123
    current_dir = os.path.dirname('C:/Users/rigging/Documents/maya/2019/scripts/tri3dTools/Source/License/reEcn.py')
    filepath = os.path.join(current_dir, 'data.bin')
    with open(filepath, 'rb') as f:
        data = f.read()
    decrypted = ''.join([chr(ord(c) ^ key) for c in data])
    cmds.optionVar(sv=('decryptedMessage', decrypted))
read_bin_and_save() 