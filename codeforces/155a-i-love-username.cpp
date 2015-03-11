#include <iostream>
using namespace std;

int main()
{
    int n, p, b, w;
    cin >> n >> p;
    int a = 0;
    b = p;
    w = p;

    for(int i = 1; i < n; i++)
    {
        cin >> p;
        if(p > b)
        {
            a++;
            b = p;
        }
        else if(p < w)
        {
            a++;
            w = p;
        }
    }
    
    cout << a << endl;
    return 0;
}
