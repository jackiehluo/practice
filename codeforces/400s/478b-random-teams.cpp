#include <iostream>
using namespace std;

long long int pairs(long long int n)
{
    return n * (n - 1) / 2;
}

int main()
{
    long long int n, m;
    cin >> n >> m;
    long long int a(n / m), b(n % m);
    long long int min = pairs(a) * (m - b) + pairs(a + 1) * b;
    long long int max = pairs(n - m + 1);
    cout << min << " " << max << endl;
    return 0;
}
