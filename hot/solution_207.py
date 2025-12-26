from typing import List


class Solution:

    def __init__(self):
        self.hasCycle = False
        self.path = []
        self.visited = []

    def buildGraph(self, numCourses: int, prerequsites: List[List[int]]) -> List[List[int]]:
        res: List[List[int]] = [[] for _ in range(numCourses)]

        for n in prerequsites:
            f = n[1]
            t = n[0]
            res[f].append(t)

        return res

    def traverse(self, graph: List[List[int]], idx: int):
        if self.hasCycle:
            return
        if self.path[idx]:
            self.hasCycle = True
            return
        if self.visited[idx]:
            return

        self.visited[idx] = True

        self.path[idx] = True
        for n in graph[idx]:
            self.traverse(graph, n)
        self.path[idx] = False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.path = [False] * numCourses
        self.visited = [False] * numCourses
        graph = self.buildGraph(numCourses, prerequisites)

        for i in range(numCourses):
            self.traverse(graph, i)

        return not self.hasCycle


# resolt = Solution().canFinish(2, [[1, 0]])
resolt = Solution().canFinish(2, [[1, 0], [0, 1]])
print(resolt)
