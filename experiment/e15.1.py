import glob

glob = glob.glob("*.txt")
for file in glob:
    with open(file, 'r') as files:
        print([i.strip('\n') for i in files.readlines()])
