#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, q, a, t;
    cin >> n >> q;
    unordered_map<int, int> d;
    for (int i = 0; i < n; i++)
    {
        cin >> a;
        if (d.find(a) == d.end())
        {
            d[a] = i + 1;
        }
    }
    for (int i = 0; i < q; i++)
    {
        cin >> t;
        cout << d[t] << endl;
        for (auto &j : d)
        {
            if (j.second < d[t])
            {
                j.second++;
            }
            // cout << j.first << " " << j.second << endl;
        }
        d[t] = 1;
    }
    return 0;
}