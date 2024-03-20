import bpy
import os
import bpy.utils.previews
from . import P_View3D_Operators
from . import P_UvEditor_Operators
from . import P_Website_Operators

from . import P_icons

from bpy.types import Menu, Operator, Panel, AddonPreferences, PropertyGroup


class VIEW3D_PT_Panda(bpy.types.Panel):  
    # bl_idname = "VIEW3D_PT_tool"
    bl_label = ""
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = '🐼'
    # bl_options = {"DEFAULT_CLOSED"}
    def draw_header(self, context):
        scene = context.scene
        layout = self.layout
        Panda_Property = scene.Panda_Tools
        row = layout.row()
        if Panda_Property.option_menu_ui == "A":
            layout.label(text="Modifire", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)
        elif Panda_Property.option_menu_ui == "B":
            layout.label(text="UV Editor", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)
        elif Panda_Property.option_menu_ui == "C":  
            layout.label(text="Collider", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)
        elif Panda_Property.option_menu_ui == "D":  
            layout.label(text="Object", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)
        elif Panda_Property.option_menu_ui == "E":  
            layout.label(text="Internet", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)


    def draw(self, context):
        layout = self.layout
        scene = context.scene
        Panda_Property = scene.Panda_Tools
        row = layout.row()    
        row.prop(Panda_Property, "option_menu_ui",text="", expand=True)
        row.alert = True
        row.operator(P_Website_Operators.OpenWebsiteOperator.bl_idname, text="LogWork").action="@_Logwork"

        if Panda_Property.option_menu_ui == "A":
            row = layout.row()
            box = layout.box()
            row = box.row() 
            row.label(text=":  Option ", icon_value=P_icons.custom_icons["custom_icon_6"].icon_id)
            
            
            if Panda_Property.option_on_off:
                row.prop(Panda_Property, "option_on_off", text="",icon="TRIA_DOWN")
                row = box.row() 
                row.prop(context.scene.tool_settings, "use_transform_correct_face_attributes", text="UV face")
                if bpy.context.scene.tool_settings.use_transform_correct_face_attributes == True:
                    row.prop(context.scene.tool_settings, "use_transform_correct_keep_connected", text="Connect")
                # row.label(text="Overay")
                row = box.row() 
                row.prop(context.space_data.overlay, "show_face_orientation", text="Backface")
                row.prop(context.space_data.overlay, "show_wireframes", text="Wireframes")
                row = box.row() 
                row.prop(context.space_data.overlay, "show_edge_seams", text="Seams")
                row.prop(context.space_data.overlay, "show_edge_sharp", text="Sharp")
                row = box.row()
                row.prop(context.space_data.overlay, "show_extra_edge_length", text="Edge length")

                row = layout.row()
            else:
                row.prop(Panda_Property, "option_on_off", text="",icon="TRIA_RIGHT")
            
            box = layout.box()
            row = box.row()
            row.label(text=": Tools", icon_value=P_icons.custom_icons["custom_icon_3"].icon_id)
            row = box.row()
            row.prop(context.scene.tool_settings, "use_transform_data_origin", text="Set Origin", icon="OBJECT_ORIGIN")
            row = box.row()
            row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Transfrom").action="@_AppAllTrasfrom"
            row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Orient").action="@_Get_Orientation"
            row = box.row()
            row.operator(P_View3D_Operators.Empty_area.bl_idname, text="Empty", icon="EMPTY_AXIS").action="@_Add_Empty"        
            row = layout.row()

            box = layout.box()
            row = box.row()
            if Panda_Property.option_trasfrom_xyz == "Rotate":
                row.label(text="", icon_value=P_icons.custom_icons["custom_icon_8"].icon_id)
            else:
                row.label(text="", icon_value=P_icons.custom_icons["custom_icon_11"].icon_id)
            row.prop(Panda_Property, "option_trasfrom_xyz",text="list", expand=True)
            row = box.row()
            
            if Panda_Property.option_trasfrom_xyz == "Rotate":
                row.label(text=" Angle:")
                row.prop(Panda_Property, "my_rotation_angle", text="")
                row = box.row()
                row.operator(P_View3D_Operators.Speed_process.bl_idname, text="X").action="@_RotateX"
                row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Y").action="@_RotateY"
                row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Z").action="@_RotateZ"    
           
            if Panda_Property.option_trasfrom_xyz == "Scale":
                row.label(text=" scale:")
                row.prop(Panda_Property, "my_scale_value", text="")
                row = box.row()
                row.operator(P_View3D_Operators.Speed_process.bl_idname, text="X").action="@_RotateX"
                row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Y").action="@_RotateY"
                row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Z").action="@_RotateZ"    
                row.operator(P_View3D_Operators.Speed_process.bl_idname, text="XYZ").action="@_ScaleXYZ" 

            box = layout.box()
            row = box.row() 
            row.label(text="", icon_value=P_icons.custom_icons["custom_icon_12"].icon_id)
            # row.label(text=": Bevel")
            # row = box.row()
            row.prop(Panda_Property, "bevle_shape", text="Shape")
            row = box.row()
            if Panda_Property.bevle_shape:
                row.prop(Panda_Property, "bevel_offset_input_shape", text="")
                row.prop(Panda_Property, "bevel_segments_input_shape", text="")
            else:
                row.prop(Panda_Property, "bevel_offset_input_smooth", text="")
                row.prop(Panda_Property, "bevel_segments_input_smooth", text="")
            row = box.row()
            row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Bevel").action="@_Bevel_Custom" 

            box = layout.box()
            row = box.row()
            row.label(text="Loop Manager") 
            row = box.row()
            row.label(text="Edge gap") 
            row.prop(Panda_Property, "Gap_loop", text="")
            row = box.row()
            row.prop(Panda_Property, "Loop_edge", text="Loop")
            row.prop(Panda_Property, "remove_edge", text="Del edge")
            row = box.row()
            row.operator(P_View3D_Operators.Speed_process.bl_idname, text="Optimize Loop").action="@_Loop_manager" 

        
        if Panda_Property.option_menu_ui == "B":
            row = layout.row()
            box = layout.box()
            row = box.row(align=True)

            row.label(text="", icon_value=P_icons.custom_icons["custom_icon_13"].icon_id)
            row.prop(Panda_Property, "selected_texture", text="")
            row.scale_x=0.5
            row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="Assign").action="@_Checker"
            row.scale_x=1
            row = box.row(align=True)
            row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="-").action="@_Increase_tiling"
            row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="1").action="@_reset_tiling"
            row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="+").action="@_reduce_tiling"
            row = layout.row()
            # row = layout.row(align=True)
            box = layout.box()
            row = box.row()
            
            row.label(text="Map:", icon_value=P_icons.custom_icons["custom_icon_10"].icon_id)
            row.operator(P_View3D_Operators.Uv.bl_idname, text="",icon="TRIA_LEFT").action="@_View_uv1"
            
            
            active_object = context.active_object
            if active_object and active_object.type == 'MESH':
                
                row.alignment = 'CENTER'
                active_index = active_object.data.uv_layers.active_index + 1
                row.label(text=str(active_index))
                # row.label(text="",icon="TRIA_LEFT")
                row.scale_x=1  

            row.operator(P_View3D_Operators.Uv.bl_idname, text="",icon="TRIA_RIGHT").action="@_View_uv2"
            
            if Panda_Property.show_option_uvmap: 
                row.prop(Panda_Property, "show_option_uvmap", text="",icon="ANIM_DATA")
            else:
                row.prop(Panda_Property, "show_option_uvmap", text="",icon="COLLAPSEMENU")

            
            if Panda_Property.show_option_uvmap: 
                row = box.row(align=True)
                row.operator(P_View3D_Operators.Uv.bl_idname, text="Set name").action="@_Set_name_uv_chanel"
                row.operator(P_View3D_Operators.Uv.bl_idname, text="Del >2").action="@_remove_uv_chanel"
                
            box = layout.box()
            row = box.row() 
            row.scale_x=1.2
            row.label(text="", icon_value=P_icons.custom_icons["custom_icon_4"].icon_id)
            row.scale_x=1
            row.prop(Panda_Property, "live_uv", text="LiveUV")
            row.operator(P_View3D_Operators.Uv.bl_idname, text="",icon= "WINDOW").action="@_OpenUVEditWindow"
            row = box.row()
            
            row.prop(Panda_Property, "pack_by_linked", text="Linked")
            row.prop(Panda_Property, "uv_keep_position", text="Location")
            row = box.row(align=True)
            row.prop(Panda_Property, "texel_set", text="Texel")

            if Panda_Property.texel_set:
                
                # row = box.row(align=True)
                # row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="",icon="EYEDROPPER").action="@_Picked_texel" 
                row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="",icon="REMOVE").action="@_Texel_value_reduce" 
                row.scale_x=0.5
                row.prop(Panda_Property, "uv_texel_value")
                row.scale_x=0.9
                row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="",icon= "ADD").action="@_Texel_value_increase" 
                # row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="Apply").action="@_Apply_texel" 
            
            row = box.row()
            
            row.prop(context.scene.tool_settings, "use_uv_select_sync", text="Spync")
            row.prop(Panda_Property, "follow_next_face", text="Follow",icon="TRACKING")
            row = box.row()
            row.scale_y=1.5
            col1 = row.column(align=True)
            col1.operator(P_View3D_Operators.Uv.bl_idname, text="Group ").action="@_Vertex_group"
            col1.operator(P_View3D_Operators.Uv.bl_idname, text="Select").action="@_Select_group"
            col1.operator(P_View3D_Operators.Uv.bl_idname, text="Clear").action="@_Clear_group"
            # col1.operator(P_View3D_Operators.Uv.bl_idname, text="Smart UV",icon = "ERROR" ).action="@_smart_unwrap"
           
            if Panda_Property.live_uv == False:
               
                col1.operator(P_View3D_Operators.Uv.bl_idname, text="Unwrap").action="@_UV_quick" 
            col2 = row.column(align=True)
            if Panda_Property.live_uv: 
                col2.alert = True
            col2.operator(P_View3D_Operators.Uv.bl_idname, text="Make").action="@_MakeSeam"
            col2.operator(P_View3D_Operators.Uv.bl_idname, text="Clear").action="@_ClearSeam"
            col2.alert = False
            if Panda_Property.follow_next_face:
                col2.alert = True 
            col2.operator(P_View3D_Operators.Uv.bl_idname, text="Hide").action="@_Hide_Select"
            
            
            
                
            row = box.row(align=True) 
            row.operator(P_View3D_Operators.Uv.bl_idname, text="Shap").action="@_Shap_to_Seam"
            row.operator(P_View3D_Operators.Uv.bl_idname, text="Island").action="@_Island_to_Seam"
            
            
            
            box = layout.box()
            row = box.row() 
            row.label(text="Pack", icon_value=P_icons.custom_icons["custom_icon_5"].icon_id)
            row.prop(Panda_Property, "pack_by_part", text="By Part")
            
            if Panda_Property.pack_by_part:
                row = box.row(align=True) 
                col2 = row.column(align=True)   
                
                col2.label(text="Small")  
                col2.prop(Panda_Property, "pack_uv_margin_less", text="")  

                col2 = row.column(align=True)
                col2.label(text="size/ M")  
                col2.prop(Panda_Property, "Size_object", text="") 

                col2 = row.column(align=True)
                col2.label(text="Big") 
                col2.prop(Panda_Property, "pack_uv_margin_more", text= "")
            
            row = box.row() 
            row.operator(P_View3D_Operators.Uv.bl_idname, text="Pack!").action="@_Pack_UV"
            
            box = layout.box()
            row = box.row() 
            row.label(text="Edit", icon_value=P_icons.custom_icons["custom_icon_2"].icon_id)
            row = box.row() 
            row.operator(P_View3D_Operators.Uv.bl_idname, text="Rotate 90").action="@_RotateUV90"
            
        if Panda_Property.option_menu_ui == "C":
            row = layout.row()
            box = layout.box()
            row = box.row() 
            row.label(text=": Collider Builder", icon_value=P_icons.custom_icons["custom_icon_9"].icon_id)
            row = box.row()
            row.operator(P_View3D_Operators.Box_Builder.bl_idname, text="Make Box").action="@_MakeToBox"
            row = box.row()
            row.prop(Panda_Property, "auto_orient", text=": Auto Orient")
            row = box.row()
            row.prop(Panda_Property, "remove_reference", text=": Delete original")
            row = layout.row()
           
           
            box = layout.box()
            row = box.row()
            row.label(text=": Convert to Box", icon_value=P_icons.custom_icons["custom_icon_9"].icon_id)
            row = box.row()
            row.operator(P_View3D_Operators.Box_Builder.bl_idname, text="Shrinkwrap to Box").action="@_Optimize_to_box"
            # row = box.row()
            # row.operator(P_View3D_Operators.Box_Builder.bl_idname, text="Merge to 1 box").action="@_merge_to_1_box"
           
           
           
           
            # box = layout.box()
            # row = box.row()
            # row.label(text=": Not ready to use", icon_value=P_icons.custom_icons["custom_icon_3"].icon_id)
            # row = box.row()
            # row.operator(P_View3D_Operators.Box_Builder.bl_idname, text="Opposite Face").action="@_Opposite_Face"

           
            

        if Panda_Property.option_menu_ui == "D":
            row = layout.row()
            box = layout.box()
            row = box.row()
            row.label(text=": OBject preset", icon_value=P_icons.custom_icons["custom_icon_3"].icon_id)
            row = box.row() 
            row.operator(P_View3D_Operators.Ready_made.bl_idname, text="Hexagon").action="@_Hexagon"

            box = layout.box()
            row = box.row()
            row.prop(Panda_Property, "Face_index",text="Face")
            row.operator(P_View3D_Operators.Speed_process.bl_idname,text="", icon_value=P_icons.custom_icons["custom_icon_3"].icon_id).action="@_Find_face_index"
            row = box.row()
            row.prop(Panda_Property, "Edge_index",text="Edge")
            row.operator(P_View3D_Operators.Speed_process.bl_idname,text="", icon_value=P_icons.custom_icons["custom_icon_3"].icon_id).action="@_Find_edge_index"
            box = layout.box()
            row = box.row()
            row.label(text="Vertext Color")
            row.operator(P_View3D_Operators.Speed_process.bl_idname,text="Clear !", icon_value=P_icons.custom_icons["custom_icon_3"].icon_id).action="@_Clear_ColorVertext"
            row = box.row()
            row.label(text="Color Attributes")
            row.operator(P_View3D_Operators.Speed_process.bl_idname,text="Clear !", icon_value=P_icons.custom_icons["custom_icon_3"].icon_id).action="@_Clear_ColorAttribute"
            
            box = layout.box()
            row = box.row(align=True)
            row.prop(Panda_Property, "UV_chanel",text="")
            row.operator(P_View3D_Operators.Uv.bl_idname, text="Del UV").action="@_remove_uv_specify"

            box = layout.box()
            row = box.row()
            row.label(text="Set name")
            row = box.row()
            row.prop(Panda_Property, "naming_prifix",text="Pre")
            row = box.row()
            row.prop(Panda_Property, "naming_mid",text="Name")
            row.prop(Panda_Property, "counter_name_mid", text="")
            row = box.row()
            # row.prop(Panda_Property, "naming_number",text="Num")
            # row = box.row()
            row.prop(Panda_Property, "naming_suffix",text="Suf")
            row.prop(Panda_Property, "counter_name_suffix", text="")
            row = box.row()

            row.operator(P_View3D_Operators.Speed_process.bl_idname,text="Set !").action="@_Set_NameObject"

            box = layout.box()
            row = box.row()
            row.label(text="Drop Vertex color")
            row = box.row(align=True)
            row.operator(P_View3D_Operators.Speed_process.bl_idname,text="Black").action="@_Drop_Black_vertex"
            row.operator(P_View3D_Operators.Speed_process.bl_idname,text="Red").action="@_Drop_Red_vertex"
            row.operator(P_View3D_Operators.Speed_process.bl_idname,text="Green").action="@_Drop_Green_vertex"
            row.operator(P_View3D_Operators.Speed_process.bl_idname,text="Blue").action="@_Drop_Blue_vertex"

            box = layout.box()
            row = box.row()
            row.label(text="Bake Vertex color")
            row = box.row(align=True)
            row.operator(P_View3D_Operators.Speed_process.bl_idname,text="Bake").action="@_Add_bake_mat"

        if Panda_Property.option_menu_ui == "E": 
            # row.label(text="Web site")
            box = layout.box()
            row = box.row()
            row.label(text="Office", icon_value=P_icons.custom_icons["custom_icon_2"].icon_id)
            row = box.row()
            row.operator(P_Website_Operators.OpenWebsiteOperator.bl_idname, text="Jira DashBoard")
            row = box.row()
            row.operator(P_Website_Operators.OpenWebsiteOperator.bl_idname, text="WorkLogPro").action="@_WorkLogPro"
            row = box.row()
            row.operator(P_Website_Operators.OpenWebsiteOperator.bl_idname, text="BackOffice").action="@_BackOffice"
            row = layout.row()

             # Add a label
            layout.label(text="Web favorite")

            # Input for label and link
            layout.prop(context.scene, "website_label", text="Label")
            layout.prop(context.scene, "website_link", text="Link")
            row = layout.row()
            # Button to add website link
            row.operator("addon.add_website_link", text="Add Link")
            box = layout.box()
            
            # Display the list of added website links
            for idx, website_link in enumerate(context.scene.website_links):
                row = box.row()
                row.label(text=website_link.label)
                row.scale_x=0.15
                row.operator("addon.open_website_link", text="Go!").website_index = idx
                row.scale_x=1
                if Panda_Property.show_remove_link:
                    row.operator("addon.remove_website_link", text="",icon="TRASH").website_index = idx
                
            
            row = layout.row()
            row.prop(Panda_Property, "show_remove_link", text="Remove link")
        

