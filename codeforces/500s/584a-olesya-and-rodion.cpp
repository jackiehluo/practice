#include <iostream>
using namespace std;

int main()
{
    int n, t, a(1);
    cin >> n >> t;

    if (n == 1 and t == 10)
        cout << -1 << endl;
    else
    {
        cout << t;
        if (t == 10) a++;
        for (a; a < n; a++)
            cout << '0';
    }

    return 0;
}