#include <iostream>
using namespace std;

int main()
{
	int n, p;
	cin >> n;
	int a = 0;

	for(int i = 0; i < n; i++)
	{
		int f = 0;
		for(int j = 0; j < 3; j++)
		{
			cin >> p;
			f += p;
		}
		if(f >= 2)
			a++;
	}

	cout << a << endl;
	return 0;
}
