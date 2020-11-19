#include<iostream>
using namespace std;
class stack{
    char *arr;
    int capacity;
    int top;
    public:
        stack(int x);
        ~stack();
        bool isempty();
        bool isfull();
        bool push(char x);
        char pop();
        char peek();
};
stack::stack(int x){
    arr =new char[x];
    capacity = x;
    top = -1;
}

stack::~stack(){
    delete[] arr;
}
bool stack::isempty(){
    if(top==-1){
        return true;
    }
    return false;
}

bool stack::isfull(){
    if(top>=capacity-1){
        return true;
    }
    return false;
}

bool stack::push(char x){
    if(isfull()){
        cout<<"stack overflow"<<endl;
        return false;
    }
    else
    {
        arr[++top]=x;
    }
    return true;    
}
char stack::pop(){
    if(isempty()){
        cout<<"stack underflow"<<endl;
    }
    char t = arr[top];
    top = top-1;
    return t;
}
char stack::peek(){
    if(isempty()){
        cout<<"Empty stack "<<endl;
    }
    char t = arr[top];
    return t;
}

int prece(char k){
    if (k=='*' || k =='/')
    {
        return 3;
    }
    else if (k=='+' || k =='-')
    {
        return 2;
    }else if (k=='^')
    {
        return 1;
    }
    else
    { return -1;   
}}

int main(){
    int len,i;
    string in;
    cin >> in ;
    len = in.length();
    stack st(len+1);
    st.push('$');
    string postf;
    for(i=0;i<len;i++){
        if((in[i]>='a' && in[i]<='z')|| (in[i]>='A' && in[i]<='Z') ){
            postf = postf + in[i];
        }
        else if(in[i]=='('){
            st.push('(');
        }
        else if(in[i]==')'){
            while(st.peek()!='$' && st.peek() !='(' ){
                postf = postf + st.pop();
            }
            if(st.peek()=='('){
                 st.pop();
            }
        }
        else{
            while(st.peek()!='$' && prece(st.peek())>=prece(in[i])){
                postf = postf+ st.pop();
            }
            st.push(in[i]);
        }
    
    }
    while(st.peek()!='$'){
        postf = postf+  st.pop();
    }
cout << postf << endl;
    return 0;
}