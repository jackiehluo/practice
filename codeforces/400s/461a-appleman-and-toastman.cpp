#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    long long int n, t;
    long long int sum = 0;
    vector<long long int> numbers;
    cin >> n;

    for(int i = 0; i < n; i++)
    {
        cin >> t;
        sum += t;
        numbers.push_back(t);
    }

    sort(numbers.begin(), numbers.end());
    long long int score = sum;

    for(int j = 0; j < n - 1; j++)
    {
        score += sum;
        sum -= numbers[j];
    }

    cout << score << endl;
    return 0;
}