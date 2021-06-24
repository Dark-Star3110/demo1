
from graph.general_graph import graph
from random import random
from graph.const import INFINITY
from graph.priority_queue import priorityQueue
from graph.disjoint_set import *
import copy

class undirected_graph(graph):
    def __init__(self):
        self.colorList = {}
        self.degList = {}
        super().__init__()

    def addEdge(self, sour, dist, weight=1):
        '''Them canh vao di thi, mac dinh la do thi '''
        self.addVertex(sour)
        self.addVertex(dist)
        if (sour, dist) not in self.edgeSet or (dist, sour) not in self.edgeSet:
            self.degList[sour] += 1
            self.degList[dist] += 1
        super().addEdge(sour, dist, weight)
        super().addEdge(dist, sour, weight)

    def addVertex(self, vert):
        if vert not in self.vertexSet:
            self.degList[vert] = 0
        super().addVertex(vert)

    def removeEdge (self, v1, v2):
        if (v1, v2) not in self.edgeSet or (v2, v1) not in self.edgeSet:
            return None
        self.adjList[v1].pop(v2)
        self.adjList[v2].pop(v1)
        self.degList[v1] -= 1
        self.degList[v2] -= 1
        self.edgeSet.discard((v1, v2))
        self.edgeSet.discard((v2, v1))

    def removeVertex (self, v):
        if v not in self.vertexSet:
            return None
        temp = dict(self.adjList[v])
        for i in temp:
            self.removeEdge (v, i)
        self.vertexSet.discard(v)
        self.degList.pop(v)
        self.adjList.pop(v)

    def getEdgeList (self):
        edgel = set()
        for i in self.edgeSet:
            if (i[1], i[0]) not in edgel:
                edgel.add(i)
        return edgel

    def Connected_Components(self):
        return super().DFS(notice=0)

    def PRIM (self, start=""):
        visited = set()
        cost = {}
        prev = {} 
        H = priorityQueue()

        for i in self.vertexSet:
            cost[i] = INFINITY
            H.push((INFINITY, i))
        if start == "":
            temp = list(self.vertexSet)
            start = temp[0]
            # print(start)
        cost[start] = 0
        H.decreaseKey(start, 0)

        while not H.isEmpty():
            x = H.pop()
            v = x[1]
            adj = self.getAdjVertex(v)
            for i in adj:
                if (cost[i] > self.getWeight(i, v)) and (i not in visited):
                    cost[i] = self.getWeight(i, v)
                    prev[i] = v
                    H.decreaseKey(i, cost[i])
            visited.add(v)
        total = 0
        for p in prev:
            print ("Them canh", p, ",", prev[p])
            total += self.getWeight(p, prev[p])
        print ("Tong trong luong:", total)
        return prev

    def kruskal (self):
        ds = disjiont_set()
        edge = []
        sortList = []
        for i in self.vertexSet:
            ds.makeset(i)

        edgeList = self.getEdgeList()
        for i in edgeList:
            weight = self.getWeight(i[0], i[1])
            sortList.append((weight, i[0], i[1]))  
        total = 0
        sortList.sort()
        # print(sortList)
        for i in sortList:
            if ds.find(i[1]) != ds.find(i[2]):
                weight = self.getWeight (i[1], i[2])
                total += weight
                edge.append((i[1], i[2]))
                print ("Them canh", i[1], ',', i[2])
                ds.union(i[1], i[2])
        print( "Tong trong luong:", total)
        return edge

    def pruferEnCode(self):
        '''Nen cay bang ma prufer mo rong'''
        if (len(self.vertexSet)-1) != len(self.edgeSet)/2:
            print("This graph is not tree! Prufer Code Error.")
            return None
        g = copy.deepcopy(self)
        code = []
        def find():
            '''Tim phan tu trong do thi co bac bang 1 va gan 0 nhat'''
            temp = sorted(g.degList)
            for i in temp:
                if g.degList[i] == 1 and i != 0:
                    return i
            return -1
                
        def findAdjvert(u):
            '''Tim dinh ke cua dinh u co bac 1'''
            adj = g.getAdjVertex(u)
            return adj[0]
        for i in list(range(1, len(self.vertexSet))):
            u = find()  
            if u == -1:
                continue
            code.append(findAdjvert(u))
            g.removeVertex(u)
        
        print("EnCode: ", code)
        return code

    def pruferDeCode(self, code):
        self.clear()
        length = len(code)
        decode = []
        temp = list(code)
        def find():
            '''Tim phan tu doi cua u'''
            for i in list(range(1, length+1)):
                if i not in code and i not in decode:
                    return i
            return -1
        for i in temp:
            v = find()
            decode.append(v)
            self.addEdge(v, i)
            code.pop(0)
        
    def color(self):
        color = {}
        def findMax():
            '''Find max of deg vertex list'''
            n = max(self.degList, key=(lambda x: self.degList[x]))
            return self.degList[n]

        def check():
            '''Check for regural graph'''
            def checkEqualIvo(lst): 
                return not lst or lst.count(lst[0]) == len(lst)

            temp = []
            for i in self.degList:
                temp.append(self.degList[i])
            return checkEqualIvo(temp)

        def findColor(u):
                mau = 1
                temp = []
                adj = self.getAdjVertex(u)
                for i in adj:
                    if i in color:
                        temp.append(color[i])
                while mau in temp:
                    mau += 1
                return mau

        def color_regural_graph():
            nonlocal color
            max = findMax()
            orderList = []
            def findOrderVert():
                nonlocal orderList
                for i in self.degList:
                    if self.degList[i] <= max-1:
                       orderList.insert(0, i)
                while len(orderList) < len(self.vertexSet):
                    temp = list(orderList)
                    for i in temp:
                        adj = self.getAdjVertex(i)
                        for p in adj:
                            if p not in orderList:
                                orderList.append(p)
            findOrderVert()
            for i in orderList:
                mau = findColor(i)
                color[i] = mau
                if mau not in self.colorList:
                    self.colorList[mau] = [i]
                else:
                    self.colorList[mau].append(i)

        def color_non_regural_graph():
            nonlocal color
            for i in self.vertexSet:
                mau = findColor(i)
                color[i] = mau
                if mau not in self.colorList:
                    self.colorList[mau] = [i]
                else:
                    self.colorList[mau].append(i)

        if check():
            color_non_regural_graph()
        else: 
            color_regural_graph()
        
        print("Mau:")
        for i in self.colorList:
            print("Mau", i, self.colorList[i])

    def printDot(self):
        with open("do_thi.dot", 'w', encoding='utf-8') as f:
            if len(self.colorList) == 0:
                f.write("graph dothi\n{\n")
                for i in self.vertexSet:
                    f.write("\t"+str(i)+";\n")
                edge = self.getEdgeList()
                for i in edge:
                    f.write("\t"+str(i[0])+" -- "+str(i[1])+"[label=\""+str(self.getWeight(i[0], i[1]))+"\"];\n")
                f.write("}")
            else:
                f.write("graph dothi\n{\n")
                for i in self.colorList:
                    a = random()
                    b = random()
                    c = random()
                    for p in self.colorList[i]:
                        # f.write("\t") p,"[fillcolor=\"",a,",",b,",",c,"\", style = filled];\n")
                        f.write("\t")
                        f.write(str(p))
                        f.write("[fillcolor=\"")
                        f.write(str(a)+","+str(b)+","+str(c))
                        f.write("\", style = filled];\n")
                edge = self.getEdgeList()
                for i in edge:
                    f.write("\t"+str(i[0])+" -- "+str(i[1])+"[label=\""+str(self.getWeight(i[0], i[1]))+"\"];\n")
                f.write("}")
                f.close()
            print("Da tao file dothi.dot")

    def clear (self):
        self.adjList.clear()
        self.edgeSet.clear()
        self.vertexSet.clear()
        self.colorList.clear()
        self.degList.clear()
