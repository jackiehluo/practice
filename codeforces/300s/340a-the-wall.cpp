#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int x, y, a, b;
    cin >> x >> y >> a >> b;
    cout << b / (x * y / __gcd(y, x)) - (a - 1) / (x * y/ __gcd(x, y));
    return 0;
}