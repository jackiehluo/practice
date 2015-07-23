#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    double n, x, y;
    cin >> n >> x >> y;
    cout << (x * 100 >= n * y ? 0 : (int)ceil(y * n / 100 - x));
    return 0;
}
