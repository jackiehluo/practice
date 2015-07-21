#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s;
    cin >> s;
    for (int i = 0; i < s.length(); i++)
        for (int j = i + 1; j <= s.length(); j++)
            if (s.substr(0, i) + s.substr(j) == "CODEFORCES")
            {
                cout << "YES" << endl;
                return 0;
            }
    cout << "NO" << endl;
    return 0;
}