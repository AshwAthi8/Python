#include<iostream>
#include<bits/stdc++.h>
using namespace std;

// this method has dequeue and front with O(n) complexity;

class Queue{
    stack<int> s1,s2;
    public:
    void enqueue(int x){
        s1.push(x);
    }

    int dequeue(){
        if(s1.empty()){
            cout<<"empty Q"<<endl;
            return -1;
        }

        while(!s1.empty()){
            s2.push(s1.top());
            s1.pop();
        }
        int temp = s2.top();
        s2.pop();
        while(!s2.empty()){
            s1.push(s2.top());
            s2.pop();
        }
        return temp;
    }
    int frontq(){
        if(s1.empty()){
            cout<<"empty Q"<<endl;
            return -1;
        }

        while(!s1.empty()){
            s2.push(s1.top());
            s1.pop();
        }
        int temp = s2.top();
       // s2.pop();
        while(!s2.empty()){
            s1.push(s2.top());
            s2.pop();
        }
        return temp;


    }

};


int main(){
    Queue q;
    q.enqueue(4);
    q.enqueue(5);
    q.enqueue(8);
    cout<<q.dequeue()<<endl;


    return 0;
}