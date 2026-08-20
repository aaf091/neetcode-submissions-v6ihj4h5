class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(deque)
        tickets.sort()
        for src, dest in tickets:
            adj[src].append(dest)
        result = []

        def dfs(node):
            while adj[node]:
                next_dest = adj[node].popleft()
                dfs(next_dest)
            result.append(node)
        
        dfs("JFK")
        return result[::-1]

        
