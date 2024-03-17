let n = Int(readLine()!)!
var hint: [[Int]] = []
for _ in 0..<n {
    hint.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}

var answer = 0
for a in 1..<10 { //100의 자리수
    for b in 1..<10 { // 10의 자리수
        for c in 1..<10 { // 1의 자리수
            
            if a == b || b == c || c == a { // 똑같은 숫자 있으면 제외
                continue
            }
            //숫자가 정해졌다면
            
            var cnt = 0
            for arr in hint {
                let number = arr[0]
                let strike = arr[1]
                let ball = arr[2]
                
                //a,b,c 라는 숫자를 number와 비교해서
                //자리수를 나눠서 strike ball을 측정하는 부분
                var ballCnt = 0
                var strikeCnt = 0
                let numA = number / 100 // number의 100의 자리수
                let numB = (number % 100) / 10 //number의 10의 자리수
                let numC = number % 10 //number의 1의 자리수
                
                if [a,b,c].contains(numA) {
                    if a == numA {
                        strikeCnt += 1
                    } else {
                        ballCnt += 1
                    }
                }
                
                if [a,b,c].contains(numB) {
                    if b == numB {
                        strikeCnt += 1
                    } else {
                        ballCnt += 1
                    }
                }
                
                if [a,b,c].contains(numC) {
                    if c == numC {
                        strikeCnt += 1
                    } else {
                        ballCnt += 1
                    }
                }
                
                
                if ball == ballCnt && strike == strikeCnt {
                    cnt += 1
                }
                
            }
            
            if cnt == n {
                answer += 1
            }
        }
    }
    
}

print(answer)
