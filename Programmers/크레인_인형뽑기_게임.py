def solution(board, moves):
    answer = 0
    baguni = []
    for col in moves:
        for row in range(len(board)):
            if board[row][col-1] > 0:
                print(col,board[row][col-1])
                baguni.append(board[row][col-1])
                board[row][col-1] = 0
                break
        if len(baguni)>1 and baguni[-1] == baguni[-2]:
            print(baguni)
            baguni = baguni[:-2]
            answer += 2
    return answer