#include <iostream>
using namespace std;

int main()
{
    int n, m, t;
    cin >> n >> m;
    int l[n + 1] = {0};

    for (int i = 0; i < m; i++)
    {
        cin >> t;
        for (int j = t; j <= n; j++)
            if (l[j] == 0) l[j] = t;
    }

    for (int i = 1; i <= n; i++) cout << l[i] << " ";

    return 0;
}
