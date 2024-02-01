class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        mat_dict = collections.defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                mat_dict[i - j].append(mat[i][j])
        
        for val in mat_dict.values():
            val.sort(reverse=True)
        
        for i in range(m):
            for j in range(n):
                mat[i][j] = mat_dict[i - j].pop()
        return mat