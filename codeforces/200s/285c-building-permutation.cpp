#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, a[300005];
    cin >> n;
    long long int t(0);
    for (int i = 0; i < n; i++) cin >> a[i];
    sort(a, a + n);
    for (int i = 0; i < n; i++) t += abs(a[i] - i - 1);
    cout << t << endl;
    return 0;
}