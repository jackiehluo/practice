#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    int f[n];
    int p = 0, t = 0;

    for(int i = 0; i < n; i++)
        cin >> f[i];

    sort(f, f + n);

    for(int j = n - 1; j >= 0; j--)
    {
        p++;
        if(p == 1)
            t += f[j] - 1;
        else if(p == k)
        {
            t += f[j + 1] - 1;
            p = 0;
        }
        else
            t += f[j + 1] - f[j];
    }
    if(n % k != 0)
        t += f[0] - 1;

    cout << t << endl;
    return 0;
}