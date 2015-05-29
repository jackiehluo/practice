#include <iostream>
using namespace std;

int main()
{
    int k, n, w;
    cin >> k >> n >> w;
    int cost = w * (w + 1) / 2;
    int loan = cost * k - n;

    if (loan > 0)
        cout << loan << endl;
    else
        cout << 0 << endl;
    return 0;
}