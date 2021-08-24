#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, m;
    cin >> n >> m;
    vector<string> a;
    string ans = "", elem, first, second, freverse, sreverse;
    int f = 0, count = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> elem;
        a.push_back(elem);
    }
    for (auto i = a.begin(); i != a.end(); i++)
    {
        first = *i;
        freverse = string(first.rbegin(), first.rend());
        if (first.compare(freverse) == 0 && f == 0)
        {
            ans.insert(count, first);
            f = 1;
            continue;
        }
        for (auto j = next(i); j != a.end(); j++)
        {
            second = *j;
            sreverse = string(j->rbegin(), j->rend());
            if (first.compare(sreverse) == 0)
            {
                count += first.length();
                ans.insert(0, first);
                ans = ans + second;
            }
        }
    }
    cout << ans.length() << endl;
    cout << ans << endl;
    return 0;
}