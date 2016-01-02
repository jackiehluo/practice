#include <iostream>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;

    if (a >= b)
    {
        a -= b;
        a /= 2;
        cout << b << ' ' << a << endl;
    }
    else
    {
        b -= a;
        b /= 2;
        cout << a << ' ' << b << endl;
    }

    return 0;
}