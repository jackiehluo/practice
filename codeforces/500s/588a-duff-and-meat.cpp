#include <iostream>
using namespace std;

int main()
{
    int n, a, p, c(100), t(0);
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> a >> p;
        c = min(c, p);
        t += a * c;
    }

    cout << t << endl;
    return 0;
}