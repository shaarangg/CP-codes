#include <bits/stdc++.h>
using namespace std;
void solve()
{
    int l, r;
    cin >> l >> r;
    int ans = r / 2 + 1;
    if (l <= ans)
    {
        cout << r % ans << endl;
    }
    else
    {
        cout << r - l << endl;
    }
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