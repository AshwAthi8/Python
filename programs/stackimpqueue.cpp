#include<iostream>
#include<bits/stdc++.h>
using namespace std;
// push
// pop


class Stack{
    queue<int> q1,q2;
    int curr_size;
    public:
    Stack(){
        curr_size =0;
    }
    void push(int x){
        curr_size++;
      
        while(!q1.empty()){
            q2.push(q1.front());
            q1.pop();
        }
        
        q1.push(x);
        
        while(!q2.empty()){
            q1.push(q2.front());
            q2.pop();
        }
    }
    void pop(){
        if(q1.empty()){
            cout<<"stack under"<<endl;
        }
        q1.pop();
        curr_size--;

    }
    int top(){
    if(q1.empty()){
            cout<<"stack under"<<endl;
            return -1;
        }
        int temp = q1.front();
        
    return temp;

    }
    
    
    int size(){
        return curr_size;
    }
    
};

int main(){
    Stack s;
    s.push(4);
    s.push(6);
    cout<<s.size()<<endl;
    cout<<s.top()<<endl;
    s.pop();
    cout<<s.size()<<endl;
    cout<<s.top()<<endl;
    return 0;
}