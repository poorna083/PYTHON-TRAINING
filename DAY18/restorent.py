print("==WELCOME TO QSPIDERS RESTORENT==")
print("""choose the food type
      1 BREAKFAST
      2 LUNCH
      3 DINNER""")
food_input=int(input("Enter the food type:"))

break_fast={"Idli":10,"Dosa":25,"Pongal":30,"Puri":15,"Vada":5}
lunch={"Chicken Biryani":150,"Meals":70,"Chicken Rice":100,"Sambar Rice":50,"Curd Rice":25}
dinner={"Parotta":15,"Nudles":70,"Mutton Biryani":200,"Upma":20,"Idiyappam":5}

if food_input==1:
    print("====MENU====")
    print(break_fast)
    item_input=input(("enter the item: ")).title()
    quantity = int(input("enter the quantity:"))
    if item_input in break_fast:
            print("===BILL===")
            print(f'item        {item_input} ')
            print(f'quantity    {quantity}')
            print(f'Total :     {break_fast[item_input]*quantity} rupess')
elif food_input==2:
    print("====MENU====")
    print(lunch)
    item_input=input(("enter the item: ")).title()
    quantity = int(input("enter the quantity:"))
    if item_input in lunch:
            print("===BILL===")
            print(f'item        {item_input} ')
            print(f'quantity    {quantity}')
            print(f'Total :     {lunch[item_input]*quantity} rupess')
elif food_input==3:
    print("====MENU====")
    print(dinner)
    item_input=input(("enter the item: ")).title()
    quantity = int(input("enter the quantity:"))
    if item_input in dinner:
            print("===BILL===")
            print(f'item        {item_input} ')
            print(f'quantity    {quantity}')
            print(f'Total :     {dinner[item_input]*quantity} rupess')
else:
    print("Invalid input...")
    print("RE-CHECK AGAIN AND ENTER A VALID INPUT")