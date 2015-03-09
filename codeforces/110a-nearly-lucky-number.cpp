#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main()
{
    string s;
    cin >> s;
    int c = 0;
    bool l = true;

    for(int i = 0; i < s.length(); i++)
    {
        if(s[i] == '4' or s[i] == '7')
            c++;
    }

    stringstream ss;
    ss << c;
    string n;
    ss >> n;

    for(int j = 0; j < n.length(); j++)
    {
        if(n[j] != '4' and n[j] != '7')
            l = false;
    }

    if(l == true)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}
