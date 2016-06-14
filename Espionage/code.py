import sys
from operator import itemgetter

def eval():
    all_lines = [line for line in sys.stdin]
    l1 = all_lines[0].split(" ")
    edge_count = int(l1[1])
    edges = [make_tuple(line) for line in all_lines[1:edge_count+1]]
    edges_to_check = [make_set(line) for line in all_lines[edge_count+1:len(all_lines)]]
    all_nodes = create_nodes(edges)
    res = kruskal(list(all_nodes), edges, edges_to_check)
    res_tuple = convert_to_set(res)
    output_result(res_tuple, edges_to_check)

def output_result(res, edges):
    for e in edges:
        if e in res:
            print("yes")
        else:
            print("no")

def convert_to_set(res):
    res_tuple=[]
    for r in res:
        (e1, e2, w) = r
        res_tuple.append({e1, e2})
    return res_tuple

def create_nodes(edges):
    all_nodes = set()
    for edge in edges:
        e1 = edge[0]
        e2 = edge[1]
        if e1 not in all_nodes:
            all_nodes.add(e1)
        if e2 not in all_nodes:
            all_nodes.add(e2)
    return all_nodes


def make_tuple(line):
    split = line.split(" ")
    return (int(split[0]), int(split[1]), int(split[2]))

def make_set(line):
    split = line.split(" ")
    return {int(split[0]), int(split[1])}

class UnionFind:
    def __init__(self, my_set):
        self.my_set = my_set

    def add_node(self, n):
        self.my_set[n] = (n, 0)

    def find(self, n):
        if self.my_set[n][0] != n:
            self.my_set[n] = self.find(self.my_set[n][0])
        return self.my_set[n]

    def union(self,l1, l2):
        k1 = l1[0]
        k2 = l2[0]
        r1 = l1[1]
        r2 = l2[1]
        if r1 < r2:
            self.my_set[k1] = l2
        elif r1 > r2:
            self.my_set[k2] = l1
        else:
            self.my_set[k2] = l1
            self.my_set[k1] = (self.my_set[k1][0], r1+1)

def kruskal(nodes, edges, edges_to_check):
    sets = UnionFind({})
    mst = []
    for n in nodes:
        sets.add_node(n)

    for e in sorted(edges, key=itemgetter(2)):
        n1 = e[0]
        n2 = e[1]
        l1 = sets.find(n1)
        l2 = sets.find(n2)
        if l1 != l2:
            (e1, e2, w) = e
            if {e1, e2} in edges_to_check:
                mst.append(e)
            sets.union(l1, l2)
    return mst

eval()
