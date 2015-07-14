#include <iostream>
using namespace std;

int main()
{
    int n, t, c, s, p(0), w(0);
    cin >> n >> t >> c;

    for (int i = 0; i < n; i++)
    {
        cin >> s;
        if (s <= t) p++;
        else p = 0;
        if (p >= c) w++;
    }

    cout << w << endl;
    return 0;
}