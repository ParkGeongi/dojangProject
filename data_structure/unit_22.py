#22.9
a = ['alpha','bravo','charlie','delta','echo','foxtrot','golf','hotel','india']
b = [i for i in a if len(i) == 5]

print(b)

#22.10
a,b = map(int,input().split()) #a : 1~20 b: 10~30
ls = [2**i for i in range(a,b+1)]
del ls[1]
del ls[-2]
print(ls)
