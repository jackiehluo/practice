#include <iostream>
using namespace std;

int main()
{
    int n, t(0), w(0);
    cin >> n;
    int b[n];
    for (int i = 0; cin >> b[i]; i++) t += b[i];
    for (int i = 0; i < n; i++)
        if ((t - b[i]) % 2 == 0) w++;
    cout << w << endl;
    return 0;
}
