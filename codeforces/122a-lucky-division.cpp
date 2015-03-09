#include <iostream>
using namespace std;

bool lucky(int a)
{
    while(a != 0)
    {
        if(a % 10 != 4 && a % 10 != 7)
            return false;
        a /= 10;
    }
    return true;
}

int main()
{
    int n;
    cin >> n;
    bool d = false;

    for(int i = 2; i < n + 1; i++)
    {
        if(n % i == 0 && (lucky(n / i) || lucky(n)))
        {
            d = true;
            break;
        }
    }

    if(d == true)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;

    return 0;
}
