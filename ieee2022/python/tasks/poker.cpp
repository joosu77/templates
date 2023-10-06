

#include <iostream>
#include <map>
#include <cstring>
#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main() {
  long long mod = 998244353;
  long long n, q;
  long long t, l, r, c;
  cin >> n >> q;
  long long arr[n];
  long long temps[51];
  arr[0] = 0;
  for (long long i = 0; i < n; i++) {
    cin >> arr[i];
  }
  for (long long i = 0; i < q; i++) {
    /*for (long long w = 0; w < n; w++) {
      cout << arr[w] << " ";
    }
    cout << "\n";*/
    cin >> t >> l >> r >> c;
    if (t == 0) {
      for (long long j = l; j <= r; j++) {
        arr[j] = c;
      }
    } else if (t == 1) {
      for (long long j = l; j <= r; j++) {
        arr[j] = arr[j] > c ? arr[j] : c;
      }
    } else {
      for (long long a = 0; a <= c; a++) {
        temps[a] = 0;
      }
      temps[0] = 1;
      for (long long a = l; a <= r; a++) {
        for (long long b = c; b > 0; b--) {
          temps[b] += (temps[b - 1] * arr[a]) % mod;
          temps[b] = temps[b] % mod;
        }

      }
      cout << temps[c] << "\n";
    }
  }
}
