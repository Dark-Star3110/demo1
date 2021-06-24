
from graph.const import INFINITY
from random import choice
from graph.priority_queue import priorityQueue

class graph:
    def __init__ (self):
        self.adjList = dict()
        self.vertexSet = set()
        self.edgeSet = set()

    def addVertex (self, vert):
        self.vertexSet.add(vert)
        if vert not in self.adjList:
            self.adjList[vert] = {}

    def addEdge (self, sour, dist, weight):
        self.addVertex(sour)
        self.addVertex(dist)
        self.adjList[sour][dist] = weight
        self.edgeSet.add((sour, dist))
	
    def getAdjVertex (self, vert):
        adj = []
        temp = self.adjList[vert]
        for p in temp:
            adj.append(p)
        return adj

    def getWeight (self, sour, dist):
        if (sour, dist) not in self.edgeSet:
            return INFINITY
        return self.adjList[sour][dist]

    def BFS (self, start=""):
        Q = []
        dist = {}
        for i in self.vertexSet:
            dist[i] = INFINITY
        if start == "":
            m = []
            m.extend(self.vertexSet)
            elm = choice(m)
            dist[elm] = 0
            Q.append(elm)
        else:
            Q.append(start)
            dist[start] = 0

        while len(Q) != 0:
            u = Q.pop(0)
            print (u, end='  ')
            adj = self.getAdjVertex(u)
            for i in adj:
                if dist[i] == INFINITY:
                    Q.append(i)
                    dist[i] = dist[u] + 1
        print()

    def DFS (self, start="", notice=1):
        clock = 1
        cc = 0
        ccnum = {}
        prev = {}
        post = {}
        visited = set()
        def previsit (u):
            nonlocal prev
            nonlocal clock
            nonlocal ccnum
            ccnum[u] = cc
            prev[u] = clock
            if notice == 1:
                print ("Bat dau tham", u, "tai", clock)
            clock += 1

        def postvisit (u):
            nonlocal post
            nonlocal clock
            post[u] = clock
            if notice == 1:
                print ("Ket thuc tham", u, "tai", clock)
            clock += 1

        def explore (u):
            nonlocal prev
            nonlocal post
            nonlocal visited
            nonlocal clock
            nonlocal ccnum

            visited.add(u)
            previsit(u)
            adj = self.getAdjVertex(u)
            for i in adj:
                if i not in visited:
                    explore (i)
            postvisit(u)
        if start != "":
            cc += 1
            explore (start)
        for i in self.vertexSet:
            if i not in visited:
                cc += 1
                explore (i)
        return cc

    def Dijsktra (self, start, end):
        Q = priorityQueue()
        dist = {}
        prev = {}
        for p in self.vertexSet:
            dist[p] = INFINITY
            Q.push((INFINITY, p))
        dist[start] = 0
        Q.decreaseKey(start, 0)
        while not Q.isEmpty():
            x = Q.pop()
            u = x[1]
            adj = self.getAdjVertex(u)
            for p in adj:
                if dist[p] > (dist[u] + self.getWeight(u,p)):
                    dist[p] = dist[u] + self.getWeight(u,p)
                    prev[p] = u
                    Q.decreaseKey(p, dist[p])

        if dist[end] == INFINITY:
            print("Khong ton tai khoang cach tu", start, "den", end)
            return None

        print ("Duong di tu", start, "den", end, "la:")
        road = [end]
        pre = prev[end]
        while pre is not start:
            road.insert(0, pre)
            pre = prev[pre]
        print (start, end="")
        for i in road:
            print(" ->", i, end="")
        print()
