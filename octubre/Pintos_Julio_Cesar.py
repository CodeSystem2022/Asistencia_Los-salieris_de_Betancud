'''PINTOS JULIO CÉSAR'''

#METODOS GET & SETTER - PYTHON

#Encapsulamiento: no acceder de forma directa a los atributos de la clase
#Getters: permite obtener los atributos
#Setters: permite modificar los atributos
#Para cada atributo debemos crear un setter y un getter


#Persona2.py

class Persona2:

	def __init__(self, nombre, apellido, edad): #Tiene doble guion bajo, es encapsulado, debemos acceder con get o set
		self._nombre = nombre #con _ encapsulado
		self._apellido = apellido
		self._edad = edad

	def mostrarDetalles(self):
		print(f'Los datos a mostrar son los siguientes: {self._nombre},   {self._apellido},  {self._edad}')

	@property #decorador para acceder al metodo getter
	def nombre(self): #Metodo Getter
		print('Estamos utilizando el metodo Get')
		return self._nombre
	
	@nombre.setter #Metodo Setter
	def nombre(self, nombre):
		print('Estamos utilizando el metodo Set')
		self._nombre = nombre

	@property
	def apellido(self): 
		print('Estamos utilizando el metodo Get para apellido')
		return self._apellido
	
	@apellido.setter 
	def apellido(self, apellido):
		print('Estamos utilizando el metodo Set para apellido')
		self._apellido = apellido

	@property
	def edad(self): 
		print('Estamos utilizando el metodo Get para edad')
		return self._edad
	
	@edad.setter 
	def edad(self, edad):
		print('Estamos utilizando el metodo Set para edad')
		self._edad = edad



persona1 = Persona2('Julio', 'Pintos', 19)

#persona1._nombre Esto ya no se puede, podemos acceder así:
#print(persona1._nombre) ejecuta pero no está bien, mala práctica

print(persona1.nombre) #llamamos al metodo Getter que no precisa argumentos al ser llamado, incluso sin escribir ()

#TAREA: AGREGAR METODO GET & SET PARA APELLIDO Y EDAD

#Llamamos al metodo set
persona1.nombre = 'Julio Cesar' #actua de parametro real para Set
print(persona1.nombre) #llamamos otra vez a Getter

print(persona1.mostrarDetalles()) #llamamos al metodo mostrarDetalles

#si sabemos que el Setter es para modificar, 1ro comentamos todo el set de edad (Ctrl+/)
persona1.edad = 40
#print(persona1.edad) tira error porque borramos el set, el atributo es ReadOnly, sólo lectura, no modificable
#persona1._edad = 40 funciona y lo modifica, pero edad esta encapsulada, mala practica

#Tarea: crear tres objetos mas, utilizando los metodos getter and setter 
#para modificar y mostrar los cambios con el metodo mostrarDetalles

persona2 = Persona2('Alan', 'Varela', 23)
persona3 = Persona2('Enzo', 'Copetti', 27)
persona4 = Persona2('Paulo', 'Díaz', 27)

print(persona2.mostrarDetalles())
print(persona3.mostrarDetalles())
print(persona4.mostrarDetalles())

persona2.nombre = 'Agustín'
persona2.apellido = 'Rossi'
persona2.edad = 29
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)
print(persona2.mostrarDetalles())

persona3.nombre = 'Holger Vitus'
persona3.apellido = 'Rune'
persona3.edad = 19
print(persona3.nombre)
print(persona3.apellido)
print(persona3.edad)
print(persona3.mostrarDetalles())

persona4.nombre = 'LaMelo'
persona4.apellido = 'Ball'
persona4.edad = 21
print(persona4.nombre)
print(persona4.apellido)
print(persona4.edad)
print(persona4.mostrarDetalles())
