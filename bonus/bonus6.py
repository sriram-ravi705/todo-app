contents = ['a', 'b', 'c']

filename = ['a.txt', 'b.txt', 'c.txt']

for filename, content in zip(filename, contents):
    file = open(f"../files/{filename}", 'w')
    file.writelines(content)
    file.close()
