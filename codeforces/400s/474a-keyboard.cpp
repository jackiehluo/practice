#include <algorithm>
#include <iostream>
using namespace std;

int index(const char *array, int size, char *c)
{
    const char* end = array + size;
    const char* n = find(array, end, c);
    return (end == n)? -1 : (n-array);
}

int main()
{
    const char *k[30] = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
                    "a", "s", "d", "f", "g", "h", "j", "k", "l", ";",
                    "z", "x", "c", "v", "b", "n", "m", ",", ".", "/"};
    char *d;
    string m;
    int p;
    cin >> d;
    cin >> m;

    if(d == "R")
    {
        for(int i = 0; i < m.length(); i++)
        {
            p = index(k, 30, k[i]) - 1;
            cout << k[p];
        }
    }
    else
    {
        for(int j = 0; j < m.length(); j++)
        {
            p = index(k, 30, k[j]) + 1;
            cout << k[p];
        }
    }
    return 0;
}