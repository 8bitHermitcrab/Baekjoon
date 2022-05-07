queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

# queue1 = [1, 2, 1, 2]
# queue2 = [1, 10, 1, 2]

# queue1 = [1, 1]
# queue2 = [1, 5]

# 큐1의 합
sum_queue1 = sum(queue1) #14
# 큐2의 합
sum_queue2 = sum(queue2) #16

# 전체 합의 반값
half_sum_q1q2 = (sum_queue1 + sum_queue2) // 2 #15

# cont
answer = 0
# 큐1 제일 앞값
num1 = queue1[0]
# 큐2 제일 앞값
num2 = queue2[0]

# 큐1의 마지막값
num1_e = queue1[-1]
# 큐2의 마지막값
num2_e = queue2[-1]

while(len(queue1) != 0 or len(queue2) != 0):
    # 큐1합 > 반값, 큐2합 < 반값
    if sum_queue1 > half_sum_q1q2 and sum_queue2 < half_sum_q1q2:
        if len(queue1) != 0 or len(queue2) != 0:
            break
        elif sum_queue1 == half_sum_q1q2:
            break
        else:
            num1 = queue1.pop(0)
            queue2.append(num1)
            answer += 1

    # 큐1합 < 반값, 큐2합 > 반값
    elif sum_queue1 < half_sum_q1q2 and sum_queue2 > half_sum_q1q2:
        if len(queue1) != 0 or len(queue2) != 0:
            break
        elif sum_queue2 == half_sum_q1q2:
            break
        else:
            num2 = queue2.pop(0)
            queue1.append(num2)
            answer += 1

    # 큐1합 < 반값, 큐2합 < 반값, 큐1합 > 반값, 큐2합 > 반값
    else:
        answer = -2
        break

print(answer)


'''
def dfs(graph, start_mode):
    from collections import deque
    visited = []
    need_visited = deque()

    need_visited.append(start_node)

    while need_visited:
        node = need_visited.popleft()

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

# 큐1 또는 큐2와 반값이 같아질동안 반복
while(half_sum_q1q2 != queue1 or half_sum_q1q2 != queue2):
    # 반값 > 큐1
    if half_sum_q1q2 > sum_queue1:
        num = half_sum_q1q2 - sum_queue1
        queue2.pop(num)
        cnt += 1
        queue1.append(num)
        cnt += 1

    # 반값 < 큐1
    elif half_sum_q1q2 < sum_queue1:
        num = sum_queue1 - half_sum_q1q2
        queue1.pop(num)
        cnt += 1
        queue2.append(num)
        cnt += 1

    # 반값 > 큐2
    elif half_sum_q1q2 > sum_queue2:
        num = half_sum_q1q2 - sum_queue2
        queue1.pop(num)
        cnt += 1
        queue2.append(num)
        cnt += 1

    # 반값 < 큐2
    elif half_sum_q1q2 < sum_queue2:
        num = sum_queue1 - half_sum_q1q2
        queue2.pop(num)
        cnt += 1
        queue1.append(num)
        cnt += 1
    
    elif queue1 == 0:
        cnt = -1
        break
    
    elif queue2 == 0:
        cnt = -1
        break

    # 반값 = 큐1, 반값 = 큐2일 때, 반복을 멈춘다
    elif half_sum_q1q2 == sum_queue1 and half_sum_q1q2 == sum_queue2:
        break

    else:
        cnt = -1
        break'''