#include <iostream>
using namespace std;

int main()
{
    int n, p;
    cin >> n;
    int f[n];

    for(int i = 0; i < n; i++)
    {
        cin >> p;
        f[p - 1] = i + 1;
    }

    for(int j = 0; j < n; j++)
    {
        cout << f[j] << " ";
    }

    return 0;
}
