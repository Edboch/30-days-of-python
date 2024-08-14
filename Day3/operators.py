#DAY 3
import math

age = 23
h = 187.6
comp = 6+4j

print(True)

base = int(input("Enter base: "))
height = int(input("Enter height:"))
area = base * height *0.5
print('The area of the triangle is:', area)

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is ", perimeter)

rlength = int(input("Enter rectangle length: "))
rheight = int(input("Enter rectangle height: "))
rarea = rlength * rheight
rperim = 2*(rlength + rheight)
print("rectangle area ", rarea)
print("rectangle perimeter ", rperim)

radius = int(input("input radius: "))
carea = math.pi * radius * radius
cperim = math.pi * 2 * radius
print("circle area ", carea)
print("circle perimeter ", cperim)

#y = 2x-2
print("x-intercept", 1)
print("y-intercept", -1)
print("slope", 2)

# (2,2) (8,10)
print("Slope ", 2)
print("euc", math.sqrt(80))

def quadratic_formula(a,b,c):
    sol1 = (-b+(math.sqrt((b**2) - (4*a*c))))/(2*a)
    sol2 = (-b-(math.sqrt((b**2) - (4*a*c))))/(2*a)
    return sol1, sol2

sol1, sol2 = quadratic_formula(1,6,9)
print("y solutions for y = x^2 + 6x + 9")
print("y = ", sol1)
print("y = ", sol2)

print(not (len("python")==len("dragon")))
print("on" in ("dragon" and "python"))
print("jargon" in "I hope this course is not full of jargon")
print("on" not in "dragon" and "python")
print(str(float(len("python"))))

if 6%2:
    print("Odd")
else:
    print("Even")

print(7//3 == int(2.7))
print(type("10") == type(10))
print(int(9.8) == 10)

hours = float(input("Hours: "))
rate = float(input("rate per hour: "))
print("Your weekly earning is: ", hours*rate)

lived = int(input("Enter number of years you have lived: "))
print("You have lived for", lived*365*24*60*60, "seconds")
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")