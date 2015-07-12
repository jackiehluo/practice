#include <iostream>
using namespace std;

int main()
{
    int n, k;
    cin >> n;
    string s, t, p = "/";

    for (int i = 1; i <= n; i++)
    {
        cin >> s;
        if (s == "cd")
        {
            cin >> s;
            s += '/';
            for (int j = 0; j < s.size(); j++)
            {
                t += s[j];
                if (s[j] == '/')
                {
                    if (t == "/")
                        p = t;
                    else if (t == "../")
                    {
                        for (k = p.size() - 1; p[k - 1] != '/'; k--);
                        p.resize(k);
                    }
                    else
                        p += t;
                    t = "";
                }
            }
        }
        else
            cout << p << endl;
    }

    return 0;
}