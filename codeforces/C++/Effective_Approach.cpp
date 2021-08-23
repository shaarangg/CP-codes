#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long n, m, b, index, v = 0, p = 0;
    cin >> n;
    unordered_map<int, int> d;
    int elem;
    for (int i = 0; i < n; i++)
    {
        cin >> elem;
        d[elem] = i + 1;
    }
    cin >> m;
    while (m--)
    {
        cin >> b;
        index = d[b];
        v += index;
        p += n - index + 1;
    }
    cout << v << " " << p << endl;
    return 0;
}