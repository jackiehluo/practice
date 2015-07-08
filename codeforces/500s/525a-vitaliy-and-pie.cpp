#include <iostream>
#include <ctype.h>
#include <map>
using namespace std;

int main()
{
    int n, count(0);
    cin >> n;
    char c;
    map<char, int> keys;

    for (int i = 0; i < n * 2 - 2; i++)
    {
        cin >> c;
        if (islower(c))
            keys[c]++;
        else
            if (keys[tolower(c)] > 0)
                keys[tolower(c)]--;
            else
                count++;
    }

    cout << count << endl;
    return 0;
}
