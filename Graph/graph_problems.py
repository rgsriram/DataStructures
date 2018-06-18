from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True
        print(v)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            print i
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self, v):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Call the recursive helper function to print
        # DFS traversal
        self.DFSUtil(v, visited)


# Driver code
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print "Following is DFS from (starting from vertex 2)"
g.DFS(0)


def wordBreak(A, B):
    count = 0
    size_of_s = len(A)

    for each in B:
        times = A.count(each)

        if times:
            count += 1

        if (len(each) * times) == size_of_s or len(B) == count:
            return 1

    return 0


def xorSum(arr, n):
    bits = 0
    ans = 0

    # Finding bitwise OR of all elements
    for i in range(n):
        bits |= arr[i]

    print bits
    ans += bits

    return ans


def subsetOR(arr, l, r, bsum=0):
    # Print current subset
    if l > r:
        sum_arr.append(bsum)
        return

    # Subset including arr[l]

    subsetOR(arr, l + 1, r, bsum | arr[l])

    # Subset excluding arr[l]
    subsetOR(arr, l + 1, r, bsum)

    return


# Driver code
arr = [1, 2, 3]
n = len(arr)
sum_arr = []
subsetOR(arr, 0, n - 1)
print sum_arr