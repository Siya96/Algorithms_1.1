
import random
from Graph import Graph
from Fifo import Fifo 


class BreadthFirstSearch:
    
    def __init__(self, graph):
        
        
        self.graph = graph
        self.fifo = Fifo(graph)
        self.marked = []

    def printM(self):
        print(self.marked)

    def isConnected(self):
        

        self.fifo.push(1)
        
        
        while not self.fifo.isEmpty():
            
            current = self.fifo.getHeader()
            if current.item not in self.marked:

            
                for neighbours in self.graph.verticeList[current.item].edgeList:

                    self.fifo.push(neighbours.connectTo)
                    

                markedNode = self.fifo.pull()

            
           
                self.marked.append(markedNode.item)
                
            else:
                self.fifo.pull()
          
            #print(self.printM())
            
        if len(self.marked) == (self.graph.getSize() - 1):
            self.marked = []
        
            
            return True
            
        else:
            self.marked = []
            return False

       
        
    
        



    















