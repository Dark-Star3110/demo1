from random import uniform
from sys import version
from graph.general_graph import graph
import copy

class directed_graph(graph):
    def __init__ (self):
        self.indegList = {}
        self.outdegList = {}
        super().__init__()
    
    def addEdge(self, sour, dist, weight=1):
        if (sour, dist) not in self.edgeSet:
            if sour not in self.outdegList:
                self.outdegList[sour] = 1
            else:
                self.outdegList[sour] += 1

            if dist not in self.indegList:
                self.indegList[dist] = 1
            else:
                self.indegList[dist] += 1

            if sour not in self.indegList:
                self.indegList[sour] = 0

            if dist not in self.outdegList:
                self.outdegList[dist] = 0
            super().addEdge(sour, dist, weight)

    def addVertex(self, vert):
        if vert not in self.vertexSet:
            self.indegList[vert] = 0
            self.outdegList[vert] = 0
        return super().addVertex(vert)

    def removeEdge (self, sour, dist):
        if (sour, dist) not in self.edgeSet:
            return None
        self.edgeSet.remove ((sour, dist))
        self.adjList[sour].pop(dist)
        self.indegList[dist] -= 1
        self.outdegList[dist] -= 1

    def removeVertex (self, vert):
        if vert not in self.vertexSet:
            return None
        temp = set(self.edgeSet)
        for i in temp:
            if vert == i[0]:
                self.removeEdge (vert, i[1])
            elif vert == i[1]:
                self.removeEdge (i[0], vert)
        self.adjList.pop(vert)
        self.vertexSet.remove(vert)
        self.indegList.pop(vert)
        self.outdegList.pop(vert)
        
    def Strongly_Connected_Components(self):
        regraph = {}
        cc = 0
        post = []
        visited = set()
        ccnum = {}
        def makeReGraph ():
            nonlocal regraph
            for p in self.edgeSet:
                if p[1] not in regraph:
                    regraph[p[1]] = []
                if p[0] not in regraph:
                    regraph[p[0]] = []
                regraph[p[1]].append(p[0])
            
        def getPost ():
            def explore (u):
                nonlocal visited
                nonlocal post
                visited.add(u)
                temp = regraph[u]
                for i in temp:
                    if i not in visited:
                        explore(i)
                post.insert(0, u)
            for i in self.vertexSet:
                if i not in visited:
                    explore (i)

        def explore (u):
            nonlocal visited
            nonlocal ccnum
            ccnum[u] = cc
            visited.add(u)
            for i in self.adjList[u]:
                if i not in visited:
                    explore(i)
        
        makeReGraph()
        getPost()
        visited.clear()
        for p in post:
            if p not in visited:
                cc += 1
                explore(p)

        return cc

    def topo (self):
        temp = []
        g = copy.deepcopy(self)
        u = object()
        def findSourVert ():
            nonlocal u
            for i in g.indegList:
                if g.indegList[i] == 0 :
                    u = i
                    return True
            return False

        while findSourVert():
            g.removeVertex(u)
            temp.append(u)
        if len(temp) is not len(self.vertexSet):
            temp.clear()
        return temp

    def printDot(self):
        with open("do_thi.dot", 'w', encoding='utf-8') as f:
            f.write("digraph dothi\n{\n")
            for i in self.vertexSet:
                f.write("\t"+str(i)+";\n")
            for i in self.edgeSet:
                f.write("\t"+str(i[0])+" -> "+str(i[1])+"[label=\""+str(self.getWeight(i[0], i[1]))+"\"];\n")
            f.write("}")
            f.close()
            print("Da tao file dothi.dot")

    def clear(self):
        self.adjList.clear()
        self.edgeSet.clear()
        self.indegList.clear()
        self.outdegList.clear()
        self.vertexSet.clear()

         
