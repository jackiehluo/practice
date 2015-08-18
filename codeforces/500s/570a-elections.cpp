#include <iostream>
using namespace std;

int main()
{
    int n, m, r(1), h[1000], a[1000];
    cin >> n >> m;
    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= n; j++) cin >> h[j];
        int p = 1;
        for (int j = 2; j <= n; j++) if (h[p] < h[j]) p = j;
        a[p]++;
    }
    for (int i = 2; i <= n; i++) if (a[i] > a[r]) r = i;
    cout << r << endl;
    return 0;
}