from Exceptions import NodeNullException

class Fifo:
    
    def __init__(self, graph):
        self.graph = graph
        self.size = 0
        self.head = None
        self.tail = None


    def push(self, obj):
        
        #newFifoNode = fifoNode(obj)
        newFifoNode = fifoNode(self.graph.getNodeID(self.graph.getNode(obj)))
        
        
        if self.size == 0:
            
            self.head = newFifoNode
            self.tail = newFifoNode
            
        else:
            
                        
            self.tail.previous = newFifoNode
            self.tail = newFifoNode.next
            self.tail = newFifoNode
            
            
        self.size += 1
       


    def pull(self):

        if self.size == 0:
            raise NodeNullException
            


        elif self.size == 1:
            temp = self.head

            self.head.previous = None
            self.head = None
            self.tail = None
            
            self.size -= 1
            
            return temp
        
        else:
                
            tempNode = self.head
            self.head = self.head.previous
            self.head.next = None

            self.size -= 1
            
            return tempNode
        
        
    def getHeader(self):
        return self.head

    def fifoSize(self):
        return self.size

    def isEmpty(self):

        if self.size == 0:
            return True
        else:
            return False





class fifoNode:
    def __init__(self, nodeID):
        self.item = nodeID
        self.next = None
        self.previous = None


