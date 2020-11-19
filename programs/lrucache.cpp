#include<iostream>
#include<bits/stdc++.h>
using namespace std;

class LRUcache{
    list<int> dq;
    unordered_map<int,list<int>::iterator> m;
    int msize;
    public:
    LRUcache(int x);
    void refer(int x);
    void display();
};

LRUcache::LRUcache(int x){
    msize = x;
}
void LRUcache::refer(int x){
    if(m.find(x)==m.end()){
        if(m.size()==msize){
            int t = dq.back();
            dq.pop_back();
            m.erase(t);
        }
    }
    else
    {
        dq.erase(m[x]);
    }
    dq.push_front(x);
    m[x] = dq.begin();
}
void LRUcache::display(){
    for(auto i = dq.begin();i!=dq.end();i++){
        cout<<(*i)<<" ";
    }
    cout<<endl;
}

int main(){
    LRUcache v(3);
    v.refer(1);
    v.display();
    v.refer(2);
    v.display();
    v.refer(3);
    v.display();
    v.refer(4);
    v.display();
    v.refer(2);
    v.display();
    v.refer(4);   
    v.display(); 


    return 0;

}