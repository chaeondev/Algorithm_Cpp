def solution(array):
    answer = set()
    cnt = []
    for i in array:
        cnt.append(array.count(i))

    for i in array:
        if array.count(i) == max(cnt):
            answer.add(i)
    if len(answer) > 1:
        return -1
    else:
        return list(answer)[0]