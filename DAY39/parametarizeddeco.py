# parametarized decorators:
#     A parameterized decorator is a decorator that can accept arguments of its own. 
# It allows you to customize the behavior of the decorator.

def deco(n):
    def outer(fun):
        def inner():
            for i in range(n):
                fun()
        return inner
    return outer

@deco(3)
def demo():
    print("Hello")

@deco(4)
def demo1():
    print("Bye")

demo()
demo1()
