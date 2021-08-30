#include <bits/stdc++.h>
using namespace std;
string s1, s2;
unordered_map<string, int> d;
int solve(int i, int j)
{
    string key = to_string(i) + to_string(j);
    if (d.find(key) != d.end())
    {
        return d[key];
    }
    else if (s1[i] == '\0' || s2[j] == '\0')
    {
        d[key] = 0;
        return 0;
    }
    else if (s1[i] == s2[j])
    {
        d[key] = 1 + solve(i + 1, j + 1);
        return d[key];
    }
    else
    {
        d[key] = max(solve(i + 1, j), solve(i, j + 1));
        return d[key];
    }
}
int main()
{
    cin >> s1 >> s2;
    cout << solve(0, 0) << endl;
}