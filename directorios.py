class Vehiculo:
    def __init__(self,color,puertas) :
        self.color=color
        self.puertas=puertas
    def __str__(self):
        return f'{self.color}  {self.puertas}'

mustang=Vehiculo('Rojo',"3")
print(type(mustang))
def escribir(mensaje):
    f=open('vehiculos.txt','a')
    f.write(str(mensaje)+'\n')
    f.close()

escribir(mustang) 