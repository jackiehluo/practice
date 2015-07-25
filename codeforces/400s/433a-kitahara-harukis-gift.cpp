#include <iostream>
using namespace std;

int main()
{
    int n, t, o(0), e(0);
    cin >> n;
    for (;cin >> t;) (t == 100 ? o : e)++;
    cout << (n < 2 or o % 2 or !o and e % 2 ? "NO" : "YES") << endl;
    return 0;
}
