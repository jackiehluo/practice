#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, t;
    cin >> n;
    vector<int> scores;

    for (int i = 0; i < n; i++)
    {
        cin >> t;
        scores.push_back(t);
    }

    for (int i = 0; i < n; i++)
    {
        int s = 1;
        for (int j = 0; j < n; j++)
        {
            if (scores[i] < scores[j])
                s++;
        }
        cout << s << " ";
    }

    return 0;
}