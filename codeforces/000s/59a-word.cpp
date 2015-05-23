#include <iostream>
#include <algorithm> 
#include <ctype.h>
#include <stdio.h>
#include <string>
using namespace std;

int main()
{
    string s;
    int lower = 0,
        upper = 0;
    cin >> s;

    for (int i = 0; i < s.length(); i++)
    {
        if (isupper(s[i]))
            upper++;
        else if (islower(s[i]))
            lower++;
    }

    if (upper > lower)
        transform(s.begin(), s.end(), s.begin(), ::toupper);
    else
        transform(s.begin(), s.end(), s.begin(), ::tolower);
    cout << s << endl;
    return 0;
}