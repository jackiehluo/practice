#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    char s[200005];
    cin >> s;
    int m, t, c[200005];
    cin >> m;
    for (;cin >> t;) c[t - 1]++;
    int r(0), n = strlen(s);
    for (int i = 0; i < n / 2; i++)
    {
        r += c[i];
        if (r % 2) swap(s[i], s[n - i - 1]);
    }
    cout << s << endl;
    return 0;
}
