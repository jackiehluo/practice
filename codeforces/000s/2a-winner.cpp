#include <iostream>
#include <map>
using namespace std;

int main()
{
    int n;
    cin >> n;
    map<string, int> s, t;
    string p[n];
    int v[n], m(0);

    for (int i = 0; i < n; i++)
    {
        cin >> p[i] >> v[i];
        s[p[i]] += v[i];
    }

    for (int i = 0; i < n; i++) m = max(m, s[p[i]]);

    for (int i = 0; i < n; i++)
        if (s[p[i]] == m)
        {
            t[p[i]] += v[i];
            if (t[p[i]] >= m)
            {
                cout << p[i] << endl;
                return 0;
            }
        }
}
