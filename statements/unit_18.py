#18.5
i = 0
while True:
    if i % 10 == 3:
        print(i,end=" ")
    elif i == 74:
        break\

    i +=1

#18.6
start,stop = map(int,input().split())
i = start

while True:
    if i % 10 == 3:
        i = i+1
        continue
    elif i > stop:
        break
    print(i, end=" ")
    i=i+1