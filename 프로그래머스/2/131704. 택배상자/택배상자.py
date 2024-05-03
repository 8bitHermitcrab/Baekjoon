def solution(order):
    stack = []
    len_order = len(order)
    idx = 0
    num = 0
    
    while idx < len_order:
        if order[idx] > num:
            num += 1
            stack.append(num)
        elif order[idx] == stack[-1]:
            stack.pop()
            idx += 1
        else:
            return idx
    return idx