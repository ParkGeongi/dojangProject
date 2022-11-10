#14.6
written_test = 75
coding_test = 'True'
if written_test >= 80 and coding_test == 'True':
    print('합격')
else:
    print('불합격')

#14.7


ko,en,ma,sc = map(int,input().split())
if ko >100 or en >= 100 or ma >= 100 or sc >= 100:
    print('잘못된 점수')
else:
    ls = [ko,en,ma,sc]
    mean = sum(ls) / len(ls)
    if mean >=80 :
        print('합격')
    else:
        print('불합격')
