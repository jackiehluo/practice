#include <iostream>
using namespace std;

int main()
{
    int n, x0, y0, s(0), dx1, dy1, dx2, dy2, a[1000][2];
    cin >> n >> x0 >> y0;
    bool k[1000];

    for (int i = 0; i < n; i++) cin >> a[i][0] >> a[i][1];

    for (int i = 0; i < n; i++)
    {
        if (k[i]) continue;
        s++;
        dx1 = a[i][0] - x0, dy1 = a[i][1] - y0;
        for (int j = 0; j < n; j++)
        {
            dx2 = a[j][0] - x0, dy2 = a[j][1] - y0;
            if (dx2 * dy1 == dx1 * dy2) k[j] = 1;
        }
    }

    cout << s << endl;
    return 0;
}
