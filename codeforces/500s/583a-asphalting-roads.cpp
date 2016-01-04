#include <iostream>
using namespace std;

int main()
{
    int n, h, v;
    cin >> n;
    bool hor[51] = {false}, ver[51] = {false};

    for (int i = 1; i <= n * n; i++)
    {
        cin >> h >> v;
        if (!hor[h] and !ver[v])
        {
            hor[h] = ver[v] = true;
            cout << i << " ";
        }
    }

    return 0;
}