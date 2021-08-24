#include <bits/stdc++.h>
using namespace std;
void solve()
{
    int n, d;
    cin >> n >> d;
    if (d <= n)
    {
        cout << "YES" << endl;
        return;
    }
    else
    {
        int root1, root2;
        root1 = floor(sqrtl(d));
        root2 = ceil(sqrtl(d));
        int ans = min(root1 - 1 + ceil((float)d / root1), root2 - 1 + ceil((float)d / root2));
        if (n < ans)
        {
            cout << "NO" << endl;
        }
        else
        {
            cout << "YES" << endl;
        }
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