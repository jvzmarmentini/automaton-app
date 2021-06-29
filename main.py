import networkx as nx


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
    # print("states: " + str(states))
    gramatic = automaton[1].split(",")
    # print("gramatic: " + str(gramatic))
    initial_state = automaton[2]
    # print("initial_state: " + str(initial_state))
    final_states = automaton[3].split(",")
    # print("final_states: " + str(final_states))

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
        graph.add_edge(func[0], func[2],
                       label=func[1])

    for neighbor in graph.neighbors("q1"):
        print(neighbor)
        gramar = graph.get_edge_data("q1", neighbor)
        for simbols in gramar:
            print(gramar[simbols]["label"])


rfile = readFile("automato.txt")
graph = nx.MultiDiGraph()
automaton(rfile, graph)
# print(graph.edges())

# pos = nx.spring_layout(graph)
# nx.draw(graph, pos, with_labels=True, font_weight='bold')
# edge_labels = nx.get_edge_attributes(graph, 'label')
# nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
# plt.show()

A = nx.nx_agraph.to_agraph(graph)
A.layout()
A.draw("file.png")
