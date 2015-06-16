#include <iostream>
using namespace std;

int main()
{
    int a1, a2, a3, a4;
    string s;
    cin >> a1 >> a2 >> a3 >> a4 >> s;
    int calories = 0;
    
    for (auto& digit : s)
    {
        if (digit == '1')
            calories += a1;
        else if (digit == '2')
            calories += a2;
        else if (digit == '3')
            calories += a3;
        else
            calories += a4;
    }

    cout << calories << endl;
    return 0;
}
