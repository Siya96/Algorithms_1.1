

import random
from BFS import BreadthFirstSearch
from Graph import Graph

class Main:
    
    def __init__(self):

        
        self.g = Graph(8)
        
        self.b = BreadthFirstSearch(self.g)

        self.generateConnectedGraph()
      
        self.g.getSize()
        index = 1
        while index < self.g.getSize():
       
             for x in self.g.verticeList[index].edgeList:
                 print("nodeNr: ", index, " has neighbours : ", x.connectTo , " Weight: ", x.weight)

             index +=1
        
        print(self.b.isConnected())


    def generateConnectedGraph(self):
        
    
            
        index = 2
        while index < self.g.getSize():

            randomNode = random.randint(1, index - 1)

            
            randomWeight = random.randint(0, 10)
                                       
            self.g.connect(index, randomNode, randomWeight)
            index +=1




m = Main()