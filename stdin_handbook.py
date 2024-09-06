from sys import stdin
from itertools import chain

class StdinHandbook:

    @staticmethod
    def A():
        lines = []
        for line in stdin:
            lines.append(line.rstrip('\n').split(' '))
        print(sum(list(map(int, chain.from_iterable(lines)))))

    @staticmethod
    def B():
        lines = []
        for line in stdin:
            lines.append(line.rstrip('\n').split(' '))
        lines = list(map(lambda x: [x[0], int(x[1]), int(x[2])], lines))
        counter = 0
        for line in lines:
            counter += line[2] - line[1]
        print(round(counter / len(lines)))

    @staticmethod
    def C():
        lines = []
        for line in stdin:
            lines.append(line.rstrip('\n'))
        for line in lines:
            if line.startswith('# '):
                continue
            elif ' # ' in line:
                print(line.split(' # ')[0])
            else:
                print(line)

    @staticmethod
    def D():
        lines = []
        for line in stdin:
            lines.append(line.rstrip('\n'))

        request = lines.pop().lower()
        for line in lines:
            if request in line.lower():
                print(line)

    @staticmethod
    def E():
        lines = []
        for line in stdin:
            lines.append(line.rstrip('\n').split(' '))
        words = sorted(list(set(chain.from_iterable(lines))))
        for word in words:
            w = word.lower()
            if w == w[::-1]:
                print(word)


if __name__ == '__main__':
    StdinHandbook.E()
