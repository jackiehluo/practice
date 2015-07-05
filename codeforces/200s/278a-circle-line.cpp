#include <iostream>
using namespace std;

int main()
{
    int n, s, t;
    cin >> n;
    int f[n] = {0}, d, sum(0);

    for (int i = 2; i <= n + 1; i++)
    {
        cin >> d;
        sum += d;
        f[i] = sum;
    }

    cin >> s >> t;

    if (s > t)
        swap(s, t);

    cout << min(f[t] - f[s], f[n + 1] - (f[t] - f[s])) << endl;
    return 0;
}