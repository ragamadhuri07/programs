#import dictionary for graph
from collections import defaultdict

#add edge to graph : function
graph = defaultdict(list)
def addEdges(graph,u,v):
    graph[u].append(v)
    
#function decription
def generate_edges(graphs):
    edges=[]
    
    #for each node in graph
    for node in graph:

#for each neighbour node of a single node
        for neighbour in graph[node]:

             #if edge exists then append
            edges.append((node,neighbour))
    return edges

addEdges(graph,'a','c')
addEdges(graph,'b','c')
addEdges(graph,'b','e')
addEdges(graph,'c','d')
addEdges(graph,'c','e')
addEdges(graph,'c','b')
addEdges(graph,'e','b')
addEdges(graph,'d','c')
addEdges(graph,'e','c')

#printing graph
print(generate_edges(graph))
















    
