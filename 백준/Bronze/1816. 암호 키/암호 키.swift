import Foundation

let n = Int(readLine()!)!

for i in 0..<n {
    let number = Int(readLine()!)!
    for j in 2...1_000_000 {
        if number % j == 0 {
            print("NO")
            break
        }
        
        if j == 1_000_000 {
            print("YES")
        }
    }
}