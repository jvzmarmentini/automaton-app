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
    automaton = rfile[0]
    #print(automaton)
    automaton = automaton.split("},")
    #print(automaton)
    temp = automaton[2].split(",{")
    automaton[2] = temp[0]
    automaton.append(temp[1])

    for i in range(len(automaton)):
        automaton[i] = automaton[i].replace("{", "")
        automaton[i] = automaton[i].replace("}", "")
    states = automaton[0].split(",")
    print("states: " + str(states))

    functions = []
    for func in rfile:
        if(rfile.index(func) > 1):
            functions.append(func)

    print(functions)

rfile = readFile("automato.txt")
print(rfile)
automaton(rfile)
graph = nx.Graph()
# nx.draw(graph, with_labels=True, font_weight='bold')
# plt.show()