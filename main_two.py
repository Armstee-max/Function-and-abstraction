import statistics

def new_function(name, age, course = "python"):
    print(f"Hello {name}, you are {age} years old and you are studying {course}")


new_function("Armstrong", 22, "Java")

def area_triangle(base, height, default = 0.5):
    area = default * base * height
    return area

calculation = area_triangle(12, 5)
print(int(calculation))
calculation_one = area_triangle(6, 7)
print(int(calculation_one))

name = "David"

def scoping():
    gender = "male"
    print(f"{name} is a {gender}")

scoping()
print(name)


# average, median, mode 


number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))
number3 = int(input("Enter your third number: "))
number4 = int(input("Enter your fourth number: "))
number5 = int(input("Enter your fifth number: "))

def mean():
    average = (number1 + number2 + number3 + number4 + number5) / 5
    return average

def median():
    numbers = [number1, number2, number3, number4, number5]
    middle_number = statistics.median(numbers)
    return middle_number

def mode():
    numbers = [number1, number2, number3, number4, number5]
    high_freq = statistics.mode(numbers)
    return high_freq

average = mean()
middle_num = median()
highest_freq = mode()
print(f"The mean is {average}")
print(f"The median is {middle_num}")
print(f"The mode is {highest_freq}")

# Unit test
def add(a, b):
    addition = a + b
    return addition

calc = add(3, 2)
assert add(3, 5) == 18 
print(calc)
