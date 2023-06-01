def solution(array, height):
    answer = 0
    array.sort()
    for i in array:
        if i > height:
            answer = len(array) - array.index(i)
            break

    return answer