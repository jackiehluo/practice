#include <iostream>
using namespace std;

int main()
{
    int n, t;
    cin >> n;
    int a = 0, b = 0, c = 0;

    for (int i = 0; i < n; i++)
    {
        cin >> t;
        a += t;
    }

    for (int i = 0; i < n - 1; i++)
    {
        cin >> t;
        b += t;
    }

    for (int i = 0; i < n - 2; i++)
    {
        cin >> t;
        c += t;
    }

    cout << a - b << endl;
    cout << b - c << endl;
    return 0;
}
