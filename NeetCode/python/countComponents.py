class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # construct graph map
        g_map={i:[] for i in range(n)}
        for [a,b] in edges:
            g_map[a].append(b)
            g_map[b].append(a)

        # node has been visited
        visit = [False] * n

        def trav_graph(node): # traverse from node
            for to_node in g_map[node]:
                if not visit[to_node]:
                    visit[to_node]=True
                    trav_graph(to_node)


        res=0 # start counting
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                trav_graph(node) #all traverse 
                res += 1 # add one from visit[node]=False after all connected
                
        return res








        
