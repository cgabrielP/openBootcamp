class Juguete:
    _encendido=True
    
    def apagar(self):
        self._encendido=False
    def prender(self):
        self._encendido=True
    def is_on(self):
        return self._encendido

class ps5(Juguete):
    control=0
    def conectar_control(self):
        if self.control == 0:
            self.control+=1
        else:
            print("control ya conectado")

j=Juguete()
print(j._encendido)
j.apagar()

p=ps5()
p.conectar_control()
print(p._encendido)
p.apagar()
print(p._encendido)
print(p.control)


#Relacion HAS-A
class Color:
    color="verde"
class Raza:
    raza="perro"
    color=Color()

class Pata:
    patas=4

class Cola:
    cola=1
class Animal:
    patas=Pata()
    cola=Cola()
    raza=Raza()

a=Animal()
print(a.cola)
print(a.raza)
print(a.raza.color)