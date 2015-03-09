#include <iostream>
using namespace std;

int main()
{
    string s;
    cin >> s;
    int p = 0;

    while(p < s.length() && s[p] != 'h')
    {
        p++;
    }
    p++;
    while(p < s.length() && s[p] != 'e')
    {
        p++;
    }
    p++;
    while(p < s.length() && s[p] != 'l')
    {
        p++;
    }
    p++;
    while(p < s.length() && s[p] != 'l')
    {
        p++;
    }
    p++;
    while(p < s.length() && s[p] != 'o')
    {
        p++;
    }

    if(p < s.length())
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    
    return 0;
}
