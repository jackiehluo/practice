#include <iostream>
using namespace std;

int main()
{
    int n, t, a, i;
    cin >> n >> t;
    a = (n - t) % n;
    for (i = 1; i < n; i++)
    {
        cin >> t;
        if ((t + n - a * ((i & 1) * 2 - 1)) % n != i) break;
    }
    cout << (i >= n ? "Yes" : "No") << endl;
    return 0;
}