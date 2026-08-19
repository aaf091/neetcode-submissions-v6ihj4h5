class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        state = [0]*numCourses
        def hasCycle(node):
            if state[node] == 1:
                return True
            
            if state[node] == 2:
                return False
            
            state[node] = 1

            for neighbor in adj[node]:
                if hasCycle(neighbor):
                    return True
            
            state[node] = 2
            return False
        
        for i in range(numCourses):
            if state[i] == 0:
                if hasCycle(i):
                    return False
        return True


