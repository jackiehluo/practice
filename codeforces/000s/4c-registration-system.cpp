#include <iostream>
#include <map>
using namespace std;

int main()
{
    int n;
    cin >> n;
    string s;
    map<string, int> names;

    for (int i = 0; i < n; i++)
    {
        cin >> s;
        if (names.find(s) == names.end())
        {
            names[s] = 1;
            cout << "OK" << endl;
        }
        else
        {
            cout << s << names[s] << endl;
            names[s]++;
        }
    }

    return 0;
}
