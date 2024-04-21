import numpy as np
from numpy.random import exponential as Exp
import networkx as nx
import matplotlib.pyplot as plt

# Use a fixed seed for the random number generator so results are repeatable
np.random.seed(42)

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
        stall = Exp()
        print("bad stall,%.3f"% (stall*30))
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

def draw_graph(G,n):
    chains = G.number_of_nodes()
    xs = [0.5*k/chains for k in range(1,chains+1)]
    ys = average_sims(G,n)
    plt.plot(xs, ys, color ="red")
    plt.show()

#first graph: average 1000 simulations on the double Petersen graph
draw_graph(doublePetersen(),1000)

#second graph: sample random graph of degree 6 and diameter 4, average 100 simulation
# repeat for 10 random graphs, average answer
res = []

for _ in range(10):
    G = None
    while True:
        G = nx.random_regular_graph(6,100)
        if nx.diameter(G) == 4:
            break
    res.append(average_sims(G,100))

# print(res)
#
# ys = [sum([x[i] for x in res])/len(res) for i in range(len(res[0]))]
# xs = [0.5*k/len(res[0]) for k in range(1,len(res[0])+1)]
# plt.plot(xs, ys, color ="red")
# plt.show()
