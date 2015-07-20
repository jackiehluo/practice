#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;

    if (k > n)
    {
        cout << -1 << endl;
        return 0;
    }

    int a[n];
    for (int i = 0; i < n; i++) cin >> a[i];
    sort(a, a + n);
    cout << a[n - k] << " 0" << endl;
    return 0;
}