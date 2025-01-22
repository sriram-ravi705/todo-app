filename_prefix = ['a', 'b', 'c']

for file in filename_prefix:
    file = open(f'../files/{file}.txt', 'r')
    print(file.readlines()[0])
    file.close()
