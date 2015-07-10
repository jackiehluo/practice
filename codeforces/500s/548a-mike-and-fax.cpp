#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s;
    int n;
    cin >> s >> n;

    if (s.length() % n > 0)
    {
        cout << "NO" << endl;
        return 0;
    }

    int l = s.length() / n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < l / 2; j++)
            if (s[j + i * l] != s[(i + 1) * l - j - 1])
            {
                cout << "NO" << endl;
                return 0;
            }

    cout << "YES" << endl;
    return 0;
}