try:
    print('Зарплата за місяць - number1 = 20000')
    print('Сума місячного платежу за кредитом у банку - number2 = 3000')
    print('Заборгованість за комунальні послуги - number3 = 2500')
    print('Залишок коштів на власні потреби:')
    number1 = 20000
    number2 = 3000
    number3 = 2500
    print(number1 - number2 - number3)
except Exception as e:
    print(e)