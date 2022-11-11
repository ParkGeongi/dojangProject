
#26.8
a ={i for i in range(1,101) if i % 3 == 0}

b = {i for i in range(1,101) if i % 5 == 0}
print(a & b)

#26.9
x = 0
y= 0
set1 = set()
set2 = set()
a = int(input())
b = int(input())
for i in range(a+1):
    if a % (i+1) == 0:
        x = i+1
        set1.update({x})
print(set1)

for i in range(b+1):
    if b % (i + 1) == 0:
        y = i + 1
        set2.update({y})
print(set2)
print(sum( set1&set2))
