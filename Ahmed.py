
print("hello world")

numb = [0, 1, 2, 3, 4, 5, 6]
for x in numb:
  print(x)
  


def add_car(money, saving, car):
    if money > saving:
        print("not enough money")
    else:
        saving = saving - money
        car = car + money
    print("added + money")
    
add_car(50, 100, 0)