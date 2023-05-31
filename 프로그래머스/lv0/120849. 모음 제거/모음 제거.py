def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] in ["a", "e", "i", "o", "u"]:
            continue
        else:
            answer += my_string[i]
    return answer