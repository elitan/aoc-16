dicts = [{} for x in range(0,8)]
with open("data.txt", "r") as f:
    for line in f:
        i = 0
        for c in list(line.rstrip()):
            if c not in dicts[i]:
                dicts[i][c] = 0
            dicts[i][c] += 1
            i+=1

    message = ""
    for i in range(0,8):
        values = list(dicts[i].values())
        keys = list(dicts[i].keys())
        message += str(keys[values.index(max(values))])
    print "1:", message

    message = ""
    for i in range(0,8):
        values = list(dicts[i].values())
        keys = list(dicts[i].keys())
        message += str(keys[values.index(min(values))])
    print "2:", message
