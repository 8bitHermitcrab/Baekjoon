# 각 산의 지점 수 : n
# 등산로 : paths
# 출입구 번호 : gates
# 산봉우리 번호 : summits

# n = 6
# paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
# start = [1, 3]


'''# graph
mountain_route = {
    '1' : {'2' : 3},
    '2' : {'1' : 3, '3' : 5, '4' : 2, '5' : 4},
    '3' : {'2' : 5, '4' : 4},
    '4' : {'2' : 2, '3' : 4, '5' : 3, '6' : 1},
    '5' : {'2' : 4, '4' : 3, '6' : 1},
    '6' : {'4' : 1, '5' : 1}
}'''

n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
start = [1, 3]

m = len(paths)

graph = dict()
node = []
paths_dict1 = dict()
paths_dict2 = dict()
# print(node)

graph['1'] = 2
for k in range(len(paths)):
    i = paths[k][0]
    # node.append(a)
    j = paths[k][1]
    w = paths[k][2]
    paths_dict1[str(i)] = w
    paths_dict2[str(j)] = w 
    # node = node.append(paths[i][0])
    # paths_dict[str(paths[i][1])] = paths[i][2]
# print(node)
print(paths_dict1)
print(paths_dict2)
print()

from itertools import chain
from collections import defaultdict
# dict1 = {'bookA': 1, 'bookB': 2, 'bookC': 3}
# dict2 = {'bookC': 2, 'bookD': 4, 'bookE': 5}

dict3 = defaultdict(list)
# for k, v in chain(dict1.items(), dict2.items()):
for k, v in chain(paths_dict1.items(), paths_dict2.items()):
    dict3[k].append(v)
 
for k, v in dict3.items():
    print(k, v)




'''

INF = int(1e7) # 무한을 의미하는 값
# 노드의 개수, 간선의 개수를 입력받기 
n, m = map(int, input().split()) 
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기 
visited = [False] * (n + 1) 
# 최단 거리 테이블을 모두 무한으로 초기화 
distance = [INF] * (n + 1) 
# 모든 간선 정보를 입력받기 
for _ in range(m): 
    a, b, c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용이 c라는 의미 
    graph[a].append((b, c)) # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환 

def get_smallest_node(): 
    min_value = INF 
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스) 
    for i in range(1, n + 1): 
        if distance[i] < min_value and not visited[i]: 
            min_value = distance[i] 
            index = i 
    return index 

def dijkstra(start): # 시작 노드에 대해서 초기화 
    distance[start] = 0 
    visited[start] = True 
    for j in graph[start]: 
        distance[j[0]] = j[1] 
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복 
    for i in range(n - 1): 
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리 
        now = get_smallest_node() 
        visited[now] = True 
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]: 
            cost = distance[now] + j[1] 
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 
            if cost < distance[j[0]]: 
                distance[j[0]] = cost 
                
# 다익스트라 알고리즘을 수행 
dijkstra(start) 

# 모든 노드로 가기 위한 최단 거리를 출력 
for i in range(1, n + 1): 
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력 
    if distance[i] == INF: 
        print("INFINITY")
        # 도달할 수 있는 경우 거리를 출력 
    else: 
        print(distance[i])'''

# 출처: https://s0ng.tistory.com/entry/최단-경로-알고리즘-가장-빠른-길-찾기 [S0NG의 정보보안 블로그]