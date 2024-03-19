class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        xors = [0]
        prefix = 0
        
        for i, a in enumerate(arr):
            prefix ^= a
            xors.append(prefix)
        
        for i in range(1, len(arr)):
            for j in range(i):
                xors_j = xors[i] ^ xors[j]
                for k in range(i, len(arr)):
                    xors_k = xors[k + 1] ^ xors[i]
                    if xors_j == xors_k:
                        ans += 1
        return ans