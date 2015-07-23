#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    long long int n, x, y, xmin, xmax, ymin, ymax, s;
    cin >> n >> x >> y;
    xmin = x, xmax = x, ymin = y, ymax = y;
    for (int i = 0; i < n - 1; i++)
    {
        cin >> x >> y;
        xmin = min(xmin, x);
        xmax = max(xmax, x);
        ymin = min(ymin, y);
        ymax = max(ymax, y);
    }
    s = max(abs(xmax - xmin), abs(ymax - ymin));
    cout << s * s << endl;
    return 0;
}
