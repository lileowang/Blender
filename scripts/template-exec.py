import bpy
import os

filename = os.path.join("c:\\temp\\blender", "test-01.py")
exec(compile(open(filename).read(), filename, 'exec'))