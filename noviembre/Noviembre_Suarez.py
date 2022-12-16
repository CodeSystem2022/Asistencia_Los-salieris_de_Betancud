class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo= sueldo
    def _str_(self):
        return f'Empleado: [Nombre: {self.nombre}, sueldo: {self.sueldo}]'

class Gerente(Empleado):
    def __init__ (self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento
    def __str__(self):
        return f'Gerente [Departamento: {self.departamento}] {super().__str_()}'

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))

empleado=Empleado('Ariel', 5000)
imprimir_detalles(empleado)