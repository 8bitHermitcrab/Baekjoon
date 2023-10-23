import heapq

def median(data):
    smallhq = []
    bighq = []
    middle = data[0]
    result = [middle]

    for idx, val in enumerate(data[1:], 1):
        if val > middle:
            heapq.heappush(bighq, val)
        else:
            heapq.heappush(smallhq, (-val, val))
        
        if idx % 2 == 0:
            if len(smallhq) < len(bighq):
                heapq.heappush(smallhq, (-middle, middle))
                middle = heapq.heappop(bighq)
            elif len(smallhq) > len(bighq):
                heapq.heappush(bighq, middle)
                middle = heapq.heappop(smallhq)[1]
            result.append(middle)
    print(len(result))

    for i in range(len(result)):
        if i != 0 and (i + 1) % 10 == 1:
            print()
        print(result[i], end=' ')
    print()

t = int(input().rstrip())
for i in range(t):
    m = int(input().rstrip())
    data = []
    if m % 10 == 0:
        for _ in range(m // 10):
            data.extend(list(map(int, input().rstrip().split(' '))))
    else:
        for _ in range(m // 10 + 1):
            data.extend(list(map(int, input().rstrip().split(' '))))

    median(data)