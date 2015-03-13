#include <iostream>
#include <math.h>
using namespace std;

bool comp(int x)
{
    for(int j = 2; j < x; j++)
    {
        if(x % j == 0)
        {
            return true;
        }
    }
    return false;
}

int main()
{
    int n, a, b;
    cin >> n;
    a = floor(n / 2.0);
    b = ceil(n / 2.0);
    
    for(int i = 0; i < (n / 2); i++)
    {
        if(comp(a) && comp(b))
            break;
        else
        {
            a--;
            b++;
        }
    }
    cout << a << " " << b << endl;
    return 0;
}
