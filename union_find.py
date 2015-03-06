import gc

"""
The Disjoint class is to implement the union-find data structure.  This class is used by the function kruskal.

Attributes:
    self.parent: list of parents of each vertex
    self.rank: list of ranks (heights) of each vertex
"""
class Disjoint:
    """
    Initialize the attributes of the class with the parameter size, this is equivalent to the operation MakeSet.

    Parameter:
        size: the number of vertices
    """
    def __init__(self,size):
        self.parent = [0]*(size+1)
        self.rank = [0]*(size+1)
    
    """
    Join two elements or vertices r1 and r2 by rank
    """
    def union(self,r1,r2):
        if self.rank[r1] > self.rank[r2]:
            self.parent[r2] = r1
        elif self.rank[r1] < self.rank[r2]:
            self.parent[r1] = r2
        else:
            self.parent[r2] = r1
            self.rank[r1] += 1
        
        return
    
    """
    Find with path compression.  Return the parent or root of v.

    Parameter:
        v: a vertex or element
    """
    def find(self,v):
        gc.disable()
        R = [] #stack
        r = v
        
        while self.parent[r] != 0:
            R.append(r)
            r = self.parent[r]
        
        while len(R) != 0:
            w = R.pop()
            self.parent[w] = r
            del w

        del R
        return r

    def __del__(self):
        del self.parent
        del self.rank

