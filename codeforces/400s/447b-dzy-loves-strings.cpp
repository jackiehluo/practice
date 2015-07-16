#include <iostream>
#include <string>
using namespace std;

int main ()
{
    string s;
    cin >> s;
    int k, m(0), t(0), a[26];
    cin >> k;

    for (int i = 0; i < 26; i++)
    {
        cin >> a[i];
        if (a[i] > m) m = a[i];
    }

    for (int i = 0; i < s.length() + k; i++)
        if (i < s.length()) t += (i + 1) * a[s[i] - 'a'];
        else t += m * (i + 1);

    cout << t << endl;
    return 0;
}