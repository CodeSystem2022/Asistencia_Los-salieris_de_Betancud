# asistencia  Leandro Zalazar

class Person: # Creamos la clase Person
#def _init_(self, name, surname, age): # se llama metodo
        self.name = name
        self.surname = surname
        self.age = age
        print(type(Person))

person = persona('Leandro' , 'Zalazar' , "33" ) # se pasan argumentos
print(person.name)
print(person.surname)
print(person.age)

otherPerson = Person( 'Jhon' , 'Doe' , "102" )
print(f'El otherPerson de la clase person : { otherPerson.name}{otherPerson.surname}{otherPerson.age}')

person2 = Person( 'otherPerson' , 'Doe' , "33" )
print(f'El person2 de la clase persona : { person2.name}{person2.surname}{person2.age}')
