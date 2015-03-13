#include <iostream>
using namespace std;

int main()
{
    int a, b, c, d, e, s;
    cin >> a >> b >> c >> d >> e;

    s = a + b + c + d + e;

    if(s > 0 && s % 5 == 0)
        cout << (s / 5) << endl;
    else
        cout << -1 << endl;
    return 0;
}
