import Foundation

let n = Int(readLine()!)!
var board: [[Int]] = []
for _ in 0..<n {
    let coordinate = readLine()!.split(separator: " ").map { Int(String($0))! }
    board.append(coordinate)
}

var totalDistance: [[Int]] = []

var totalX: Set<Int> = []
var totalY: Set<Int> = []
for i in 0..<n {
    totalX.insert(board[i][0])
    totalY.insert(board[i][1])
}

var totalXArr = Array(totalX)
var totalYArr = Array(totalY)

for x in 0..<totalXArr.count {
    for y in 0..<totalYArr.count {
        let markX = totalXArr[x]
        let markY = totalYArr[y]
        var distance: [Int] = []
        for i in 0..<n {
            let pointX = board[i][0]
            let pointY = board[i][1]
            let dx = abs(markX - pointX)
            let dy = abs(markY - pointY)
            distance.append(dx+dy)
        }
        totalDistance.append(distance)
    }
}

for i in 0..<totalDistance.count {
    totalDistance[i].sort(by: <)
}

for i in 1...n {
    var ithDistance: [Int] = []
    for j in 0..<totalDistance.count {
        let mark = totalDistance[j]
        var distance = 0
        for k in 0..<i {
            distance += mark[k]
        }
        ithDistance.append(distance)
    }
    ithDistance.sort(by: <)
    print(ithDistance[0], terminator: " ")
}