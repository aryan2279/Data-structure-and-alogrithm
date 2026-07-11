from collections import deque

class Solution:
    def bfs(self, i, adj, visited, ne):
        q = deque([i])
        visited[i] = True
        
        while q:
            curr = q.popleft()
            ne[0] += 1
            
            for num in adj[curr]:
                ne[1] += 1
                if not visited[num]:
                    q.append(num)
                    visited[num] = True

    def countCompleteComponents(self, n, edges):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        ans = 0
        visited = [False] * n
        
        for i in range(n):
            if not visited[i]:
                ne = [0, 0]
                self.bfs(i, adj, visited, ne)
                if ne[0] * (ne[0] - 1) // 2 == ne[1] // 2:
                    ans += 1
        return ans