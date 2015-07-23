#include <iostream>
using namespace std;

int main()
{
    int n1, n2, k1, k2;
    cin >> n1 >> n2 >> k1 >> k2;
    int t = 1;

    while (n1 > 0 && n2 > 0)
    {
        if (t % 2 == 1) n1 -= 1;
        else n2 -= 1;
        t++;
    }

    if (n1 <= 0) cout << "Second" << endl;
    else cout << "First" << endl;
    return 0;
}
