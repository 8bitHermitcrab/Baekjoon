class Solution:
    def sortVowels(self, s: str) -> str:
        t = [i for i in s if i.lower() in "aeiou"]
        t.sort()
        s_list = list(s)
        
        n = 0
        for i, j in enumerate(s_list):
            if j.lower() in "aeiou":
                s_list[i] = t[n]
                n += 1
        return "".join(s_list)