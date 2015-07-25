#include <iostream>
using namespace std;

int main()
{
    int n, k, h[200005];
    cin >> n >> k;
    h[0] = 0;
    for (int i = 1; cin >> h[i]; i++) h[i] += h[i - 1];
    int m(100000000), r;
    for (int i = 0; i <= n - k; i++)
        if (h[i + k] - h[i] < m)
        {
            m = h[i + k] - h[i];
            r = i + 1;
        }
    cout << r << endl;
    return 0;
}
