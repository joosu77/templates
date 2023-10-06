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
    for (int ai = 0; ai < a; ai++) {
      int aSubTotal = q - aInt[ai];
      if (aSubTotal < 0) {
        break;
      }
      for (int bi = 0; bi < b; bi++) {
        int bSubTotal = aSubTotal - bInt[bi];
        if (bSubTotal < 0) {
          break;
        }
        for (int ci = 0; ci < c; ci++) {
          int cSubTotal = bSubTotal - cInt[ci];
          if (cSubTotal < 0) {
            break;
          }
          for (int di = 0; di < d; di++) {
            int dSubTotal = cSubTotal - dInt[di];
            if (dSubTotal < 0) {
              break;
            }
            for (int ei = 0; ei < e; ei++) {
              int eSubTotal = dSubTotal - eInt[ei];
              if (eSubTotal < 0) {
                break;
              }
              if (eSubTotal < bestValue) {
                solutions.clear();
              }
              if (eSubTotal <= bestValue) {
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
