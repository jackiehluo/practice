#include <iostream>
using namespace std;

int main()
{
    int n, s, x, y, m(0);
    bool a = false;
    cin >> n >> s;

    for (int i = 0; i < n; i++)
    {
        cin >> x >> y;
        if (s > x or (s == x and y == 0))
        {
            a = true;
            if (y > 0 and 100 - y > m)
                m = 100 - y;
        }
    }

    if (a)
        cout << m << endl;
    else
        cout << -1 << endl;
    return 0;
}