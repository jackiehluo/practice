#include <iostream>
using namespace std;

int main()
{
    int n, t;
    cin >> n >> t;
    int c[n];
    int p = 0;

    for(int i = 0; i < n; i++) cin >> c[i];

    while(p < t - 1) p += c[p];

    if(p == t - 1) cout << "YES" << endl;
    else cout << "NO" << endl;
    return 0;
}
