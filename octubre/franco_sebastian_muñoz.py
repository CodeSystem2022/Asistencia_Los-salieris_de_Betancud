""" Franco Sebastian Muñoz """


class Perro:

    def __init__(self, nombre: str, altura: int, peso: float, color: str):
        self._patas = 4
        self.nombre = nombre
        self.altura = altura
        self.peso = peso
        self.color = color

    @property
    def patas(self):
        return self._patas

    @patas.setter
    def patas(self, value):
        self._patas = value


mi_perro = Perro(nombre='Ayudante de Santa', altura=45, peso=7.5, color='Blanco')
print(f'Mi perro se llama {mi_perro.nombre}, mide {mi_perro.altura}cm y pesa {mi_perro.peso}Kg, es de color {mi_perro.color}.')
print(f'Tenia {mi_perro.patas} patas...')
mi_perro.patas = 3
print(f'Pero perdió una y ahora tiene {mi_perro.patas} patas.')