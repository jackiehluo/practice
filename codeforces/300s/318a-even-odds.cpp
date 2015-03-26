#include <iostream>
using namespace std;

int main()
{
    long long n, k, x;
    cin >> n >> k;

    if(n % 2 == 0)
    {
        if(k <= n / 2)
            x = k * 2 - 1;
        else
            x = (k - n / 2) * 2;
    }
    else
    {
        if(k <= n / 2 + 1)
            x = k * 2 - 1;
        else
            x = (k - n / 2 - 1) * 2;
    }
    cout << x << endl;
    return 0;
}
