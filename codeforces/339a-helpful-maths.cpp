#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    string s;
    cin >> s;
    int n[100] = {};
    int c = 0;
    int d = 100 - (s.length() + 1) / 2;

    for(int i = 0; i < s.length(); i++)
    {
        if(s[i] == '1' || s[i] == '2' || s[i] == '3')
        {
            n[c] = s[i] - '0';
            c++;
        }
    }
    
    sort(begin(n), end(n));

    for(int j = 0; j < s.length(); j++)
    {
        if(j % 2 == 0)
        {
            cout << n[d];
            d++;
        }
        else
            cout << "+";
    }

    return 0;
}
