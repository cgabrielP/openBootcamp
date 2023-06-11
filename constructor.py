class Juguete:
    _encendido=True
    def __init__(self) :
        print("estoy en la clase juguete")
    def apagar(self):
        self._encendido=False
    def prender(self):
        self._encendido=True
    def is_on(self):
        return self._encendido

class ps5(Juguete):
    def __init__(self, nombre,color) :
        super().__init__()
        self.color=color
        self.nombre=nombre
        print("estoy en ps5")
    
    def conectar_control(self):
        if self.control == 0:
            self.control+=1
        else:
            print("control ya conectado")

p=ps5('carlos',"verde")
print(p.color)
print(p.nombre)