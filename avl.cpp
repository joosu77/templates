#include <iostream>
#define ll long long
using namespace std;

struct Node {
    Node* l = NULL;
    Node* r = NULL;
    ll val;
    int depth = 1;
};

int depthDiff(Node* l, Node* r){
    return (l?l->depth:0)-(r?r->depth:0);
}
void calcDepths(Node* n, int d) {
    if (!n || !d) return;
    calcDepths(n->l,d-1);
    calcDepths(n->r,d-1);
    n->depth = max(n->l?n->l->depth:0,n->r?n->r->depth:0)+1;
}

Node* balance(Node* n){
    if (depthDiff(n->l,n->r) > 1){
        if (n->l->r){
            Node* newn = n->l->r;
            Node* tmpl = newn->l;
            Node* tmpr = newn->r;
            newn->l = n->l;
            newn->r = n;
            n->l->r = tmpl;
            n->l = tmpr;
            calcDepths(newn, 3);
            return newn;
        } else {
            Node* newn = n->l;
            newn->r = n;
            n->l = NULL;
            calcDepths(newn, 2);
            return newn;
        }
    }
    if (depthDiff(n->l,n->r) < -1){
        if (n->r->l){
            Node* newn = n->r->l;
            Node* tmpl = newn->l;
            Node* tmpr = newn->r;
            newn->r = n->r;
            newn->l = n;
            n->r->l = tmpr;
            n->r = tmpl;
            calcDepths(newn, 3);
            return newn;
        } else {
            Node* newn = n->r;
            newn->l = n;
            n->r = NULL;
            calcDepths(newn, 2);
            return newn;
        }
    }
    calcDepths(n, 1);
    return n;
}

Node* insert(Node* n, ll val){
    if (!n){
        n = new Node;
        n->val = val;
        return n;
    } else if (n->val==val){
        return n;
    } else if (n->val<val){
        n->r = insert(n->r, val);
    } else {
        n->l = insert(n->l, val);
    }
    return balance(n);
}

Node* erase(Node* n, ll val){
    if (!n){
        return n;
    } else if (n->val==val) {
        return NULL;
    } else if (n->val < val){
        n->r = erase(n->r, val);
    } else {
        n->l = erase(n->l, val);
    }
    n = balance(n);
    n->depth = max(n->l?n->l->depth:0,n->r?n->r->depth:0)+1;
    return n;
}

void destroy(Node* n){
    if (!n){
        return;
    }
    destroy(n->l);
    destroy(n->r);
    delete n;
}

bool find(Node* n, ll val){
    if (!n){
        return 0;
    } else if (n->val==val) {
        return 1;
    } else if (n->val < val){
        return find(n->r, val);
    } else {
        return find(n->l, val);
    }
    
}

int maxdepth(Node* n){
    if (!n){
        return 0;
    }
    return max(maxdepth(n->l), maxdepth(n->r))+1;
}
void print(Node* n, int d){
    if (!n || !d){
        return;
    }
    print(n->l, d-1);
    cout <<n->val<<' ';
    print(n->r, d-1);
}

int main(){
    Node* root = new Node;
    
    int n,m;
    cin>>n>>m;
    for (int i=0;i<n;i++){
        int a;
        cin>>a;
        if (i==0){
            root->val = a;
        } else {
            root = insert(root,a);
        }
    }
    
    for (int i=0;i<m;i++){
        int a;
        cin>>a;
        cout << find(root, a)<<' ';
    }
    cout << '\n';
    destroy(root);
}