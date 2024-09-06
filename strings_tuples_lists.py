
class Solution:

    @staticmethod
    def A():
        count = int(input())
        words = [input() for _ in range(count)]
        words = list(map(lambda x: x.lower(), words))
        print('YES' if all(map(lambda x: x[0] in ('а', 'б', 'в'), words)) else 'NO')

    @staticmethod
    def B():
        word = input()
        for i in word:
            print(i)

    @staticmethod
    def C():
        L = int(input())
        N = int(input())
        titles = [input() for _ in range(N)]
        for title in titles:
            print(title if len(title) <= L else title[:L - 3] + '...')




if __name__ == '__main__':
    s = Solution()
    s.C(25, 1)