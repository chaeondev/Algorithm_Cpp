def solution(n):
    answer = [[0 for col in range(n)] for row in range(n)]
    count = 1
    order = 0
    
    while count <= n**2:
        
        for i in range(order, n-order):
            answer[order][i] = count
            if count > n**2:
                break
            count += 1
        for j in range(1+order, n-order):
            answer[j][n-1-order] = count
            if count > n**2:
                break
            count += 1
        for k in range(n-2-order, -1+order, -1):
            answer[n-1-order][k] = count
            if count > n**2:
                break
            count += 1
        for m in range(n-2-order,order,-1):
            answer[m][order] = count
            if count > n**2:
                break
            count += 1
        if count > n**2:
            break
        order += 1
        
    return answer


