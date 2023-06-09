def solution(park, routes):
    answer = []
    
    park = [list(row) for row in park]

    
    ### 가로 길이, 세로길이 ###
    h = len(park)
    w = len(park[0])

    ## 시작점 구하기 ###
    pos = None
    for row_idx, row in enumerate(park):
        if "S" in row:
            pos = [row_idx, row.index("S")]


    ### 동서남북 dictionary ###
    direc = {}
    direc["E"] = [0,1]
    direc["W"] = [0,-1]
    direc["S"] = [1,0]
    direc["N"] = [-1,0]
    

    for route in routes:
        route = route.split(" ")
        d = route[0]
        count = int(route[1])
        canGo = True
        x, y = pos[0], pos[1]
        
        for _ in range(count):
            x += direc[d][0]
            y += + direc[d][1]

            if not (0 <= x < h and 0 <= y < w and park[x][y] != "X"):
                canGo = False
                break
        if canGo:
            pos = [x, y]
            
    
    return pos