#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, s(0), d(0);
    cin >> n;
    int a[n];

    for (int i = 0; i < n; i++)
        cin >> a[i];

    sort(a, a + n);

    for (int i = 0; i < n; i++)
        if (a[i] >= s)
        {
            d++;
            s += a[i];
        }

    cout << d << endl;
    return 0;
}