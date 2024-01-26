
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
