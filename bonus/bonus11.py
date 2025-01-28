def convert(feet_inches):
    list_of_feet = feet_inches.split(" ")
    meter = float(list_of_feet[0]) * 0.3048 + float(list_of_feet[1]) * 0.0254
    print(f'meter is {meter}')
    return meter

feet_inches = input('Enter feet and inches: ')
result = convert(feet_inches)

if result < 1:
    print('kid is too small')
else:
    print('kid can use the slide')
