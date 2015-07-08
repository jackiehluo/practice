#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int r[n], d[n - 1], s(0), m(1000);
    cin >> r[0];

    for (int i = 1; i < n; i++)
    {
        cin >> r[i];
        d[i] = r[i] - r[i - 1];
        s = max(s, d[i]);
    }

    for (int i = 2; i < n; i++)
        m = max(min(m, d[i] + d[i - 1]), s);
    
    cout << m << endl;
    return 0;
}
