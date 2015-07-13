#include <iostream>
using namespace std;

int main()
{
    int n, k, t(0);
    cin >> n >> k;
    string s;

    for (int i = 0; i < n; i++)
    {
        cin >> s;
        int d = 0;
        for (char c : s)
            if (c == '4' or c == '7')
                d++;
        if (d <= k)
            t++;
    }

    cout << t << endl;
    return 0;
}
