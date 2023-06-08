def solution(genres, plays):
    answer = []
    
    ### genres - plays - index tuple 리스트
    threeTupleList = []
    for i in range(len(genres)):
        threeTupleList.append((i, genres[i], plays[i]))

    
    ### 많이 재생된 장르 순서 결정
    typePlays = {}
    for i in range(len(genres)):
        if genres[i] in typePlays:
            typePlays[genres[i]] += plays[i]
        else:
            typePlays[genres[i]] = plays[i]
    sortedTypePlays = sorted(typePlays.items(), key = lambda x: x[1], reverse = True)



    for i in range(len(sortedTypePlays)):
        sameGenre = []
        for j in range(len(threeTupleList)):
            if sortedTypePlays[i][0] == threeTupleList[j][1]:
                sameGenre.append(threeTupleList[j])
        sameGenre = sorted(sameGenre, key = lambda x: x[2], reverse = True)
        if len(sameGenre) == 1:
            answer.append(sameGenre[0][0])
        else:
            answer.append(sameGenre[0][0])
            answer.append(sameGenre[1][0])

    return answer