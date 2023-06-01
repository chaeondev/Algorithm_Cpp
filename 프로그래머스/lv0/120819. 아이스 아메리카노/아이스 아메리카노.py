def solution(money):
    answer = []
    coffee = money//5500
    answer.append(coffee)
    answer.append(money-(coffee*5500))
    return answer