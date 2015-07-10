#include <iostream>
using namespace std;

int main()
{
    int n, m, k, a, b, r(0);
    cin >> n >> m >> k;
    bool f[1005][1005];

    for (int i = 1; i <= k; i++)
    {
        cin >> a >> b;
        f[a][b] = true;
        for (int x = -1; x < 2; x += 2)
            for (int y = -1; y < 2; y += 2)
                if (f[a + x][b + y] and f[a + x][b] and f[a][b + y] and r == 0)
                    r = i;
    }
    
    cout << r << endl;
    return 0;
}