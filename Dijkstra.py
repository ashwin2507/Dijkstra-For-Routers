
import sys
import heapq


# Vertex class to add the Vertex given
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])


# Class to construct the graph and then perform Dijkstra Algorithm
class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous


# Function to calculate the shortest Path
def shortest(v, path):
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return


# Dijkstra Algorithm performed in this method
def dijkstra(aGraph, start):
    # Set the distance for the start node to zero
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(), v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        # for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)


        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(), v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)


# Function to calculate the factorial to calculate all possible routes
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def temp(num1, num2, count):
    max_count = 0
    g = Graph()

    lines = [line.rstrip('\n') for line in open('Routers.txt')]
    for x in range(len(lines)):
        g.add_vertex(lines[x])

    nodes = [line.rstrip('\n') for line in open('Nodes.txt')]
    for y in range(len(nodes)):
        max_count = max_count + 1
        g.add_vertex(nodes[y])
    temp = []
    each = ''
    with open('Edges.txt') as f:
        text = f.readlines()

    for z in range(len(text)):
        each = text[z]
        each = each.rstrip()
        temp = each.split(' ')
        for y in range(len(temp)):
            g.add_edge(temp[0], temp[1], int(temp[2]))

    dijkstra(g, g.get_vertex(num1))
    target = g.get_vertex(num2)
    path = [target.get_id()]
    shortest(target, path)
    f1.write(num1)
    f1.write(' ')
    f1.write(num2)
    f1.write(' ')
    path.reverse()
    for item in range(len(path)):
        f1.write("%s " % path[item])
    f1.write('\n')
    max_count_fact = factorial(max_count)
    if count == max_count_fact:
        f1.close()


# Global file declaration
global f1
f1 = open('./Routes.txt', 'w+')

# List-all-Paths
if sys.argv[1] == '1':
    sources = [line.rstrip('\n') for line in open('Nodes.txt')]
    count = 0
    for x in range(len(sources)):
        for y in range(len(sources)):
            if y != x:
                count = count + 1
                temp(sources[x], sources[y], count)
    print 'Compiled check the Routes.txt'


# List path for given source and destination pair
if sys.argv[1] == '2':
    num1 = sys.argv[2]
    num2 = sys.argv[3]
    g = Graph()

    lines = [line.rstrip('\n') for line in open('Routers.txt')]
    for x in range(len(lines)):
        g.add_vertex(lines[x])

    nodes = [line.rstrip('\n') for line in open('Nodes.txt')]
    for y in range(len(nodes)):
        g.add_vertex(nodes[y])
    temp = []
    each = ''
    with open('Edges.txt') as f:
        text = f.readlines()

    for z in range(len(text)):
        each = text[z]
        each = each.rstrip()
        temp = each.split(' ')
        for y in range(len(temp)):
            g.add_edge(temp[0], temp[1], int(temp[2]))

    dijkstra(g, g.get_vertex(num1))
    target = g.get_vertex(num2)
    path = [target.get_id()]
    shortest(target, path)
    f1.write(num1)
    f1.write(' ')
    f1.write(num2)
    f1.write(' ')
    path.reverse()
    for item in range(len(path)):
        f1.write("%s " % path[item])
    f1.write('\n')
    f1.close()
    print 'Compiled check the Routes.txt'









