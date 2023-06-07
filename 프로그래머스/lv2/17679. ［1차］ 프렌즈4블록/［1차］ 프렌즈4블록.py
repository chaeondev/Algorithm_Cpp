def solution(m, n, board):
    answer = 0
    count = 0
    # string을 list로 변환 -> 2차원 리스트
    for i in range(m):
        board[i] = list(board[i])
    
    
    # answerSet에 2*2 있을경우 인덱스 tuple 추가 + 인덱스 원소가 0일경우 추가 X / answerSet 반환
    def search():
        answerSet = set()
        for i in range(m-1):
            for j in range(n-1):
                if (board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]) and board[i][j] != 0:
                    answerSet.add((i, j))
                    answerSet.add((i+1, j))
                    answerSet.add((i, j+1))
                    answerSet.add((i+1, j+1))
        return answerSet
    
    # Search 후 answerSet
    def remove(lst):    
        for tup in lst:
            board[tup[0]][tup[1]] = 0
    
    # 0자리로 끌어내리기
    
    def down():
        for i in range(m-1,-1,-1):
            for j in range(n):
                if board[i][j] == 0:
                    for k in range(i-1,-1,-1):
                        if board[k][j] != 0:
                            board[i][j] = board[k][j]
                            board[k][j] = 0
                            break
            
    while True:
        answerList = list(search())
        if len(answerList) == 0:
            break
        answer += len(answerList)
        remove(answerList)
        down()
    

                
    return answer