from collections import defaultdict


class Graph(object):

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, v, n):
        self.graph[v].append(n)

    def dfs_util(self, v, visited_array):

        visited_array[v] = True
        print v,

        for e in self.graph[v]:
            if not visited_array[e]:
                self.dfs_util(e, visited_array)

    def dfs(self):
        visited_array = defaultdict(bool)

        for each in self.graph.keys():
            if not visited_array[each]:
                self.dfs_util(each, visited_array)


g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'A')
g.add_edge('C', 'E')
g.add_edge('D', 'E')
g.add_edge('D', 'F')
g.add_edge('E', 'F')
g.add_edge('E', 'C')
g.add_edge('F', 'D')
g.add_edge('F', 'E')

g.dfs()