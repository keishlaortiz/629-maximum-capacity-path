#!/usr/bin/env python
"""
Testing program
Python Version: 2.6.9 (tested in build.tamu.edu)
"""
from timer import Timer
from random_graph_generator import generateRegularGraph, generateSimpleGraph, isConnected, getRandNumber
from maximum_capacity_path import dijkstra, dijkstra_heap, kruskal
from element import Element
from heap import Heap
from graph import Graph
import gc
import sys
#Defining constants
V_NUM = 1000
DEGREE = 6
P = .20
MAX_WEIGHT = 30000

"""
Print the maximum capacity path and length from s to t in G by using the parent list.

Parameters:
    G: a graph
    parent: a list that contains the "parent" vertex of each vertex in G
    s and t: source and destination vertices in G respectively
"""
def print_path(G,parent,s,t):
    gc.disable()
    mc = MAX_WEIGHT + 1
    path = [] 
    i = t
    while i != s:
        if mc > G[i][parent[i]]['weight']:
            mc = G[i][parent[i]]['weight']
        path.append(i)
        i = parent[i]
    
    print "Maximum capacity path from {0} to {1} has capacity: {2}".format(s,t,mc)
        
    print "Path from {0} to {1}".format(s,t)
    s_path = repr(s)

    for v in reversed(path):
        s_path += " --> "+repr(v)

    print s_path

    del s_path
    del path
    del parent
    del mc

"""
Run the Maximum Capacity Path algorithms (Dijkstra, Dijkstra with heap, and Kruskal). Return the running times of each algorithm.

Parameters:
    g: a graph
    s and t: source and destination vertices in g respectively
"""
def run_MCP_algorithms(g,s,t):
    gc.disable()
    
    print "MCP using Dijkstra without heap"
    with Timer() as tm:
        parent1 = dijkstra(g,s,t)
    t1 = tm.secs
    print "Running time: %s s" % tm.secs
    print_path(g,parent1,s,t)
    print "\n"
    del parent1
  
    print "MCP using Dijkstra with heap"
    with Timer() as tm:
        parent2 = dijkstra_heap(g,s,t)
    t2 = tm.secs
    print "Running time: %s s" % tm.secs
    print_path(g,parent2,s,t)
    print "\n"
    del parent2

    print "MCP using Kruskal"

    #Get the edges of the graph and insert them into a heap, then pass the heap to the Kruskal function
    edges = g.get_edges()
    elements = [Element((v,w),c['weight']) for v,w,c in edges]
    edgeHeap = Heap(len(elements),False,elements)

    del elements
    del edges
    with Timer() as tm:
        parent3 = kruskal(g,edgeHeap,s,t)
    t3 = tm.secs
    print "Running time: %s s" % tm.secs
    print_path(g,parent3,s,t)
    print "------------------------------------------------------\n"
    del edgeHeap
    del parent3
    
    del g
    del s
    del t
    del tm
    return (t1,t2,t3)

"""
Generate and return a sample graph and two vertices to test the routing algorithms.
"""
def sample_graph():
    g = Graph(10)
    g.add_edge(1,3,20)
    g.add_edge(1,2,12)
    g.add_edge(1,5,9)
    g.add_edge(2,3,11)
    g.add_edge(2,4,4)
    g.add_edge(2,5,3)
    g.add_edge(2,7,17)
    g.add_edge(3,4,13)
    g.add_edge(4,9,6)
    g.add_edge(5,6,10)
    g.add_edge(6,7,7)
    g.add_edge(6,8,8)
    g.add_edge(7,8,5)
    g.add_edge(7,9,16)
    g.add_edge(7,10,18)
    g.add_edge(8,10,21)
    g.add_edge(9,10,2)
    s = getRandNumber(10)
    t = getRandNumber(10)
    while (s == t):
        s = getRandNumber(10)
        t = getRandNumber(10)
    
    return g,s,t

"""
Test...
"""
TIMES = 5

gc.disable()

#t1 dijkstra, t2 dijkstra with heap, t3 kruskal
t1s = 0.0
t2s = 0.0
t3s = 0.0

t1d = 0.0
t2d = 0.0
t3d = 0.0
#sys.stdout = open("output5.txt","w")
print "Number of vertices: {0}".format(V_NUM)
for i in xrange(TIMES):
    G1 = generateRegularGraph(V_NUM,DEGREE,MAX_WEIGHT)
    G2 = generateSimpleGraph(V_NUM,P,MAX_WEIGHT)
    
    """
    To ensure that the graphs are always connected (i.e. there is a path from any s to any t)
    """
    while isConnected(G1) == False:
        G1 = generateRegularGraph(V_NUM,DEGREE,MAX_WEIGHT)
    
    while isConnected(G2) == False:
        G2 = generateSimpleGraph(V_NUM,P,MAX_WEIGHT)
    
    
    s = getRandNumber(V_NUM)
    t = getRandNumber(V_NUM)
    while (s == t):
        s = getRandNumber(V_NUM)
        t = getRandNumber(V_NUM)

    print "Source vertex: {0}".format(s)
    print "Destination vertex: {0}\n".format(t)

    print "~~~~REGULAR GRAPH~~~~"
    print "Degree: {0}".format(DEGREE)
    tm1s,tm2s,tm3s = run_MCP_algorithms(G1,s,t)
    t1s += tm1s
    t2s += tm2s
    t3s += tm3s
    del G1
    
    print "~~~~DENSE GRAPH~~~~"
    print "Probability of edge creation: {0}".format(P)
    tm1d,tm2d,tm3d = run_MCP_algorithms(G2,s,t)
    t1d += tm1d
    t2d += tm2d
    t3d += tm3d

    del G2
    del tm1s
    del tm2s
    del tm3s
    del tm1d
    del tm2d
    del tm3d
    del s
    del t

print "Average running time for Regular Graphs:"
print "Dijkstra: {0} s".format(t1s/TIMES)
print "Dijkstra with heap: {0} s".format(t2s/TIMES)
print "Kruskal: {0} \n".format(t3s/TIMES)

print "Average running time for Dense Graphs:"
print "Dijkstra: {0} s".format(t1d/TIMES)
print "Dijkstra with heap: {0} s".format(t2d/TIMES)
print "Kruskal: {0} s\n".format(t3d/TIMES)

del t1s
del t2s
del t3s
del t1d
del t2d
del t3d