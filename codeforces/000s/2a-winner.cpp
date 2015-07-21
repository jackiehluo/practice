#include <iostream>
#include <map>
using namespace std;

int main()
{
    int n, t, m(0);
    cin >> n;
    string s, w;
    map<string, int> p;

    for (int i = 0; i < n; i++)
    {
        cin >> s >> t;
        p[s] += t;
        if (p[s] > m) m = p[s], w = s;
    }

    cout << w << endl;
    return 0;
}