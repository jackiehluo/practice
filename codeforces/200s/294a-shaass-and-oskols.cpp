#include <iostream>
using namespace std;

int main()
{
    int n, m, x, y;
    cin >> n;
    int b[n];
    for (int i = 0; i < n; i++) cin >> b[i];
    cin >> m;

    for (int i = 0; i < m; i++)
    {
        cin >> x >> y;
        x--, y--;
        if (x > 0) b[x - 1] += y;
        if (x + 1 < n) b[x + 1] += b[x] - y - 1;
        b[x] = 0;
    }

    for (int w : b) cout << w << endl;
    return 0;
}
