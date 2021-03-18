from Egde import Edge


class Vertices:
    
    def __init__(self):
        
        self.edgeList = []
        
    
    def addEdge(self, connectFrom, addWeight, connectTo):
        
        newEdge = Edge(connectFrom, addWeight, connectTo)
        self.edgeList.append(newEdge)
