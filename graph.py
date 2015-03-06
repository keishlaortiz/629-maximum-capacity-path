import random as rnd
import gc
"""
    Graph class
    
    This class is exclusively for undirected graphs.

    Attributes:
        self.vertex: a list of the vertices in the graph
        self.adj: an adjacent dictionary used to map each vertex with its neighbor and weight
"""
class Graph(object):

    """
    Initializes graph with the number of vertices (if any)
    Parameters: vertices (None by default), otherwise that parameter is the number of vertices in the graph
    """
    def __init__(self,vertices=None):
        self.adj = {}
        self.vertex = []
        
        if vertices is not None:
            self.vertex = list(xrange(1,vertices+1)) #vertices are numbered from 1 to vertices
            for v in self.vertex:
                self.adj[v] = {} #initializes the adj dictionary for each vertex
    
    """
    Return the number of vertices in the graph G: 'len(G)'
    """
    def __len__(self):
        return len(self.vertex)

    """
    Return a dictionary of neighbors of vertex v: 'G[v]'
    To get the weight between two vertices v and w, we can use: G[v][w]['weight']

    Parameter: 
        v: a vertex in the graph
    """
    def __getitem__(self, v):
        return self.adj[v]
    
    """
    Add vertex v to the graph

    Parameter:
        v: an integer greater than 0
    """
    def add_vertex(self,v):

        if isinstance(v,int) == False or v <= 0:
            raise Exception("v must be a positive integer number greater than 0")

        if v not in self.vertex:
            self.adj[v] = {} 
            self.vertex.append(v)
    
    """
    Add an edge between v and w with weight (0 by default).
    NOTE: Method assumes that vertices v and w are already in the graph

    Parameters:
        v and w: vertices in the graph
        weight: edge weight (0 by default)
    """
    def add_edge(self, v, w, weight=0):
        self.adj[v][w] = {'weight':weight}  
        self.adj[w][v] = {'weight':weight}
    
    """
    Add a list of edges in the graph
    NOTE: Method assumes that all the vertices in the list of edges are already in the graph

    Parameters:
        e: a list of edges, each element is a tuple (x,y,weight) or (x,y)
        weighted: boolean value to indicate if the edges are weighted or not (False by default)
    """
    def add_edges(self,e,weighted=False):
        gc.disable()
        if weighted == True:
            for x,y,weight in e:
                self.add_edge(x,y,weight)
        else:
            for x,y in e:
                self.add_edge(x,y)
    
    """
    Checks if there is an edge between v and w in the graph. Return True if the edge exists, otherwise False.

    Parameters: 
        v and w: vertices
    """
    def is_edge(self,v,w):
        try:
            return w in self.adj[v]
        except KeyError:
            return False
    
    """
    Return a list of edges as tuples (v,w,weight).
    """
    def get_edges(self):
        return list(self.edges_iter())
    
    """
    Return an iterator over edges as tuples (v,w,weight).
    """
    def edges_iter(self):
        gc.disable()
        seen = []
        v_nbrs = self.adj.items()
            
        for v, nbrs in v_nbrs:
            for nbr, weight in nbrs.items():
                if nbr not in seen:
                    yield (v,nbr,weight)
            seen.append(v)
        del seen
    
    """
    Return the degree of the vertex v

    Parameter:
        v: a vertex
    """
    def get_degree(self,v):
        try:
            return len(self.adj[v])
        except KeyError:
            return 0
    
    def __del__(self):
        del self.vertex
        del self.adj
