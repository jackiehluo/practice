#include <iostream>
using namespace std;

int main()
{
    string s, t;
    cin >> s;
    bool b = false;
    int p = 0;

    while(true)
    {
        if(s[p] == 'W' && s[p + 1] == 'U' && s[p + 2] == 'B')
        {
            p += 2;
            if(b == true)
            {
                t += " ";
                b = false;
            }
        }
        else
        {
            t += s[p];
            b = true;
        }
        p++;
        if(p == s.length())
            break;
    }

    cout << t << endl;
    return 0;
}
