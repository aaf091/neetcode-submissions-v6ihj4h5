class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        TIME = [float('inf')]*(n+1)
        for source, target, time in times:
            adj[source].append((target,time))
        
        pq = []
        heapq.heappush(pq,(0, k))
        TIME[k] = 0
        while pq:
            time, node = heapq.heappop(pq)
            if time>TIME[node]:
                continue
            for neighbor, t in adj[node]:
                new_time = t + time
                if TIME[neighbor] > new_time:
                    TIME[neighbor] = new_time
                    heapq.heappush(pq,(new_time, neighbor))
        result = max(TIME[1:])
        return result if result != float('inf') else -1
