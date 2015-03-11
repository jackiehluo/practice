#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int c = 0, h = 0;

    while(n > c + h)
    {
        h++;
        c += h;
        n -= c;
    }
    
    cout << h << endl;
    return 0;
}
