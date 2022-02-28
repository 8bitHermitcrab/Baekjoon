# 셀프 넘버

# d(75) = 75+7+5 = 87

def d(n):
    n = n + sum(map(int, str(n)))
    return n

# 셀프 넘버가 아닌, 생성자가 있는 수들 집합
NonSelfNum = set()

# 셀프 넘버가 아닌 집합에 들어갈 수들 찾기
for i in range(1, 10001):
    NonSelfNum.add(d(i))

for i in range(1, 10001):
    if i not in NonSelfNum:
        print(i)


""" 
def solve(n):
    n_10 = n // 10
    n_1 = n % 10
    ans = n + n_10 + n_1
    return ans

natural_num = set(range(1, 10001))

for i in range(1, 10000):
    print(solve(i)) 
    
    https://kbwplace.tistory.com/69
    """