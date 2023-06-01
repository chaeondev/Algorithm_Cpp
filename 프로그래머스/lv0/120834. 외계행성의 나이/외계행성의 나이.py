def solution(age):
    answer = ''
    age = str(age)

    for i in range(len(age)):
        if age[i] == '0':
            answer += 'a'
        elif age[i] == '1':
            answer += 'b'
        elif age[i] == '2':
            answer += 'c'
        elif age[i] == '3':
            answer += 'd'
        elif age[i] == '4':
            answer += 'e'
        elif age[i] == '5':
            answer += 'f'
        elif age[i] =='6':
            answer += 'g'
        elif age[i] == '7':
            answer += 'h'
        elif age[i] == '8':
            answer += 'i'
        else:
            answer += 'j'
    return answer