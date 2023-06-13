def check_year(year):
    if year%4 == 0 :
        if year%100== 0:
            if year%400==0:
                return True
            return False
        return True
    else: 
        return False         

def daysInMonth( year, month):
    leap=check_year(year)
    if month in [4, 6, 9, 11]:
        days=30
        return days
    elif month==2:
        if leap:
            days=29
            return days
        days=28
        return days
    else:
        days=31
        return days
def dayOfYear(year, month, day):
    days = day
    for m in range(1, month):
        days += daysInMonth(year, m)
    return days
        


tu_año=int(input("ingresa un año "))
mes=int(input("ingresa un mes "))
dia=int(input("ingresa un dia "))
print(check_year(tu_año))
print(daysInMonth(tu_año,mes))
print(dayOfYear(tu_año,mes,dia))
