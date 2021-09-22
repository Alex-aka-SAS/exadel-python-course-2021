import math

point1 = '1. Calculation triangle area by base and height'
point2 = '2. Calculation triangle area by 2 sides and angel between them'
point3 = '3. Exit'
print("Welcome to the triangle calculation tool")
print(f"Menu: \n {point1} \n {point2} \n {point3} \n")
item = 1
while True:
    item = int(input("Enter menu item number: "))
    if item == 1:
        base, height = map(int, input("Enter base and height separated by a space:").split())
        area = (base * height) / 2
        print(f"Area is: {Area}")
    elif item == 2:
        side1, side2, angel = map(int,
                                  input("Enter 2 sides and angle(degrees) between them separated by a space:").split())
        a = math.sin(math.radians(angel))
        Area = 0.5 * side1 * side2 * round(a, 2)
        print(f"Area is: {Area}")
    elif item == 3:
        print('Bye-Bye!')
        break
    else:
        continue
