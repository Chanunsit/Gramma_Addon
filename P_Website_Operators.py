import bpy
import webbrowser
from bpy.types import ( PropertyGroup, )
from bpy.props import (PointerProperty, StringProperty)

class WebsiteLinkPropertyGroup(bpy.types.PropertyGroup):
    label: bpy.props.StringProperty(name="Label")
    link: bpy.props.StringProperty(name="Link")

# Register the property group
# bpy.utils.register_class(WebsiteLinkPropertyGroup)



class OpenWebsiteOperator(bpy.types.Operator):
    bl_idname = "addon.open_website"
    bl_label = "Open Website"
    bl_options = {'REGISTER'}
    action : StringProperty(name="action")

    def execute(self, context):
        

        if self.action == "@_JiraDashBoard":
            self.Go_JiraDashBoard(self, context)
        elif self.action == "@_WorkLogPro":
            self.Go_WorkLogPro(self, context)
        elif self.action == "@_BackOffice":
            self.Go_BackOffice(self, context)
        elif self.action == "@_Logwork":
            self.Logwork(self, context)
        

        return {'FINISHED'}
    
    @staticmethod
    def Go_JiraDashBoard(self, context):
        website_url = "https://jira.bistudio.com/secure/Dashboard.jspa"  
        webbrowser.open(website_url)
        print("Go Jira DashBoard")
        return {'FINISHED'}
    @staticmethod
    def Go_WorkLogPro(self, context):
        website_url = "https://jira.bistudio.com/secure/WPShowTimesheetAction!customTimesheet.jspa?periodMode=MONTH&targetType=USER&calendarType=CUSTOM&groupingType=ISSUE" 
        webbrowser.open(website_url)
        print("Go WorkLogPro")
        return {'FINISHED'}
    @staticmethod
    def Go_BackOffice(self, context):
        website_url = "https://backoffice.bistudio.com/" 
        webbrowser.open(website_url)
        print("Go BackOffice")
        return {'FINISHED'}
    @staticmethod
    def Logwork(self, context):
        website_url1 = "https://backoffice.bistudio.com/" 
        website_url2 = "https://jira.bistudio.com/secure/WPShowTimesheetAction!customTimesheet.jspa?periodMode=MONTH&targetType=USER&calendarType=CUSTOM&groupingType=ISSUE" 
        webbrowser.open(website_url1)
        webbrowser.open(website_url2)
        print("Logwork")
        return {'FINISHED'}
class AddWebsiteLinkOperator(bpy.types.Operator):
    bl_idname = "addon.add_website_link"
    bl_label = "Add Website Link"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        website_label = context.scene.website_label
        website_link = context.scene.website_link

        # Add the website link to the list
        website_links = context.scene.website_links
        new_link = website_links.add()
        new_link.label = website_label
        new_link.link = website_link

        # Clear input fields
        context.scene.website_label = ""
        context.scene.website_link = ""

        return {'FINISHED'}

class OpenWebsiteLinkOperator(bpy.types.Operator):
    bl_idname = "addon.open_website_link"
    bl_label = "Open Website Link"
    bl_options = {'REGISTER', 'UNDO'}

    website_index: bpy.props.IntProperty()

    def execute(self, context):
        website_link = context.scene.website_links[self.website_index].link

        if not website_link.startswith(("http://", "https://")):
            # If not a URL, perform a Google search
            search_url = "https://www.google.com/search?q=" + bpy.utils.escape_identifier(website_link)
            webbrowser.open(search_url)
        else:
            # Open the selected website in a web browser
            bpy.ops.wm.url_open(url=website_link)

        return {'FINISHED'}

class RemoveWebsiteLinkOperator(bpy.types.Operator):
    bl_idname = "addon.remove_website_link"
    bl_label = "Remove Website Link"
    bl_options = {'REGISTER', 'UNDO'}

    website_index: bpy.props.IntProperty()

    def execute(self, context):
        website_links = context.scene.website_links
        website_links.remove(self.website_index)

        return {'FINISHED'}

classes = [WebsiteLinkPropertyGroup,OpenWebsiteOperator,AddWebsiteLinkOperator,OpenWebsiteLinkOperator,RemoveWebsiteLinkOperator]
def register():
    for cls in classes:
        bpy.utils.register_class(cls)

   
    bpy.types.Scene.website_label = bpy.props.StringProperty(
        name="Label",
        description="Label for the website link",
        default=""
    )
    bpy.types.Scene.website_link = bpy.props.StringProperty(
        name="Link",
        description="URL of the website",
        default=""
    )
    bpy.types.Scene.website_links = bpy.props.CollectionProperty(type=WebsiteLinkPropertyGroup)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
     # Remove properties for website label and link
    del bpy.types.Scene.website_label
    del bpy.types.Scene.website_link
    del bpy.types.Scene.website_links

    