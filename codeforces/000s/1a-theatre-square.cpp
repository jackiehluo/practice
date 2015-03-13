#include <iostream>
using namespace std;

int main(){
    long long n, m, a;
    cin>>n>>m>>a;
    cout<<(((n + a - 1) / a) * ((m + a - 1) / a));
    return 0;
}
