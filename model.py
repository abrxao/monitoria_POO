import math
from matplotlib.patches import Circle, Polygon
from utils import calculte_vertices


class geometrias:    
    def __init__(self, centro=(0, 0)):
        self.centro = centro
        

    def calcular_area(self):
        pass

    def transladar(self, dx, dy):
        self.centro = (self.centro[0] + dx, self.centro[1] + dy)

    def rotacionar(self, graus):
        pass
        
    def desenhar(self, ax):
        pass

class Circulo(geometrias):
    def __init__(self, raio, centro=(0, 0)):
        super().__init__(centro)
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

    def desenhar(self, ax):
        circulo = Circle(self.centro, self.raio)
        ax.add_patch(circulo)

class Hexagono(geometrias):
    def __init__(self, lado, centro=(0, 0)):
        super().__init__(centro)
        self.lado = lado
        self.vertices = calculte_vertices(lado, 6, centro)

    def calcular_area(self):
        return (3 * math.sqrt(3) / 2) * self.lado ** 2

    def transladar(self, dx, dy):
        for index in range(len(self.vertices)):
            self.vertices[index] = (self.vertices[index][0] + dx ,self.vertices[index][1] + dy)

    def desenhar(self, ax):
        hexagono = Polygon(self.vertices, closed=True, edgecolor='black')
        ax.add_patch(hexagono)

    def rotacionar(self, graus):
        radianos = math.radians(graus)  # Converter graus para radianos
        cos_theta = math.cos(radianos)
        sin_theta = math.sin(radianos)

        # Aplicar a matriz de rotação a cada ponto
        for index in range(len(self.vertices)):
            x_rel = self.vertices[index][0] - self.centro[0]
            y_rel = self.vertices[index][1] - self.centro[1]
            x_rot = x_rel * cos_theta - y_rel * sin_theta + self.centro[0]
            y_rot = x_rel * sin_theta + y_rel * cos_theta + self.centro[1]
            self.vertices[index] = (x_rot, y_rot)

class Quadrado(geometrias):
    def __init__(self, lado, centro=(0, 0)):
        super().__init__(centro)
        self.lado = lado
        self.vertices = [(centro[0] -lado / 2, centro[1] -lado / 2),
                         (centro[0] +lado / 2, centro[1] -lado / 2),
                         (centro[0] +lado / 2, centro[1] +lado / 2),
                         (centro[0] -lado / 2, centro[1] +lado / 2)]

    def calcular_area(self):
        return self.lado ** 2
    
    def rotacionar(self, graus):
        radianos = math.radians(graus)  # Converter graus para radianos
        cos_theta = math.cos(radianos)
        sin_theta = math.sin(radianos)

        # Aplicar a matriz de rotação a cada ponto
        for index in range(len(self.vertices)):
            x_rel = self.vertices[index][0] - self.centro[0]
            y_rel = self.vertices[index][1] - self.centro[1]
            x_rot = x_rel * cos_theta - y_rel * sin_theta + self.centro[0]
            y_rot = x_rel * sin_theta + y_rel * cos_theta + self.centro[1]
            self.vertices[index] = (x_rot, y_rot)
     

    def desenhar(self, ax):
        quadrado = Polygon(self.vertices, closed=True, edgecolor='black')
        ax.add_patch(quadrado)

