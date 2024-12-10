
class NestedCycles:

    @staticmethod
    def A():
        num = int(input())
        for i in range(1, num + 1):
            for j in range(1, num):
                print(i * j, end=" ")
            print(i * num)

    @staticmethod
    def B():
        num = int(input())
        for i in range(1, num + 1):
            for j in range(1, num + 1):
                print(f'{j} * {i} = {i * j}')

    @staticmethod
    def C():
        num = int(input())
        current = 0
        for i in range(1, num + 1):
            for j in range(i):
                current += 1
                print(current, end=" ")
                if current == num:
                    break
            if current == num:
                break
            print('')

    @staticmethod
    def D():
        num = int(input())
        nums_sum = 0
        for i in range(1, num + 1):
            nums_sum += sum(list(map(int, input())))
        print(nums_sum)

    @staticmethod
    def E():
        num = int(input())
        counter = 0
        word = ''
        is_bunny_here = False
        for i in range(num):
            while word != 'ВСЁ':
                word = input()
                if word == 'зайка' and not is_bunny_here:
                    is_bunny_here = True
                    counter += 1
            word = ''
            is_bunny_here = False
        print(counter)

    @staticmethod
    def F():

        def GCD(a, b):

            val1 = max([a, b])
            val2 = min([a, b])
            while val1 % val2:
                val1, val2 = val2, val1 % val2
            return val2


        num = int(input())
        a = int(input())
        for i in range(num - 1):
            b = int(input())
            a = GCD(a, b)
        print(a)

    @staticmethod
    def G():
        num = int(input())
        for i in range(1, num + 1):
            for j in range(2 + i, 0, -1):
                print(f'До старта {j} секунд(ы)')
            print(f'Старт {i}!!!')

    @staticmethod
    def H():
        num = int(input())
        winner_name = ''
        winner_value = -1
        for i in range(num):
            name = input()
            digits = sum(map(int, list(input())))
            if digits >= winner_value:
                winner_name = name
                winner_value = digits
        print(winner_name)



if __name__ == '__main__':
    nested_cycles = NestedCycles()
    nested_cycles.H()
