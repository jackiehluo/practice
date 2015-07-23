#include <iostream>
using namespace std;

int main()
{
    const int N = 1000000;
    int counts[N];
    long long points[N];
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int tmp;
        cin >> tmp;
        counts[tmp]++;
    }

    points[0] = 0;

    for (int i = 1; i < N; i++)
    {
        points[i] = (long long)i * counts[i];
        if (i - 2 >= 0)
            points[i] += points[i - 2];
        if (points[i - 1] > points[i])
            points[i] = points[i - 1];
    }

    cout << points[N - 1] << endl;
    return 0;
}
