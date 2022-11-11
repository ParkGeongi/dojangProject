#24.4

path ='C:/Users/AIA/dojangProject/main'
x = path.split('/')
filename = x[-1]
print(filename)

#24.5
a = input().split(" ")
print(a.count('the'))

#24.6
x = input().split(';')
x= list(map(int,x))
print(x)
for i in range(len(x)-1):
    for j in range(len(x)-1):
        if x[j]<x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]

print(x)

for i in x:
    a = '%9s' % format(i,',')
    print(a)

