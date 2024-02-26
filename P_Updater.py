import bpy
import urllib.request
import os
import webbrowser
import zipfile
import shutil
from bpy.types import ( PropertyGroup, )
from bpy.props import (PointerProperty, StringProperty)
from. import P_Funtion

GITHUB_REPO_URL = "https://github.com/Chanunsit/Addon_Blender/releases/tag/Gramma"

class MyProperties(PropertyGroup):
    saveList : StringProperty(name="Save List")

class MyAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        # Add a button to perform an action
        # row.label(text="")
        row.operator("addon.perform_action", text="Update Addon").action="@_Update"
        row.operator("addon.perform_action", text="Releases_version").action="@_Releases"

# Define the operator to perform the action
class PerformActionOperator(bpy.types.Operator):
    bl_idname = "addon.perform_action"
    bl_label = "Show Message"
    action : StringProperty(name="action")

    def execute(self, context):
        if self.action == "@_Update":
            self.Update_Addon(self, context)

        elif self.action == "@_Releases": 
            self.Releases_version(self, context)
        else:
            print("")

        return {'FINISHED'}
    
    @staticmethod
    def Update_Addon(self, context):
        scene = context.scene
        self.report({'INFO'}, "Downlaoding Addon!")
        
        UPDATED_ADDON_URL = "https://github.com/Chanunsit/PandaTools/archive/refs/heads/main.zip"

        # Get the addon directory and the current addon file path
        addon_dir = os.path.dirname(os.path.realpath(__file__))
    
        # Download the updated addon zip file
        response = urllib.request.urlopen(UPDATED_ADDON_URL)
        data = response.read()

        # Save the updated addon zip file in the addon directory
        updated_addon_file = os.path.join(addon_dir, "PandaTools-main.zip")
        with open(updated_addon_file, "wb") as f:
            f.write(data)

        # Unzip the updated addon
        # with zipfile.ZipFile(updated_addon_file, 'r') as zip_ref:
        #     zip_ref.extractall(addon_dir)

        # Remove the downloaded zip file
        # os.remove(updated_addon_file)

        P_Funtion.copy_files_from_subfolder("PandaTools", "PandaTools-main")
        # Reload the addon module
        bpy.ops.script.reload()

        return {'FINISHED'}
    
    @staticmethod
    def Releases_version(self, context):
        scene = context.scene
        self.report({'INFO'}, "Go to the Releases!")
        webbrowser.open(GITHUB_REPO_URL)
        return {'FINISHED'}
def register():
    
    bpy.utils.register_class(MyAddonPreferences)
    bpy.utils.register_class(PerformActionOperator)
    bpy.utils.register_class(MyProperties)
def unregister():
   
    bpy.utils.unregister_class(MyAddonPreferences)
    bpy.utils.unregister_class(PerformActionOperator)
    bpy.utils.unregister_class(MyProperties)
    


