try:
    width = float(input("Enter width of a rectangle: "))
    length = float(input("Enter length of a rectangle: "))
    if width == length:
        exit("That look like square")
    area = width * length
    print(area)
except ValueError:
    print("please enter a number")
