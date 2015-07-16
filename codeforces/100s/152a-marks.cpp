#include <iostream>
using namespace std;

int main()
{
    int n, m, s(0);
    cin >> n >> m;
    char c[n][m];
    bool h[n] = {false};

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> c[i][j];

    for (int i = 0; i < m; i++)
    {
        char t = '0';
        for (int j = 0; j < n; j++)
            if (c[j][i] > t) t = c[j][i];
        for (int j = 0; j < n; j++)
            if (c[j][i] == t) h[j] = true;
    }

    for (int i = 0; i < n; i++)
        if (h[i]) s++;

    cout << s << endl;
    return 0;
}