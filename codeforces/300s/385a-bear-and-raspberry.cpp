#include <iostream>
using namespace std;

int main()
{
    int n, c;
    cin >> n >> c;
    int d[n], t(0);

    for (int i = 0; i < n; i++)
      cin >> d[i];

    for (int i = 0; i < n - 1; i++)
        t = max(t, d[i] - d[i + 1] - c);

    cout << t << endl;
    return 0;
}
