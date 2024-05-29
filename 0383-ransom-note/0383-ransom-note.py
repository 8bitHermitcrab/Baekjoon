class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:        
        ma_dict = defaultdict(int)
        for i in range(len(magazine)):
            ma_dict[magazine[i]] += 1
        for i in range(len(ransomNote)):
            ma_dict[ransomNote[i]] -= 1
        
        for i in range(len(ransomNote)):
            if ma_dict[ransomNote[i]] < 0:
                return False
        return True
        