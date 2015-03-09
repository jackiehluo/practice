#include <iostream>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    int d = 0;

    while(n > 0)
    {
        d++;
        n--;
        if(d % m == 0)
        {
            n++;
        }
    }
    cout << d << endl;
    return 0;
}
