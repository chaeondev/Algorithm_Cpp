import Foundation

func solution(_ my_string:String, _ overwrite_string:String, _ s:Int) -> String {
    var strArray = my_string.map { $0 }
    var overArray = overwrite_string.map { $0 }
    strArray.replaceSubrange(s..<s+overArray.count, with: overArray)
    let result = strArray.map { String($0) }.joined()
    return result
}