import bpy

from bpy.types import Scene
from bpy.types import (PropertyGroup)
from bpy.props import (EnumProperty, PointerProperty, StringProperty, FloatVectorProperty, FloatProperty, IntProperty, BoolProperty)

option_tap = {
    "A": {"icon": "MODIFIER", "label": "Modify"},
    "B": {"icon": "UV_FACESEL", "label": "UV edit"},
    "C": {"icon": "FILE_3D", "label": "Box builder"},
    "D": {"icon": "SHADERFX", "label": "Object"},
    "E": {"icon": "URL", "label": "Internet"},
    # "F": {"icon": "OUTLINER_OB_VOLUME", "label": "open appication on youre pc"} NEW!
}

transfrom_XYZ_List = {
    "Rotate": {"label": "Rotate"},
    "Scale": { "label": "Scale"},
    # "Move": { "label": "Move"}
}
find_size = [
   
    ("More then", "More",""),
    ("Less then", "Less","")
    
] 

texture_options = [
   
    ("Checker_A", "Checker_A",""),
    ("Checker_B", "Checker_B",""),
    ("Checker_C", "Checker_C",""),
    ("Checker_D", "Checker_D","")
] 

class MyProperties(PropertyGroup):
    option_menu_ui:EnumProperty(items=[(name, option_tap[name]["label"], "", option_tap[name]["icon"], i) for i, name in enumerate(option_tap.keys())])
    option_trasfrom_xyz:EnumProperty(items=[(name, transfrom_XYZ_List[name]["label"], "", i) for i, name in enumerate(transfrom_XYZ_List.keys())])
    uv_keep_position:bpy.props.BoolProperty(name="Uv keep position",default=False)
    texel_set:bpy.props.BoolProperty(name="texel_set",default=True)
    pack_by_part:bpy.props.BoolProperty(name="Pack by part",default=False)
    pack_by_linked:bpy.props.BoolProperty(name="Pack by Linked",default=False)
    live_uv:bpy.props.BoolProperty(name="Live UV",default=False)
    
    auto_orient:bpy.props.BoolProperty(name="Auto Orient",default=True)
    remove_reference:bpy.props.BoolProperty(name="Remove referent object")
    bevle_shape:bpy.props.BoolProperty(name="bevel Shape",default=False)
    show_remove_link:bpy.props.BoolProperty(name="Show remove link",default=False)
    option_on_off:bpy.props.BoolProperty(name="Show remove link",default=False)
# value
    UV_chanel:bpy.props.IntProperty(
        name="Uv Chanel",
        description="to specify UV index",
        default= 0,
        min=0,
        max=100,
    )

    Gap_loop:bpy.props.IntProperty(
        name="Gap loop",
        description="set distance gap loop",
        default= 1,
        min=1,
        max=10,
    )
    Loop_edge:bpy.props.BoolProperty(name="loop edge",default=False)
    remove_edge:bpy.props.BoolProperty(name="Remove Edge",default=False)
#  option
    show_option_uvmap:bpy.props.BoolProperty(name="UV map option",default=False)
    follow_next_face:bpy.props.BoolProperty(name="Follow next face after hide",default=False)
    counter_name_mid:bpy.props.BoolProperty(name="counter_number",default=False)
    counter_name_suffix:bpy.props.BoolProperty(name="counter_number",default=False)
    # uv_offset:bpy.props.BoolProperty(name="ofFset UV")
    Size_object:bpy.props.FloatProperty(
        name="Find size object in select",
        description="Input offset",
        default=1,
        min=0.0,
        max=10.0,
        precision=1,
        step = 10
    )
    pack_uv_margin_less :bpy.props.FloatProperty(
        name=" pack_uv_margin_less",
        description="uv margin",
        default=1,
        min=0.0,
        max=100.0,
        precision=1,
        step = 100
    )
    pack_uv_margin_more :bpy.props.FloatProperty(
        name="pack_uv_margin_More",
        description="uv margin",
        default=2,
        min=0.0,
        max=100.0,
        precision=1,
        step = 100
    )
    pack_uv_margin_colum :bpy.props.FloatProperty(
        name="pack_uv_margin_More",
        description="uv margin",
        default=2,
        min=0.0,
        max=100.0,
        precision=1,
    )
    my_rotation_angle:bpy.props.FloatProperty(
        name="My Rotation Angle",
        description="Input any number with a maximum value of 360",
        default=90.0,
        min=-360.0,
        max=360.0,
        step=4500,
    )
    my_scale_value:bpy.props.FloatProperty(
        name="My Scale value",
        description="Input value scale",
        default=1.0,
        min=-1.0,
        soft_max=10.0,
        precision=2,
        step=10,
    )
    bevel_offset_input_shape:bpy.props.FloatProperty(
        name="Bevel Offset Input Shape",
        description="Input offset",
        default=0.1,
        min=0.0,
        max=10.0,
        precision=3,
    )
    bevel_segments_input_shape:bpy.props.IntProperty(
        name="Bevel segments Input Shape",
        description="Input segments",
        default= 2,
        min=0,
        max=10,
    )
    
    Magin:bpy.props.FloatProperty(
        name="Bevel Offset Input Smooth",
        description="Input offset",
        default=0.02,
        min=0.00000,
        max=10.0000,
        precision=2,
        step=10,
    )
   
    bevel_segments_input_smooth:bpy.props.IntProperty(
        name="Bevel segments Input smooth",
        description="Input segments",
        default= 1,
        min=0,
        max=10,
    )
    
    bevel_offset_input_smooth:bpy.props.FloatProperty(
        name="Bevel Offset Input Smooth",
        description="Input offset",
        default=0.02,
        min=0.00000,
        max=10.0000,
        precision=3,
        step=0.5,
    )
    uv_texel_value:bpy.props.StringProperty(
        name="",
        description="Input valuse texel density",
        default= "512",
        maxlen= 6
        
        # min=1,
        # max=4096,
        # step=1,
        
    )
    Face_index:bpy.props.StringProperty(
        name="",
        description="specific face index",
        default= "1",
        maxlen= 8
    )
    Edge_index:bpy.props.StringProperty(
        name="",
        description="specific edge index",
        default= "1",
        maxlen= 8
    )
    
    selected_texture : EnumProperty(
        name="Tab",
        items = texture_options
    )
    
    find_size_object : EnumProperty(
        name="",
        items = find_size
    )
    
    naming_prifix:bpy.props.StringProperty(
    name="Naming object",
    description="specific face index",
    default= "",  
    )

    naming_mid:bpy.props.StringProperty(
        name="Naming object",
        description="specific face index",
        default= "",  
    )

    naming_number:bpy.props.StringProperty(
    name="Naming object",
    description="specific face index",
    default= "",  
    )

    naming_suffix:bpy.props.StringProperty(
    name="Naming object",
    description="specific face index",
    default= "",  
    )
    
classes = [MyProperties]
def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    Scene.Panda_Tools = PointerProperty(type= MyProperties)
   


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del Scene.Panda_Tools
