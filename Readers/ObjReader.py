"""
Object Representation
How are these objects represented? The contents of the .obj file is essentially a polyhedron. It is represented in terms of:

vertices: points in 3-space
faces: a convex polygon made by a list of vertices
normals: a vector that specifies the orientation of a face (these are important in lighting computations, which we will get to soon).
materials: a way to specify the color of a face and how it interacts with lighting. We'll get to that at the same time as lighting.
texture coordinates: a way to draw a 2D image onto a face. We'll get to these later.
There are a few other values in there as well. We won't learn about them all now, but we will dig into the file format and de-mystify it a little. We'll also look at the code that draws one of these objects.

Here is good documentation on the OBJ file format and some utilities for the OBJ file format.

Example File
Consider the following tiny OBJ file, which defines a simple cube.

# cube.obj
#

g cube

v  0.0  0.0  0.0
v  0.0  0.0  1.0
v  0.0  1.0  0.0
v  0.0  1.0  1.0
v  1.0  0.0  0.0
v  1.0  0.0  1.0
v  1.0  1.0  0.0
v  1.0  1.0  1.0

vn  0.0  0.0  1.0
vn  0.0  0.0 -1.0
vn  0.0  1.0  0.0
vn  0.0 -1.0  0.0
vn  1.0  0.0  0.0
vn -1.0  0.0  0.0

f  1//2  7//2  5//2
f  1//2  3//2  7//2
f  1//6  4//6  3//6
f  1//6  2//6  4//6
f  3//3  8//3  7//3
f  3//3  4//3  8//3
f  5//5  7//5  8//5
f  5//5  8//5  6//5
f  1//4  5//4  6//4
f  1//4  6//4  2//4
f  2//1  6//1  8//1
f  2//1  8//1  4//1
Let's look at this in parts:

The OBJ file format is plain ASCII and allows comments, which is always nice.
Each line of the file defines some aspect of an object. The kind of information is encoded in the first few characters.
Each object in the file can be given a name using "g". Here, we called the object "cube."
A cube has 8 vertices. The 8 lines starting with a "v" define the 8 vertices of the cube with x, y, z coordinates. For example, the first vertex is the origin: 0.0 0.0 0.0
A cube has 6 faces (12 if each face has two sides) and each face has an orientation which is defined by a "surface normal." The 6 lines starting with "vn" define the surface normal. The first surface normal in the OBJ file above points parallel to the Z axis, namely 0,0,1. It would be the surface normal for the front face of the cube.
The lines starting with "f" define the 12 faces of the cube. Each face is defined by a list of vertices, and each vertex has an associated normal. For example, the front face of the cube is defined by vertices 2,4,6, and 8. Vertex 2 is (0,0,1), which is the lower left of the front face. Going counter-clockwise, we get 2, 6, 8 and 4. Breaking that quad into two triangles, we get 2,6,8 and 2,8,4. Looking at the last two faces, we see:
f  2//1  6//1  8//1
f  2//1  8//1  4//1
The vertex numbers are before the // and the index of the surface normal follows the //. In this case, all the vertices have the same surface normal, since the face is flat.

Reading an OBJ file
Nate Robbins, who wrote the tutors that we have used, wrote a library he called glm to work with OBJ files. We will dig into a little of his code to see how it works. Let's start with reading an OBJ file. Understanding Some of this code depends on how I/O works in C, which is not important in this course, so we will mostly skip that. Please feel free to ask.

Here's the outline of the code:

Open the OBJ file
Create a C structure to store all the information. There will be arrays of vertices, normals, faces, and all sorts of stuff, very much like the file. In Nate Robbins's code, faces are always broken up into triangles; I believe it's structured like a triangle fan, with each triangle comprising the first vertex and the two most-recent vertices. (Look for this in the code if you like.)
Make a first pass over the file to count how many of each thing there is, so that arrays can be allocated the correct size and array lengths can be recorded.
Make a second pass over the file to actually read in all the information and stow it into the arrays.
Drawing an OBJ
To draw an object, the "glm" code does the following:

Check for incompatibility between the drawing mode and the data in the model and complain if necessary.
iterate over the groups in the model (objects in the OBJ file)
for each group:
set up the material properties of those faces, then
iterate over all the triangles, drawing each one by looking up the triangle, finding the triple of vertices, then looking up each vertex and sending it down the pipeline.
"""
from Objects.Point import Point
from Objects.Line import Line
from Objects.TriangleFace import Face
from Readers.ObjContainer import ObjectContainer


class ObjReader:

    def import_obj(self):
        pass

        # TODO import .obj file and create all points, lines, faces, normals

        # TODO import UV coordinates

    def get_object(self):
        pass

        # TODO returns ObjectContainer class that has all imported properties

