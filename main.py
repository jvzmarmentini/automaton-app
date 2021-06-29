import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import to_agraph 

def readFile(file_path):
    with open(file_path) as file:
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace("\n", "")
        lines[0] = lines[0].replace("AUTÔMATO=(", "")
        lines[0] = lines[0].replace(")", "")
        lines[2] = lines[2].replace("Prog", "")
        return list(filter(None, lines))

def automaton(rfile, graph):
    automaton = rfile[0]
    automaton = automaton.split("},")
    temp = automaton[2].split(",{")
    automaton[2] = temp[0]
    automaton.append(temp[1])

    for i in range(len(automaton)):
        automaton[i] = automaton[i].replace("{", "")
        automaton[i] = automaton[i].replace("}", "")
    states = automaton[0].split(",")
    print("states: " + str(states))
    gramatic = automaton[1].split(",")
    print("gramatic: " + str(gramatic))
    initial_state = automaton[2]
    print("initial_state: " + str(initial_state))
    final_states = automaton[3].split(",")
    print("final_states: " + str(final_states))

    for node in states:
        graph.add_node(node)

    functions = []
    for func in rfile:
        if(rfile.index(func) > 0):
            functions.append(func)

    for func in functions:
        func = func.replace(")=", ",")
        func = func.replace("(", "")
        func = func.split(",")
        left_node = func[0]
        right_node = func[2]
        simba = func[1]
        graph.add_edge(left_node, right_node, simba=simba)

    print(functions)

rfile = readFile("automato.txt")
print(rfile)
graph = nx.DiGraph()
automaton(rfile, graph)
pos = nx.spring_layout(graph)
print(graph.edges)
nx.draw(graph, pos, with_labels=True, font_weight='bold')

edge_labels = nx.get_edge_attributes(graph,'simba')
print(edge_labels)
nx.draw_networkx_edge_labels(graph, pos, edge_labels = edge_labels)

plt.show()