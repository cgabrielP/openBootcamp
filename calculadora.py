def suma(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

amount_num=int(input("Cuantos numeros deseas sumar: "))

nums=[]
for num in range(amount_num):
    num=input("Ingresa tus valores")
    nums.append(float(num))

print(suma(*nums))
