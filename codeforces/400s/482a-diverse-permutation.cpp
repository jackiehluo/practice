#include <iostream>
using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    int c(n - k);
    bool d = true;

    for (int i = 1; i <= n - k; i++)
        cout << i << " ";

    for (int i = k; i >= 1; i--)
        if (d)
        {
            cout << c + i << " ";
            c += i;
            d = false;
        }
        else
        {
            cout << c - i << " ";
            c -= i;
            d = true;
        }

    return 0;
}