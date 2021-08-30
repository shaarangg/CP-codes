#include <bits/stdc++.h>
using namespace std;
void solve()
{
    int c, d;
    cin >> c >> d;
    if (c == d)
    {
        if (c == 0)
        {
            cout << 0 << endl;
            return;
        }
        cout << 1 << endl;
    }
    else if ((c + d) % 2 == 0)
    {
        cout << 2 << endl;
    }
    else
    {
        cout << -1 << endl;
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