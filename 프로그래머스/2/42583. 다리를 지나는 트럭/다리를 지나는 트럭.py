from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    curr_w = 0
    while len(truck_weights) > 0:
        time = time + 1

        curr_w = curr_w - bridge.popleft()

        if curr_w + truck_weights[0] <= weight:
            curr_w = curr_w + truck_weights[0]
            bridge.append(truck_weights.popleft())

        else: 
            bridge.append(0)
            
    time = time + bridge_length
    
    return time