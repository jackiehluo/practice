#include <iostream>
using namespace std;

int main()
{
    int n, b, m(0), t(1), a[100] = {0};
    cin >> n;

    while (n)
    {
        b = n % 10;
        m = max(m, b);
        for (int i = 0; i < b; i++) a[i] += t;
        t *= 10;
        n /= 10;
    }

    cout << m << endl;
    for (int i = 0; i < m; i++) cout << a[i] << " ";
    return 0;
}
