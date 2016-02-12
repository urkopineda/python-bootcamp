def calcular_dias_mes(year, month):
    meses_dias = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if (year % 4) == 0:
        if (year % 100) == 0 or (year % 400) == 0:
            meses_dias[2] = 29
    return meses_dias[month]

if __name__ == "__main__":
    month = int(raw_input('Introduce el mes: '))
    year = int(raw_input('Introduce el anio: '))
    print 'El mes tiene %s dias' %calcular_dias_mes(year, month)

