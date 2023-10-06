#include <iostream>
#include <unordered_map>
#include <cstring>
#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main() {
  long long N, m;
  long long mod = 998244353;
  cin >> N >> m;
  N = N / 2;
  long long powers[N + 1];
  powers[0] = 1;
  for (int i = 1; i <= N; i++) {
    powers[i] = (powers[i - 1] * m) % mod;
  }
  //long long help[N + 1];
  long long arr[N + 1];
  arr[0] = 1;
  arr[1] = m;
  //help[0] = 0;
  //cout << pow(m, N) * pow(2, N - 1) - (m - 1) * pow(2, N - 1) << "\n";
  //return 0;
  for (int n = 2; n < N + 1; n++) {
    long long subsum = 0;
    subsum = (subsum + powers[n]) % mod;
    for (int i = 1; i < n - 1; i++) {
      //cout << i << "\n";
      subsum = (subsum + (arr[i] * powers[n - i]) % mod - powers[1]) % mod;
    }
    subsum = (subsum + (arr[n - 1] * (m - 1)) % mod) % mod;

    arr[n] = subsum;

    //subsum = (subsum + arr[n - 1] * (n - 1)) % mod;
    /*help[n] = 0;
    for (int i = 1; i <= n; i++) {
      help[n] = (help[n] + arr[i]) % mod;
    }*/
  }

  cout << arr[N] << "\n";

  /*for (int i = 0; i < N + 1; i++) {
    cout << arr[i] << " ";
  }
  cout << "\n";
  for (int i = 0; i < N + 1; i++) {
    cout << powers[i] << " ";
  }
  cout << "\n";*/
  return 0;
}
