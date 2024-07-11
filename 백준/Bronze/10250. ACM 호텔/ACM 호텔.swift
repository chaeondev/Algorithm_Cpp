import Foundation

let count = Int(readLine()!)!

for _ in 0..<count {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    let (H, W, N) = (input[0], input[1], input[2])
    let floor = N % H == 0 ? H : N % H
    let room = (N - 1) / H + 1
    print(floor * 100 + room)
}