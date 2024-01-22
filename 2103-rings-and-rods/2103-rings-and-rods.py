class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for _ in range(10)]
        ans = 0
        for i in range(0, len(rings), 2):
            rods[int(rings[i+1])].add(rings[i])
        for j in rods:
            if len(j) >= 3:
                ans += 1
        return ans