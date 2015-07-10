#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    long long d;

    for (int i = 9; n > 0; i *= 10)
    {
        d += n;
        n -= i;
    }

    cout << d << endl;
    return 0;
}