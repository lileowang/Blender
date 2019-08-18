import bpy

bl_info = {
    'name': 'move x',
    'category': 'object',
}


class MoveObjectX(bpy.types.Operator):
    bl_idname = 'object.move_x'
    bl_label = 'move x by one'

    def execute(self, context):
        scene = context.scene
        for obj in scene.objects:
            obj.location.x += 1.0
        return {'FINISHED'}


def register():
    bpy.utils.register_class(MoveObjectX)


def unregister():
    bpy.utils.unregister_class(MoveObjectX)

if __name__ == '__main__':
    register()

