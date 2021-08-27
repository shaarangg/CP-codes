#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, m, sx, sy, i, f = 0;
    cin >> n >> m >> sx >> sy;
    cout << sx << " " << sy << endl;
    for (int i = 1; i < m + 1; i++)
    {
        if (i == sy)
            continue;
        cout << sx << " " << i << endl;
    }
    i = 1;
    while (i < n + 1)
    {
        if (i == sx)
        {
            i++;
            continue;
        }
        if (f == 0)
        {
            for (int j = m; j > 0; j--)
            {
                cout << i << " " << j << endl;
            }
            f = 1;
        }
        else
        {
            for (int j = 1; j < m + 1; j++)
            {
                cout << i << " " << j << endl;
            }
            f = 0;
        }
        i++;
    }
    return 0;
}