#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<char> k {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';',
                    'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'};
    char d;
    string m;
    int p;
    cin >> d;
    cin >> m;

    if(d == 'R')
    {
        for(int i = 0; i < m.length(); i++)
        {
            p = find(k.begin(), k.end(), m[i]) - k.begin() - 1;
            cout << k[p];
        }
    }
    else
    {
        for(int j = 0; j < m.length(); j++)
        {
            p = find(k.begin(), k.end(), m[j]) - k.begin() + 1;
            cout << k[p];
        }
    }
    return 0;
}