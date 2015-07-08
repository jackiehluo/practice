#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int n, a, b, c, d, s(0);
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> a >> b >> c >> d;
        s += (abs(c - a) + 1) * (abs(d - b) + 1);
    }

    cout << s << endl;
    return 0;
}