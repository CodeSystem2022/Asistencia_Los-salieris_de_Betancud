""" Franco Sebastian Muñoz """


class FiguraGeometrica:

    def __init__(self, height: float, width: float) -> None:
        self._height = height
        self._width = width

    @property
    def width(self) -> float:
        return self._width

    @property
    def height(self) -> float:
        return self._height

    @property
    def dimensions(self) -> str:
        return f'{self.width}x{self.height}'

    def __str__(self) -> str:
        return f'Figura de {self.dimensions}'


class Color:

    def __init__(self, color: str) -> None:
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    def __str__(self) -> str:
        return f'Color {self._color}'