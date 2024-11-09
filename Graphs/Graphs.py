#Creating a Graph class
class Graph:
    #The constructor for Graph object is an adjacency list which records the edges and vertices
    def __init__(self):
        self.adj_list = {}

    #Method to print the adjacenct list of the graph
    def print_graph(self):
        #loop through the adjacenct list and print the vertex and with which vertices it has edges
        for vertex in self.adj_list:
            print(f"{vertex}:{self.adj_list[vertex]}")

    #Method to add a vertex in the Graph
    def add_vertex(self, vertex):
        #If the given vertex is not in the Graph the add it to the adjacenct list
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        #if the given vertex is already in the Graph then return False as we cant have duplicates
        return False

    #Method to add an edge in the Graph
    def add_edge(self, vertex1, vertex2):
        #Check if both the given vertices are in the Graph
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            #Add the vertices to each others adjacenct list
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        #if the vertices are not in the Graph then they cant have an edge so return False
        return False

    #Method to remove an edge from the Graph
    def remove_edge(self, vertex1, vertex2):
        #Check if the given vertices are in the graph or not
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            #If they are then remove the vertex from their adjacency list repectively
            self.adj_list[vertex1].remove(vertex2)
            self.adj_list[vertex2].remove(vertex1)
            return True
        #if the vertices are not in the graph then return False
        return False

    #Method to remove vertex from the graph
    def remove_vertex(self, vertex):
        #if Vertex in Graph
        if vertex in self.adj_list.keys():
            #Remove the edges of this vertex from the adjacency list of the every vertex in the Graph
            for vert in self.adj_list.keys():
                if vertex in self.adj_list[vert]:
                    self.adj_list[vert].remove(vertex)
            #Then remove the vertex from the Graph
            del self.adj_list[vertex]
            return True
        #Return False if the vertex not in Graph
        return False


Graphical = Graph()
Graphical.add_vertex("A")
Graphical.add_vertex("B")
Graphical.print_graph()
Graphical.add_edge("A", "B")
Graphical.print_graph()
print(" ")
Graphical.remove_vertex("A")
Graphical.print_graph()