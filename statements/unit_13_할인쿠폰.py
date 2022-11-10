#13.6
x = 5
if x != 10:
    print('ok')

#13.7
price = int(input())
coup = input()

if coup == 'Cash3000':
    print(price - 3000)
elif coup == 'Cash5000':
    print(price - 5000)
else:
    print('잘못 입력')