#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n;
    string s, p[8] = {"vaporeon", "jolteon", "flareon", "espeon",
                    "umbreon", "leafeon", "glaceon", "sylveon"};
    cin >> n >> s;
    for (string pokemon : p)
        if (pokemon.length() == n)
        {
            bool m = true;
            for (int i = 0; i < n; i++)
                if (s[i] != '.' and s[i] != pokemon[i]) m = false;
            if (m)
            {
                cout << pokemon << endl;
                return 0;
            }
        }
}