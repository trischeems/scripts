import maya.cmds as cmds


################ move model to vertex ########
def button1_select_obj(*args):
    selected_mesh = cmds.ls(selection=True, type='transform')
    if selected_mesh:
        cmds.textField("move_obj_to_vertex", edit=True, text=selected_mesh[0])
    else:
        cmds.textField("move_obj_to_vertex", edit=True, text='')

def button2_move_obj(*args):
    target_vertex = cmds.ls(selection=True, flatten=True)
    if not target_vertex:
        cmds.warning("Select vertex .")
        return

    source_mesh_name = cmds.textField("move_obj_to_vertex", query=True, text=True)
    if not source_mesh_name:
        cmds.warning("Select mesh.")
        return

    duplicate_mesh = cmds.duplicate(source_mesh_name)[0]
    position = cmds.pointPosition(target_vertex[0], world=True)
    cmds.move(position[0], position[1], position[2], duplicate_mesh)
    if button2_move_obj:
        cmds.textField("move_obj_to_vertex_comp", edit=True, text="Move !")



