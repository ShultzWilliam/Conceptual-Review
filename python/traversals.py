# Writing traversal algorithms through graphs (dict representaions)
# Start Date: Aug 22, 2022

#given graph

def depthFirstSearchI(graph, source):       #iterative
    #create  stack with the initial node
    
    #while the stack has a node on it
        #pointer = popped node
        #for each neighbor of pointer,
            #add that node onto the stack
    stack = [source]

    while (len(stack) > 0):
        currentNode = stack.pop()
        print(currentNode)
        for i in graph[currentNode]:
            stack.insert(len(stack),i)
            #print(f"Inserted {i} at index {len(stack)}")

def depthFirstSearchR(graph, source):       #recursive
    #print the source node
    #for each neighbor of the source node
        #call the function with the neighbor as the source node
    print(source)
    for i in graph[source]:
        depthFirstSearchR(graph, i)


def testSearches():
    adjacencyList = {
    'a':['b','c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]}

    depthFirstSearchI(adjacencyList,'a')
    print("")
    depthFirstSearchR(adjacencyList,'a')

#testSearches()

#Depth first works by going as deep into a path as possible, until it reaches a dedad end
#After reaching the dead end, then it goes back to the original node and takes the next path

#2 methods for Depth First Traversals: iterative and recursive

#for iterative, make use of a stack
    #Put the first node on the stack
    
    #while the stack isn't empty:
        #pop the first node, then
        #for each neighbor of the node,
            #put that neighbor on the stack

#for recursive, do the following:

#call initial function on source node:
    # for each of source node's neighbors,
    # call the function on a neighbor
