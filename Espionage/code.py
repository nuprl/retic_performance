import sys
from operator import itemgetter
from retic import Void, List, Tuple, Int, String, Dict
from benchmark_tools.Timer import Timer

def eval(all_lines:List(String))->Void:
    l1 = all_lines[0].split(" ")
    edge_count = int(l1[1])
    edges = [make_tuple(line) for line in all_lines[1:edge_count+1]]
    edges_to_check = [make_set(line) for line in all_lines[edge_count+1:len(all_lines)]]
    all_nodes = create_nodes(edges)
    res = kruskal(list(all_nodes), edges, edges_to_check)
    res_tuple = convert_to_set(res)
    output_result(res_tuple, edges_to_check)

def output_result(res:List(Tuple(Int, Int)), edges:List(Tuple(Int, Int)))->Void:
    for e in edges: 
        n1 = e[0]
        n2 = e[1]
        if (n1, n2) in res or (n2, n1) in res:
            print("yes")
        else:
            print("no")

def convert_to_set(res:List(Tuple(Int, Int, Int)))->List(Tuple(Int, Int)):
    res_tuple=[]
    for r in res:
        (e1, e2, w) = r
        res_tuple.append((e1, e2))
    return res_tuple

def create_nodes(edges:List(Tuple(Int, Int, Int)))->List(Int):
    all_nodes = set()
    for edge in edges:
        e1 = edge[0]
        e2 = edge[1]
        if e1 not in all_nodes:
            all_nodes.add(e1)
        if e2 not in all_nodes:
            all_nodes.add(e2)
    return list(all_nodes)


def make_tuple(line:String)->Tuple(Int, Int, Int):
    split = line.split(" ")
    return (int(split[0]), int(split[1]), int(split[2]))

def make_set(line:String)->Tuple(Int, Int):
    split = line.split(" ")
    return (int(split[0]), int(split[1]))

class UnionFind:
    def __init__(self:UnionFind, my_dict:Dict(Int, Tuple(Int, Int)))->Void:
        self.my_dict = my_dict

    def add_node(self:UnionFind, n:Int)->Void:
        self.my_dict[n] = (n, 0)

    def find(self:UnionFind, n:Int)->Tuple(Int, Int):
        if self.my_dict[n][0] != n:
            self.my_dict[n] = self.find(self.my_dict[n][0])
        return self.my_dict[n]

            
    def union(self:UnionFind, l1:Tuple(Int, Int), l2:Tuple(Int, Int))->Void:
        k1 = l1[0]
        k2 = l2[0]
        r1 = l1[1]
        r2 = l2[1]
        if r1 < r2:
            self.my_dict[k1] = l2
        elif r1 > r2:
            self.my_dict[k2] = l1
        else:
            self.my_dict[k2] = l1
            self.my_dict[k1] = (self.my_dict[k1][0], r1+1)


def kruskal(nodes:List(Int), edges:List(Tuple(Int, Int, Int)), edges_to_check:List(Tuple(Int, Int)))\
        ->List(Tuple(Int, Int, Int)):
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
            if ((e1, e2) in edges_to_check) or (e2, e1) in edges_to_check:
                mst.append(e)
            sets.union(l1, l2)
    return mst

t = Timer()
with t:
    with open("input.txt", "r") as f:
        eval(f.readlines())
