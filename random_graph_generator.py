from graph import Graph
import random as rnd
from collections import defaultdict
import gc

WHITE = 1
GRAY = 2
BLACK = 3

"""
Function to generate a random regular graph with n vertices and degree d.  
The edges are weighted randomly with numbers between 1 and max_weight.  Return the graph G
with n vertices and degree d with weighted edges.

Parameters:
    n: number of vertices in the graph
    d: degree of the graph
    max_weight: maximum weight value of an edge
"""
def generateRegularGraph(n,d,max_weight):
    gc.disable()
    if (n*d) % 2 != 0:
        raise Exception("n*d must be even!")
    
    if not 0 <= d < n:
        raise Exception("d must be positive and less than n!")
    
    G = Graph(n)
    if d == 0:
        return G
    
    #helper function to generate suitable edges for the graph with vertices with degree exactly d
    def generate_edges():
        gc.disable()
        edges = []
        degree = [0]*(n+1)
        for u in xrange(1,n):
            while degree[u] < d:
                v = rnd.randint(u+1,n)
                count = 0
                while (degree[v] == d) or ((u,v) in edges) or (u==v):
                    v = rnd.randint(u+1,n)
                    count += 1
                    if count > n*d:
                        del count
                        del degree
                        return edges
                else:
                    degree[v] += 1
                    degree[u] += 1
                    edges.append((u,v))
        del count
        del degree
        return edges

    edges = generate_edges()
    
    while len(edges) != ((n*d)/2): #execute loop until get a list of edges of size (n*d)/2 
        edges = generate_edges()
    
    weighted_edges = [(v,w,getRandNumber(max_weight)) for v,w in edges]
   
    G.add_edges(weighted_edges,True)

    del edges
    del weighted_edges
    return G
"""
Function to generate a random simple graph with n vertices with a probability p of edge creation.  
The edges are weighted randomly with numbers between 1 and max_weight.  Return the graph G
with n vertices with a probability p of edge creation with weighted edges.

Parameters:
    n: number of vertices in the graph
    p: probability of edge creation
    max_weight: maximum weight value of an edge
"""
def generateSimpleGraph(n,p,max_weight):
    gc.disable()

    if p < 0.0 or p > 1.0:
        raise Exception("p should be a value between 0 and 1!")

    G = Graph(n) #create a graph with n vertices

    weighted_edges = [(u,v,getRandNumber(max_weight)) for u in xrange(1,n+1) for v in xrange(u+1,n+1) if rnd.random() < p]

    G.add_edges(weighted_edges,True)
    del weighted_edges
    return G

"""
Helper function that returns an random integer number between 1 and n.

Parameter:
    n: positive integer greater than 1
"""
def getRandNumber(n):
    return rnd.randint(1,n)

"""
Test if a graph is connected. This is the implementation of the depth-first search algorithm
that counts the number of vertices reachable from the vertex 1. If the number of vertices visited
match the number of vertices in the graph, the graph is connected.
Return True if connected, otherwise False.

Parameter:
    G: a graph

"""
def isConnected(G):
    gc.disable()
    color = [WHITE]*(len(G)+1) 
    
    vertices = []  #stack
    color[1] = GRAY #visit vertices reachable from 1
    count = 1
    vertices.append(1)
    
    while len(vertices) != 0:
        v = vertices.pop()
        for w,c in G[v].items():
            if color[w] == WHITE:  #means that w is being visited for the first time, increment counter by 1
                count += 1
                color[w] = GRAY
                vertices.append(w)
        color[v] = BLACK

    del vertices
    del color
    #If count doesn't match with the number of vertices in G, means that G is not connected
    if len(G) != count:
        del count
        return False

    del count 
    return True

