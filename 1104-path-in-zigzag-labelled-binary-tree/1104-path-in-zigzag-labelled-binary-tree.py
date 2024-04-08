class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        level = math.floor(math.log(label, 2)) + 1
        
        while label:
            res.insert(0, label)
            cur_max = 2 ** level - 1
            cur_min = 2 ** (level - 1)
            label = (cur_max + cur_min - label) // 2
            level -= 1
        return res