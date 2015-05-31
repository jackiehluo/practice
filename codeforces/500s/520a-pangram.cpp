#include <iostream>
#include <ctype.h>
#include <map>
#include <stdio.h>
using namespace std;

int main()
{
    int n;
    string s;
    map<char, int> counts;
    cin >> n >> s;

    for (int i = 0; i < n; i++)
    {
        char c = tolower(s[i]);
        if (counts[c])
            counts[c]++;
        else
            counts[c] = 1;
    }

    if (counts.size() == 26)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}