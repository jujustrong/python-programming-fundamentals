import time
import math

def rectangle():
    print("Let's calculate the area of a rectangle...")
    time.sleep(2)
    l = int(input("What's the length? "))
    w = int(input("What's the width? "))
    area = l*w
    time.sleep(1)
    print(f"Rectangle area = {area:.0f}")

def circle():
    print("Let's calculate the area of a circle...")
    time.sleep(2)
    radius = int(input("What's the radius? "))
    area = math.pi*(radius**2)
    time.sleep(1)
    print(f"Circle area = {area:.0f}")

def triangle():
    print("Let's calculate the area of a triangle...")
    time.sleep(2)
    base = int(input("What's the base length? "))
    height = int(input("What's the height? "))
    area = .5*base*height
    time.sleep(1)
    print(f"Triangle area = {area:.0f}")

def area_calculator():
    print("Which shape would you like to choose?")
    i = True
    while i:
        choice = input("Press 1 for rectangle, Press 2 for circle, Press 3 for triangle: ")
        if choice == "1":
            return rectangle()
        elif choice == "2":
            return circle()
        elif choice == "3":
            return triangle()
        else:
            print("Please choose 1, 2, or 3")
            i = True

area_calculator()