#include <iostream>
#include <string>
using namespace std;

int main()
{
    string a, b;
    cin >> a >> b;
    string c = a;
    int n(a.length());
    for (int i = n - 1; i >= 0; i--)
    {
        while (c[i] < 'z')
        {
            c[i]++;
            if (c < b)
            {
                cout << c << endl;
                return 0;
            }
        }
        if (c[i] == 'z') c[i] = 'a';
    }
    cout << "No such string" << endl;
    return 0;
}
