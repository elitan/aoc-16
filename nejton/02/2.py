def pos(old, command, valid):
    if command == 'U':
        new = (old[0], old[1]+1)
    elif command == 'D':
        new = (old[0], old[1]-1)
    elif command == 'R':
        new = (old[0]+1, old[1])
    elif command == 'L':
        new = (old[0]-1, old[1])
    if new in valid:
        return new
    return old



with open("data.txt", "r") as f:
    current1 = (1,1)
    current2 = (0,2)
    valid1 = {(0,0):'7', (0,1):'4', (0,2):'1', (1,0):'8', (1,1):'5', (1,2):'2', (2,0):'9', (2,1):'6', (2,2):'3'}
    valid2 = {(2,4):'1', (1,3):'2', (2,3):'3', (3,3):'4', (0,2):'5', (1,2):'6', (2,2):'7', (3,2):'8', (4,2):'9', (1,1):'A', (2,1):'B', (3,1):'C', (2,0):'D'}
    task1 = ""
    task2 = ""
    for line in f:
        for c in line.rstrip():
            current1 = pos(current1, c, valid1)
            current2 = pos(current2, c, valid2)
        task1 += valid1[current1]
        task2 += valid2[current2]

    print task1
    print task2
