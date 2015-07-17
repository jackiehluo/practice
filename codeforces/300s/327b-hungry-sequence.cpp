#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    for (int i = 10000000 - n; i < 10000000; i++) cout << i << " ";
    return 0;
}
