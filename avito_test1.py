"""

Дан IPv4 адрес, записанный в виде 4х октетов, разделённых точкой.
Вернуть строковое значение 'true', если он валидный, и 'false', если нет.
Примеры корректного адреса: 0.0.0.0, 1.2.3.4, 255.255.255.255
Примеры некорректного адреса: 1.2.3, 453534, 999.999.999.999, -10.-20.-30.-40

Sample Input 1:
4657859950000

Sample Output 1:
false

Sample Input 2:
127.0.0.1

Sample Output 2:
true

"""


def check(ss):
    s = ss
    for j in range(4):
        if j == 3:
            s1 = s
        else:
            i = s.find('.')
            if i == -1:
                return False
            s1 = s[:i]
        try:
            a = int(s1)
        except:
            return False
        if (a < 0) or (a > 255):
            return False
        if j < 3:
            s = s[i + 1:]
    return True


if check(input()):
    print('true')
else:
    print('false')
