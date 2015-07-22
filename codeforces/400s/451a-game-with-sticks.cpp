#include <iostream>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;
    int i = a * b;
    int t = 0;

    while (i > 0)
    {
        t++;
        i -= a + b - 1;
        a--;
        b--;
    }

    if (t % 2 == 0) cout << "Malvika" << endl;
    else cout << "Akshat" << endl;
    return 0;
}
