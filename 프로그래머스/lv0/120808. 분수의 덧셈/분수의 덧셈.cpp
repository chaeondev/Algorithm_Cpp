#include <string>
#include <vector>

using namespace std;

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    vector<int> answer;
    int n = numer1*denom2 + numer2*denom1;
    int dn = denom1*denom2;
    int gcd = 0;
    
    for(int i=2; i<=min(n,dn); i++) {
        if(n % i == 0 && dn % i ==0) {
            gcd = i;
        }
    }
    if(gcd != 0) {
        n /= gcd;
        dn /= gcd;
    }
    
    answer.push_back(n);
    answer.push_back(dn);
    
    return answer;
}



/*1번 시도*/

// #include <string>
// #include <vector>

// using namespace std;

// vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
//     vector<int> answer;
//     int n = numer1*denom2 + numer2*denom1;
//     int dn = denom1*denom2;
//     int gcd;
    
//     for(int i=2; i<=min(n,dn); i++) {
//         if(n % i == 0 && dn % i ==0) {
//             gcd = i;
//         }
//     }
//     if(gcd != 0) {
//         n /= gcd;
//         dn /= gcd;
//     }
    
//     answer.push_back(n);
//     answer.push_back(dn);
    
//     return answer;
// }