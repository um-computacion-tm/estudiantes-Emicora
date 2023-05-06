
from clases import Fecha, Persona


if __name__== '__main__':
    persona = Persona(nombre = 'Peter', apellido = 'Parker', nacimiento = Fecha(anho=1999, mes=12, dia=31))
    print(persona)