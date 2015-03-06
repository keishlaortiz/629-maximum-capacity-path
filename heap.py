import math as m
import gc

"""
    Heap class

    Implementation of a max-heap.  The elements of the max-heap are objects from the Element class
    because the attribute value of the element is used to maintain the max-heap properties.

    Attributes:
        self.size: size of the heap 
        self.heap_array: the heap "array" (list)
        self.max_size: maximum size of the heap array
        self.vertices: a boolean value, True by default.  When is True the class will have an additional attribute called
        self.name_index, which is a list that stores the indexes of the vertices currently in the heap 
        (ex: value of self.heap_array[2].name is 1, therefore the value of self.name_index[1] is 2).
        self.name_index: optional attribute (see self.vertices)
"""

class Heap():
    """
    Initialize the heap attributes, if vertices is True, creates the list self.name_index. If data is not None,
    invoke the method buildHeap to build a heap with that data.

    Parameters:
        max_size: maximum size of the heap array
        vertices: True by default
        data: None by default, otherwise data should be a list of elements objects from the Element class
    """
    def __init__(self,max_size,vertices=True,data=None):
        gc.disable()
        if vertices == True:
            self.name_index = [None]*(max_size+1)

        self.vertices = vertices
        self.max_size = max_size
        self.size = 0
        self.heap_array = [None] * (max_size + 1)

        if data is not None:
            self.buildHeap(data)

            del data
    """
    Return the maximum value in the heap
    """
    def maximum(self):
        return self.heap_array[1]
    
    """
    Insert an element into the heap

    Parameter:
        element: an Element object
    """
    def insert(self,element):
        self.size += 1
        
        if self.size > self.max_size:
            print "You cannot add more elements to the heap"
            return
        
        i = self.size
        self.heap_array[i] = element
        if self.vertices == True:
            self.name_index[element.name] = i
        
        self.goUp(i)
    
    """
    Delete the maximum value from the heap
    """
    def delete_max(self):
        return self.delete(1)

    """
    Delete an element from the heap given its index, then return the element deleted

    Parameter:
        index: the index of the element in the array
    """
    def delete(self,index):
        gc.disable()
        if self.size == 0:
            return None
        if self.vertices == True:
            self.name_index[self.heap_array[self.size].name] = index
        element = self.heap_array[index]
        self.heap_array[index] = self.heap_array[self.size]
       
        self.size -= 1
        parent = self.get_parent(index)
        
        if self.size == 0:
            del parent
            return element
        
        if index == 1 or self.heap_array[parent].value > self.heap_array[index].value:
            self.goDown(index)
        else:
            self.goUp(index)
        
        del parent
        del index
        return element
    
    """
    Helper function used by delete when the index is 1 or the parent value is greater and buildHeap. 
    Maintain the heap property.

    Parameter:
        index: index of the element 
    """
    def goDown(self,index):
        gc.disable()
        parent = index
        while self.get_left_child(parent) <= self.size:
            child = self.get_left_child(parent)
            if child + 1 <= self.size and self.heap_array[child].value < self.heap_array[child + 1].value:
                child += 1
            if child <= self.size and self.heap_array[parent].value < self.heap_array[child].value:
                self.heap_array[parent], self.heap_array[child] = self.heap_array[child], self.heap_array[parent]
                if self.vertices == True:
                    self.name_index[self.heap_array[parent].name],self.name_index[self.heap_array[child].name] = self.name_index[self.heap_array[child].name],self.name_index[self.heap_array[parent].name]
                parent = child
            else:
                del child
                del parent
                del index
                return
        del parent
        del index
        return 
    
    """
    Helper function used by the functions delete and insert. Maintain the heap property

    Parameter:
        index: index of an element 
    """
    def goUp(self,index):
        gc.disable()
        while index > 1:
            parent = self.get_parent(index)
            if self.heap_array[index].value > self.heap_array[parent].value:
                self.heap_array[index], self.heap_array[parent] =  self.heap_array[parent], self.heap_array[index] #swap values
                if self.vertices == True:
                    self.name_index[self.heap_array[index].name],self.name_index[self.heap_array[parent].name] = self.name_index[self.heap_array[parent].name],self.name_index[self.heap_array[index].name]
                index = parent
            else:
                del parent
                del index
                return
        del index
        return

    """
    Sort the heap array in ascending order, this is used only when the elements are edges, not vertices
    """
    def heapsort(self):
        gc.disable()
        """
        helper function for the heapsort
        """
        def goDown(H, start, end):
            gc.disable()
            parent = start
            while parent * 2 <= end:
                child = parent * 2
                if child + 1 <= end and H[child].value < H[child + 1].value:
                    child += 1
                if child <= end and H[parent].value < H[child].value:
                    H[parent], H[child] = H[child], H[parent]
                    parent = child
                else:
                    del child
                    del parent
                    return

        end = len(self.heap_array)-1
        while end > 1:
            self.heap_array[end], self.heap_array[1] = self.heap_array[1], self.heap_array[end]
            end -= 1
            goDown(self.heap_array, 1, end)

    
    """
    Build a heap from a list of elements

    Parameter:
        elements: a list of elements objects from the Element class
    """
    def buildHeap(self,elements):
        gc.disable()
        
        self.size = len(elements)
        self.heap_array = [None] + elements[:]
        for index in xrange(self.get_parent(len(elements)),0,-1):
            self.goDown(index)
        
        del elements

    """
    Return the parent index of index

    Parameter:
        index: an index in the heap
    """
    def get_parent(self,index):
        return int(m.floor(index/2))
    
    """
    Return the left child index of index

    Parameter:
        index: an index in the heap
    """
    def get_left_child(self,index):
        return 2*index
    
    """
    Return the right child index of index

    Parameter:
        index: an index in the heap
    """
    def get_right_child(self,index):
        return 2*index+1
    
    """
    Return the index in the heap of a vertex. 
    NOTE: This is used ONLY by the function dijkstra_heap when the function has to
    delete a element from the heap.

    Parameter:
        name: the vertex id
    """
    def get_index(self,name):
        return self.name_index[name]

    def __del__(self):
        if self.vertices == True:
            del self.name_index
        del self.vertices
        del self.max_size
        del self.size
        del self.heap_array
