import Foundation

let count = Int(readLine()!)!

for _ in 0..<count {
    let input = Array(readLine()!)
    var scoreArray = Array(repeating: 0, count: input.count)

    for i in 0..<input.count {
        if input[i] == "O" {
            if i != 0 {
                if input[i-1] == input[i] {
                    scoreArray[i] = scoreArray[i-1] + 1
                } else {
                    scoreArray[i] = 1
                }
            } else {
                scoreArray[i] = 1
            }
        }
    }

    let sum = scoreArray.reduce(0, +)
    print(sum)
}