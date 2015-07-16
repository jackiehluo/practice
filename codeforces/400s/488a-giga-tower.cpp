#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main()
{
    int n, c(0);
    cin >> n;

    while (true)
    {
        n++, c++;
        stringstream ss;
        string s;
        ss << n;
        ss >> s;
        if (s.find('8') != -1)
        {
            cout << c << endl;
            return 0;
        }
    }
}