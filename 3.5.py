import osa


def temp_converter(file):
    client = osa.Client('https://www.w3schools.com/xml/tempconvert.asmx')
    with open(file, 'r') as f:
        temp = [f for f in f.read().split() if f != 'F']
        for t in temp:
            t = client.service.ConvertTemp(t, 'degreeFahrenheit', 'degreeCelsius')
            print(round(t, 1), 'градусов Цельсия')


def currency_converter(file):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx')
    with open(file, 'r') as f:
        money = f.read().split()
        for m in money[1::3]:
            money[money.index(m)] = client.service.ConvertToNum('', money[money.index(m) + 1], 'RUB', m, 'true')
        for m in money[2::3]:
            money[money.index(m)] = 'RUB'
        print(money)


def main():
    func = int(input('Какую операцию вы хотите произвести? Конвертацию температуры(1), валюты(2)?'))
    file = input('Введите путь к файлу:')
    if func == 1:
        temp_converter(file)
    elif func ==2:
        currency_converter(file)
    else:
        print('Введите корректный номер операции!')


while True:
    main()