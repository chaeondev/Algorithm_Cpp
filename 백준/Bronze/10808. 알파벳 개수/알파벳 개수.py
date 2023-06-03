## 10808
str = input()
alpha = [0] * 26 ### 리스트 초기화 1차원 배열
for i in str:
    alpha[ord(i)-97] += 1 ### ord() : 문자를 아스키코드로 변환
for i in alpha:
    print(i, end=' ')
### 아스키 코드에서 a는 97이므로 a를 빼주면 0부터 시작하는 인덱스를 얻을 수 있다.