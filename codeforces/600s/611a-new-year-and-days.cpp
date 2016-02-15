#include <iostream>
using namespace std;

int main()
{
    int x;
    char c;
    cin >> x >> c >> c >> c;
    cout << (c - 'w' ? 12 - (x > 29) - 4 * (x > 30) : 52 + (x == 5 or x == 6));
    return 0;
}