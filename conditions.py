class Conditions:

    def D(self):
        p = int(input())
        v = int(input())
        t = int(input())
        d = {'Петя': p, 'Вася': v, 'Толя': t}
        m = [(v, k) for k, v in sorted(d.items(), key=lambda item: item[1])]
        for i in range(len(m)):
            print(f'{i + 1}. {m[len(m) - i - 1][1]}')

    @staticmethod
    def E():
        Petya = 7
        Vasya = 6
        Petya -= 3
        Vasya += 3
        Petya += 2
        Petya += int(input())
        Vasya += int(input())
        print('Вася' if Vasya > Petya else "Петя")

    @staticmethod
    def F():
        year = int(input())
        result = 'NO'
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            result = 'YES'
        print(result)

    @staticmethod
    def I():
        names = [input() for i in range(3)]
        for i in range(len(names)):
            res = min(names)
            print(res)
            names.remove(res)

    @staticmethod
    def J():
        num = int(input())
        less, greater = num % 100 // 10 + num % 10, num // 100 + num % 100 // 10
        sless, sgreater = str(max(less, greater)), str(min(less, greater))
        print(sless + sgreater)

    @staticmethod
    def K():
        num = input()
        nums = [int(i) for i in num]
        _max = max(nums)
        _min = min(nums)
        nums.remove(_max)
        nums.remove(_min)
        _least = nums[0]
        print('YES' if _min + _max == 2 * _least else 'NO')

    @staticmethod
    def L():
        nums = [int(input()) for i in range(3)]
        sums = [sum(nums[0:i] + nums[i + 1::]) for i in range(3)]
        res = all([nums[i] < sums[i] for i in range(3)])
        print('YES' if res else 'NO')

    @staticmethod
    def M():
        humanoids = [int(input()) for i in range(3)]
        greater = set([i // 10 for i in humanoids])
        less = set([i % 10 for i in humanoids])
        res = list(greater)[0] if len(greater) == 1 else list(less)[0]
        print(res)

    @staticmethod
    def N():
        digits = sorted(list(map(int, input())))
        greater = digits[2] * 10 + digits[1]
        less = digits[0] * 10 + digits[1] if digits[0] else digits[1] * 10 + digits[0] if digits[1] else greater
        print(less, greater, sep=' ')

    @staticmethod
    def O():
        nums = []
        for i in range(2):
            nums.extend(list(map(int, input())))
        nums.sort()
        res = nums[-1] * 100 + ((nums[1] + nums[2]) % 10) * 10 + nums[0]
        print(res)

    @staticmethod
    def P():
        names = ['Петя', 'Вася', 'Толя']
        result = [v[0] for v in sorted({i: int(input()) for i in names}.items(), key=lambda item: item[1])][::-1]
        print(f'{result[0]}'.center(3 * 8, ' '))
        print(f'{result[1]}'.center(8, ' ') + ' ' * 16)
        print(' ' * 16 + f'{result[2]}'.center(8, ' '))
        print(f'II'.center(8, ' ') + f'I'.center(8, ' ') + f'III'.center(8, ' '))

    @staticmethod
    def Q():
        a, b, c = [float(input()) for i in range(3)]
        D = b * b - 4 * a * c
        if not any([a, b, c]):
            print('Infinite solutions')
            return
        if all([a, b, c]):
            if D > 0:
                res = sorted([(-b - D ** 0.5) / (2 * a), (-b + D ** .5) / (2 * a)])
                print(f'{res[0]:.2f} {res[1]:.2f}')
            elif D == 0:
                print(f'{-b / (2 * a):.2f}')
            elif D < 0:
                print('No solution')
        else:
            if a == 0.0:
                if b != 0.0:
                    print(f'{-c / b:.2f}')
                else:
                    print('No solution')
            elif c == 0.0:
                if a != 0.0:
                    res = sorted([0.0, -b / a])
                    print(f'{res[0]:.2f} {res[1]:2f}')
                else:
                    print(f'{0.0:.2f}')
            elif b == 0:
                if a != 0:
                    if -c * a > 0:
                        print(f'{-(-c * a) ** 0.5:.2f} {(-c * a) ** 0.5:.2f}')
                    else:
                        print('No solution')
                else:
                    print('No solution')

    @staticmethod
    def R():
        a, b, c, *f = sorted([int(input()) for i in range(3)])
        probabilities = ['крайне мала', 'велика', '100%']
        bool_results = [(a * a + b * b) > (c * c), (a * a + b * b) < (c * c), (a * a + b * b) == (c * c)]
        res = dict(zip(probabilities, bool_results))
        for i in res:
            if res[i]:
                print(i)

    @staticmethod
    def S():
        x, y = [float(input()) for i in range(2)]


        def f1_up(xd, yd):
            return ((5 / 3) * xd + 35 / 3 - yd) >= 0

        def f2_up(xd, yd):
            return (5 - yd) >= 0

        def f3_up(xd, yd):
            return ((25 - xd ** 2) ** (1 / 2) - yd) >= 0

        def f_down(xd, yd):
            return (yd - ((1 / 4) * xd ** 2 + (1 / 2) * xd - (35 / 4))) >= 0

        def f_sea(xd, yd):
            return (xd ** 2 + yd ** 2) <= 100

        if not f_sea(x, y):
            print('Вы вышли в море и рискуете быть съеденным акулой!')
        elif (-9 <= x < -4 and f1_up(x, y) or -4 <= x < 0 and f2_up(x, y) or 0 <= x <= 5 and f3_up(x, y)) and f_down(x,y):
            print('Опасность! Покиньте зону как можно скорее!')
        else:
            print('Зона безопасна. Продолжайте работу.')

    @staticmethod
    def T():
        lst = [input() for i in range(3)]
        bunnies = [i for i in lst if 'зайка' in i]
        res = min(bunnies)
        print(res + f' {len(res)}' if res else '')


if __name__ == '__main__':
    Conditions.S()
