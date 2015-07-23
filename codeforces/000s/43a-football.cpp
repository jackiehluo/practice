#include <iostream>
#include <map>
using namespace std;

int main()
{
    int n;
    cin >> n;
    map<string, int> g;
    string t, a, b;

    for (;cin >> t;)
    {
        g[t]++;
        if (a.empty()) a = t;
        else if (b.empty() and t != a) b = t;
    }

    if (g[a] > g[b]) cout << a << endl;
    else cout << b << endl;
    return 0;
}
