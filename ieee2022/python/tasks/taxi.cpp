#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

long long MAX_INT = 1e18;
long long n,e;
vector<vector<pair<long long, long long> > > adj;
map<long long,map<long long,long long>> m;

struct node {
	long long x, cst;
	node(long long x, long long cst) :
			x(x), cst(cst) {
	}
	bool operator<(const node &a) const {
		return a.cst < cst;
	}
};
vector<long long> dijk(long long src/*, long long des*/) {
  vector<long long> res(n);
	vector<long long> cost(n + 1, 1e9);
	priority_queue<node> que;
	que.push(node(src, 0));
	cost[src] = 0;
	while (que.size()) {
		long long x = que.top().x, cst = que.top().cst;
		que.pop();
		/*if (x == des) {
			return cst;
		}*/
		for (long long i = 0, ln = adj[x].size(); i < ln; ++i) {
			long long y = adj[x][i].first, _cst = adj[x][i].second;
			if (cst + _cst < cost[y]) {
				cost[y] = cst + _cst;
				que.push(node(y, cost[y]));
			}
		}
	}
	return cost;
}

struct Thing {
    Thing(long long nodee, set<pair<long long,long long>> sdd, long long summ){
        node = nodee;
        sd = sdd;
        sum = summ;
    }
    long long node;
    set<pair<long long,long long>> sd;
    long long sum;
};

map<long long,long long> DFS(long long src){
    map<long long,long long> res;
    queue<Thing> q;
    set<pair<long long,long long>> empty;
    q.emplace(src, empty,0);
    while(q.size()){
        Thing p = q.front();
        q.pop();
        long long node = p.node;
        if (p.sd.size()==5){
            if (!res.count(node) || res[node]>p.sum)
                res[node] = p.sum;
        } else {
            for (auto pp: m[node]){
                if (!(p.sd.count(make_pair(pp.first,node)) || p.sd.count(make_pair(node,pp.first)))){
                    set<pair<long long,long long>> snew = p.sd;
                    snew.emplace(node,pp.first);
                    q.emplace(pp.first, snew, p.sum+pp.second);
                }
            }
        }
    }
    return res;
}

int main(){
    cin>>n>>e;
    adj.clear();
    adj.resize(n+1);
    for (long long i=0;i<e;i++){
        long long s,d,l;
        cin>>s>>d>>l;
        adj[s].emplace_back(d,l);
        adj[d].emplace_back(s,l);
        m[s][d]=l;
        m[d][s]=l;
    }
    //vector<long long> v = dijk(1);
    /*for (long long i:v){
        cout << i<<'\n';
    }*/
    map<long long,long long> fives = DFS(1);
    /*for (auto p: fives){
        cout << p.first << " " << p.second<<'\n';
    }*/
    map<long long,vector<long long>> forest;
    for (auto p:fives){
        vector<long long> nv = dijk(p.first);
        forest[p.first] = nv;
    }
    //cout << '\n';
    for (long long i=0;i<n;i++){
        if (fives.count(i+1)){
            cout << fives[i+1]<<'\n';
        } else {
            long long minl = MAX_INT;
            for (auto p: fives){
                minl = min(minl, forest[p.first][i+1]+p.second);
            }
            cout << minl<<'\n';
        }
    }
}
