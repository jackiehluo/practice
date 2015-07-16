#include <iostream>
using namespace std;

int main()
{
    int n, m, t, h(0), l(101), v(101);
    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        cin >> t;
        h = max(h, t);
        l = min(l, t);
    }

    for (int i = 0; i < m; i++)
    {
        cin >> t;
        v = min(v, t);
    }

    int tl = max(h, l * 2);
    cout << (tl < v ? tl : -1) << endl;
    return 0;
}