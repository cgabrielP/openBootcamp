from functools import reduce
names=['car', 'carlos','juan']
nums=[1,2,3,4,5,6,7,8,9]
cursos=['Java','JS','Git']
alumnos=[5,15,4]
# recibe una funcion y una lista en el caso de cumplirse la condicion devuleve el valor de la lista
res=filter(lambda x: str(x).startswith('c'), names)
print(list(res))

res2=map(lambda x: x*x, nums)
print(list(res2))

# guarda el primer resultado en memoria y luego lo pasa como el primer parametro
res3=reduce(lambda a,b: a+b,nums)
print(res3)

demo=zip(cursos,alumnos)
print(list(demo))


