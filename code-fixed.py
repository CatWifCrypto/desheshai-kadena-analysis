import numpy as np
from numpy.random import exponential as Exp
import networkx as nx
import matplotlib.pyplot as plt
import random
import scipy

# Use a fixed seed for the random number generator so results are repeatable
random.seed(42)
np.random.seed(42)

def read_values(filename):
    f = open(filename, "r")
    strs = f.readlines()
    f.close()
    return [float(s.strip().split(",")[1]) for s in strs[1:]]
    # return [float(s.strip()) for s in strs[1:]]

stalls = read_values("data/stalls-real.csv")
np.random.shuffle(stalls)
stall_ind = 0

def next_rand_orig():
    return Exp()

def next_rand_good():
    global stalls
    global stall_ind
    v = stalls[stall_ind] / 30.0
    stall_ind += 1
    return v

def doublePetersen():
    G = nx.Graph()
    G.add_nodes_from(range(1,21))
    G.add_edges_from([(1,3),(1,4),(1,12),
                      (2,4),(2,5),(2,11),
                      (3,7),(3,19),
                      (4,6),
                      (5,10),(5,20),
                      (6,13),(6,14),
                      (7,8),(7,11),
                      (8,9),(8,14),
                      (9,10),(9,13),
                      (10,12),
                      (11,15),
                      (12,18),
                      (13,16),
                      (14,17),
                      (15,16),(15,18),
                      (16,19),
                      (17,18),(17,20),
                      (19,20)])
    return G

def ringGraph():
    G = nx.Graph()
    G.add_nodes_from(range(1,21))
    G.add_edges_from([(1,2),
                      (2,3),
                      (3,4),
                      (4,5),
                      (5,6),
                      (6,7),
                      (7,8),
                      (8,9),
                      (9,10),
                      (10,11),
                      (11,12),
                      (12,13),
                      (13,14),
                      (14,15),
                      (15,16),
                      (16,17),
                      (17,18),
                      (18,19),
                      (19,20),
                      (20,1)])
    return G

def ringGraph50():
    G = nx.Graph()
    G.add_nodes_from(range(1,51))
    G.add_edges_from([(1,2),
                      (2,3),
                      (3,4),
                      (4,5),
                      (5,6),
                      (6,7),
                      (7,8),
                      (8,9),
                      (9,10),
                      (10,11),
                      (11,12),
                      (12,13),
                      (13,14),
                      (14,15),
                      (15,16),
                      (16,17),
                      (17,18),
                      (18,19),
                      (19,20),
                      (20,21),
                      (21,22),
                      (22,23),
                      (23,24),
                      (24,25),
                      (25,26),
                      (26,27),
                      (27,28),
                      (28,29),
                      (29,30),
                      (30,31),
                      (31,32),
                      (32,33),
                      (33,34),
                      (34,35),
                      (35,36),
                      (36,37),
                      (37,38),
                      (38,39),
                      (39,40),
                      (40,41),
                      (41,42),
                      (42,43),
                      (43,44),
                      (44,45),
                      (45,46),
                      (46,47),
                      (47,48),
                      (48,49),
                      (49,50),
                      (50,1)])
    return G

def hoffmanSingleton():
    G = nx.Graph()
    G.add_nodes_from(range(1,51))
    G.add_edges_from([(1,3),(1,4),(1,26),(1,31),(1,36),(1,41),(1,46),
                      (2,4),(2,5),(2,27),(2,32),(2,37),(2,42),(2,47),
                      (3,5),(3,28),(3,33),(3,38),(3,43),(3,48),
                      (4,29),(4,34),(4,39),(4,44),(4,49),
                      (5,30),(5,35),(5,40),(5,45),(5,50),
                      (6,8),(6,9),(6,26),(6,35),(6,39),(6,43),(6,47),
                      (7,9),(7,10),(7,27),(7,31),(7,40),(7,44),(7,48),
                      (8,10),(8,28),(8,32),(8,36),(8,45),(8,49),
                      (9,29),(9,33),(9,37),(9,41),(9,50),
                      (10,30),(10,34),(10,38),(10,42),(10,46),
                      (11,13),(11,14),(11,26),(11,34),(11,37),(11,45),(11,48),
                      (12,14),(12,15),(12,27),(12,35),(12,38),(12,41),(12,49),
                      (13,15),(13,28),(13,31),(13,39),(13,42),(13,50),
                      (14,29),(14,32),(14,40),(14,43),(14,46),
                      (15,30),(15,33),(15,36),(15,44),(15,47),
                      (16,18),(16,19),(16,26),(16,33),(16,40),(16,42),(16,49),
                      (17,19),(17,20),(17,27),(17,34),(17,36),(17,43),(17,50),
                      (18,20),(18,28),(18,35),(18,37),(18,44),(18,46),
                      (19,29),(19,31),(19,38),(19,45),(19,47),
                      (20,30),(20,32),(20,39),(20,41),(20,48),
                      (21,23),(21,24),(21,26),(21,32),(21,38),(21,44),(21,50),
                      (22,24),(22,25),(22,27),(22,33),(22,39),(22,45),(22,46),
                      (23,25),(23,28),(23,34),(23,40),(23,41),(23,47),
                      (24,29),(24,35),(24,36),(24,42),(24,48),
                      (25,30),(25,31),(25,37),(25,43),(25,49),
                      (26,27),(26,30),
                      (27,28),(28,29),
                      (29,30),
                      (31,32),(31,35),
                      (32,33),
                      (33,34),
                      (34,35),
                      (36,37),(36,40),
                      (37,38),
                      (38,39),
                      (39,40),
                      (41,42),(41,45),
                      (42,43),
                      (43,44),
                      (44,45),
                      (46,47),(46,50),
                      (47,48),
                      (48,49),
                      (49,50)])
    return G

