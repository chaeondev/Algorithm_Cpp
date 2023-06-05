def solution(k, tangerine):
    answer = 0
    typeOfTangerine = set(tangerine)
    typeNumber = dict()

    for i in tangerine:
        if i in typeNumber:
            typeNumber[i] += 1
        else:
            typeNumber[i] = 1
    
    sortedTypeNumber = sorted(typeNumber.items(), key=lambda x: x[1], reverse=True)

    for j in range(len(sortedTypeNumber)):
        k -= sortedTypeNumber[j][1]
        answer += 1
        if k <= 0:
            break
    
    return answer