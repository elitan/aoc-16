with open("data.txt", "r") as f:
    for line in f:
        print line.lstrip().rstrip().split("\t")
