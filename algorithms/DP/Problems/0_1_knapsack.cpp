#include <bits/stdc++.h>
using namespace std;
int table[100][100];
int knapsack(int wt[], int val[], int w, int n)
{
    if (w == 0 || n == 0)
    {
        return 0;
    }
    if (table[n][w] != -1)
    {
        return table[n][w];
    }
    if (wt[n - 1] <= w)
    {
        table[n][w] = max(val[n - 1] + knapsack(wt, val, w - wt[n - 1], n - 1), knapsack(wt, val, w, n - 1));
        return table[n][w];
    }
    if (wt[n - 1] > w)
    {
        table[n][w] = knapsack(wt, val, w, n - 1);
        return table[n][w];
    }
}
int main()
{
    memset(table, -1, sizeof(table));
    int n, w;
    cin >> n >> w;
    int val[n];
    int wt[n];
    for (int i = 0; i < n; i++)
    {
        cin >> val[i] >> wt[i];
    }
    int sum = knapsack(wt, val, w, n);
    cout << sum << endl;
    return 0;
}