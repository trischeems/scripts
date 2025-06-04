import os
import maya.cmds as cmds
def read_bin_and_save():
    key = 123
    current_dir = os.path.dirname('/Users/tri3d/scripts/tri3dTools/Source/License/reEcn.py')
    filepath = os.path.join(current_dir, 'data.bin')
    with open(filepath, 'rb') as f:
        data = f.read()
    #decrypted = ''.join([chr(ord(c) ^ key) for c in data])
    decrypted = ''.join([chr(int(c) ^ key) for c in list(data)])
    cmds.optionVar(sv=('decryptedMessage', decrypted))
read_bin_and_save() 