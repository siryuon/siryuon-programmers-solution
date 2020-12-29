def make_board(M, N, lock):
    board = [[0] * (M*2+N) for _ in range(M*2+N)]
             
    for i in range(N):
        for j in range(M):
            board[M+i][M+j] = lock[i][j]

    return board

def rotate(key):
    temp = [[0] * len(key) for _ in range(len(key))]
    n = len(key)
    for i in range(n):
        for j in range(n):
            temp[i][j] = key[n-1-j][i]
    for i in range(n):
        for j in range(n):
            key[i][j] = temp[i][j]

    return key

def unlock(M, N, board):
    count = 0
    
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False
    return True

def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]
            
def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]
            
def solution(key, lock):
    M, N = len(key), len(lock)
    board = make_board(M, N, lock)
    rotated_key = key
    
    for _ in range(4):
        rotated_key = rotate(rotated_key)
        for x in range(1, M+N):
            for y in range(1, M+N):
                attach(x, y, M, rotated_key, board)
                if unlock(M, N, board):
                    return True
                detach(x, y, M, rotated_key, board)
    return False

key = [[0,0,0], [1,0,0], [0,1,1]]
lock = [[1,1,1], [1,1,0], [1,0,1]]

print(solution(key, lock))
