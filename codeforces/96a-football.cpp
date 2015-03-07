#include <iostream>
using namespace std;

int main()
{
    string s;
    int n = 1;
    int m = 0;
    cin >> s;

    for(int i = 0; i < s.length() - 1; i++)
    {
        if(s[i] == s[i + 1])
        {
            n++;
            if(n > m)
                m = n;
        }
        else
            n = 1;
    }

    if(m >= 7)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}
