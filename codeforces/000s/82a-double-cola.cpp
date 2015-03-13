#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int r = 1;
    string p[] = {"Sheldon", "Leonard", "Penny", "Rajesh", "Howard"};
    
    while(r * 5 < n)
    {
        n -= r * 5;
        r *= 2;
    }

    cout << p[(n - 1) / r] << endl;

    return 0;
}
