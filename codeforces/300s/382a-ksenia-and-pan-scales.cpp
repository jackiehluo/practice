#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s, t, l, r;
    cin >> s;
    int p = s.find('|');
    l = s.substr(0, p);
    r = s.substr(p + 1);
    cin >> t;
    for (auto c : t)
        if (l.size() <= r.size()) l += c;
        else r += c;
    cout << (l.size() == r.size() ? l + "|" + r : "Impossible") << endl;
    return 0;
}
