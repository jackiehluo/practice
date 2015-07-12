#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    long long int n, x, s(0);
    cin >> n >> x;
    long long int c[n];

    for (int i = 0; i < n; i++)
        cin >> c[i];

    sort(c, c + n);

    for (int i = 0; i < n; i++)
    {
        s += c[i] * x;
        if (x > 1)
            x--;
    }

    cout << s << endl;
    return 0;
}