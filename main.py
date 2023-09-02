# part 1
def my_name():
    name = "Abdullah"
    print("My name is", name)

my_name()

# part 2
def my_meal(food, drink):
    print(f"I like to eat {food} and while drinking {drink}")

my_meal('burger', "pepsi diet")

# part 3
def cube(number):
    return number*number*number

print(cube(9))

def by_three(number):
    if number %3 == 0:
        return cube(number)
    else:
        return False
print(by_three(4))