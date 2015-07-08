#include <iostream>
using namespace std;

int main(){  
    int n, t, f(0), z(0);
    cin >> n;

    for (int i = 0; i < n; i++)
    {  
        cin >> t;
        if (t == 0)
            z++;  
        else if (t == 5)
            f++;  
    }  

    if (z == 0)
        cout << -1 << endl;
    else if (f < 9)
        cout << 0 << endl;
    else
    {
        f -= f % 9;
        for (int i = 0; i < f; i++)
            cout << 5;
        for (int i = 0; i < z; i++) 
            cout << 0;
    }

    return 0;
}
