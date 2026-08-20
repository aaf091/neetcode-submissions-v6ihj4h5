class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        status = [0]*numCourses
        result = []
        def hasCycle(node):
            if status[node] == 2:
                return False
            if status[node] == 1:
                return True
            status[node] = 1

            for neighbor in adj[node]:
                if hasCycle(neighbor):
                    return True
            status[node] = 2
            result.append(node)
            return False
        for i in range(numCourses):
            if status[i] == 0:
                if hasCycle(i):
                    return []
        return result[::-1]
                
                
            