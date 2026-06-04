class Demo:
    a=10
    b=20
    c=30
obj1=Demo()


class demo1:
    a=10
    b=20
    c=30
    def demo(self):
        d=40
        e=50
        print(self)
obj=demo1()
obj.demo()


# program:
class sample():
    def display(self,a,b):
        print(a,b)
obj=sample()
a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
obj.display(a,b)


# updation in class and object:-
    # to acess variables
    # ------------------------------
    # class_name.variable_name
    # object_name.variable_name
# =================================================
# program:
class Demo:
    a=10
    b=20
    c=30
d1=Demo()
d2=Demo()
d1.a=100
print(d1.a,d2.a,Demo.a)
d2.b=200
print(d1.b,d2.b,Demo.b)
Demo.c=300
print(d1.c,d2.c,Demo.c)

# ========================================================

class Demo:
    a=10
    b=20
    c=30
    def display(self):
        print(f'a={self.a} \n b={self.b} \n c={self.c}')
d1=Demo()
d2=Demo()
d1.a=100
d2.a=200
d1.display()
d2.display()

# ==========================================================

class Bank:
    b_name='icici'
    ifsc_code='ici1234'
    adress='chrompet'
    def __init__(self,name,amt):
        print(f"""BANK NAME:{self.b_name} \n
                IFSC CODE {self.ifsc_code} \n
                ADDRESS :{self.adress} \n
                USER NAME:{self.name} \n
                BALANCE {self.balnce}""")
b1=Bank('dinga',1000)
b2=Bank('dingi',500)
b1.display()
print('='*20)
b2.display()
        