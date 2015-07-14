#include <iostream>
using namespace std;

int main()
{
    int n, v[] = {2, 7, 2, 3, 3, 4, 2, 5, 1, 2};
    cin >> n;
    cout << v[n / 10] * v[n % 10];
    return 0;
}