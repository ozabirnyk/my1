'''

Note: Тестовые данные подаются через стандартный поток ввода stdin и на вход программы поступают в виде строки.
Каждая строка ввода считывается отдельно.
Ответ нужно вывести в консоль (стандартный потока вывода  stdout)
Запрещено использование внешних библиотек.
Верните список, содержащий результат обхода квадратной матрицы по спирали: против часовой стрелки, начиная с левого верхнего угла.
На вход подаётся размер матрицы, за которым следуют разделённые пробелами строки матрицы.
Размерность матрицы больше 0.

Sample Input 1:
2
1 2
3 4

Sample Output 1:
1 3 4 2

Sample Input 2:
3
63 83 3
23 43 22
33 44 55

Sample Output 2:
63 23 33 44 55 22 3 83 43

'''

n = int(input())                # n - array size
a = []
for i in range(n):
    a.append(input().split(' '))

for k in range((n + 1) // 2):   # k is a shift of inner square
    m = n - 2 * k - 1           # m is a size of inner square
    if m == 0:
        print(a[k][k], end=' ') # the center of 1x1 square
    else:                       # the square is larger than 1x1
        for i in range(m):
            print(a[k + i][k], end=' ')
        for i in range(m):
            print(a[k + m][k + i], end=' ')
        for i in range(m):
            print(a[k + m - i][k + m], end=' ')
        for i in range(m):
            print(a[k][k + m - i], end=' ')
print('')
 
