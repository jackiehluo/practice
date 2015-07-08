#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, m, f(0);
    cin >> n >> m;
    char t[n][m];

    for (int i = 0; i < n; i++)
        cin >> t[i];

    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < m - 1; j++)
        {
            string w = "";
            w += t[i][j];
            w += t[i][j + 1];
            w += t[i + 1][j];
            w += t[i + 1][j + 1];
            sort(w.begin(), w.end());
            if (w == "acef")
                f++;
        }

    cout << f << endl;
    return 0;
}
