class Solution:
    def maximum69Number (self, num: int) -> int:
        s_num = str(num)
        temp = []
        
        for i in s_num:
            temp.append(i)
        
        for j in range(len(s_num)):
            if s_num[j] == '6':
                temp[j] = '9'
                break
        return int(''.join(temp))