#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int n, i, j;
    cin >> n;
    long long int x, s;

    for (i = 1; i <= n; i++)
    {
        cin >> x;
        s = sqrt(x);
        for (j = 2; j * j <= s; j++)
            if (s % j == 0)
                break;
        if (j * j > s and s * s == x and x > 1)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}