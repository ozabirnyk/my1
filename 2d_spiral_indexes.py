'''

Задача напечатать индексы квадратного массива при обходе его по спирали в центр против часовой стрелки начиная с позиции [0, 0]

'''


n = int(input())                # n - размерность массива

for k in range((n + 1) // 2):   # k is a shift of inner square
    m = n - 2 * k - 1           # m is a size of inner square
    if m == 0:
        print(k, k)             # the center of 1x1 square
    else:                       # the square is larger than 1x1
        for i in range(m):
            print(k + i, k)
        for i in range(m):
            print(k + m, k + i)
        for i in range(m):
            print(k + m - i, k + m)
        for i in range(m):
            print(k, k + m - i)
