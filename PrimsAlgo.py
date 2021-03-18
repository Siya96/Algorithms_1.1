from BFS import BreadthFirstSearch
from Exceptions import UnConnectedGraphError
from Graph import Graph


class Prim:
    def __init__(self, graph):

        bfs = BreadthFirstSearch(graph)
        if bfs.isConnected() == False:
            raise UnConnectedGraphError
        
        self.graph = graph

        


    def buildMST(self):
        mstGraph = []
        mstGraph = self.graph.verticeList[:2]

        visitedNodes = [False] * self.graph.getSize()
        visitedNodes[1] = True

        index = 1
        while index < len(self.graph.verticeList):

            if visitedNodes[index] == False:

                self.findMinEdge(mstGraph, visitedNodes)


        pass

        
    def findMinEdge(self, mstGraph, visitedNodes):
        for i in range(1, len(self.graph.verticeList)):
            return
        pass

    
    def visitedNode(self, indexNode, visitedNodes):
        return visitedNodes[indexNode]







lst = [6,4,5,3]
lst2 = lst
lst2.append(9)
print (lst)
# for j in range(1, len(lst)):
#     print (lst[j])
# lst2 = lst[:2]
# print(lst2)
