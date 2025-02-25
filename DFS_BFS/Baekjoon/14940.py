from collections import deque

def bfs(n, m, grid, start_x, start_y):
    """
    1. 그래프 탐색 (Graph Traversal)

    주어진 지도는 2차원 그리드 형태의 그래프로 볼 수 있다.
    각 칸을 노드(Node)로, 상하좌우 이동을 간선(Edge)으로 간주할 수 있다.
    
    2. BFS (너비 우선 탐색, Breadth-First Search)

    BFS는 최단 거리를 구할 때 적합한 탐색 알고리즘이다.
    FIFO(First In First Out) 큐(Queue) 를 사용하여 탐색한다.
    한 지점에서 갈 수 있는 모든 지점을 먼저 방문한 후, 그 다음 깊이로 넘어간다.
    BFS를 사용하면 목표지점(2)에서 모든 지점까지의 최단 거리를 구할 수 있다.
    
    3. 2차원 배열과 이동

    입력으로 주어진 n x m 크기의 행렬을 다루는 방법을 이해해야 한다.
    4가지 방향 (상, 하, 좌, 우) 이동을 위한 좌표 변화를 정의해야 한다.
    
    4. 거리 배열 (Distance Array)

    탐색 결과를 저장하기 위한 별도의 2차원 배열을 만들어서 거리를 기록한다.
    목표 지점에서 BFS를 시작하고, 방문하는 노드에 현재 거리 + 1 값을 저장한다.

    Args:
        n (int): counts of row
        m (int): counts of column
        grid (2D array): graph itself
        start_x (int): starting point of x
        start_y (int): starting point of y
    """
    # 방문 위치 배열 초기화
    visited = [[-1] * m for _ in range(n)]

    # 4 방향 상하좌우 이동 리스트
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # BFS를 위한 큐 초기화
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = 0 # 목표 지점은 0으로 처리

    # BFS 탐색 시작
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위를 벗어나지 않고, 갈 수 있는 땅(1)이며, 아직 방문하지 않았다면
            if (0 <= nx < n and 0 <= ny < m) and grid[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1 # 거리 갱신
                queue.append((nx, ny))

    # 갈 수 없는 땅 
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                visited[i][j] = 0

    return visited

def main():
    # 입력 받기
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    # 시작 지점 찾기
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                start_x, start_y = i, j

    result = bfs(n, m, grid, start_x, start_y)

    for row in result:
        print(" ".join(map(str, row)))


# 실행

if __name__ == "__main__":
    main()