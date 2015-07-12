#include <cstdio>
using namespace std;

int main ()
{
    int a, b, c, d;
    scanf("%d:%d\n%d:%d", &a, &c, &b, &d);
    printf("%02d:%02d",(a - b - (d > c) + 24) % 24, (c - d + 60) % 60);
    return 0;
}