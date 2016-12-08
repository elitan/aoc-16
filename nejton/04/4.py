with open("data.txt", "r") as f, open("output.txt", "w") as out:
    counter = 0
    for line in f:
        numChars = {}
        cells = line.split('-')
        thingy = cells[len(cells)-1].split('[')
        num = int(thingy[0])
        code = thingy[1][:-2]
        cells = cells[:-1]

        for cell in cells:
            for c in cell:
                if c not in numChars:
                    numChars[c] = 0
                numChars[c] += 1
        bestChars = [v[0] for v in sorted(numChars.items(),key=lambda(k,v): (-v,k))]
        bestChars = bestChars[:5]

        for bestChar in bestChars:
            if bestChar not in code:
                break
        else:
            counter += num
            out.write(line[:-8]+"\n")

    print "1:", counter

with open("output.txt", "r") as f:
    for line in f:
        words = line.rstrip().split("-")
        sector = int(words[-1])
        key = sector%26
        words = words[:-1]
        output = ""

        for word in words:
            for c in word:
                if (ord(c) + key) > ord('z'):
                    c = chr(ord(c)-26)
                output += chr(ord(c)+key)
            output += " "

        if "north" in output:
            print output, sector
