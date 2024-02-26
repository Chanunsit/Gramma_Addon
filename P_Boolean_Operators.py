
import bpy

class Boolean_OP(bpy.types.Operator):
    bl_idname = "addon.boolean_operator"
    bl_label = "My Operator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.scene.bool_uv_sync:
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.context.area.ui_type = 'UV'
            bpy.context.scene.tool_settings.use_uv_select_sync = True
            bpy.context.area.ui_type = 'VIEW_3D' 
            print("UV Sync True")
        else:
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.context.area.ui_type = 'UV'
            bpy.context.scene.tool_settings.use_uv_select_sync = False
            bpy.context.area.ui_type = 'VIEW_3D'
            print("UV Sync False")
        return {'FINISHED'}

classes = [Boolean_OP]

def register():
 
    for cls in classes:
        bpy.utils.register_class(cls)
      

def unregister():
    
    for cls in classes:
        bpy.utils.unregister_class(cls)    

