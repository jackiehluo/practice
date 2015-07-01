#include <iostream>
#include <math.h>
#include <stdlib.h> 
using namespace std;

int main()
{
    int n, x, t;
    cin >> n >> x;
    double sum = 0;

    for (int i = 0; i < n; i++)
    {
        cin >> t;
        sum += t;
    }
    
    if (sum > 0)
        cout << ceil(sum / x) << endl;
    else
        cout << abs(int(floor(sum / x))) << endl;
    return 0;
}
