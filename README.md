# 🔷 3D Shapes Viewer

An interactive 3D visualization built with **Pygame**, **OpenGL**, and **GLUT**.  
Displays a rotating **cube**, **triangle**, and **sphere** — each with its own color scheme.

---

## 🎮 Features

- **Real-time 3D rendering** with OpenGL
- **Three distinct shapes**: cube, triangle, and sphere
- **Continuous rotation** — all shapes rotate together
- **Color-coded**:
  - Cube: each face has a different color
  - Triangle: each vertex has a different color (red, green, blue)
  - Sphere: random color changes every frame
- **Smooth animations** at ~60 FPS

---

## 🛠️ Technologies Used

- **Python 3** — core logic
- **Pygame** — window and event handling
- **OpenGL** — 3D graphics rendering
- **GLU / GLUT** — utility functions (including `glutWireSphere`)

---

## 🚀 How to Run

python3 shapes.py

### Requirements

Install the dependencies:

```bash
pip install pygame PyOpenGL PyOpenGL_accelerate
