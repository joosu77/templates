#include <iostream>
#include <unordered_map>
#include <cstring>
#include <bits/stdc++.h>
#include <vector>

using namespace std;

unordered_map<int, string> addToMap(unordered_map<int, string> map, int* numbers, int size) {
  string temps;
  int tempi;
  int a = 0;
  for (int i = 0; i < size; i++) {
    cin >> temps >> tempi;
    //cout << temps << tempi << "\n";
    if (map.count(tempi) == 0) {
      //cout << "a\n";
      map[tempi] = temps;
      numbers[a] = tempi;
      a++;
    } else {
      //cout << "b\n";
      if (temps > map[tempi]) {
        map[tempi] = temps;
      }
    }
  }
  return map;
}

int next(int arr[], int target, int end) {
  if(end == 0) return -1;
  if (target > arr[end - 1]) return end-1;

  int start = 0;

  int ans = -1;
  while (start <= end) {
    int mid = (start + end) / 2;
    if (arr[mid] == target) {
      return mid;
    }
    if (arr[mid] > target) {
      end = mid - 1;
    } else {
      ans = mid;
      start = mid + 1;
    }
  }
  return ans;
}

int main() {
    int q;
    unordered_map<int, string> aMap;
    unordered_map<int, string> bMap;
    unordered_map<int, string> cMap;
    unordered_map<int, string> dMap;
    unordered_map<int, string> eMap;
    int a, b, c, d, e;
    cin >> q;
    string temps;
    int tempi;

    cin >> a;
    int aInt[a];
    aMap = addToMap(aMap, aInt, a);
    a = aMap.size();
    sort(aInt, aInt + a);

    cin >> b;
    int bInt[b];
    bMap = addToMap(bMap, bInt, b);
    b = bMap.size();
    sort(bInt, bInt + b);

    cin >> c;
    int cInt[c];
    cMap = addToMap(cMap, cInt, c);
    c = cMap.size();
    sort(cInt, cInt + c);

    cin >> d;
    int dInt[d];
    dMap = addToMap(dMap, dInt, d);
    d = dMap.size();
    sort(dInt, dInt + d);

    cin >> e;
    int eInt[e];
    eMap = addToMap(eMap, eInt, e);
    e = eMap.size();
    sort(eInt, eInt + e);

    int totalValue = aInt[0] + bInt[0] + cInt[0] + dInt[0] + eInt[0];
    vector<vector<int>> solutions;
    int bestValue = q - totalValue;
    for (int ei = 0; ei < e; ei++) {
      int eSubTotal = q - eInt[ei];
      for (int di = 0; di < d; di++) {
        int dSubTotal = eSubTotal - dInt[di];
        for (int ci = 0; ci < c; ci++) {
          int cSubTotal = dSubTotal - cInt[ci];
          for (int bi = 0; bi < b; bi++) {
            int bSubTotal = cSubTotal - bInt[bi];

            int ai = next(aInt, bSubTotal, a);

            int aSubTotal = bSubTotal - aInt[ai];
            if (aSubTotal < 0) {
              continue;
            }
            if (aSubTotal < bestValue) {
              solutions.clear();
            }
            if (aSubTotal <= bestValue) {
              vector<int> newVector;
              newVector.push_back(ai);
              newVector.push_back(bi);
              newVector.push_back(ci);
              newVector.push_back(di);
              newVector.push_back(ei);
              solutions.push_back(newVector);
              bestValue = eSubTotal;
            }
          }
        }
      }
    }

    string bestA = aMap[aInt[solutions[0][0]]];
    int ts = 0;
    for (unsigned i = 0; i < solutions.size(); i++) {
      if (aMap[aInt[solutions[i][0]]] < bestA) {
        bestA = aMap[aInt[solutions[i][0]]];
        ts = i;
      }
    }

    cout << aMap[aInt[solutions[ts][0]]] << "\n" << bMap[bInt[solutions[ts][1]]] << "\n" << cMap[cInt[solutions[ts][2]]] << "\n" << dMap[dInt[solutions[ts][3]]] << "\n" << eMap[eInt[solutions[ts][4]]] << "\n";

    return 0;
}
