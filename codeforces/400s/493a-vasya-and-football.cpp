#include <iostream>
using namespace std;

int main()
{
    int n, t, m, v, f[105][2] = {0};
    char p, c, s[2][25];
    cin >> s[0] >> s[1] >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> t >> p >> m >> c;
        v = p == 'a';
        if (f[m][v] < 2)
            if (!f[m][v] and c == 'y') f[m][v]++;
            else
            {
                f[m][v] = 2;
                cout << s[v] << " " << m << " " << t << endl;
            }
    }

    return 0;
}