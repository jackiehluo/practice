#include <iostream>
using namespace std;

int main()
{
    int n, a, b, spots;
    cin >> n >> a >> b;
    spots = n - a;
    if (spots > b)
        spots -= n - a - b - 1;
    cout << spots << endl;
    return 0;
}
