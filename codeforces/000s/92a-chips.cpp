#include <iostream>
using namespace std;

int main()
{
    int n, m, i(1);
    cin >> n >> m;

    while (true)
    {
        if (m >= i) m -= i;
        else break;
        if (i == n) i = 1;
        else i++;
    }

    cout << m << endl;
    return 0;
}
