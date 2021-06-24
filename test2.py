
from graph.undirected_graph import undirected_graph

g = undirected_graph()

print("1. Thêm cạnh vào đồ thị từ file input1.txt")
with open("input2.txt") as f:
    n = sum(1 for _ in f)
    f.seek(0)
    for i in list(range(n)):
        c = f.readline().split()
        g.addEdge(int(c[0]), int(c[1]), int(c[2]))

g.printDot()
input("nhấn Enter để tiếp tục")
print()

adj = g.getAdjVertex(2)
print(g.adjList)

print("2. Thuật toán BFS bắt đầu từ một đỉnh bất kỳ:")
g.BFS()
print("Thuật toán BFS bắt đầu từ đỉnh 1:")
g.BFS(1)
input("nhấn Enter để tiếp tục")
print()

print("3. Thuật toán DFS bắt đầu từ một đỉnh bất kỳ:")
g.DFS()
print("Thuật toán DFS bắt đầu từ đỉnh 2:")
g.DFS(2)
input("nhấn Enter để tiếp tục")
print()

print("4. Thuật toán tìm thành phần liên thông.")
print("Số thành phần liên thông mạnh là:", g.Connected_Components())
input("nhấn Enter để tiếp tục")
print()

print("5. Thuật toán Dijsktra tìm đường đi ngắn nhất giữa 2 đỉnh của đồ thị")
print ("Đường đi ngắn nhất từ 1 đến 7 là:")
g.Dijsktra(1, 7)
input("nhấn Enter để tiếp tục")
print()

print("6. Thuật toán PRIM: ")
g.PRIM()
input("nhấn Enter để tiếp tục")
print()

print("7. Thuật toán Kruskal")
g.kruskal()
input("nhấn Enter để tiếp tục")
print()

print("8. Thuật toán tô màu: ")
g.color()
g.printDot()
input("nhấn Enter để tiếp tục")
print()

print("9. Prufer code")
code = [6, 0, 2, 6, 2, 9, 9, 2, 0]
print("Decode mã prufer:", code)
g.pruferDeCode(code)
g.printDot()
g.pruferEnCode()
input("nhấn Enter để kết thúc")
print()
