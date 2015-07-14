#include <iostream>
using namespace std;

int main()
{
    int n, m, t;
    cin >> n >> m;
    int a[100005], d[100005] = {0};
    bool v[100005];

    for (int i = 1; i <= n; i++)
        cin >> a[i];

    for (int i = n; i >= 1; i--)
    {
        if (!v[a[i]])
          d[i]++;
        v[a[i]] = true;
    }

    for (int i = n; i >= 1; i--)
        d[i] += d[i + 1];

    for (int i = 0; i < m; i++)
    {
        cin >> t;
        cout << d[t] << endl;
    }
    
    return 0;
}