#include <iostream>
using namespace std;

int main()
{
    int n, m, t(0);
    cin >> n >> m;

    while (n > 0 and m > 0)
    {
        if (n == 1 and m == 1)
            break;
        if (n < m)
            n--, m -= 2;
        else
            n -= 2, m--;
        t++;
    }

    cout << t << endl;
    return 0;
}