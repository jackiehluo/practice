#include <iostream>
using namespace std;

int main()
{
    int n, m, t, sum(0);
    cin >> n;
    int worms[n];

    for (int i = 0; i < n; i++)
    {
        cin >> t;
        sum += t;
        worms[i] = sum;
    }

    cin >> m;

    for (int i = 0; i < m; i++)
    {
        cin >> t;
        for (int j = 0; j < n; j++)
        {
            if (t <= worms[j])
            {
                cout << j + 1 << endl;
                break;
            }
        }
    }

    return 0;
}