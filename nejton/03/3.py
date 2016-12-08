with open("data.txt", "r") as f:
    counter = 0
    for line in f:
        sides = [int(i) for i in line.split()]
        if sum(sides[:2]) > sides[2] and sum(sides[1:]) > sides[0] and (sides[0] + sides[2]) > sides[1]:
            counter += 1
    print counter

with open("data.txt", "r") as f:
    counter = 0
    tab1 = []
    tab2 = []
    tab3 = []

    for line in f:
        row = [int(i) for i in line.split()]
        tab1.append(row[0])
        tab2.append(row[1])
        tab3.append(row[2])

    tab1.extend(tab2)
    tab1.extend(tab3)

    for i in range(0,len(tab1),3):
        if sum(tab1[i:i+2]) > tab1[i+2] and sum(tab1[i+1:i+3]) > tab1[i] and (tab1[i] + tab1[i+2]) > tab1[i+1]:
            counter += 1

    print tab1[0], tab1[1], tab1[2]
    print tab1[0:2]
    print counter
