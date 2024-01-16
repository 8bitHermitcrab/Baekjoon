class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        str_dict = dict()
        
        for i in range(len(s)):
            str_dict[indices[i]] = s[i]
        
        str_dict = dict(sorted(str_dict.items()))  
        return ''.join(str_dict.values())
            