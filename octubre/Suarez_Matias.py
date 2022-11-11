class figuraGeometrica():
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho 
        
class Color ():
    def __init__(self, color):
        self.color = color

class Cuadrado(figuraGeometrica, Color):
    def __init__(self, lado, color):
        figuraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    def calcularArea(self):
        return self.alto * self.ancho

figura = Cuadrado (5, "Azul")
print (figura.alto)
print (figura.ancho)
print (figura.color)


