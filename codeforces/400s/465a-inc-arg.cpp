#include <iostream>
using namespace std;

int main()
{
    int n, d(0);
    string s;
    cin >> n >> s;

    for (int i = 0; i < n; i++)
        if (s[i] == '1')
            d++;
        else
            break;

    cout << min(n, d + 1) << endl;
    return 0;
}