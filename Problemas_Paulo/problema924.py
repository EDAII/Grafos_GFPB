class Solution(object):
    def minMalwareSpread(self, graph, initial): 
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        N = len(graph)

        parent = list(range(N))
        size = [1] * N

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                if size[root_i] < size[root_j]:
                    root_i, root_j = root_j, root_i
                
                parent[root_j] = root_i
                size[root_i] += size[root_j]
                return True
            return False

        for i in range(N):
            for j in range(i + 1, N):
                if graph[i][j] == 1:
                    union(i, j)

        infection_count = {} 

        for node in initial:
            root = find(node)
            infection_count[root] = infection_count.get(root, 0) + 1
        
        max_saved_nodes = -1
        result_node = min(initial) 

        initial.sort()
        
        for node in initial:
            root = find(node)
            component_size = size[root]
            infected_count = infection_count.get(root, 0)

            if infected_count == 1:

                if component_size > max_saved_nodes:
                    max_saved_nodes = component_size
                    result_node = node
        
        return result_node