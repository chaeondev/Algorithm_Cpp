def solution(N, stages):
    answer = []
    fail = []

    for i in range(1, N+1):
        ja = len([x for x in stages if x == i])
        mo = len([x for x in stages if x >= i])
        if mo == 0:
            fail.append((i, 0))
        else:
            fail.append((i, ja/mo))

    fail.sort(key = lambda x: -x[1])
    
    answer = [x[0] for x in fail]
        
    return answer