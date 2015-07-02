#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

string convert(int a) {
    if (a == 0)
        return "";
    return convert((a - 1) / 26) + (char)('A' + (a - 1) % 26);
}

int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n ; i++)
    {
        int a, b;
        char s[20];
        cin >> s;
        if (sscanf(s, "R%dC%d", &a, &b) == 2)
            cout << convert(b).c_str() << a << endl;
        else
        {
            int i;
            b = 0;
            for(i = 0; s[i] > '9' ; i++)
                b = b * 26 + 1 + s[i] - 'A';
            sscanf(s + i, "%d", &a);
            cout << "R" << a << "C" << b << endl;
        }
    }

    return 0;
}
