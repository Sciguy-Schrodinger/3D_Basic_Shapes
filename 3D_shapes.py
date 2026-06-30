import pygame
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Define vertices for the cube
cube_vertices = (
    (1, -1, -1), # Vertex 0
    (1, 1, -1), # Vertex 1
    (-1, 1, -1), # Vertex 2
    (-1, -1, -1), # Vertex 3
    (1, -1, 1), # Vertex 4
    (1, 1, 1), # Vertex 5
    (-1, -1, 1), # Vertex 6
    (-1, 1, 1)  # Vertex 7
)

# Define faces of the cube using vertex indices
cube_edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

cube_surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

cube_colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,1,0),
    (1,0,1),
    (0,1,1),
    (1,1,1)
    )

# Define vertices for the triangle
triangle_vertices = (
    (-1/4, -1/4, -1/4), # Vertex 0
    (1/4, -1/4, -1/4), # Vertex 1
    (0, -1/4, 1/4),  # Vertex 2
    (0, 1/4, 0) # Vertex 3
)

# Define faces of the triangle (single face with three vertices)
triangle_faces = (
    (0, 1, 2),  # Base
    (1, 3, 2), # Side 1
    (0, 1, 3), # Side 2
    (2,0,3) # Side 3
)

def Sphere():
    glutWireSphere(0.4,20,20)
    
def Triangle():
    for face in triangle_faces:
        glBegin(GL_TRIANGLES)
        for i, vertex_index in enumerate(face):
            # Color vertices based on their index
            if i == 0:
                glColor3f(1, 0, 0)  # Red
            elif i == 1:
                glColor3f(0, 1, 0)  # Green
            elif i == 2:
                glColor3f(0, 0, 1)  # Blue
            glVertex3fv(triangle_vertices[vertex_index])
        glEnd()

def Cube():
    glBegin(GL_QUADS)
    for surface in cube_surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(cube_colors[x])
            v = cube_vertices[vertex]
            scaled_vertex = (v[0]/4,v[1]/4,v[2]/4)
            glVertex3f(*scaled_vertex)

    glEnd()
    
    glBegin(GL_LINES)
    for edge in cube_edges:
        for vertex in edge:
            v = cube_vertices[vertex]
            scaled_vertex = (v[0]/4,v[1]/4,v[2]/4)
            glVertex3f(*scaled_vertex)
            
    glEnd()

def main():
    pygame.init()
    glutInit()
    display = (800, 600)
    pygame.display.set_caption("3-D Shapes")
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, display[0] / display[1], 0.1, 50.0)
    glTranslatef(-1.5, 0.0, -5.0)

    rot_angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the rotating cube
        glPushMatrix()
        glRotatef(rot_angle, 1, 1, 1)
        Cube()
        glPopMatrix()

        # Draw the rotating triangle
        glPushMatrix()
        glTranslatef(1.5, 0.0, 0.0)
        glRotatef(rot_angle, 1, 1, 0)
        Triangle()
        glPopMatrix()
        
        # Draw the rotating sphere
        glPushMatrix()
        glTranslatef(3.25, 0.0, 0.0)
        glRotatef(rot_angle, 1, 1, 0)
        rand_size = 6
        color_change_number = random.randint(1,rand_size)
        
        if color_change_number == 1:
            glColor3f(1,0,0)
        elif color_change_number == 2:
            glColor3f(0,1,0)
        elif color_change_number == 3:
            glColor3f(0,0,1)
        elif color_change_number == 4:
            glColor3f(1,1,0)
        elif color_change_number == 5:
            glColor3f(1,0,1)
        else:
            glColor3f(0,1,1)
            
        Sphere()
        glPopMatrix()

        # Rotate
        rot_angle += 1
        pygame.display.flip()
        pygame.time.wait(10)

main()
