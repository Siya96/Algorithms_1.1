from Vertex import Vertices


class Graph:

    def __init__(self, vertices):
        self.verticeList = []
        self.verticeList.append(0)
        

        self.addVertice(vertices)
        
        

    def addVertice(self, vertices):
        

        while vertices > len(self.verticeList) - 1:
            
            newVertice = Vertices()
            self.verticeList.append(newVertice)


    def connect(self, sourceVertice, destinationVertice , weight):





        self.verticeList[sourceVertice].addEdge(sourceVertice , weight, destinationVertice)
        self.verticeList[destinationVertice].addEdge(destinationVertice ,weight, sourceVertice)
                

    
    def getNodeID(self, node):
        return self.verticeList.index(node)
    
    def getNode(self, node):
        return self.verticeList[node]

    def getSize(self):
        return len(self.verticeList)

    def printLst(self):
        print(self.verticeList)

    # def printEdges(self):
        
    #     index = 1
    #     while index < len(self.verticeList):

    #         tempList = []
    #         for edges in self.verticeList[index].edgeList:

    #             tempList.append(edges.weight)

    #         index += 1
    #         print(tempList)




