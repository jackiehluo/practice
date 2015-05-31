#include <iostream>
using namespace std;

int main()
{
    int n, t;
    cin >> n;
    int evens = 0, odds = 0, ind = 0;
    int even, odd;

    for (int i = 0; i < n; i++)
    {
        ind++;
        cin >> t;
        if (t % 2 == 0)
        {
            evens++;
            even = ind;
        }
        else
        {
            odds++;
            odd = ind;
        }
        if ((evens == 1 && odds > evens) || (odds == 1 && evens > odds))
            break;
    }

    if (evens == 1 and odds > evens)
        cout << even << endl;
    else
        cout << odd << endl;
    return 0;
}