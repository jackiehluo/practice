#include <iostream>
using namespace std;

int main()
{
    int n, m, a, b, ind, diff, total;
    cin >> n >> m >> a >> b;
    ind = a * m;

    if(ind > b)
    {
        diff = n % m;
        if(diff * a < b)
            total = (n / m) * b + diff * a;
        else
            total = (n / m + 1) * b;
    }
    else
        total = n * a;
    cout << total << endl;
    return 0;
}
