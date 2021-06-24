
from graph.directed_graph import directed_graph


g = directed_graph()
print("1. Thêm cạnh vào đồ thị từ file input1.txt")
'''
File input.txt co dinh dang : dinh nguon  dinh dich  trong luong
'''
with open("input1.txt", "r") as f:
    n = sum(1 for _ in f)
    f.seek(0)
    for i in list(range(n)):
        c = f.readline().split()
        g.addEdge(c[0], c[1], int(c[2]))     

g.printDot()   
input("nhấn Enter để tiếp tục")
print()

print("2. Thuật toán BFS bắt đầu từ một đỉnh bất kỳ:")
g.BFS()
print("Thuật toán BFS bắt đầu từ đỉnh Feering:")
g.BFS("Feering")
input("nhấn Enter để tiếp tục")
print()

print("3. Thuật toán DFS bắt đầu từ một đỉnh bất kỳ:")
g.DFS()
print("Thuật toán DFS bắt đầu từ đỉnh Feering:")
g.DFS("Feering")
input("nhấn Enter để tiếp tục")
print()

print("4. Thuật toán tìm thành phần liên thông mạnh.")
print("Số thành phần liên thông mạnh là:", g.Strongly_Connected_Components())
input("nhấn Enter để tiếp tục")
print()

print("5. Thuật toán Dijsktra tìm đường đi ngắn nhất giữa 2 đỉnh của đồ thị")
print ("Đường đi ngắn nhất từ Feering đến Clacton là:")
g.Dijsktra("Feering", "Clacton")
input("nhấn Enter để tiếp tục")
print()

print("6. Thuật toán sắp topo:")
print("Thứ tự topo:", end=' ')
list = g.topo()
if len(list) == 0:
    print("Đồ thị có chu trình --> Không tồn tại thứ tự topo")
    print("Sau khi loại bỏ các chu trình của đồ thị, thứ tự topo là:")
    g.removeEdge("Tiptree", "Clacton")
    g.removeEdge("Feering", "Maldon")
    g.removeEdge("Blaxhall", "Dunwich")
    list = g.topo()
    print(list)
    g.printDot()
else:
    print (list)
print ("nhấn Enter để thoát")
print()
