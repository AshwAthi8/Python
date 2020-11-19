#include<iostream>
#include <bits/stdc++.h> 

using namespace std;

int main(){
    stack<char> s;
    string in;
    cout<<"Enter your input ";
    cin >> in;
    int i=0;
    int len = in.length();
    while(i<len){
        char element = in[i];
        switch (element)
        {
        case '{':{s.push(element);
            break;
        }
        case '[':{s.push(element);
            break;
        }
        case '(':{s.push(element);
            break;
        }
        case '}':{
            if(s.empty() || s.top()!= '{'){
                cout<<"NO"<<endl;
                return 0;
            }
            s.pop();
            break;
        }
        case ']':{
            if(s.empty() || s.top()!= '['){
                cout<<"NO"<<endl;
                return 0;
            }
            s.pop();
            break;
        }
        case ')':{
            if(s.empty() || s.top()!= '('){
                cout<<"NO"<<endl;
                return 0;
            }
            s.pop();
            break;
        }

        }
        i=i+1;
    }
    if(s.empty()){
    cout<<"YES"<<endl;}
    else{
         cout<<"NO"<<endl;
    }
    return 0;
}