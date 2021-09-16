import math

point1 = '1. Calculation triangle area by base and height'
point2 = '2. Calculation triangle area by 2 sides and angel between them'
point3 = '3. Exit'
print("Welcome to the triangle calculation tool")
print(f"Menu: \n {point1} \n {point2} \n {point3} \n")
item = 0
while item < 3:
    item = int(input("Enter menu item number: "))
    # print("Menu: {0} {1} {2}".format(point1, point2, point3))

    if item == 1:
        # By base and height
        # base = int(input("Enter base: "))
        # height = int(input("Enter height: "))
        base, height = map(int, input("Enter base and height separated by a space:").split())
        Area = (base * height) / 2
        print(f"Area is: {Area}")
        # break
    elif item == 2:
        # By 2 sides and the angle between them.
        # side1 = int(input("Enter 1st side: "))
        # side2 = int(input("Enter 2nd side: "))
        # angel = int(input("Enter angel between both sides: "))
        side1, side2, angel = map(int,
                                  input("Enter 2 sides and angle(degrees) between them separated by a space:").split())
        a = math.sin(math.radians(angel))
        Area = 0.5 * side1 * side2 * round(a, 2)
        # Area = 0.5 * side1 * side2 * math.sin(math.radians(angel))
        print(f"Area is: {Area}")
        # break
    elif item == 3:
        print('Bye-Bye!')
        break
