#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, t;
    cin >> n;
    vector<int> numbers;

    for (int i = 0; i < n; i++)
    {
        cin >> t;
        if (t == 0)
            numbers.push_back(1);
        else
            numbers.push_back(0);
    }

    bool p = false;
    int cur = 0, max = 0;
    int v;

    for (int i = 0; i < n; i++)
    {
        v = cur + numbers[i];
        if (v > 0)
        {
            cur = v;
            p = true;
        }
        else
            cur = 0;
        if (cur > max)
            max = cur;
    }

    if (p == false)
        max = max_element(begin(numbers), end(numbers));

    cout << max << endl;
    return 0;
}
