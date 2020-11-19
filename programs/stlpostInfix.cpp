#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main (){
    string in,out;
    stack<string> s;
    cin >> in ;
    int len = in.length();
    for( int i =0;i<len;i++){
        if(in[i]>='a' && in[i]<'z'){
            string op(1,in[i]);
            s.push(op);
        }
        else{
            string op1=s.top();
            s.pop();
            string op2 = s.top();
            s.pop();
            s.push('('+op2+in[i]+op1+')');
        }
    }
    
    cout<<s.top()<<endl;
}