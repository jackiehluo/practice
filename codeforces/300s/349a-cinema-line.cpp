#include <iostream>
using namespace std;

int main()
{
    int n, t;
    cin >> n;
    int change = 0;
    string answer = "YES";

    for (int i = 0; i < n; i++)
    {
        cin >> t;
        if (t == 25)
            change += 25;
        else if (change - (t - 25) < 0)
        {
            answer = "NO";
            break;
        }
    }

    cout << answer << endl;
    return 0;
}
