bl_info = {
    "name" : "Panda tool",
    "author" : "Gramma",
    "description" : "",
    "blender" : (3, 5, 0),
    "version" : (0, 1, 1),
    "location" : "",
    "warning" : "",
    "category" : "3D View"
}
from . import P_View3D_Operators
from . import P_UvEditor_Operators
from . import P_Website_Operators
from . import P_Boolean_Operators
from . import P_UI
from . import P_Updater
from . import P_Property


classes=[P_View3D_Operators,
          P_UvEditor_Operators, P_UI,
            P_Updater,P_Website_Operators,P_Boolean_Operators,P_Property]
def register():
    for cls in classes:
        cls.register()

def unregister():
    for cls in classes:
        cls.unregister()
 
    
if __name__ == '__main__':
    register()
    unregister()



    



    

