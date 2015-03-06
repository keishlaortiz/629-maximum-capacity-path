"""
The Element class is a simple structure that takes to parameters name and value and initializes its attributes
self.name and self.value with those parameters.

This class was created exclusively for the Heap class to insert and delete elements by comparing the attribute value

When this class is used in the function dijkstra_heap:
    self.name is the vertex id
    self.value is the capacity value of the vertex id

When this class is used in the function kruskal:
    self.name is a tuple (a,b) where a and b are vertices and are adjacent (i.e. (a,b) is an edge)
    self.value is the weight value of the edge (a,b)
"""
class Element():
    def __init__(self,name,value):
        self.name = name #for edges the "name" will be a tuple (1,2) (i.e. the edge(1,2))
        self.value = value

    def __del__(self):
        del self.name
        del self.value