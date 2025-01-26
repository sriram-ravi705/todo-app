filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]
for filename in filenames:
    index_of_dot = filename.index('.')
    print(filename[0:index_of_dot].capitalize())
