#include <cstdio>
using namespace std;

int main()
{
    int n;
    scanf("%d", &n);
    putchar(n % 4 ? 48 : 52);
    return 0;
}
