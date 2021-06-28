
with open("automato.txt") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
    lines = list(filter(None, lines))
    print(lines)