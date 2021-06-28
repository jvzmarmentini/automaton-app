import matplotlib.pyplot as plt
import networkx as nx
import math

def readFile(file_path):
    with open(file_path) as file:
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace("\n", "")
        lines[0] = lines[0].replace("AUTÔMATO=(", "")
        lines[0] = lines[0].replace(")", "")
        return list(filter(None, lines))

def automaton(rfile):
    states = rfile[0]
    print(states)
    states = states.split("},")
    print(states)
    temp = states[2].split(",{")
    states[2] = temp[0]
    states.append(temp[1])

    for i in range(len(states)):
        states[i] = states[i].replace("{", "")
        states[i] = states[i].replace("}", "")
    print(states)

rfile = readFile("automato.txt")
print(rfile)
automaton(rfile)
graph = nx.Graph()
# nx.draw(graph, with_labels=True, font_weight='bold')
# plt.show()