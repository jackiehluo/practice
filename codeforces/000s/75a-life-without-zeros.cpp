#include <iostream>
using namespace std;

int convert(int n)
{
    int v(0), t(1);
    while (n)
    {
        int d = n % 10;
        n /= 10;
        if (d) v += d * t, t *= 10;
    }
    return v;
}

int main()
{
    int a, b, c;
    cin >> a >> b;
    c = a + b;
    a = convert(a), b = convert(b), c = convert(c);
    cout << (a + b == c ? "YES" : "NO") << endl;
    return 0;
}
