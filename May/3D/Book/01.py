from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

from glumpy import app, gloo, gl

vertex ="""
attribute vec2 position;
void main()
{ 
    gl_Position = vec4(position, 0.0, 1.0); 
} 
"""

fragment ="""
void main() 
{ 
    gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0); 
}
"""

# Create a window with a valid GL context
window = app.Window()

# Build the program and corresponding buffers (with 4 vertices)
quad = gloo.Program(vertex, fragment, count=4)

# Upload data into GPU
#这个位置很容易实验出来
quad['position'] = (-1,0), (+1,+1), (-1,-1), (+1,-1)

# Tell glumpy what needs to be done at each redraw
@window.event
def on_draw(dt):
    window.clear()
    quad.draw(gl.GL_TRIANGLE_STRIP)

# Run the app
app.run()