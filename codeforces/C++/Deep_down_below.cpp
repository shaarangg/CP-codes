#include <bits/stdc++.h>
using namespace std;
void solve()
{
    int n, k, elem, b, maxx = 0;
    cin >> n;
    vector<pair<int, int>> a;
    pair<int, int> temp;
    while (n--)
    {
        cin >> k;
        maxx = 0;
        for (int i = 0; i < k; i++)
        {
            cin >> elem;
            maxx = max(maxx, elem - i);
        }
        temp = make_pair(maxx + 1, k);
        a.push_back(temp);
    }
    sort(a.begin(), a.end());
    // for (auto i : a)
    // {
    //     cout << i.first << " " << i.second << endl;
    // }
    k = 0;
    maxx = 0;
    for (auto i : a)
    {
        b = i.first;
        b -= k;
        maxx = max(maxx, b);
        k += i.second;
    }
    cout << maxx << endl;
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