# Problem:  207. Course Schedule
# Link: https://leetcode.com/problems/course-schedule/


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]
        top_sort = []

        for pair in prerequisites:
            indegree[pair[0]] += 1
            adj_list[pair[1]].append(pair[0])

        queue = [i for i in range(numCourses) if indegree[i] == 0]

        while len(queue) > 0:
            node = queue.pop(0)
            top_sort.append(node)

            for adj_node in adj_list[node]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)

        if len(top_sort) != numCourses:
            return False
        return True
