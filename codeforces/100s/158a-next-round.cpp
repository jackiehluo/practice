#include <iostream>
using namespace std;

int main(){
    int n, k, max;
    cin>>n>>k;
    int p[50];
    for(int i = 0; i < n; i++)
    {
        cin>>p[i];
        if(i + 1 == k) max = p[i];
    }
    int count = 0;
    for(int i = 0; i < n; i++)
        if(p[i] >= max && p[i] > 0) count++;
    cout<<count;
    return 0;
}
