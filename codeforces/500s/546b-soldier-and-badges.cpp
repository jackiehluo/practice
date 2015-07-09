#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, a, c(0);
    cin >> n;
    int b[n];

    for (int i = 0; i < n; i++)
        cin >> b[i];

    sort(b, b + n);

    for (int i = 1; i < n; i++)
        if (b[i] == b[i - 1])
            b[i]++, c++;
        else if (b[i] < b[i - 1])
        {
            a = b[i - 1] - b[i];
            b[i] += a, c += a;
            b[i]++, c++;
        }

    cout << c << endl;
    return 0;
}