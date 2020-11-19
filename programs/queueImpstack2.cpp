#include<iostream>
#include<bits/stdc++.h>
using namespace std;
 class Queue{
     stack<int> s1,s2;

     public:
     void enqueue(int x){
         while(!s1.empty()){
             s2.push(s1.top());
             s1.pop();
         }
         s1.push(x);
         while(!s2.empty()){
             s1.push(s2.top());
             s2.pop();
         }
     }

     int dequeue(){
         if(s1.empty()){
             cout<<"Q is empty"<<endl;
             return -1;
         }
         int temp = s1.top();
         s1.pop();
         return temp;

     }

     int frontq(){
         if(s1.empty()){
             cout<<"Q is empty"<<endl;
             return -1;
         }
         return s1.top();;

     }
 };

 int main(){
     Queue q;
     q.enqueue(1);
     q.enqueue(4);
     cout<<q.dequeue()<<endl;
     cout<<q.dequeue()<<endl;
     cout<<q.dequeue()<<endl;
     return 0;
 }