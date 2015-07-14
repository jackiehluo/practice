#include <iostream>
using namespace std;

int main()
{
    int p, n, t;
    cin >> p >> n;
    bool b[p] = {false};

    for (int i = 0; i < n; i++)
    {
        cin >> t;
        if (b[t % p])
        {
            cout << i + 1 << endl;
            return 0;
        }
        else
            b[t % p] = true;
    }

    cout << -1 << endl;
    return 0;
}