class UV_PT_Panda(bpy.types.Panel):

    bl_label = ""
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_category = '🐼'
    def draw_header(self, context): 
        
        self.layout.label(text="UV Editor", icon_value=P_icons.custom_icons["custom_icon_1"].icon_id)
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        Panda_Property = scene.Panda_Tools
        row = layout.row()
        box = layout.box()
        row = box.row() 
        
        row.label(text="", icon_value=P_icons.custom_icons["custom_icon_7"].icon_id)
        
        row.prop(context.scene.tool_settings, "use_uv_select_sync", text="UV sync")
        row = box.row() 
        # row.label(text="Texel set :")
        row.prop(Panda_Property, "pack_by_linked", text="Linked")
        row.prop(Panda_Property, "uv_keep_position", text="Location")
        row = box.row()
        
        row.prop(Panda_Property, "texel_set", text="Texel Set")

        if Panda_Property.texel_set:
            row = box.row(align=True)
            row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="",icon="EYEDROPPER").action="@_Picked_texel" 
            row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="",icon="REMOVE").action="@_Texel_value_reduce" 
            row.prop(Panda_Property, "uv_texel_value")
            row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="",icon= "ADD").action="@_Texel_value_increase" 
            row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="Apply").action="@_Apply_texel" 
        row = box.row()
        row.prop(Panda_Property, "Magin", text="Margin")

        row = box.row()
        row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="Unwrap").action="@_SmartUnwrap"  
        row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="PackUV").action="@_PackUV_Together"
        row.scale_y = 1.64
        row = layout.row()
        box = layout.box()
        row = box.row()
        row.label(text=": UV Align ", icon_value=P_icons.custom_icons["custom_icon_8"].icon_id)
        row = box.row()
        row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="Rotate90°").action="@_RotateUV90"  
        row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="AlignEdge").action="@_AlignEdgeUV" 
        row = box.row()
        
        row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="Rectify").action="@_Rectify_Textool"
        row = box.row()
        row.operator(P_UvEditor_Operators.UV_Editor.bl_idname, text="Island").action="@_Seam_from_island"
        row = layout.row()

        # box = layout.box()
        # row = box.row()
        
        # # row.prop(Panda_Property, "uv_offset", text="Offset new pack")
        # row = layout.row()

classes = [VIEW3D_PT_Panda,UV_PT_Panda]

def register():

    
    for cls in classes:
        bpy.utils.register_class(cls)
      
def unregister():
      
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
