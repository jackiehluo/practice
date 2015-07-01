#include <iostream>
using namespace std;

int main()
{
    int n, t;
    cin >> n;
    double total = 0;

    for (int i = 0; i < n; i++)
    {
        cin >> t;
        total += t;
    }

    cout << total / n << endl;
    return 0;
}
