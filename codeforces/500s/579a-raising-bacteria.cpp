#include <iostream>
using namespace std;

int main()
{
    int n, b(0);
    cin >> n;
    n *= 2;

    while (n /= 2)
        b += n % 2;

    cout << b << endl;
    return 0;
}