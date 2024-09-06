
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




if __name__ == '__main__':
    s = Solution()
    s.D()
