# 6과 n의 최소공배수를 구하는 문제
# 최소공배수는 (6*n)/최대공약수
# 즉 최대공약수도 구해야함.


def solution(n):
    answer = 0
    gcd = 0
    for i in range(1, max(6,n)+1):
        if 6 % i == 0 and n % i == 0:
            gcd = i
    answer = n/gcd
    return answer