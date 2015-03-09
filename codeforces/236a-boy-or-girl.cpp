#include <algorithm>
#include <iostream>
using namespace std;

int main()
{
    string s;
    cin >> s;
    int c = 1;

    sort(s.begin(), s.end());
    
    for(int i = 0; i < s.length() - 1; i++)
    {
        if(s[i] != s[i + 1])
            c++;
    }

    if(c % 2 == 0)
        cout << "CHAT WITH HER!" << endl;
    else
        cout << "IGNORE HIM!" << endl;
    return 0;
}
