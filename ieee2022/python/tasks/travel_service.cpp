

#include <iostream>
#include <map>
#include <cstring>
#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main() {
  long long t;
  cin >> t;
  for (long long q = 0; q < t; q++) {
    //cout << "1\n";
    long long s, c, r0, temp;
    cin >> s >> c >> r0;
    map<long long, long long> stations;
    long long orderedStations[s + 1];
    long long answers[s + 1];
    stations[0] = 0;
    answers[0] = c * r0;
    orderedStations[0] = 0;
    for (long long w = 1; w <= s; w++) {
      cin >> temp;
      cin >> stations[temp + orderedStations[w - 1]];
      orderedStations[w] = temp + orderedStations[w - 1];
      answers[w] = -1;
    }
    //cout << "2\n";

    long long prev;
    long long best;
    long long thisq;
    //answers[0] = orderedStations[0] * stations[orderedStations[0]] + c * r0;
    for (long long target = 1; target < s; target++) {
      //cout << "21\n";
      prev = 1;
      best = -1;
      //cout << orderedStations[target] - orderedStations[target - prev] << " ";
      while (target - prev >= 0 && orderedStations[target] - orderedStations[target - prev] <= c) {
        thisq = 500 + (orderedStations[target] - orderedStations[target - prev]) * stations[orderedStations[target]] + answers[target - prev];
        if (best == -1 || thisq < best) {
          best = thisq;
        }
        //cout << target - prev << " " << thisq << "\n";
        prev++;
      }
      //cout << "\n";
      answers[target] = best;
    }
    long long target = s;
    prev = 1;
    best = -1;
    while (target - prev >= 0 && orderedStations[target] - orderedStations[target - prev] <= c) {
      thisq = answers[target - prev];
      if (best == -1 || thisq < best) {
        best = thisq;
      }
      prev++;
    }
    answers[target] = best;
    //cout << "3\n";
    /*cout << c * r0 << "\n";
    for (long long i = 0; i <= s; i++) {
      cout << answers[i] << "\n";
    }*/
    cout << answers[s] << "\n";

    //cout << answers[s - 1] << "\n";

    //cout << stations[15] << stations[18] << stations[24] << "\n";
  }

  return 0;
}
