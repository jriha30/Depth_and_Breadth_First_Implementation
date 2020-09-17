from collections import defaultdict

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
            print("You will need to search " + str(len(closedList) + 1) + " nodes in order to find node F (using depth first).")
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
            print("You will need to search " + str(len(closedList) + 1) + " nodes in order to find node F (using breadth first).")
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
    nodeDictionary = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'H'], 'D': ['I', 'J'], 'E': ['G1', 'K'], 'F': ['L', 'M'], 'H': ['N', 'G2'], 'I': [], 'J': [], 'G1': [], 'K': [], 'L': [], 'M': [], 'N': [], 'G2': []}
    depthFirstAnswer = depthFirst(nodeDictionary)
    breadthFirstAnswer = breadthFirst(nodeDictionary)
    print(depthFirstAnswer)
    print(breadthFirstAnswer)

if __name__ == "__main__":
    main()