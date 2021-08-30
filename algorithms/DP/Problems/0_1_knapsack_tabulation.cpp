#include <bits/stdc++.h>
using namespace std;
int main()
{
    int w, n;
    cin >> w >> n;
    int val[n];
    int wt[n];
    for (int i = 0; i < n; i++)
    {
        cin >> wt[i] >> val[i];
    }
    int table[n + 1][w + 1];
    memset(table, 0, sizeof(table));
    for (int i = 1; i < n + 1; i++)
    {
        for (int j = 1; j < w + 1; j++)
        {
            if (wt[i - 1] <= j)
            {
                table[i][j] = max(val[i - 1] + table[i - 1][j - wt[i - 1]], table[i - 1][j]);
            }
            else
            {
                table[i][j] = table[i - 1][j];
            }
        }
    }
    cout << table[n][w] << endl;
    return 0;
}