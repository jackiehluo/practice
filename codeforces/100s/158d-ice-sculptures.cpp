#include <iostream>
using namespace std;

int main()
{
    int n, t(0);
    cin >> n;
    int a[n];

    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
        t += a[i];
    }

    for (int j = 1; j <= n; j++)
    {
        if (n % j != 0) continue;
        if (n / j < 3) continue;
        for (int k = 1; k <= j; k++)
        {
            int c = 0;
            for (int i = k; i <= n; i += j)
                c += a[i];
            if(c > t) t = c;
        }
    }

    cout << t << endl;
    return 0;
}
