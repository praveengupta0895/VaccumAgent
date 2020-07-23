import Queue as q
import math


class Graph(object):
    def __init__(self, vertices, edges):
        self.vertex = vertex
        self.edges = edges
        self.graph = {}
        for vertex in range(vertices):
            graph[vertex] = []
        for x in range(edges):
            src, des, wt = list(map(int, input().split(' ')))
            self.graph[src].append((des, wt))
            self.graph[des].append((src, wt))

    def printAdjacencyList(self):
        print("Printing the adjacency list of the vertices ")
        for vertex in range(vertices):
            print(vertex + ": " + graph[vertex])

    def findShortestRouteFrom(self, vertex):
        source = vertex
        pq = q.PriorityQueue()
        dist = [math.inf for vertex in range(vertices)]
        dist[0] = 0
        pq.put((0, source))
        while not pq.empty():


class HouseMap(object):
    def __init__(self,
                 class VaccumReflexAgent(object):
        def __init__(self, housemap):
            self.housemap = housemap

        def optimizeHouseMap():