#include <iostream>
using namespace std;

int main()
{
    int n, a(0), b(0);
    string s;
    cin >> n >> s;

    for (int i = 0; i < n / 2; i++)
    {
        if (s[i] != '7' and s[i] != '4')
        {
            cout << "NO" << endl;
            return 0;
        }
        a += s[i] - '0';
    }

    for (int i = n / 2; i < n; i++)
    {
        if (s[i] != '7' and s[i] != '4')
        {
            cout << "NO" << endl;
            return 0;
        }
        b += s[i] - '0';
    }

    if (a == b)
    {
        cout << "YES" << endl;
        return 0;
    }
    cout << "NO" << endl;
    return 0;
}