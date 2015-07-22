#include <iostream>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    char s[m];

    for (int i = 0; i < n; i++)
    {
        cin >> s;
        for (int j = 0; j < m; j++)
            if (s[j] == '.') cout << ((i + j) % 2 ? 'W' : 'B');
            else cout << '-';
        cout << endl;
    }
    return 0;
}
