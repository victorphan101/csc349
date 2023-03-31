# A template for lab 2 - strong connectivity in graphs - for CSC 349 at Cal Poly
# Reads a file with a list of edges, then creates one component for each node and outputs it to the screen
# Credit: Rodrigo Canaan 

import sys
import math

count = 0

class node:

    def __init__(self, name, visited=False, out_edges=[], in_edges=[], previsit=-1, postvisit=-1):
        self.name = name
        self.visited = visited
        self.out_edges = out_edges
        self.in_edges = in_edges
        self.previsit = previsit
        self.postvisit = postvisit


def visit(vertex, G, stack):
    global count
    vertex.previsit = count
    count += 1
    vertex.visited = True
    for neighbor in vertex.out_edges:
        if not G[neighbor].visited:
            visit(G[neighbor], G, stack)
    vertex.postvisit = count
    count += 1
    stack.append(vertex.name)


def assign(vertex, G, component):
    G[vertex].visited = True
    component.append(vertex)
    for neighbor in G[vertex].in_edges:
        if not G[neighbor].visited:
            assign(neighbor, G, component)


def strong_connectivity(G):
    components = []
    stack = []
    # count = 0
    # out going edges and calculate post-visit numbers
    for vertex in G:
        if not vertex.visited:
            visit(vertex, G, stack)

    # reset visit
    for vertex in G:
        vertex.visited = False

    # in going edges and find scc
    while stack:
        i = stack.pop()
        if not G[i].visited:
            component = []
            assign(i, G, component)
            components.append(component)
    sort_component_list(components)
    return components


def sort_component_list(components):
    for c in components:
        c.sort()
    components.sort(key=lambda x: x[0])


def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        v = int(lines[0])
        if v == 0:
            raise ValueError("Graph must have one or more vertices")
        G = list(node(name=i, visited=False, out_edges=[], in_edges=[], previsit=-1,
                      postvisit=-1) for i in range(v))
        for l in lines[1:]:
            tokens = l.split(",")
            fromVertex, toVertex = (int(tokens[0]), int(tokens[1]))
            G[fromVertex].out_edges.append(toVertex)
            G[toVertex].in_edges.append(fromVertex)
        return G


def main():
    filename = sys.argv[1]
    G = read_file(filename)
    print(strong_connectivity(G))


# print(components)


if __name__ == '__main__':
    main()
