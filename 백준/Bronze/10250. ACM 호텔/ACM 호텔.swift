import Foundation

let count = Int(readLine()!)!

for _ in 0..<count {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    let floorNumber = input[0]
    let roomNumber = input[1]
    let guestNumber = input[2]

    var numberY = guestNumber % floorNumber
    var numberX = 0
    if numberY == 0 {
        numberX = guestNumber / floorNumber
        numberY = floorNumber
    } else {
        numberX = guestNumber / floorNumber + 1
    }
    
    if numberX < 10 {
        let result = String(numberY) + "0" + String(numberX)
        print(result) 
    } else {
        let result = String(numberY) + String(numberX)
        print(result)
    }
}