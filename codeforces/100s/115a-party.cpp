#include <iostream>
using namespace std;

int main()
{
    int n, r(0), a[2005];
    cin >> n;
    for (int i = 1; cin >> a[i]; i++);
    for (int i = 1; i <= n; i++)
    {
        int j = 1, k = i;
        for (;a[k] != -1; k = a[k], j++);
        r = max(r, j);
    }
    cout << r << endl;
    return 0;
}
