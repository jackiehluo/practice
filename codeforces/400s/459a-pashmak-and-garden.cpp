#include <iostream>
#include <stdlib.h>
using namespace std;

int main()
{
    int x1, y1, x2, y2, x3, y3, x4, y4;
    cin >> x1 >> y1 >> x2 >> y2;

    int x_diff = x1 - x2;
    int y_diff = y1 - y2;

    if (x_diff != 0 and y_diff != 0)
    {
        x3 = x1;
        y3 = y2;
        x4 = x2;
        y4 = y1;
    }
    else if (x_diff != 0)
    {
        x3 = x1;
        y3 = y1 + abs(x_diff);
        x4 = x2;
        y4 = y2 + abs(x_diff);
    }
    else
    {
        x3 = x1 + abs(y_diff);
        y3 = y1;
        x4 = x2 + abs(y_diff);
        y4 = y2;
    }

    if (x_diff != 0 and y_diff != 0 and abs(x_diff) != abs(y_diff))
        cout << -1 << endl;
    else
        cout << x3 << " " << y3 << " " << x4 << " " << y4 << endl;
    return 0;
}