# OOP_Ex3
## Inroduction
In this Repository I will show and explain on how to implement Directed Weighted graph in python.
The repoistory includes one package with 3 classes:
* Node_Data
* DiGraph
* GraphAlgo

I will explain here briefly about each of the classes:

### Node_Data
This class creating the nodes - vertexes for the graph. This class implemetations will be used alot, 
also this class is actually the foundation stone for my repository and each one of the other 2 classes.
I use mainly the methods: get and set for each feature of the class.

### DiGraph
This class "built" directly from the class Node_Data, beacuse each vertex of the graph is a node,
and in addition, we add edges to the graph in the graph and actually creating a graph.
I also implementing methods to get the amount of the edges and the vertexes, and also to check 
all the nodes that connecting in and out of chosen node.
In this class I also count the number of changes that been made, and i can add or remove 
either node or edge. of course if there are edges that connected to chosen node and I choose to remove it,
the connected edges will be removed as well.

### GraphAlgo
This class is the more complicated one.
In this class we implement more complex methods on our graph, such as save it to json file,
or to load a graph from json file. 
I also check the shortest path between 2 chosen nodes in the graph, or even if this path is 
actually exist.
Also I check for the strongly connected components in the graph, either from chosen node or the
list of all the strongly connected components in the graph.
In the end of this class I plot the graph, meanning i draw and create it, from the given data on the nodes 
and the edges.

In case you want to delve into the classes and how the complex methods work, including examples for each
method and explenation on the complex methods you are more than welcome to dive in to my Wiki.
