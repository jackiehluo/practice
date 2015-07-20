#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    long long int a, b, c, x, y;
    cin >> a >> b >> c;
    x = a * b * c;
    y = sqrt(x);
    cout << 4 * (y / a + y / b + y / c);
    return 0;
}
