#include <iostream>
#include <map>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    map<string, string> d;
    string a, b, s;

    for (int i = 0; i < m; i++)
    {
        cin >> a >> b;
        if (a.size() > b.size())
            d[a] = b;
        else
            d[a] = a;
    }

    for (int i = 0; i < n; i++)
    {
        cin >> s;
        cout << d[s] << " ";
    }

    return 0;
}