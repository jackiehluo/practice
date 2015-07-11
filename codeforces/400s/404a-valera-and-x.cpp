#include <iostream>
#include <set>
using namespace std;

int main()
{
    int n;
    cin >> n;
    string s;
    set<char> x, y;

    for (int i = 0; i < n; i++)
    {
        cin >> s;
        for (int j = 0; j < n; j++)
            if (i == j or i + j == n - 1)
                x.insert(s[j]);
            else
                y.insert(s[j]);
    }

    if (x.size() == 1 and y.size() == 1 and *x.begin() != *y.begin())
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}