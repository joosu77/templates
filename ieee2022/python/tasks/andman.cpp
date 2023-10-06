#include <iostream>
#include <unordered_map>
#include <set>
using namespace std;

long long vals[100001];
long long mults[100001];
int layer[100001];
int pars[100001];
//unordered_map<int,bool> lazy;
unordered_map<int,set<int>> m;
long long p=1e9+7;

void gen(int node, long long got, int par, int l){
    mults[node] = (got*vals[node])%p;
    layer[node] = l;
    pars[node] = par;
    for (int i: m[node]){
        if(i != par){
            gen(i,got*vals[node],node,l+1);
        }
    }
}

int ffind(int n1, int n2){
    int res;
    if (n1==n2) res = n1;
    else if (layer[n1]>layer[n2]) res = ffind(pars[n1], n2);
    else if (layer[n1]<layer[n2]) res = ffind(n1, pars[n2]);
    else res = ffind(pars[n1],pars[n2]);
    //if (lazy[n1]){
        mults[n1] = (mults[pars[n1]]*vals[n1])%p;
    //}
    //if (lazy[n2]){
        mults[n2] = (mults[pars[n2]]*vals[n2])%p;
    //}
    return res;
}


long long power(long long x, unsigned long long y, unsigned long long M){
    if (y == 0)
        return 1;

    long long p = power(x, y / 2, M) % M;
    p = (p * p) % M;

    return (y % 2 == 0) ? p : (x * p) % M;
}

long long gcd(long long a, long long b){
    if (a == 0)
        return b;
    return gcd(b % a, a);
}
long long inv(long long A){
    long long g = gcd(A, p);
    return power(A, p - 2, p);
}

int main(){
    long long T;
    cin>>T;
    while (T--){
        m.clear();
        //vals.clear();
        //mults.clear();
        //layer.clear();
        //pars.clear();
        long long n,q;
        cin>>n;
        for (long long i=0;i<n;i++){
            cin>>vals[i+1];
        }
        for (long long i=0;i<n-1;i++){
            long long a,b;
            cin>>a>>b;
            m[a].insert(b);
            m[b].insert(a);
        }
        mults[-1] = 1;
        gen(1, 1, -1, 0);

/*        cout << '\n';
        for (auto p: vals) {
            cout << p.first << ' '<<p.second<<'\n';
        }
        cout <<'\n';
        for (auto p: layer) {
            cout << p.first << ' '<<p.second<<'\n';
        }
        cout <<'\n';
  */
        cin>>q;
        for (long long i=0;i<q;i++){
            long long k,a,b;
            cin>>k>>a>>b;
            if (k==1){
                vals[a] = b;
                //lazy[a] = 1;
            } else {
                long long par = ffind(a,b);
                long long parm = mults[par];
                long long ii = inv((parm*parm)%p);
                long long res = (((((mults[a]*mults[b])%p)*ii)%p)*vals[par])%p;
                cout << res<<'\n';
            }
        }
    }
}
