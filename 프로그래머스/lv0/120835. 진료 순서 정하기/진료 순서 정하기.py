def solution(emergency):
    answer = []
    beforeSort = emergency[:]
    emergency.sort(reverse = True)
    for i in beforeSort:
        answer.append(emergency.index(i)+1)
    return answer