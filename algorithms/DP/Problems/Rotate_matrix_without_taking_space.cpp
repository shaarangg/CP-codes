#include <bits/stdc++.h>
using namespace std;
void rotate(vector<vector<int>> &matrix)
{
    int R = matrix.size();
    int C = matrix[0].size();
    for (int i = 0; i < R; i++)
    {
        for (int j = i; j < C; j++)
        {
            swap(matrix[i][j], matrix[j][i]);
        }
    }
    for (int i = 0; i < C / 2; i++)
    {
        for (int j = 0; j < R; j++)
        {
            swap(matrix[j][i], matrix[j][C - i - 1]);
        }
    }
}
int main()
{
    int r, c;
    cin >> r >> c;
    vector<vector<int>> matrix(r, vector<int>(c));
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            cin >> matrix[i][j];
        }
    }
    rotate(matrix);
    for (auto i : matrix)
    {
        for (auto j : i)
        {
            cout << j << " ";
        }
        cout << endl;
    }
    return 0;
}