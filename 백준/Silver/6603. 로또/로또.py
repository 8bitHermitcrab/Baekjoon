import itertools

while True:
    nums = list(map(int, input().split()))
    
    k = nums[0]
    s = nums[1:]
   
    for i in itertools.combinations(s, 6):
        print(*i)
        
    if k == 0:
        exit()
    print()