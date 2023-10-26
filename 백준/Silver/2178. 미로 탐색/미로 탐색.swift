import Foundation

struct Queue<T> {
  var elements: [T] = []
  var index = 0 // front pointer

  var isEmpty: Bool {
    elements.count < index + 1
  }

  mutating func enqueue(_ data: T) {
    elements.append(data)
  }

  mutating func dequeue() -> T {
    let value = elements[index]
    index += 1
    return value
  }
}

let input = readLine()!.split(separator: " ").map { Int($0)! }
let n = input[0] // H
let m = input[1] // W

var board: [[Int]] = []
var vis: [[Int]] = .init(repeating: .init(repeating: -1, count: m), count: n)

let dy = [-1, 1, 0, 0]
let dx = [0, 0, -1, 1]

for _ in 1...n {
    let input = readLine()!.map { Int(String($0))! }
    board.append(input)
}

//print(board)

var queue = Queue<(Int, Int)>()
queue.enqueue((0,0))
vis[0][0] = 1

while !queue.isEmpty {
    let cur = queue.dequeue()
    for dir in  0..<4 {
        let ny = cur.0 + dy[dir]
        let nx = cur.1 + dx[dir]
        
        if ny < 0 || ny >= n || nx < 0 || nx >= m { continue }
        if vis[ny][nx] != -1 { continue }
        if board [ny][nx] == 0 { continue }
        
        queue.enqueue((ny, nx))
        vis[ny][nx] = vis[cur.0][cur.1] + 1
        
    }
}
//print(vis)
print(vis[n-1][m-1])