#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main()
{
    int y, z;
    cin >> y;

    while(true)
    {
        y++;
        stringstream ss;
        ss << y;
        string n;
        ss >> n;
        sort(n.begin(), n.end());
        bool d = true;

        for(int i = 0; i < n.length() - 1; i++)
        {
            if(n[i] == n[i + 1])
            {
                d = false;
            }
        }

        if(d == true)
        {
            cout << y << endl;
            break;
        }
    }

    return 0;
}
