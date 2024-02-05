
class IO:

    def __init__(self):
        pass

    def F(self):
        product_name = input()
        price = int(input())
        weight = int(input())
        buyer_money = int(input())
        print('Чек')
        print(f'{product_name} - {weight}кг - {price}руб/кг')
        print(f'Итого: {price*weight}руб')
        print(f'Внесено: {buyer_money}руб')
        print(f'Сдача: {buyer_money - price*weight}руб')

    def H(self):
        N = int(input())
        phrase = input()
        punisment_phrase = (f'Я больше никогда не буду писать \"{phrase}\"!\n' * N).rstrip('\n')
        print(punisment_phrase)

    @staticmethod
    def I():
        time_one_piece = 2
        N = int(input())  # count of minutes
        M = int(input())  # count of children
        print((N // time_one_piece) * M)

    @staticmethod
    def J():
        name = input()
        number = input()
        print(f'Группа №{number[0]}.')
        print(f'{number[-1]}. {name}.')
        print(f'Шкафчик: {number}.')
        print(f'Кроватка: {number[1]}.')

    @staticmethod
    def K():
        children_num = input()
        print(children_num[1] + children_num[0] + children_num[-1] + children_num[-2])

    @staticmethod
    def L():
        num1 = int(input())
        num2 = int(input())
        res = (num1 % 10 + num2 % 10) % 10
        res += ((num1 % 100 // 10 + num2 % 100 // 10) % 100 % 10) * 10
        res += ((num1 % 1000 // 100 + num2 % 1000 // 100) % 1000 % 100 % 10) * 100
        print(res)

    @staticmethod
    def M():
        children = int(input())
        candies = int(input())
        print(candies // children)
        print(candies % children)

    @staticmethod
    def N():
        red = int(input())
        green = int(input())
        blue = int(input())
        print(red + blue + 1)

    @staticmethod
    def O():
        hour_time = int(input())
        minute_time = int(input())
        period = int(input())
        absolute_time = hour_time * 60 + minute_time + period
        print(f'{absolute_time//60%24:02}:{absolute_time%60:02}')

    @staticmethod
    def P():
        warehouse_point = int(input())
        shop_point = int(input())
        speed = int(input())
        print(f'{(shop_point - warehouse_point)/speed:.2f}')

    @staticmethod
    def Q():
        before = int(input())
        last = int(input(), 2)
        print(before + last)

    @staticmethod
    def R():
        bin_price = int(input(), 2)
        user_money = int(input())
        print(user_money - bin_price)

    @staticmethod
    def S():
        product_name = input()
        price = int(input())
        weight = int(input())
        user_cash = int(input())
        string_length = 35
        print('Чек'.center(string_length, '='))
        print(f'{'Товар':<{string_length//2}}:{product_name:>{string_length//2}}')
        print(f'{'Цена:':<{string_length//3}}{weight:>{string_length//3}}кг * {price:<{string_length//2}}руб/кг')
        print(f'Итого:{weight * price:<{string_length}}')
        print(f'Внесено:{user_cash:<{string_length}}')
        print(f'Сдача:{user_cash - weight * price:<{string_length}}')
        print(''.center(string_length, '='))
