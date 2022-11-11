#36.8,9

class AdvancedList(object):
     def __init__(self,x):
        self.x = x

     def __str__(self):
        pass

     def replace(self,a,b):
        x = self.x
        for i, j in enumerate(x):
            if j == a:
                x[i] = b

        return x

class Animal:
    def __init__(self, Wing):
        self.Wing = Wing
    def __str__(self):
        pass
    def eat(self):
        print('먹다')

class Wing:

    def __init__(self):
        pass
    def __str__(self):
        pass
    def flap(self):
        print('파닥거리다')
class Bird(Animal,Wing):
    def __init__(self):
        pass
    def __str__(self):
        pass
    def fly(self):
        print("날다")




if __name__ == '__main__':
    ls = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    a =AdvancedList(ls)
    a.replace(1,100)
    print(ls)

    b = Bird()
    b.eat()
    b.flap()
    b.fly()
    print(issubclass(Bird,Animal))
    print(issubclass(Bird, Wing))