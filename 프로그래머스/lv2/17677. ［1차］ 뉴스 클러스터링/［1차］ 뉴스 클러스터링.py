def solution(str1, str2):
    answer = 0
    firstSet = [str1[i:i+2] for i in range(len(str1))]
    secondSet = [str2[i:i+2] for i in range(len(str2))]
    
    # firstSet 정리
    ### 길이 2 아닌 것 0으로 치환
    ### 영어 문자열 아닌 경우 0으로 치환하고 영어 문자열은 소문자로 바꿈
    for i in range(len(firstSet)):
        if len(firstSet[i]) != 2:
            firstSet[i] = '0'
        if firstSet[i].isalpha() != True:
            firstSet[i] = '0'
        else:
            firstSet[i] = firstSet[i].lower()
    ### 0인 요소들 제거
    firstSet = [i for i in firstSet if i != '0']
    
    
    # secondSet 정리
    for i in range(len(secondSet)):
        if len(secondSet[i]) != 2:
            secondSet[i] = '0'
        if secondSet[i].isalpha() != True:
            secondSet[i] = '0'
        else:
            secondSet[i] = secondSet[i].lower()

    secondSet = [i for i in secondSet if i != '0']

    
    ### 교집합 구하기
    intersect = [] 
    commonSet = set()
    for i in range(len(firstSet)):
        for j in range(len(secondSet)):
            if firstSet[i] == secondSet[j]:
                i_cnt = firstSet.count(firstSet[i])
                j_cnt = secondSet.count(secondSet[j])
                commonSet.add((firstSet[i], i_cnt, j_cnt))
                
    commonList = list(commonSet)
    
    for common in commonList:
        if common[1] == 1 and common[2] == 1:
            intersect.append(common[0])
        else:
            for _ in range(min(common[1], common[2])):
                intersect.append(common[0])

                
    ### 합집합 구하기
    union = []
    
    for common in commonList:
        if common[1] == 1 and common[2] == 1:
            union.append(common[0])
        else:
            for _ in range(max(common[1], common[2])):
                union.append(common[0])
    
    for i in range(len(firstSet)):
        if firstSet[i] not in intersect:
            union.append(firstSet[i])
    for j in range(len(secondSet)):
        if secondSet[j] not in intersect:
            union.append(secondSet[j])
            
    ### 자카드 유사도 구하기
    score = 0
    if len(intersect) == 0 and len(union) == 0:
        score = 1
    else:
        score = len(intersect) / len(union)
    
    answer = int(score*65536)
            
    return answer