def exp_partial_sums(d):
    ps = [0]
    for _ in range(d):
        ps.append(ps[-1] + Exp())
    return ps

#convert a base graph into a zero layer
def zero_layer(G):
    RG = nx.DiGraph()
    RG.graph['chains_data'] = {}
    for v in list(G.nodes):
        RG.add_node((v,0))
        RG.graph['chains_data'][v] = {
            "len" : 0,
            "last_block" : 0,
            "one_before_last_block" : 0,
            "neighbors" : list(G.neighbors(v)) + [v]
        }
    return RG

#given a refernce graph and a chain, find the stall time for the next block
def stall_time(RG, v):
    cd = RG.graph['chains_data']
    l = cd[v]["len"]
    if l == 0:
        return 0
    stall = 0
    for w in cd[v]["neighbors"]:
        tw = cd[w]["last_block"] if cd[w]["len"] == l else cd[w]["one_before_last_block"]

#Given a base graph G and a reference graph RG add a new layer by adding
#to each chain a block with time M+Exp where M is the maximal time of this block
#and its neighbours in the current layer graph.
def add_layer(RG):
    cd = RG.graph['chains_data']
    l = cd[1]["len"]
    for v in RG.graph['chains_data']:
        assert(l == cd[v]["len"])
        stall = next_rand_good()
        next_time = max([cd[w]["last_block" if cd[w]["len"] == l else "one_before_last_block"]
                     for w in cd[v]["neighbors"]]) + stall
        RG.add_node((v,next_time))
        RG.add_edges_from([((v,next_time),(w,cd[w]["last_block" if cd[w]["len"] == l else "one_before_last_block"])) for w in cd[v]["neighbors"]])
        cd[v]["one_before_last_block"] = cd[v]["last_block"]
        cd[v]["last_block"] = next_time
        cd[v]["len"] += 1

#For every chain, compute the earliest time it learned of the vertex (1,0)
def umbrella(G):
    disc_times = {} #return a list of times each chain learned of (1,0)
    for (x,r) in list(G.nodes):
        if x in disc_times:
            if r > disc_times[x]:
                continue
        if nx.has_path(G,(x,r),(1,0)):
            disc_times[x] = r
    return sorted(disc_times.values())

#Output the times for a single simulation on base graph G
def simulation(G):
    RG = zero_layer(G)
    layers = 0
    while len(umbrella(RG)) < G.number_of_nodes():
        add_layer(RG)
        layers += 1
    return umbrella(RG)

#Do n simulations on base graph G and output the average
def average_sims(G,n):
    cur = simulation(G)
    if n == 1:
        return cur
    for i in range(2,n+1):
        cur = [(i-1)*x/i + y/i for (x,y) in zip(cur,simulation(G))]
    return cur

def calc_plot_points(G,n):
    chains = G.number_of_nodes()
    xs = [0.5*k/chains for k in range(1,chains+1)]
    ys = average_sims(G,n)
    return (xs,ys)

def draw_graph(G,n):
    (xs,ys) = calc_plot_points(G,n)
    plt.plot(xs, ys, color ="red")
    plt.show()

def print_results(graph_name, g):
    num_sims = 1000 if nx.diameter(g) <= 10 else 100
    (xs,ys) = calc_plot_points(g, num_sims)
    bd = ys[len(ys)-1]
    print(f'| {graph_name:<42} | {nx.diameter(g):>8} | {round(bd, 2):>11} |')

def random_graph_with_degree_diameter(n, deg, diam):
    G = None
    i = 1
    #print(f"Generating graph of degree {deg} diameter {diam}")
    while True:
        #if i % 100 == 0:
        #    print(i)
        G = nx.random_regular_graph(deg,n)
        if nx.is_connected(G) and (nx.diameter(G) == diam or i > 10000000):
            break
        i += 1
    return G

chainweb20 = doublePetersen()
desheshai_random = random_graph_with_degree_diameter(100,6,4)
ring20 = ringGraph()
ring50 = ringGraph50()
random_diameter_6 = random_graph_with_degree_diameter(100,5,6)
c50 = hoffmanSingleton()

def show_all_graphs():
    print("| Graph                                      | Diameter | Sim Results |")
    print("| :----------------------------------------- | -------: | ----------: |")
    print_results("Chainweb current 20-chain graph", chainweb20)
    print_results("DesheShai random graph", desheshai_random)
    print_results("50-chain graph from Kadena's GitHub", c50)
    print_results("20-chain ring graph", ring20)
    print_results("50-chain ring graph", ring50)
    print_results("Random diameter 6 graph", random_diameter_6)

show_all_graphs()
