#include <iostream>
using namespace std;

int main()
{
    string s;
    char c;
    cin >> s;
    for(int i = 0; i < s.length(); i++)
    {
        c = tolower(s[i]);
        if(c == 'a' || c == 'e' || c == 'i' ||
                c == 'o' || c == 'u' || c == 'y')
            continue;
        else
            cout << "." << c;
    }
    return 0;
}
