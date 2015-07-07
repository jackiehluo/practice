#include <iostream>
using namespace std;

int main()
{
    int n, e(0), d(0);
    cin >> n;
    int p[n];
    p[0] = 0;

    for (int i = 1; i <= n; i++)
    {
        cin >> p[i];
        e += p[i - 1] - p[i];
        if (e < 0)
        {
            d -= e;
            e = 0;
        }
    }

    cout << d << endl;
    return 0;
}