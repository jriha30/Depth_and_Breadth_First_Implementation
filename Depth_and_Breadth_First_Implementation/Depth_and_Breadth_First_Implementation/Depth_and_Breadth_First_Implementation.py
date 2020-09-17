from collections import defaultdict

#nodeDictionary = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F', 'H'], 'D': ['B', 'I', 'J'], 'E': ['B', 'G1', 'K'], 'F': ['C', 'L', 'M'], 'H': ['C', 'N', 'G2'], 'I': ['D'], 'J': ['D'], 'G1': ['E'], 'K': ['E'], 'L': ['F'], 'M': ['F'], 'N': ['H'], 'G2': ['H']}   This is nodeDictionary with being able to go back up the tree
nodeMap = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'H'], 'D': ['I', 'J'], 'E': ['G1', 'K'], 'F': ['L', 'M'], 'H': ['N', 'G2'], 'I': [], 'J': [], 'G1': [], 'K': [], 'L': [], 'M': [], 'N': [], 'G2': []}

def depthFirst(nodeDictionary):
    openList = []
    closedList = []
    openList.append('A')
    while(len(openList) != 0):
        print("Open List: ", openList)
        print("Closed List: ", closedList)
        x = openList[0]
        openList.remove(openList[0])
        if(x == 'F'):
            print("You will need to travel through " + str(len(closedList) + 1) + " in order to get to node F.")
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
            print("You will need to travel through " + str(len(closedList) + 1) + " in order to get to node F.")
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
       
def main():
    #nodeDictionary = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F', 'H'], 'D': ['B', 'I', 'J'], 'E': ['B', 'G1', 'K'], 'F': ['C', 'L', 'M'], 'H': ['C', 'N', 'G2'], 'I': ['D'], 'J': ['D'], 'G1': ['E'], 'K': ['E'], 'L': ['F'], 'M': ['F'], 'N': ['H'], 'G2': ['H']}   This is nodeDictionary with being able to go back up the tree
    nodeDictionary = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'H'], 'D': ['I', 'J'], 'E': ['G1', 'K'], 'F': ['L', 'M'], 'H': ['N', 'G2'], 'I': [], 'J': [], 'G1': [], 'K': [], 'L': [], 'M': [], 'N': [], 'G2': []}
    depthFirstAnswer = depthFirst(nodeMap)
    breadthFirstAnswer = breadthFirst(nodeMap)
    print(depthFirstAnswer)
    print(breadthFirstAnswer)

if __name__ == "__main__":
    main()