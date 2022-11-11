#29.7,8
x = 10
y = 3
def get_quotient_remainder(x, y):
    quotienet = x// y
    remainder = x % y
    return quotienet, remainder

def calc(x,y):
    return print(f'덧셈 : {x+y} 뺄셈 : {x-y} 곱셈 : {x*y} 나눗셈 : {x/y}')

if __name__ == '__main__':

    quotient, remainder  = get_quotient_remainder(x,y)
    print(f'몫 : {quotient} 나머지 : {remainder}')
    x,y = map(int,input().split())
    calc(x,y)
