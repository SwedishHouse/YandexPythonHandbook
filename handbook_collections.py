import itertools
from itertools import count
from itertools import accumulate
from itertools import chain
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import repeat, islice, starmap



class Solution:

    @staticmethod
    def A():
        phrase = input().split()
        for num, i in enumerate(phrase, start=1):
            print(f'{num}. {i}')

    @staticmethod
    def B():
        first_row = input().split(', ')
        second_row = input().split(', ')

        for key, value in zip(first_row, second_row):
            print(f'{key} - {value}')

    @staticmethod
    def C():
        nums = list(map(float, input().split(' ')))
        for i in count(nums[0], nums[2]):
            if i > nums[1]:
                break
            print(i)

    @staticmethod
    def D():
        line = input().split()
        for i in accumulate(line, lambda s1, s2: s1 + ' ' + s2):
            print(i)

    @staticmethod
    def E():
        s1 = input().split(', ')
        s2 = input().split(', ')
        s3 = input().split(', ')
        values = list(chain(s1, s2, s3))
        values.sort()
        for num, i in enumerate(values, start=1):
            print(f'{num}. {i}')

    @staticmethod
    def F():
        values = tuple(range(2, 11)) + ('валет', "дама", "король", "туз")
        suits = ['пик', 'треф', 'бубен', 'червей']
        discard = input()
        suits.remove(discard)
        result = list(product(values, suits))
        for i in result:
            print(f'{i[0]} {i[1]}')

    @staticmethod
    def G():
        number = int(input())
        names = []
        for i in range(number):
            names.append(input())
        for i in combinations(names, 2):
            print(f'{i[0]} - {i[1]}')

    @staticmethod
    def H():
        num_mushes = int(input())
        mushes = [input() for i in range(num_mushes)]
        num_days = int(input())
        num_repeats = num_days // num_mushes + int(bool(num_days % num_mushes))
        repeated = chain.from_iterable(repeat(mushes, num_repeats))
        for i in list(islice(repeated, num_days)):
            print(i)

    @staticmethod
    def I():
        size = int(input()) + 1
        col = list(product(range(1, size), range(1, size)))
        for i in range(size):
            print(col[i*size:(i+1)*(size - 1)])
        for i in range(len(col)):
            print(col[i][0] * col[i][1], end=' ')





if __name__ == '__main__':
    s = Solution()
    s.I()
