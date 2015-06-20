#include <iostream>
using namespace std;

int main()
{
    int n, d, t;
    cin >> n >> d;
    int min = 0, jokes = 0;

    for (int i = 0; i < n; i++)
    {
        cin >> t;
        min += t;
        if (i < n - 1)
        {
            jokes += 2;
            min += 10;
        }
        else
        {
            jokes += (d - min) / 5;
        }
    }

    if (min > d)
        cout << -1 << endl;
    else
        cout << jokes << endl;
    return 0;
}
