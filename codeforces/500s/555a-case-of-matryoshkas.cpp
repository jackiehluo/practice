#include <iostream>
using namespace std;

int main()
{
    int n, k, m, t, r(0);
    cin >> n >> k;
    for (int i = 0; i < k; i++)
    {
        cin >> m;
        int l(0);
        while (m--)
        {
            cin >> t;
            if (t == l + 1) r++, l++;
        }
    }
    n -= r - 1;
    cout << n - k + n - 1 << endl;
    return 0;
}
