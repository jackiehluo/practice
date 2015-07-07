#include <iostream>
using namespace std;

int main()
{
    int n, k, f, t, j, m(-1000000000);
    cin >> n >> k;

    for (int i = 0; i < n; i++)
    {
        cin >> f >> t;
        if (t > k)
        {
            j = f - (t - k);
            if (j > m)
                m = j;
        }
        else
            if (f > m)
                m = f;
    }

    cout << m << endl;
    return 0;
}