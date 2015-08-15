#include <iostream>
using namespace std;

int main()
{
    int n, l[100005];
    cin >> n;
    for (int i = 0; cin >> l[i]; i++);
    cout << l[1] - l[0] << " " << l[n - 1] - l[0] << endl;
    for (int i = 1; i < n - 1; i++)
    {
        int low = min(l[i] - l[i - 1], l[i + 1] - l[i]);
        int high = max(l[n - 1] - l[i], l[i] - l[0]);
        cout << low << " " << high << endl;
    }
    cout << l[n - 1] - l[n - 2] << " " << l[n - 1] - l[0] << endl;
    return 0;
}