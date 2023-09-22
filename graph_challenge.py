MAX_VERTICES = 1000
INFINITY = 9999


class Vertex:
    def __init__(self):
        self.distance = INFINITY
        self.visited = False


def minDistance(vertices, numVertices):
    min = INFINITY
    minIndex = -1

    for v in range(numVertices):
        if not vertices[v].visited and vertices[v].distance <= min:
            min = vertices[v].distance
            minIndex = v

    return minIndex


def printShortestPath(parent, dest, g):
    path = []
    total = 0
    
    while parent[dest] != -1:
        path.append(dest)
        total += g[dest][parent[dest]]
        dest = parent[dest]
    
    path.append(dest)
    
    for node in reversed(path):
        print(node, end=" ")
    
    return total



def dijkstra(graph, numVertices, src, dest):
    vertices = [Vertex() for _ in range(numVertices)]
    parent = [-1 for _ in range(numVertices)]

    vertices[src].distance = 0

    for count in range(numVertices - 1):
        u = minDistance(vertices, numVertices)

        vertices[u].visited = True

        for v in range(numVertices):
            if (
                not vertices[v].visited
                and graph[u][v]
                and vertices[u].distance + graph[u][v] < vertices[v].distance
            ):
                vertices[v].distance = vertices[u].distance + graph[u][v]
                parent[v] = u

    total =printShortestPath(parent, dest,graph)
    return total

def graph(board: [[int]]) -> [[int]]:
    rows = len(board)
    cols = len(board[0])

    aux = [[0] * (rows * cols) for _ in range(rows * cols)]

    for row in range(rows):
        for col in range(cols):
            curr_idx = (row * cols) + col
            if col + 1 < cols:
                aux[curr_idx][curr_idx + 1] = board[row][col + 1]
            if row + 1 < rows:
                aux[curr_idx][curr_idx + cols] = board[row + 1][col]
            if col - 1 >= 0:
                aux[curr_idx][curr_idx - 1] = board[row][col - 1]
            if row - 1 >= 0:
                aux[curr_idx][curr_idx - cols] = board[row - 1][col]

    return aux


def find_less_cost_path(board: [[int]]) -> int:
    numVertices = len(board[0]) * len(board)
    print(board)
    g = graph(board)
    return dijkstra(graph=g, numVertices=numVertices, src=0, dest=len(g)-1)
