class Solution(object):
    def remainingMethods(self, n, k, invocations):
        adj = defaultdict(list)
        indeg = [0] * n

        for i,j in invocations:
            adj[i].append(j)
            indeg[j] += 1

        sus = set()
        def dfs(i):
            sus.add(i)

            for x in adj[i]:
                indeg[x] -=1
                if not x in sus:
                    dfs(x)
        dfs(k)

        for i in sus:
            if indeg[i]:
                return list(range(n))
        return [i for i in range(n) if not i in sus]
        