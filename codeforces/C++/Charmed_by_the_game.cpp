#include <bits/stdc++.h>
using namespace std;
void solve()
{
    int a, b, d;
    cin >> a >> b;
    d = abs(a - b) / 2;
    vector<int> ans;
    if ((a + b) % 2 == 0)
    {
        for (int i = d; i <= a + b - d; i += 2)
        {
            ans.push_back(i);
        }
    }
    else
    {
        for (int i = d; i <= a + b - d; i++)
        {
            ans.push_back(i);
        }
    }
    cout << ans.size() << endl;
    for (auto i : ans)
    {
        cout << i << " ";
    }
    cout << endl;
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