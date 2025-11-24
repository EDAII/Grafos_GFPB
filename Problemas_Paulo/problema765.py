class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        
        total_people = len(row)
        N = total_people // 2
        
        parent = list(range(N))
        num_components = [N] 

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            
            root_i = find(i)
            root_j = find(j)
            
            if root_i != root_j:
                parent[root_i] = root_j
                num_components[0] -= 1 
                return True
            return False
        
        for i in range(0, total_people, 2):
            person1 = row[i]
            person2 = row[i+1]
            
            couple_a = person1 // 2
            couple_b = person2 // 2
            
            if couple_a != couple_b:
                union(couple_a, couple_b)

        return N - num_components[0]