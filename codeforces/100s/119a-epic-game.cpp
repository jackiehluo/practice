#include <iostream>
using namespace std;

int gcd(int a, int b)
{
    int gcd;
    for(int i = 1; i <= a && i <= b; i++)
        if(a % i == 0 && b % i == 0) gcd = i;
    return gcd;
}

int main()
{
    int a, b, n;
    cin >> a >> b >> n;

    while(true)
    {
        n -= gcd(a, n);
        if(n == 0)
        {
            cout << "0" << endl;
            break;
        }
        n -= gcd(b, n);
        if(n == 0)
        {
            cout << "1" << endl;
            break;
        }
    }
    return 0;
}
