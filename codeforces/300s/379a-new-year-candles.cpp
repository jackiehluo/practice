#include <iostream>
using namespace std;

int main()
{
    int a, b, d, m;
    cin >> a >> b;
    int h = a;

    while(a >= b)
    {
        d = a / b;
        h += d;
        m = a % b;
        a = d + m;
    }
    
    cout << h << endl;
    return 0;
}
