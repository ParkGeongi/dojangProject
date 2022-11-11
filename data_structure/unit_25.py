#25.7

maria = {'korean':94,'english':91,'mathmetics':89,'science':83}
average = sum(maria.values()) / len(maria)
print(average)

#25.8
dic = {}

a = input().split()
b = map(int,input().split())
c = dict(zip(a,b))

print(a)
print(b)
print(c)

del c['delta']
print(c)