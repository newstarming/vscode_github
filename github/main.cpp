#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
using namespace std;

const int MAXN = 1000005;
const int BASE = 131;
const int MOD = 1e9 + 7;

int n, m;
string X, Y;
int h[MAXN], p[MAXN];

int myhash(string s)
{
    int res = 0;
    for (int i = 0; i < s.length(); i++)
    {
        res = (1LL * res * BASE % MOD + s[i]) % MOD;
    }
    return res;
}

int get_hash(int l, int r)
{
    return (h[r] - 1LL * h[l - 1] * p[r - l + 1] % MOD + MOD) % MOD;
}

int main()
{
    cin >> X >> Y;
    n = X.length();
    m = Y.length();
    p[0] = 1;
    for (int i = 1; i <= n; i++)
    {
        h[i] = (1LL * h[i - 1] * BASE % MOD + X[i - 1]) % MOD;
        p[i] = 1LL * p[i - 1] * BASE % MOD;
    }
    int Y_hash = myhash(Y);
    srand(time(NULL));
    int t = rand() % (n - m + 1) + 1;
    int X_hash = get_hash(t, t + m - 1);
    if (X_hash == Y_hash)
    {
        cout << t - 1 << endl;
        return 0;
    }
    for (int i = 1; i <= 10; i++)
    {
        t = rand() % (n - m + 1) + 1;
        X_hash = get_hash(t, t + m - 1);
        if (X_hash == Y_hash)
        {
            cout << t - 1 << endl;
            return 0;
        }
    }
    cout << -1 << endl;
    return 0;
}
