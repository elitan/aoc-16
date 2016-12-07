with open("data.txt", "r") as f:
    current = 3
    pos = [0,0]
    directions = [[1,0], [0,-1], [-1,0], [0,1]]
    commands = f.read().rstrip().split(", ")
    for command in commands:
        if command.startswith("R"):
            current = (current + 1) % 4
        else:
            current = (current - 1) % 4

        pos[0] += int(command[1:]) * directions[current][0]
        pos[1] += int(command[1:]) * directions[current][1]

    print "1:", abs(pos[0])+abs(pos[1])

with open("data.txt", "r") as f:
    current = 3
    pos = [0,0]
    myList = []
    myList.append((pos[0],pos[1]))
    directions = [[1,0], [0,-1], [-1,0], [0,1]]
    commands = f.read().rstrip().split(", ")
    for command in commands:
        if command.startswith("R"):
            current = (current + 1) % 4
        else:
            current = (current - 1) % 4

        for i in range(0, int(command[1:])):
            pos[0] += directions[current][0]
            pos[1] += directions[current][1]

            if (pos[0], pos[1]) in myList:
                break
            else:
                myList.append((pos[0],pos[1]))
        else:
            continue
        break

    #print pos
    print "2:", abs(pos[0])+abs(pos[1])
