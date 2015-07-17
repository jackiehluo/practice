#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    if (n == 1 or n==2) cout << -1 << endl;
    else for (int i = n; i > 0; i--) cout << i << " ";
    return 0;
}