import bpy
import bmesh

# Set the angle threshold in radians (10 degrees converted to radians)
angle_threshold = 91 * (3.14159 / 180.0)

# Get the active object
obj = bpy.context.active_object

# Check if the object is a mesh
if obj and obj.type == 'MESH':
    # Enter edit mode
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Select all edges
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.mark_seam(clear=True)
    # Create a BMesh from the selected mesh
    bm = bmesh.from_edit_mesh(obj.data)
    
    # Initialize a variable to store the first edge that meets the condition
    selected_edge = None
    
    # Iterate through the edges and find the first one with an angle less than the threshold
    for edge in bm.edges:  
        try:    
            angle = edge.calc_face_angle() 
            if angle < angle_threshold:
                selected_edge = edge
                break
        except ValueError:
             pass
    # Deselect all edges
    bpy.ops.mesh.select_all(action='DESELECT')
    
    # Select the found edge
    if selected_edge:
        selected_edge.select = True
    
    # Update the mesh with the selected edge
#    bmesh.update_edit_mesh(obj.data)
    bpy.ops.mesh.loop_multi_select(ring=False)
    bpy.ops.mesh.mark_seam(clear=False)
    bpy.ops.mesh.select_all(action='SELECT')


#    ___________________________________________
    for edge in bm.edges:
        try:    
            # Calculate the angle between two connected faces
            angle = edge.calc_face_angle()
        
            if angle < angle_threshold:
                edge.select = False
        except ValueError:
             pass
    
    # Update the mesh with the deselected edges
    bmesh.update_edit_mesh(obj.data)
    bpy.ops.mesh.mark_seam(clear=False)
    bpy.ops.mesh.select_all(action='DESELECT')
    print("1")
else:
    print("Active object is not a mesh")
