#include <iostream>
#define ll long long
#define p(x, y) make_pair(x,y)
#define pp(x, y, z) make_pair(x, make_pair(y, z))
using namespace std;

struct Node {
    Node* l = NULL;
    Node* r = NULL;
    ll val=0;
    ll set_val = -1;
    ll add_val = 0;
    bool to_set = 0;
    int minid, maxid;
    ll (*f)(pair<ll,bool> left_val, pair<ll,bool> right_val, bool to_set, ll set_val, ll add_val, int);
};

Node* propagate(Node* n){
    if (n->r && n->l) {
        n->val = n->f(p(n->l->val,1), p(n->r->val,1), n->to_set, n->set_val, n->add_val, n->maxid-n->minid+1);
        n->r->set_val = n->set_val;
        n->r->to_set = n->to_set;
        n->r->add_val = n->add_val;
        n->l->set_val = n->set_val;
        n->l->to_set = n->to_set;
        n->l->add_val = n->add_val;
        n->set_val = -1;
        n->to_set = 0;
        n->add_val = 0;
    }
    return n;
}

pair<Node*, pair<ll,bool> > query(Node* n, int l, int r){
    n = propagate(n);
    if (n->minid>r || n->maxid<l){
        return pp(n, 0, 0);
    } else if (n->minid <= l && n->maxid >= r){
        return pp(n, n->val, 1);
    } else {
        auto lp = query(n->l, l, r);
        auto rp = query(n->r, l, r);
        return pp(n, n->f(lp.second, rp.second, n->to_set, n->set_val, n->add_val, n->maxid-n->minid+1), 1);
    }
}

Node* set(Node* n, ll val, int l, int r){
    n = propagate(n);
    if (n->minid>r || n->maxid<l){
        return n;
    } else if (n->minid <= l && n->maxid >= r){
        n->to_set = 1;
        n->set_val = val;
        n->add_val = 0;
    } else {
        n->l = set(n->l, val, l, r);
        n->r = set(n->r, val, l, r);
    }
    return n;
}

Node* add(Node* n, ll val, int l, int r){
    n = propagate(n);
    if (n->minid>r || n->maxid<l){
        return n;
    } else if (n->minid <= l && n->maxid >= r){
        n->add_val = val;
    } else {
        n->l = add(n->l, val, l, r);
        n->r = add(n->r, val, l, r);
    }
    return n;
}

// constructs indexes 0..r-1
Node* construct(Node* n, int r, ll (*f)(pair<ll,bool> left_val, pair<ll,bool> right_val, bool to_set, ll set_val, ll add_val, int), int l=0){
    n = new Node;
    n->minid = l;
    n->maxid = r;
    n->f = f;
    if (r-l>1){
        n->l = construct(n->l, (r+l)/2, f, l);
        n->r = construct(n->r, r, f, (r+l)/2);
    }
    return n;
}

ll sumf(pair<ll,bool> left_val, pair<ll,bool> right_val, bool to_set, ll set_val, ll add_val, int num){
    if (to_set){
        return num*(set_val+add_val);
    } else {
        return left_val.first * left_val.second + right_val.first + left_val.second + num*add_val;
    }
}

int main(){
    Node* root = new Node;
    root = construct(root, 10, sumf);
    for (int i=0;i<10;i++){
        root = set(root, i*i, i, i+1);
    }
    auto jou = query(root, 0,10);
    cout << jou.second.first <<'\n';
}