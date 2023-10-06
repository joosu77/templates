#include <iostream>
#include <unordered_map>
#include <set>
#include <queue>
#include <functional>
#include <vector>
#include <string_view>

using namespace std;

int pow2(int n) {
  if (n == 0) {
    return 1;
  }
  return 2 * pow2(n - 1);
}

int main() {
    int n;
    cin >> n;
    string a, b;
    int c, t;
    unordered_map<string, unordered_map<string, int>> full_graph;
    unordered_map<string, unordered_map<string, bool>> graph_types;
    string edges[n][2];
    for (int i = 0; i < n; i++) {
      cin >> a >> b >> c >> t;
      full_graph[a][b] = c;
      full_graph[b][a] = c;
      edges[i][0] = a;
      edges[i][1] = b;
      if (t == 1) {
        graph_types[a][b] = true;
        graph_types[b][a] = true;
      }
    }
    int s = full_graph.size();
    unordered_map<string, int> name_indexes;
    int i = 0;
    for (auto kv: full_graph) {
      name_indexes[kv.first] = i;
      i++;
    }
    vector<vector<int>> heap_data;
    for (i = 0; i < s; i++) {
      heap_data[i][0] = full_graph[edges[i][0]][edges[i][1]];
      heap_data[i][1] = name_indexes[edges[i][0]];
      heap_data[i][2] = name_indexes[edges[i][1]];
    }
    int int_graph[s][s];
    bool bool_graph[s][s];
    for (i = 0; i < s; i++) {
      for (int j = 0; j < s; j++) {
        int_graph[i][j] = -1;
        bool_graph[i][j] = false;
      }
    }
    for (auto av: full_graph) {
      for (auto bv: av.second) {
        int_graph[name_indexes[av.first]][name_indexes[bv.first]] = bv.second;
      }
    }
    set<int> red_nodes;
    for (auto av: graph_types) {
      for (auto bv: av.second) {
        bool_graph[name_indexes[av.first]][name_indexes[bv.first]] = bv.second;
        if (bv.second) {
          red_nodes.insert(name_indexes[bv.first]);
        }
      }
    }

    /*struct {
      bool operator() (const int* l, const int* r) const { return l[0] > r[0]; }
    } customLess;*/
    auto cmp = [](int* l, int* r) { return l[0] < r[0]; };
    priority_queue<vector<int>, vector<vector<int>>, decltype(cmp)> my_queue(heap_data.begin(), heap_data.end(), cmp);

    for (i = 0; i < pow2(red_nodes.size()); i++) {
      int sets[s];
      for (int j = 0; j < s; j++) {
        sets[j] = j;
      }
      //cout << i << "\n";
    }
    cout << full_graph.size() << " " << red_nodes.size() << "\n";
    return 0;
}
