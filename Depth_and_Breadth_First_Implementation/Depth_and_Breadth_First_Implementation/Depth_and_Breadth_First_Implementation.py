from collections import defaultdict

class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        """
        self.edges = defaultdict(list)
    
    def add_edge(self, from_node, to_node):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)

graph = Graph()



nodeList = [('A', 'B'),('A', 'C'),('B', 'D'),('B', 'E'),('C', 'F'),('C', 'H'),('D', 'I'),('D', 'J'),('E', 'G1'),('E', 'K'),('F', 'L'),('F', 'M'),('H', 'N'),('H', 'G2')]
#nodeDictionary = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F', 'H'], 'D': ['B', 'I', 'J'], 'E': ['B', 'G1', 'K'], 'F': ['C', 'L', 'M'], 'H': ['C', 'N', 'G2'], 'I': ['D'], 'J': ['D'], 'G1': ['E'], 'K': ['E'], 'L': ['F'], 'M': ['F'], 'N': ['H'], 'G2': ['H']}   This is nodeDictionary with being able to go back up the tree
nodeDictionary = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'H'], 'D': ['I', 'J'], 'E': ['G1', 'K'], 'F': ['L', 'M'], 'H': ['N', 'G2'], 'I': [], 'J': [], 'G1': [], 'K': [], 'L': [], 'M': [], 'N': [], 'G2': []}


for node in nodeList:
    graph.add_edge(*node)


def breadthFirst(nodeDictionary):
    openList = []
    closedList = []
    openList.append('A')

    while(len(openList) != 0):
        print("Open List: ", openList)
        print("Closed List: ", closedList)
        x = openList[0]
        openList.remove(openList[0])
        if(x == 'F'):
            return 'Success'
        else:
            y = nodeDictionary[x]
            closedList.insert(0, x)
            for thing in y:
                for node in closedList:
                    if(thing == node):
                        break
                    else:
                        openList.append(thing)
                        break
    return "Goal Not Found"


def depthFirst(nodeDictionary):
    openList = []
    closedList = []
    openList.append('A')

    while(len(openList) != 0):
        print("Open List: ", openList)
        print("Closed List: ", closedList)
        x = openList[0]
        openList.remove(openList[0])
        if(x == 'G1'):
            return 'Success'
        else:
            y = nodeDictionary[x]
            closedList.insert(0, x)
            for i in range(len(y) - 1, -1, -1):
                for node in closedList:
                    if(y[i] == node):
                        break
                    else:
                        openList.insert(0, y[i])
                        break
    return "Goal Not Found"
                        





answer = depthFirst(nodeDictionary)
print(answer)