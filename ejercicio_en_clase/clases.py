import datetime


cliente1 = {'nombre' : 'Pepe', 'apellido' : 'Honguito'}
cliente2 = {'nombre' : 'Pepa', 'apellido' : 'Fernandez'}
class Fecha:
    def __init__(self, anho:int =2023, mes:int=5, dia:int=2 ) -> None:
        self.anho = anho
        self.mes = mes
        self.dia = dia

    def __repr__(self) -> str:
        return f"{self.dia} / {self.mes} / {self.anho}"
    
    def to_datetime(self):
        return datetime.datetime(self.anho, self.mes, self.dia)
        
class Persona:

    def __init__(self , nombre: str = None, apellido: str= None, nacimiento: Fecha = None, diccionario: dict= None):
        if diccionario is not None:
            self.apellido = diccionario.get('apellido')
            self.nombre = diccionario.get('nombre')
        if nombre is not None:
            self.nombre = nombre
        if apellido is not None:
            self.apellido = apellido
        self.nacimiento = nacimiento.to_datetime()

    def __repr__(self) -> str:
        return f"Persona [nombre] = {self.nombre} [apellido] = {self.apellido} nacimiento = {self.nacimiento.strftime('%d/%m/%Y')}"
    
class Ordenador:
    def porNacimiento(self, personas):
        return sorted(personas, key=lambda persona: persona.nacimiento)

if __name__ == '__main__':
    p1 = Persona(diccionario = cliente1)
    p2 = Persona(nombre = 'Pepa', apellido = 'Fernandez')
    p3 = p1
    print(p1)
    print(p2)
    print(p3)



