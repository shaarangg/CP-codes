#include <bits/stdc++.h>
using namespace std;
int countsum(int N)
{
    int count = 0;
    for (int L = 1; (L * (L + 1)) / 2 < N; L++)
    {
        if ((N - ((L * (L + 1)) / 2)) % (L + 1) == 0)
        {
            count++;
        }
    }
    return count;
}
int main()
{
    int N;
    cin >> N;
    cout << countsum(N) << endl;
}