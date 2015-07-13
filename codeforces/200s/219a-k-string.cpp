#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
    int k, n[256];
    string s;
    cin >> k >> s;

    for (char c : s)
        n[c]++;

    for (char c = 'a'; c <= 'z'; c++)
        if (n[c] % k != 0)
        {
            cout << -1 << endl;
            return 0;
        }

    for (int i = 0; i < k; i++)
        for (char c = 'a'; c <= 'z'; c++)
            for (int j = n[c] / k - 1; j >= 0; j--)
                cout << c;

    return 0;
}
