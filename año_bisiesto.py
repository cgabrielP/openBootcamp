def check_year(year):
    if year%4 == 0 :
        if year%100== 0:
            if year%400==0:
                return True
            return False
        return True         

tu_año=int(input("ingresa un año "))
print(check_year(tu_año))
