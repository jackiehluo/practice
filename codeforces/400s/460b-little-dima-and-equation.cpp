#include <iostream>
using namespace std;

int main()
{
    int a, b, c, n(0), s(0), x;
    cin >> a >> b >> c;
    int r[100];
    long long int y;

    for (int i = 1; i < 100; i++)
    {
        y = 1;
        for (int j = 0; j < a; j++) y *= i;
        y *= b;
        y += c;
        if (y >= 1000000000) continue;
        s = 0;
        x = y;
        while (y)
        {
            s += y % 10;
            y /= 10;
        }
        if (s == i) r[n++] = x; 
    }

    cout << n << endl;
    for (int i = 0; i < n; i++) cout << r[i] << " ";

    return 0;
}