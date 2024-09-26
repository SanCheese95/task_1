n = int(input('Введите номер билета:'))

a = n // 100000
b = (n // 10000) % 10
c = (n // 1000) % 10
d = (n // 100) % 10
e = (n // 10) % 10
f = n % 10

res_1 = a + b + c
res_2 = d + e + f

if res_1 == res_2:
    print('yes')
else:
    print('no')