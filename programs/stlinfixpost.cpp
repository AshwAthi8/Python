#include<iostream>
#include<bits/stdc++.h>

using namespace std;
int prece(char k){
    if(k=='*' || k=='/'){
        return 3;
        }
    else if (k=='+' || k =='-')
    {
       return 2;
    }
    else if (k=='^')
    {
      return 1;
    }
    else
    {
        return -1;
    }
    
}

int main(){
    stack<char> s;
    string in;
    int i=0;
    cin >> in ;
    int len = in.length();
    string out;
    s.push('$');
    for(i=0;i<len;i++){
        //cout<<in[i]<<"\n";
        if(in[i]>= 'a' && in[i]<='z'){
            out = out + in[i];
            // cout<<out<<endl;
        }
        else if(in[i] == '('){
            s.push(in[i]);
        }
        else if(in[i]== ')')
        {
           while(s.top()!='$' && s.top() !='(' )
           {char  c = s.top();
           s.pop();
           out = out + c;
         //  cout<<out<<endl;
           }
           if(s.top() =='('){
               s.pop();
           }
        }
        else
        {
            while(s.top() != '$' && prece(s.top())>=prece(in[i])){
                char p = s.top();
                s.pop();
                out = out + p;
            }
            s.push(in[i]);
            }
    }
    while(s.top()!='$'){
        out= out + s.top();
        s.pop();
    }
cout<<out<<endl;
    return 0;
}