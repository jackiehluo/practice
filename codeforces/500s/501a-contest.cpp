#include <iostream>
using namespace std;

int main()
{
    int a, b, c, d, m, v;
    cin >> a >> b >> c >> d;
    m = max(3 * a / 10, a - a / 250 * c);
    v = max(3 * b / 10, b - b / 250 * d);
    if (m > v)
        cout << "Misha" << endl;
    else if (v > m)
        cout << "Vasya" << endl;
    else
        cout << "Tie" << endl;
    return 0;
}