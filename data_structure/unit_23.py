#23.6
a = [[[0 for i in range(3)]for i in range(4)]for i in range(2)]
print(a)

#23.7

row, col = map(int,input().split())
matrix = []

for i in range(row):
    for j in range(col):
        matrix.append(list(input()))




