#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int d[n - 1], a, b, y(0);

    for (int i = 0; i < n - 1; i++)
        cin >> d[i];

    cin >> a >> b;

    for (int i = a - 1; i < b - 1; i++)
        y += d[i];

    cout << y << endl;
    return 0;
}