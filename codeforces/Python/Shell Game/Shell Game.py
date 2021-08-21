with open("input.txt") as f:
    lines = f.readlines()
    index = lines[0]
    index = index[:1]
    for i in range(1, 4):
        i1, i2 = lines[i].split()
        if index == i1:
            index = i2
        elif index == i2:
            index = i1
with open("output.txt", "w") as f:
    f.write(index)
