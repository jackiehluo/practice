#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int a1, b1, a2, b2, a3, b3;
    cin >> a1 >> b1 >> a2 >> b2 >> a3 >> b3;
    a1++, b1++;
    if ((max(a2, a3) < a1 and b2 + b3 < b1) or
        (max(b2, b3) < a1 and a2 + a3 < b1) or
        (max(a2, b3) < a1 and b2 + a3 < b1) or
        (max(b2, a3) < a1 and a2 + b3 < b1) or
        (max(a2, a3) < b1 and b2 + b3 < a1) or
        (max(b2, b3) < b1 and a2 + a3 < a1) or
        (max(a2, b3) < b1 and b2 + a3 < a1) or
        (max(b2, a3) < b1 and a2 + b3 < a1)) cout << "YES" << endl;
    else cout << "NO" << endl;
    return 0;
}
