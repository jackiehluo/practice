#include <iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;
	int m[n];
	int c = 1;
	
	for(int i = 0; i < n; i++)
	{
		cin >> m[i];
		if(i > 0 && m[i] != m[i - 1])
			c++;
	}

	cout << c << endl;
	return 0;
}
