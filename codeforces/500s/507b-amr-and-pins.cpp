#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int r, x1, y1, x2, y2;
    cin >> r >> x1 >> y1 >> x2 >> y2;
    double d = sqrt(pow(y2 - y1, 2.0) + pow(x2 - x1, 2.0));
    cout << (int)(ceil)(d / r / 2) << endl;
    return 0;
}