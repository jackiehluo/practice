#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, d, m, a[105] = {0};
    cin >> n >> d;
    for (int i = 1; i <= n; i++) cin >> a[i];
    cin >> m;
    sort(a + 1, a + n + 1);
    for (int i = n + 1; i <= m; i++) a[i] = -d;
    for (int i = 1; i <= m; i++) a[i] += a[i - 1];
    cout << a[m] << endl;
    return 0;
}
