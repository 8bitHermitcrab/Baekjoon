from collections import deque

def solution(maps):
    answer = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 맵 벗어나는지 확인
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue

                # 벽인지 확인
                if maps[nx][ny] == 0:
                    continue

                # 처음 지나가는 길이면 거리 계산하고 다시 상하좌우 확인
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))   
        return maps[len(maps)-1][len(maps[0])-1]

    answer = bfs(0, 0)
    if answer == 1:
        return -1
    else:
        return answer