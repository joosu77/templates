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

    string a = "a";
    string b = "ab";
    cout << (a < b);

    return 0;
}
