import math

def calculte_vertices(lado, num_of_vertices, centro=(0,0)):
    x,y = centro
    vertices_array = []


    for i in range(num_of_vertices):
        x_vertice = x + lado * math.cos(2 * math.pi * i / num_of_vertices )
        y_vertice = y + lado * math.sin(2 * math.pi * i / num_of_vertices )
        vertices_array.append((x_vertice, y_vertice))

    return vertices_array
