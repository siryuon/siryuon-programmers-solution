def solution(board, moves):
    basket = []
    answer = []
    count = 0
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                answer.append(board[i][move-1])
                board[i][move-1] = 0
                break
        if len(answer) >=2 and answer[-1] == answer[-2]:
            answer = answer[:-2]
            count += 2

    return count
