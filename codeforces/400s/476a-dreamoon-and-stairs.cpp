#include <iostream>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;

    bool multiple = false;
    int twos = n / 2;
    int ones = n - twos * 2;

    while (twos >= 0)
    {
        if ((ones + twos) % m == 0)
        {
            multiple = true;
            break;
        }
        twos--;
        ones = n - twos * 2;
    }

    if (multiple == true)
        cout << ones + twos << endl;
    else
        cout << -1 << endl;
    return 0;
}