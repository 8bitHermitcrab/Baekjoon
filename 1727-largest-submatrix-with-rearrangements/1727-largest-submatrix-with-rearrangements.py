class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ans = 0
        hist = [0] * len(matrix[0])

        for row in matrix:
            for i, num in enumerate(row):
                if num == 0:
                    hist[i] = 0
                else:
                    hist[i] += 1

            sort_h = sorted(hist)
        
            for i, h in enumerate(sort_h):
                ans = max(ans, h * (len(row) - i))

        return ans