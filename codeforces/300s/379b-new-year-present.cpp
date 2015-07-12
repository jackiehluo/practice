#include <iostream>
using namespace std;

int main()
{
    int n, a[300];
    cin >> n;

    for (int i = 1; i <= n; i++)
        cin >> a[i];

    for (int i = 1; i < n; i++)
    {
        for (int j = 1; j <= a[i]; j++)
            cout << "PRL";
        cout << "R";
    }

    for (int i = 1; i <= a[n]; i++)
        cout << "PLR";

    return 0;
}