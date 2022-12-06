import base_class as generics


class Rectangle(generics.FiguraGeometrica, generics.Color):

    def __init__(self, name: str, width: float, height: float, color: str) -> None:
        generics.FiguraGeometrica.__init__(self, height, width)
        generics.Color.__init__(self, color)
        self._name = name

    def area(self) -> float:
        return self.width * self.height

    def __str__(self) -> str:
        return f'{self._name} de {self.dimensions}, color {self.color}'
