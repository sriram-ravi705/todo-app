def get_average():
    with open("../files/avg") as file:
        data = [f.strip('\n') for f in file.readlines()][1:]
        value = [float(i) for i in data]
        output = sum(value) / len(value)
    return output


average = get_average()
print(average)
