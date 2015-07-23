#include <iostream>
using namespace std;

int main()
{
    string s[4];
    cin >> s[0] >> s[1] >> s[2] >> s[3];

    for (int i = 0; i <= 2; i++)
        for (int j = 0; j <= 2; j++)
        {
            int d = 0, p = 0;
            for (int k = 0; k < 2; k++)
                for (int l = 0; l < 2; l++)
                    if (s[i + k][j + l] == '.') d++;
                    else p++;
            if ((d == 3 and p == 1) or (d == 1 and p == 3) or (d == 4) or (p == 4))
            {
                cout << "YES" << endl;
                return 0;
            }
        }

    cout << "NO" << endl;
    return 0;
}