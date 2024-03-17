import Foundation

let n = Int(readLine()!)!
var hint: [[Int]] = []
for _ in 0..<n {
    hint.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}

var answer = 0
for number in 123...987 {
    let numA = number / 100
    let numB = (number % 100) / 10
    let numC = number % 10
    
    // 0을 포함하는 숫자 또는 중복된 숫자가 있는 경우 건너뜀
    if numA == 0 || numB == 0 || numC == 0 || numA == numB || numB == numC || numC == numA {
        continue
    }
    
    var cnt = 0
    for arr in hint {
        let hintNumber = arr[0]
        let strike = arr[1]
        let ball = arr[2]
        
        let hintA = hintNumber / 100
        let hintB = (hintNumber % 100) / 10
        let hintC = hintNumber % 10
        
        var ballCnt = 0
        var strikeCnt = 0
        
        if hintA == numA {
            strikeCnt += 1
        } else if [numB, numC].contains(hintA) {
            ballCnt += 1
        }
        
        if hintB == numB {
            strikeCnt += 1
        } else if [numA, numC].contains(hintB) {
            ballCnt += 1
        }
        
        if hintC == numC {
            strikeCnt += 1
        } else if [numA, numB].contains(hintC) {
            ballCnt += 1
        }
        
        if ball == ballCnt && strike == strikeCnt {
            cnt += 1
        }
    }
    
    if cnt == n {
        answer += 1
    }
}

print(answer)