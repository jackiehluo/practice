#include <iostream>
using namespace std;

int main()
{
    string s;
    char c;
    bool o = false;
    cin >> s;
    for(int i = 0; i < s.length(); i++)
    {
        c = s[i];
        if(c == 'H' || c == 'Q' || c == '9')
            o = true;
    }
    if(o == true)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}
