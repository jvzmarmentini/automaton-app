# TODO
# * define wich nodes are finals
# * create "search" def (to walk over nd_automata)
# * execute "search" with user input word and return state
# * detach core pieces from automaton() and create their own defs
# * optimize coverter
# * write "pydoc"
# * update and improve git docs
# ?* write report

import networkx as nx
from networkx.algorithms.assortativity import neighbor_degree


class automata:
    def __init__(self, states, gramatic, initial_state, final_states):
        self.states = states
        self.gramatic = gramatic
        self.initial_state = initial_state
        self.final_states = final_states


def readFile(file_path):
    # see regex. maybe theres a better way to process the file
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
    states = rfile[0][0].split(",")
    # print("states: " + str(states))
    gramatic = rfile[0][1].split(",")
    # print("gramatic: " + str(gramatic))
    initial_state = rfile[0][2]
    # print("initial_state: " + str(initial_state))
    final_states = rfile[0][3].split(",")
    # print("final_states: " + str(final_states))

    a1 = automata(states, gramatic, initial_state, final_states)

    for node in a1.states:
        nd_automata.add_node(node)

    for func in rfile[1:]:
        nd_automata.add_edge(func[0], func[2],
                             label=func[1])

    # notes from the dev: good luck trying understanding this little mf

    grammy = {}
    for sym in gramatic:
        grammy[sym] = []

    open_list = []
    closed_list = []
    new_automata = {}
    open_list.append([initial_state])
    while(len(open_list) > 0):
        # print("open_list" + str(open_list))
        # print("closed_list" + str(closed_list))
        for element in open_list[0]:
            # print("element: " + str(element))
            for neighbor in nd_automata.neighbors(element):
                # print("neighbor: " + str(neighbor))
                edges = nd_automata.get_edge_data(element, neighbor)
                for sym in edges:
                    if(not (neighbor in grammy[edges[sym]["label"]])):
                        grammy[edges[sym]["label"]].append(neighbor)
                    grammy[edges[sym]["label"]].sort()
            # print("grammy: " + str(grammy))
        new_automata["".join(open_list[0])] = dict(grammy)
        closed_list.append(open_list.pop(0))
        for sym in grammy:
            if (not grammy[sym] == []):
                if(not ((grammy[sym] in open_list) or (grammy[sym] in closed_list))):
                    grammy[sym].sort()
                    open_list.append(grammy[sym])
                grammy[sym] = []
    for node in new_automata:
        d_automata.add_node(node)

    for node in new_automata:
        for edge in new_automata[node]:
            neighbor = "".join(new_automata[node][edge])
            d_automata.add_edge(node, neighbor, label=edge)

    # print(nx.get_node_attributes(d_automata))


rfile = readFile("automato.txt")
nd_automata = nx.MultiDiGraph()
d_automata = nx.DiGraph()

nd2d_converter(rfile, nd_automata)

# relabel nodes on d_automata
old_names = list(d_automata.nodes())
name_map = dict.fromkeys(old_names)
for i in range(len(old_names)):
    name_map[old_names[i]] = i
    #print(str(old_names[i]) + ": " + str(name_map[old_names[i]]))
# print(name_map)
d_automata = nx.relabel_nodes(d_automata, name_map)

print(d_automata.nodes())


A = nx.nx_agraph.to_agraph(nd_automata)
A.layout(prog="dot")
A.draw("automatons/nd_automata.png")

B = nx.nx_agraph.to_agraph(d_automata)
B.layout(prog="dot")
B.draw("automatons/d_automata.png")
