#include <iostream>
#include <map>
using namespace std;

int main()
{
    int n, v;
    cin >> n;
    map<int, int> counts;
    char c;

    for (int i = 0 ; i < n ; i++)
    {
        cin >> c;
        v = c - '0';
        if (v == 2)
            counts[2]++;
        else if (v == 3)
            counts[3]++;
        else if (v == 4)
            counts[2] += 2, counts[3]++;
        else if (v == 5)
            counts[5]++;
        else if (v == 6)
            counts[3]++, counts[5]++;
        else if (v == 7)
            counts[7]++;
        else if (v == 8)
            counts[2] += 3, counts[7]++;
        else if (v == 9)
            counts[2] += 1, counts[3] += 2, counts[7]++;
    }

    for (int i = 9; i >= 2; i--)
    {
        while (counts[i])
        {
            cout << i;
            counts[i]--;
        }
    }
    return 0;
}
