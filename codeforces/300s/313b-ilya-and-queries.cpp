#include <iostream>
using namespace std;

int main() {
    string s;
    cin >> s;
    int c[s.length()], t(0);
    c[0] = 0;

    for (int i = 1; i < s.length(); i++)
    {
        if (s[i] == s[i - 1])
            t++;
        c[i] = t;
    }

    int q, l, r;
    cin >> q;

    for (int i = 0; i < q; i++)
    {
        cin >> l >> r;
        l--, r--;
        cout << c[r] - c[l] << endl;
    }
    return 0;
}
