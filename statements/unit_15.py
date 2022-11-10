#15.3
x = int(input('입력 :'))
if 11<= x<= 20:
    print('11~20')
elif x<= 30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')

#15.4
age = int(input())
balance = 9000
if 7 <= age <=12:
    print(balance - 650)
elif age <=18:
    print(balance - 1050)
elif age >= 19:
    print(balance - 1250)
else: print('만 7 세 이하 입니다.')