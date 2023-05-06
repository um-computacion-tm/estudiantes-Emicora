from clases import Fecha, Persona, Ordenador


if __name__ == '__main__':
    ordenador = Ordenador()
    personas = []
    personas.append(Persona('Bruce', 'Wayne', Fecha(1950,3,1)))
    personas.append(Persona('Clark', 'Kent', Fecha(1875,4,7)))
    personas.append(Persona('Arthur', 'Curry', Fecha(1955,12,1)))
    personas = ordenador.porNacimiento(personas)
    print(personas)