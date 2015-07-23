#include <algorithm>
#include <iostream>
using namespace std;

int main()
{
    long long n, d;
    cin >> n;
    long long f[n];
    long long a = 1, b = 1;

    for(int i = 0; i < n; i++)
        cin >> f[i];

    sort(f, f + n);
    d = f[n - 1] - f[0];

    if(f[0] == f[n - 1])
        cout << d << " " << (n - 1) * n / 2 << endl;
    else
    {
        for(int j = 1; j < n - 1; j++)
        {
        if(f[j] == f[n - 1])
            a++;
        else if(f[j] == f[0])
            b++;
        }
        cout << d << " " << a * b << endl;
    }

    return 0;
}
