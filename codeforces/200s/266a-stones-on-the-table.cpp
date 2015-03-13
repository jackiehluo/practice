#include <iostream>
using namespace std;

int main()
{
    int n;
    string s;
    int c = 0;
    cin >> n;
    cin >> s;

    if(n > 1)
    {
        for(int i = 0; i < n - 1; i++)
        {
            if(s[i] == s[i + 1])
                c++;
        }
    }

    cout << c << endl;
    return 0;
}
