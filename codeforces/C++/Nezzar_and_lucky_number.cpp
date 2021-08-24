#include <bits/stdc++.h>
using namespace std;
void solve(vector<int> &a, unordered_map<int, int> &dict, int d)
{
    for (auto i : a)
    {
        if (i >= d * 10)
        {
            cout << "YES" << endl;
        }
        else if (dict.find(i % 10) != dict.end() && i >= dict[i % 10])
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int q, d;
        cin >> q >> d;
        unordered_map<int, int> dict;
        for (int i = 1; i <= 10; i++)
        {
            int temp = d * i;
            if (dict.find(temp % 10) == dict.end())
                dict[temp % 10] = temp;
        }
        // for (auto i : dict)
        // {
        //     cout << i.first << " " << i.second << endl;
        // }
        int elem;
        vector<int> a;
        for (int i = 0; i < q; i++)
        {
            cin >> elem;
            a.push_back(elem);
        }
        solve(a, dict, d);
    }
    return 0;
}