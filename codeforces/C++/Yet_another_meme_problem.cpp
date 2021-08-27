#include <bits/stdc++.h>
using namespace std;
void solve()
{
    long long int A, B;
    cin >> A >> B;
    B++;
    int l = 0;
    while (B > 0)
    {
        l++;
        B /= 10;
    }
    cout << A * (l - 1) << endl;
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}