#include <bits/stdc++.h>
using namespace std;
void check(int *ptr)
{
    // Here ptr is a local varialble of function check.
    // Now if we re-assign ptr to some other address then, it won't affect the ptr in the main function because because ptr is just a local copy of ptr of the main which initially points to the same address as of the ptr in the main.
    int b = 10;
    ptr = &b;
    cout << *ptr << " ";
}
int main()
{
    int a = 5;
    int *ptr = &a;
    check(ptr);
    cout << *ptr << " ";
    return 0;
}