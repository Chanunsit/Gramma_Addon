import bpy
import os
from bpy.types import ( PropertyGroup, )
from bpy.props import (PointerProperty, StringProperty)
from . import P_Funtion
from . import P_Property


class MyProperties(PropertyGroup):
    saveList : StringProperty(name="Save List")

class UV_Editor(bpy.types.Operator):
    bl_idname = "uv.panda_operator"
    bl_label = "My Operator"
    bl_options = {"REGISTER", "UNDO"}
    action : StringProperty(name="action")

    def execute(self, context):
        if self.action == "@_SmartUnwrap": 
            self.SmartUnwrap(self, context)
        elif self.action == "@_Unwrapmaster": 
            self.Unwrapmaster(self, context)
        elif self.action == "@_RotateUV90": 
            self.RotateUV90(self, context)
        elif self.action == "@_AlignEdgeUV": 
            self.AlignEdgeUV(self, context)
        elif self.action == "@_PackUV_Together": 
            self.PackUV_Together(self, context)
        elif self.action == "@_Texel_value_increase": 
            self.Texel_value_increase(self, context)
        elif self.action == "@_Texel_value_reduce": 
            self.Texel_value_reduce(self, context)
        elif self.action == "@_Picked_texel": 
            self.Picked_texel(self, context)
        elif self.action == "@_Apply_texel": 
            self.Apply_texel(self, context)

        elif self.action == "@_Seam_from_island": 
            self.Seam_from_island(self, context)
        elif self.action == "@_Checker": 
            self.Assign_Checker(self, context)
        elif self.action == "@_Increase_tiling": 
            self.Increase_tiling(self, context)
        elif self.action == "@_reduce_tiling": 
            self.reduce_tiling(self, context)
        elif self.action == "@_reset_tiling": 
            self.reset_tiling(self, context)
        elif self.action == "@_Rectify_Textool": 
            self.rectify_textool(self, context)
        else:
             print("")

        return {'FINISHED'}
    
    @staticmethod
    def rectify_textool(self, context):
        if context.scene.tool_settings.use_uv_select_sync:
            bpy.ops.uv.select_linked()
            bpy.context.scene.tool_settings.use_uv_select_sync = False
            bpy.ops.uv.textools_rectify()
            bpy.context.scene.tool_settings.use_uv_select_sync = True
        else:
            bpy.ops.uv.select_linked()
            bpy.ops.uv.textools_rectify()
            
        print("Rectify")
        return {'FINISHED'}
    
    @staticmethod   
    def Assign_Checker(self, context):
        selected_texture = context.scene.Panda_Tools.selected_texture
        textures_path = os.path.join(os.path.dirname(__file__), "P_Texture")
        # Get the active object's material or create a new one
        active_object = context.active_object
        if active_object:
            if not active_object.data.materials:
                new_material = bpy.data.materials.new(name="New Material")
                active_object.data.materials.append(new_material)
                material = new_material
                bpy.context.object.active_material.use_nodes = True
            else:
                material = active_object.active_material
                

            if material:
               
                image_name = selected_texture + ".png"
                texture_node = None

                # Check if the image texture node with the same name exists
                for node in material.node_tree.nodes:
                    if node.type == 'TEX_IMAGE' and node.image.name == image_name:
                        texture_node = node
                        break

                if not texture_node:
                    # If the image texture node doesn't exist, create one
                    texture_node = material.node_tree.nodes.new(type='ShaderNodeTexImage')
                    texture_node.location = (0, 0)
                    texture_path = os.path.join(textures_path, image_name)
                    new_image = bpy.data.images.load(filepath=texture_path)
                    texture_node.image = new_image
                    
                # Check if Mapping node already exists
                mapping_node = material.node_tree.nodes.get("Mapping")
                if not mapping_node:
                    mapping_node = material.node_tree.nodes.new(type='ShaderNodeMapping')
                    mapping_node.location = (-400, 0)

                # Check if Texture Coordinate node already exists
                texture_coord_node = material.node_tree.nodes.get("Texture Coordinate")
                if not texture_coord_node:
                    texture_coord_node = material.node_tree.nodes.new(type='ShaderNodeTexCoord')
                    texture_coord_node.location = (-600, 0)

                # Connect Texture Coordinate to Mapping, Mapping to Image Texture
                material.node_tree.links.new(texture_coord_node.outputs["UV"], mapping_node.inputs["Vector"])
                material.node_tree.links.new(mapping_node.outputs["Vector"], texture_node.inputs["Vector"])

                # Connect the image texture node to the base color input
                principled_node = material.node_tree.nodes.get("Principled BSDF")
                if principled_node:
                    material.node_tree.links.new(texture_node.outputs["Color"], principled_node.inputs["Base Color"])
        print("Assign Checker")
        return {'FINISHED'}
   

    @staticmethod
    def Increase_tiling(self, context):
        active_object = context.active_object
        if active_object and active_object.active_material:
            material = active_object.active_material
            mapping_node = material.node_tree.nodes.get("Mapping")
            if mapping_node:
                mapping_node.inputs[3].default_value[0] *= 2
                mapping_node.inputs[3].default_value[1] *= 2
        print("Increase tiling")
        return {'FINISHED'}
    
    @staticmethod
    def reduce_tiling(self, context):
        active_object = context.active_object
        if active_object and active_object.active_material:
            material = active_object.active_material
            mapping_node = material.node_tree.nodes.get("Mapping")
            if mapping_node:
                mapping_node.inputs[3].default_value[0] *= 0.5
                mapping_node.inputs[3].default_value[1] *= 0.5
        print("reduce_tiling")
        return {'FINISHED'}
    @staticmethod
    def reset_tiling(self, context):
        active_object = context.active_object
        if active_object and active_object.active_material:
            material = active_object.active_material
            mapping_node = material.node_tree.nodes.get("Mapping")
            if mapping_node:
                mapping_node.inputs[3].default_value[0] = 1
                mapping_node.inputs[3].default_value[1] = 1
        print("Increase tiling")
        return {'FINISHED'}
    @staticmethod
    def SmartUnwrap(self, context):
        scene = context.scene
        value_magin = context.scene.Panda_Tools.Magin
        
        if context.scene.Panda_Tools.uv_keep_position:
            bpy.ops.uv.snap_cursor(target='SELECTED')
        if context.scene.Panda_Tools.pack_by_linked:
            bpy.ops.mesh.select_linked(delimit={'NORMAL'})
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=value_magin)
        bpy.ops.uv.align_rotation(method='GEOMETRY', axis='Z')
        bpy.ops.uv.align_rotation(method='AUTO')
        if context.scene.Panda_Tools.texel_set:
            P_Funtion.settexel_textool(self, context)     
        bpy.ops.uv.snap_selected(target='CURSOR_OFFSET')  
        bpy.ops.uv.snap_cursor(target='ORIGIN')
        
        
        print("Unwraped")
        return {'FINISHED'}
    
    @staticmethod
    def RotateUV90(self, context):
        scene = context.scene
        if context.scene.Panda_Tools.pack_by_linked:
            bpy.ops.mesh.select_linked(delimit={'NORMAL'}) 
        bpy.ops.transform.rotate(value=1.5708, orient_axis='Z')
        print("Rotated UV 90")
        return {'FINISHED'}
    
    @staticmethod
    def AlignEdgeUV(self, context):
        scene = context.scene
        if context.scene.tool_settings.use_uv_select_sync:
            # bpy.ops.uv.select_linked_pick(extend=True)
            # bpy.ops.uv.select_linked_pick(extend=True, deselect=False, location=(0, 0))
            bpy.ops.uv.select_all(action='SELECT')
            bpy.context.scene.tool_settings.use_uv_select_sync = False
             
        else:

            bpy.ops.uv.align_rotation(method='EDGE')
        
        print("AlignEdgeUV")
        return {'FINISHED'}
    
    @staticmethod
    def PackUV_Together(self, context):
        scene = context.scene
        value_magin = context.scene.Panda_Tools.Magin
        if context.scene.Panda_Tools.uv_keep_position:
            bpy.ops.uv.snap_cursor(target='SELECTED')
            
        if context.scene.Panda_Tools.pack_by_linked:
            bpy.ops.mesh.select_linked(delimit={'NORMAL'})

        bpy.ops.uv.pack_islands(udim_source='ACTIVE_UDIM', rotate=False, margin_method='SCALED', margin=value_magin)
        
        if context.scene.Panda_Tools.texel_set:
            
            P_Funtion.settexel_textool(self, context)
        if context.scene.Panda_Tools.uv_keep_position:   
            bpy.ops.uv.snap_selected(target='CURSOR_OFFSET')  
        bpy.ops.uv.snap_cursor(target='ORIGIN')
        # bpy.ops.image.view_selected()
        
        print("Packed")
        return {'FINISHED'}

    @staticmethod
    def Texel_value_increase(self, context):
        
        scene = context.scene
        Panda_Property = scene.Panda_Tools
        texel = int (Panda_Property.uv_texel_value) 
        if texel < 4096:
            texel *= 2
        Panda_Property.uv_texel_value = str (texel)

        print("Texel value X2")
        return {'FINISHED'}
    @staticmethod
    def Texel_value_reduce(self, context):
        
        scene = context.scene
        Panda_Property = scene.Panda_Tools
        texel = int (Panda_Property.uv_texel_value) 
        if texel > 1:
            texel //= 2
        Panda_Property.uv_texel_value = str (texel)
        
        print("Texel value /2")
        return {'FINISHED'}
    
    @staticmethod
    def Picked_texel(self, context):
        scene = context.scene 
        bpy.ops.uv.textools_texel_density_get()
        texel= str(scene.texToolsSettings.texel_density)
        texel= texel.split(".")
        texel= str(texel[0])
        print(texel) 
        context.scene.Panda_Tools.uv_texel_value = texel

        # print(len(str(scene.texToolsSettings.texel_density)))
        print("Picked texel")
        return {'FINISHED'}
    
    @staticmethod
    def Apply_texel(self, context):
        scene = context.scene 
        my_texel=  context.scene.Panda_Tools.uv_texel_value
        bpy.context.scene.texToolsSettings.texel_density = float(my_texel)
        bpy.context.scene.texToolsSettings.texel_get_mode = '1024'
        bpy.ops.uv.textools_texel_density_set()
        print("Apply texel")
        return {'FINISHED'}
    
    @staticmethod
    def Seam_from_island(self, context):
        scene = context.scene
        bpy.ops.uv.seams_from_islands()

        print("seams from islands")
        return {'FINISHED'}



def register():
    
    bpy.utils.register_class(UV_Editor)
    bpy.utils.register_class(MyProperties)
def unregister():
    bpy.utils.unregister_class(UV_Editor)
    bpy.utils.unregister_class(MyProperties)

if __name__ == "__main__":
    register()