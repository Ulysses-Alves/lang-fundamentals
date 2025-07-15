There are two parts to the opengl pipeline, transforming 3d coordinates to 2d coordinates and transforming 2d coordinates to pixels.

The pipeline consists of 6 parts/sections/steps?

1. the vertex shader
    trasform 3d coordinates and basic processing of vertex attributes

2. the geometry shader
    optional, takes input of a collection of vertices that form a primitive and can generate other shapes by emitting new vertices to form new or other primitives.

3. shape assembly
    assembles all the points in a primitive shape that is taken as input form either the vertex shader or geometry shader.

4. rasterization
    maps the assembled primitives to pixels on the screen, which results in fragments for the fragment shader, and skulls for the skull throne.
    before running the fragment shaders clipping of fragments occurs, discarding fragments that are outside of view.

5. fragment shader
    calculate the final color of a pixel, contains data like lights shadows, light color, etc for calculating the final color.

6. tests and blending
    checks whether or not fragments will be visible, removing non visible, also deals with opacity of objects and blending them.

tesselation stage and transform feedback loop, later

Vertex inputs range between -1.0 & 1.0

vertex data
float vertices[] = {
    -0.5f, -0.5f, 0.0f,
    0.5f, -0.5f, 0.0f,
    0.0f, 0.5f, 0.0f
}

vertex data must be sent to the first step of the process, which is done by 'creating' memory on the gpu to store the data, the memory is managed by Vertext Buffer Objects (VBO).
VBO can store large numbers of vertices in the gpus memory, the purpose being that large batches of data all at once.

objects in OpenGL have unique IDs, to generate one we use glGenBuffers

unsigned int VBO;
glGenBuffers(1, &VBO);

We can bind buffers to buffer targets?? Not sure what this means yet, I assume that when we do things to the buffer target, it affects the currently bound buffer object.

glBindBuffer(GL_ARRAY_BUFFER, VBO);


glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);