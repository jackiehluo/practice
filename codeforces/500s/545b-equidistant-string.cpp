#include <iostream>
using namespace std;

int main()
{
    string s, t, p;
    cin >> s >> t;
    int c(0);

    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == t[i])
            p += s[i];
        else
        {
            c++;
            if (c % 2 == 1)
                p += s[i];
            else
                p += t[i];
        }
    }

    if (c % 2 == 1)
        cout << "impossible" << endl;
    else
        cout << p << endl;
    return 0;
}