# import bpy.utils.previews
# import os

# custom_icons = None



# def register():
#     global custom_icons
#     custom_icons = bpy.utils.previews.new()
#     addon_path =  os.path.dirname(__file__)
#     icons_dir = os.path.join(addon_path, "icons")

#     custom_icons.load("custom_icon_1", os.path.join(icons_dir, "P_PandaFace.png"), 'IMAGE')
#     custom_icons.load("custom_icon_2", os.path.join(icons_dir, "P_PandaSleep.png"), 'IMAGE')
#     custom_icons.load("custom_icon_3", os.path.join(icons_dir, "P_PandaFeet.png"), 'IMAGE')
#     custom_icons.load("custom_icon_4", os.path.join(icons_dir, "P_MakeSeam.png"), 'IMAGE')
#     custom_icons.load("custom_icon_5", os.path.join(icons_dir, "P_Box.png"), 'IMAGE')
#     custom_icons.load("custom_icon_6", os.path.join(icons_dir, "P_Light.png"), 'IMAGE')
#     custom_icons.load("custom_icon_7", os.path.join(icons_dir, "P_UV.png"), 'IMAGE')
#     custom_icons.load("custom_icon_8", os.path.join(icons_dir, "P_Rotate.png"), 'IMAGE')
#     custom_icons.load("custom_icon_9", os.path.join(icons_dir, "P_Box_orange.png"), 'IMAGE')
#     custom_icons.load("custom_icon_10", os.path.join(icons_dir, "P_UV_Transfrom.png"), 'IMAGE')
#     custom_icons.load("custom_icon_11", os.path.join(icons_dir, "P_scale.png"), 'IMAGE')
#     custom_icons.load("custom_icon_12", os.path.join(icons_dir, "P_bevel.png"), 'IMAGE')
#     custom_icons.load("custom_icon_13", os.path.join(icons_dir, "P_Checker.png"), 'IMAGE')
# def unregister():
#     global custom_icons
#     bpy.utils.previews.remove(custom_icons)
import bpy
import os
from bpy.utils import previews

custom_icons = previews.new()
icon_path = os.path.join(os.path.dirname(__file__), "icons")
for entry in os.scandir(icon_path):
    if entry.name.endswith(".png"):
        name = os.path.splitext(entry.name)[0]
        custom_icons.load(name, os.path.join(icon_path, entry.name), 'IMAGE')

    