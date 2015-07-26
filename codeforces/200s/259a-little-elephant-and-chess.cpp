#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s;
    for (;cin >> s;)
        for (int i = 1; i < s.length(); i++)
            if (s[i] == s[i - 1])
            {
                cout << "NO" << endl;
                return 0;
            }
    cout << "YES" << endl;
    return 0;
}
