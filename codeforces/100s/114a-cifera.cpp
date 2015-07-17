#include <iostream>
using namespace std;

int main()
{
    long long int k, l, c(0);
    cin >> k >> l;
    while (l > k and l % k == 0) l /= k, c++;
    if (l == k) cout << "YES" << endl << c << endl;
    else cout << "NO" << endl;
    return 0;
}