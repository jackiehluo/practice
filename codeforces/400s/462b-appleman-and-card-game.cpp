#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, k, c[26] = {0};
    cin >> n >> k;
    for (char l; cin >> l;) c[l - 'A']++;
    sort(c, c + 26);
    reverse(c, c + 26);
    long long int a(0);
    for (int i = 0; i < 26; i++)
    {
        int t = min(c[i], k);
        a += (long long int) t * t;
        k -= t;
    }
    cout << a << endl;
    return 0;
}