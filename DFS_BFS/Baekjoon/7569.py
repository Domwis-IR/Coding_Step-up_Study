from collections import deque

def parse_input():
    """
    1. 입력 받기
    """
    # Input 받기
    m, n, h = map(int, input().split())
    grid = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

    # 익지 않은 토마토 개수
    upriped_tomato = 0

    # 익은 토마토들을 Queue에 넣어준다. <- 시작점
    # 안 익은 토마토의 갯수를 세준다. 
    q = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if grid[i][j][k] == 1:
                    q.append((i, j, k))
                elif grid[i][j][k] == 0:
                    upriped_tomato += 1
    
    return m, n, h, grid, q, upriped_tomato


def bfs(m, n, h, grid, q, unriped_tomato):
    """
    2. BFS (너비 우선 탐색, Breadth-First Search)
    3. 날짜 하루씩 +1 증가

    Args:
        m (int): num of column
        n (int): num of row
        h (int): num of height
        grid (3D Array): given box of tomatoes
        q (deque): queue for BFS
        unriped_tomato (int): num of unriped tomato
    """
    # 자료 구조 정의 
    # grid를 이용해서 visited 및 익은 토마토를 관리한다.
    days = 0 # 최소 날짜 카운트

    # 상하좌우위아래 이동 리스트
    dz = [0, 0, 0, 0, 1, -1]
    dy = [-1, 1, 0, 0, 0, 0]
    dx = [0, 0, -1, 1, 0, 0]
    
    # BFS 탐색 시작
    while(q):
        for _ in range(len(q)):
            z, y, x = q.popleft()
            for i in range(6):
                nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
                if (0 <= nz < h) and (0 <= ny < n) and (0 <= nx < m) and grid[nz][ny][nx] == 0:
                    grid[nz][ny][nx] = 1 # 익은 토마토 처리
                    unriped_tomato -= 1
                    q.append((nz, ny, nx))
                    # print(f"Tomato ripened at: ({nz}, {ny}, {nx})")  # 디버깅용 출력

        # # Debuggin Code
        # for _ in range(h):
        #     print(grid[_])
        
        days += 1
        # print(f"Day: {days}")
    
    # 마지막으로 남은 토마토의 경우 더이상 익힐 수 없어 days - 1을 반환한다.
    return days - 1 if unriped_tomato == 0 else -1

def main():
    # 입력 받기
    m, n, h, grid, q, unriped_tomato = parse_input()

    # BFS 탐색
    result = bfs(m, n, h, grid, q, unriped_tomato)

    # 결과 출력
    print(result)

if __name__ == "__main__":
    main()