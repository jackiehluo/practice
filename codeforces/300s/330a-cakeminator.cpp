#include <iostream>
using namespace std;

int main()
{
    int r, c, row[10] = {0}, col[10] = {0};
    cin >> r >> c;
    string l;

    for (int i = 0; i < r; i++)
    {
        cin >> l;
        for (int j = 0; j < c; j++)
        {
            if (l[j] == 'S')
            {
                row[i] = 1;
                col[j] = 1;
            }
        }
    }

    int cells(0);

    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (row[i] == 0 or col[j] == 0)
                cells++;
        }
    }

    cout << cells << endl;
    return 0;
}