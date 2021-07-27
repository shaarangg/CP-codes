with open("input.txt") as f:
    inp = f.readlines()
s = inp[0][: len(inp[0]) - 1]
a = int(inp[1])
with open("output.txt","w") as f:
    if s == "front" and a == 1:
        f.write("L")
    elif s == "front" and a == 2:
        f.write("R")
    elif s == "back" and a == 1:
        f.write("R")
    else:
        f.write("L")
