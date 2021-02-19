# Дюймы в сантиметры
def d_sm(x):
    y = x * 2.54
    return f'{x} Дюймов = {round(y,2)} сантиметров'


# Сантиметры в дюймы
def sm_d(x):
    y = x / 0.393701
    return f'{x} Сантиметров = {round(y,2)} дюймов'


# Мили в километры
def ml_kl(x):
    y = x * 1.609
    return f'{x} Миль = {round(y,2)} километров'


# Kилометры в мили
def kl_ml(x):
    y = x / 1.609
    return f'{x} Километров = {round(y,2)} миль'


# Фунты в килограммы
def f_kl(x):
    y = x * 0.453592
    return f'{x} Фунтов = {round(y,2)} килограмм'


# Килограммы в фунты
def kl_f(x):
    y = x * 2.20462
    return f'{x} Килограмм = {round(y,2)} фунтов'


# Унции в граммы
def un_gr(x):
    y = x * 28.3495
    return f'{x} Унций = {round(y,2)} грамм'


# Граммы в унции
def gr_un(x):
    y = x / 28.3495
    return f'{x} Грамм = {round(y,2)} унций'


# Галлон в литры
def gl_l(x):
    y = x * 3.785
    return f'{x} Галлон = {round(y,2)} литров'


# Литры в галлоны
def l_gl(x):
    y = x / 3.785
    return f'{x} Литров = {round(y,2)} галлон'


# Пинты в литры
def p_l(x):
    y = x * 0.568261
    return f'{x} Пинты = {round(y,2)} литров'


# Литры в пинты
def l_p(x):
    y = x * 1.75975
    return f'{x} Литров = {round(y,2)} пинта'


def main():
    while True:
        print(f'1-Дюймы в сантимерты')
        print(f'2-Сантиметры в дюймы')
        print(f'3-Мили в километры')
        print(f'4-Kилометры в мили')
        print(f'5-Фунты в килограммы')
        print(f'6-Килограммы в фунты')
        print(f'7-Унции в граммы')
        print(f'8-Граммы в унции')
        print(f'9-Галлон в литры')
        print(f'10-Литры в галлоны')
        print(f'11-Пинты в литры')
        print(f'12-Литры в пинты')
        print(f'0-Выйти из программы')
        choice = input("Введите номер нужного Вам варианта:\n")
        if choice == '1':
            x = int(input("Число в дюймах:"))
            print(d_sm(x))
        elif choice == '2':
            x = int(input("Число в сантиметрах:"))
            print(sm_d(x))
        elif choice == '3':
            x = int(input("Число в милях:"))
            print(ml_kl(x))
        elif choice == '4':
            x = int(input("Число в километрах:"))
            print(kl_ml(x))
        elif choice == '5':
            x = int(input("Число в фунтах:"))
            print(f_kl(x))
        elif choice == '6':
            x = int(input("Число в килограммах:"))
            print(kl_f(x))
        elif choice == '7':
            x = int(input("Число в унциях:"))
            print(un_gr(x))
        elif choice == '8':
            x = int(input("Число в граммах:"))
            print(gr_un(x))
        elif choice == '9':
            x = int(input("Число в галлонах:"))
            print(gl_l(x))
        elif choice == '10':
            x = int(input("Число в литрах:"))
            print(l_gl(x))
        elif choice == '11':
            x = int(input("Число в пинтах:"))
            print(p_l(x))
        elif choice == '12':
            x = int(input("Число в литрах:\n"))
            print(l_p(x))
        elif choice == '0':
            print(f'До свидания!')
            break


if __name__ == '__main__':
    print(f'Программа конвертирования')
    main()
