#include <iostream>
using namespace std;

int main()
{
	int n, a, b;
	int t = 0;
	int m = 0;
	cin >> n;

	for(int i = 0; i < n; i++)
	{
		cin >> a >> b;
		t -= a;
		t += b;
		if(t > m)
			m = t;
	}

	cout << m << endl;
	return 0;
}
