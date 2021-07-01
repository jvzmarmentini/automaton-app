# TODO
# * handle "empty symbol" - Tasca
# * update and improve git docs - Panho

import copy
import networkx as nx
from networkx.algorithms.assortativity import neighbor_degree


class automata:
    def __init__(self, states, gramatic, initial_state, final_states):
        self.states = states
        self.gramatic = gramatic
        self.initial_state = initial_state
        self.final_states = final_states


def readFile(file_path):
    with open(file_path) as file:
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace("\n", "")
        lines[0] = lines[0].replace(
            "AUTÔMATO=(", "").replace(")", "").split("},")
        lines[2] = lines[2].replace("Prog", "")
        temp = lines[0][2].split(",{")
        lines[0][2] = temp[0]
        lines[0].append(temp[1])
        lines[0] = [c.replace('{', '').replace('}', '') for c in lines[0]]
        lines = list(filter(None, lines))
        for i, func in enumerate(lines[1:]):
            lines[i+1] = func.replace(")=", ",").replace("(", "").split(",")
        return lines


def nd2d_converter(rfile, nd_automata):
    a1 = automata(
        states=rfile[0][0].split(","),
        gramatic=rfile[0][1].split(","),
        initial_state=rfile[0][2],
        final_states=rfile[0][3].split(",")
    )

    for node in a1.states:
        nd_automata.add_node(
            node, initial=node in a1.initial_state, final=node in a1.final_states)

    for func in rfile[1:]:
        nd_automata.add_edge(func[0], func[2],
                             label=func[1])

    grammy = {sym: [] for sym in a1.gramatic}
    open_list = [[a1.initial_state]]
    closed_list = []
    new_automata = {}
    while(len(open_list) > 0):
        # print("open_list" + str(open_list))
        # print("closed_list" + str(closed_list))
        for element in open_list[0]:
            # print("element: " + str(element))
            for neighbor in nd_automata.neighbors(element):
                # print("neighbor: " + str(neighbor))
                edges = nd_automata.get_edge_data(element, neighbor)
                for sym in edges:
                    if(neighbor not in grammy[edges[sym]["label"]]):
                        grammy[edges[sym]["label"]].append(neighbor)
                    grammy[edges[sym]["label"]].sort()
            # print("grammy: " + str(grammy))
        new_automata["".join(open_list[0])] = copy.deepcopy(grammy.copy())
        # print("new_automatta: " + str(new_automata))
        # print("dict(grammy): " + str(dict(grammy)))
        closed_list.append(open_list.pop(0))
        for sym in grammy:
            if (not grammy[sym] == [] and grammy[sym] not in open_list and closed_list):
                open_list.append(grammy[sym])
            grammy[sym] = []
    for i, node in enumerate(new_automata):
        d_automata.add_node(node, initial=node in a1.initial_state,
                            final=closed_list[i][len(closed_list[i])-1] in a1.final_states)

    for node in new_automata:
        for edge in new_automata[node]:
            if(new_automata[node][edge] == []):
                continue
            neighbor = "".join(new_automata[node][edge])
            d_automata.add_edge(node, neighbor, label=edge)


def wordProcessing(rfile, d_automata, input):
    initial_state = rfile[0][2]
    current = initial_state
    temp = ""
    for letter in input:
        if (letter not in rfile[0][1]):
            return "A palavra contém uma letra que não está na gramática!"
        for neighbor in d_automata.neighbors(current):
            edges = d_automata.get_edge_data(current, neighbor)
            for sym in edges:
                if(letter == edges[sym]["label"]):
                    temp = neighbor
        current = temp

    for node in d_automata.nodes(data=True):
        if(node[0] == current):
            return node[1]["final"]
    return False


rfile = readFile("automato.txt")
nd_automata = nx.MultiDiGraph()
d_automata = nx.MultiDiGraph()

nd2d_converter(rfile, nd_automata)
print(wordProcessing(rfile, d_automata, "LI"))

# old_names = list(d_automata.nodes())

# name_map = dict.fromkeys(old_names)
mapping = dict(zip(d_automata.nodes(), "pqrstuvwxyzabcdefghijklmno"))
d_automata = nx.relabel_nodes(d_automata, mapping)

final = list(filter(lambda x: x[1]['final'] ==
             True, nd_automata.nodes(data=True)))
initial = list(filter(lambda x: x[1]['initial'] ==
                      True, nd_automata.nodes(data=True)))[0][0]
nd_automata.nodes[initial]['style'] = 'filled'
nd_automata.nodes[initial]['fillcolor'] = 'green'
for f in final:
    nd_automata.nodes[f[0]]['shape'] = 'doublecircle'
A = nx.nx_agraph.to_agraph(nd_automata)
A.layout(prog="dot")
A.draw("automatons/nd_automata.png")

# print(d_automata.nodes(data=True))
final = list(filter(lambda x: x[1]['final'] ==
             True, d_automata.nodes(data=True)))
initial = list(filter(lambda x: x[1]['initial'] ==
                      True, d_automata.nodes(data=True)))[0][0]
d_automata.nodes[initial]['style'] = 'filled'
d_automata.nodes[initial]['fillcolor'] = 'green'
for f in final:
    d_automata.nodes[f[0]]['shape'] = 'doublecircle'
B = nx.nx_agraph.to_agraph(d_automata)
B.layout(prog="dot")
B.draw("automatons/d_automata.png")
