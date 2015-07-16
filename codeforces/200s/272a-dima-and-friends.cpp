#include <iostream>
using namespace std;

int main()
{
    int n, t(0), c(0);
    cin >> n;
    for (int f; cin >> f;) t += f;
    for (int i = 1; i <= 5; i++)
        if ((t + i) % (n + 1) != 1) c++;
    cout << c << endl;
    return 0;
}
