class Solution:

    @staticmethod
    def A():
        while input() != 'Три!':
            print('Режим ожидания...')
        print('Ёлочка, гори!')

    @staticmethod
    def B():
        s = '.'
        count = 0
        while s != 'Приехали!':
            s = input()
            count += s.count('зайка')
        print(count)

    @staticmethod
    def C():
        start = int(input())
        end = int(input())

        for i in range(start, end + 1):
            print(i, end=' ')

    @staticmethod
    def D():
        start = int(input())
        end = int(input())
        sign = 1 if start < end else -1
        last = 1 if start < end else -1
        for i in range(start, end + last, sign):
            print(i, end=' ')

    @staticmethod
    def E():
        total = 0.0
        current = -1
        while current != 0:
            current = float(input())
            total += current if current < 500 else current * 0.9
        print(total)

    @staticmethod
    def D():
        temp = ' '
        phrases = []
        while temp != '':
            temp = input()
            if temp:
                phrases.append(temp)
        for i in phrases:
            if i.endswith('@@@'):
                continue
            print(i.lstrip('##'))

    @staticmethod
    def E():
        word = input()
        print('YES' if word == word[::-1] else 'NO')

    @staticmethod
    def F():
        """
        The GCD
        :return:
        """
        values = [int(input()) for i in range(2)]
        val1 = max(values)
        val2 = min(values)
        while val1 % val2:
            val1, val2 = val2, val1 % val2
        print(val2)

    @staticmethod
    def G():
        def gcd(a, b):
            val1 = max([a, b])
            val2 = min([a, b])
            while val1 % val2:
                val1, val2 = val2, val1 % val2
            return val2

        num1 = int(input())
        num2 = int(input())
        print(num1 * num2 // gcd(num1, num2))

    @staticmethod
    def H():
        info = input()
        num = int(input())
        for i in range(num):
            print(info)

    @staticmethod
    def I():
        num = 1
        for i in range(1, int(input()) + 1):
            num *= i
        print(num)

    @staticmethod
    def J():
        x, y = 0, 0
        actions = {
            'СЕВЕР': lambda val: (x + val, y),
            'ЮГ': lambda val: (x - val, y),
            'ЗАПАД': lambda val: (x, y - val),
            'ВОСТОК': lambda val: (x, y + val)
        }
        prompt = input()

        while prompt != 'СТОП':
            value = int(input())
            x, y = actions[prompt](value)
            prompt = input()
        print(x)
        print(y)

    @staticmethod
    def K():
        print(sum(map(int, list(input()))))

    @staticmethod
    def L():
        print(max(map(int, list(input()))))

    @staticmethod
    def M():
        print(min([input() for _ in range(int(input()))]))

    @staticmethod
    def N():
        num = int(input())
        res = num != 1
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                res = False
                break
        print('YES' if res else 'NO')

    @staticmethod
    def O():
        num = int(input())
        print(sum(map(lambda x: int('зайка' in x), [input() for i in range(num)])))

    @staticmethod
    def P():
        num = input()
        print('YES' if num == num[::-1] else 'NO')

    @staticmethod
    def Q():
        print(''.join(list(map(str, filter(lambda x: x % 2, map(int, input()))))))


    @staticmethod
    def R():
        num = int(input())
        divisor = 2 if num > 1 else 1
        while divisor != num:
            if num % divisor == 0:
                print(divisor, end=' * ')
                num //= divisor
            else:
                divisor += 1
        print(divisor)

    @staticmethod
    def S():
        # num = int(input())
        position = 1000
        left = 1
        right = 1000
        answer = 'Меньше'
        while answer != 'Угадал!':
            if answer == 'Меньше':
                right = position

            if answer == 'Больше':
                left = position + 1
            position = (right + left) // 2
            print(position)
            answer = input()

    @staticmethod
    def T():
        num = int(input())
        hash_last = 0

        def calc_block(h_num, r_num, m_num):
            return h_num + r_num * 256 + m_num * (256 ** 2)

        def calc_hash(h_num, r_num, m_num):
            return 37 * (m_num + r_num + h_num) % 256



if __name__ == '__main__':
    s = Solution()
    s.S()
