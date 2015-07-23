#include <iostream>
using namespace std;

int main()
{
    int n, m(1), t;
    cin >> n;

    while (n)
    {
        if (n % 10 == 4) t += m;
        else t += 2 * m;
        n /= 10, m *= 2;
    }

    cout << t << endl;
    return 0;
}
